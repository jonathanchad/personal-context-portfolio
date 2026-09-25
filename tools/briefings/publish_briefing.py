#!/usr/bin/env python3
"""
publish_briefing.py — render a spoken-briefing script with ElevenLabs and publish it
to Jonathan's private podcast feed (Supabase Storage).

Runs on the Mac (the cloud workspace cannot reach ElevenLabs or Supabase).
Standard library only. ffmpeg is used if present for clean chunk joins; otherwise
raw MP3 concatenation is used (fine for ElevenLabs output).

Usage
  One file:   python3 publish_briefing.py --script scripts/x.md [--title ...] [--dry-run]
  Watch mode: python3 publish_briefing.py --inbox scripts      (what launchd runs; see install.sh)

Keys live in ~/.config/briefings/env (outside iCloud), one per line:
  ELEVENLABS_API_KEY=...
  SUPABASE_SERVICE_KEY=...      service-role key for the bts-operations project
  BRIEFING_VOICE_ID=...         default voice

Script format
  Optional front matter (title / summary / source / slug / voice), then plain spoken prose.
  Blank lines separate paragraphs. Optional headings:
    ## MAIN BRIEFING      (default if no headings)
    ## SHORT CUT          (optional 60–120 s version, published as a second episode)
  No markdown, links, bullets or tables — the audio-briefing skill produces this shape.
"""
import argparse, datetime as dt, json, os, re, shutil, subprocess, sys, tempfile, urllib.request, urllib.error
from xml.sax.saxutils import escape

SUPABASE_URL = "https://ihosjunvapgjuajoezak.supabase.co"
BUCKET = "jcs-briefings"
TABLE = "jcs_briefing_episodes"
FEED_TITLE = "JCS Briefings"
FEED_DESC = "Spoken briefings generated from working documents. Private feed."
FEED_AUTHOR = "Breakthrough Strategies Co."
FEED_EMAIL = "jonathan@breakthroughstrategies.co"
FEED_LINK = "https://breakthroughstrategies.co"
DEFAULT_MODEL = "eleven_multilingual_v2"
OUTPUT_FORMAT = "mp3_44100_128"
CHUNK_CHARS = 4500          # stay well under the per-request character limit
BITRATE_BPS = 128_000       # for duration estimate from byte size

ENV_FILE = os.path.expanduser("~/.config/briefings/env")   # KEY=value lines; kept out of iCloud

def die(msg, code=2):
    print(f"ERROR: {msg}", file=sys.stderr); sys.exit(code)

def load_env_file():
    if not os.path.exists(ENV_FILE): return
    for line in open(ENV_FILE, encoding="utf-8"):
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line: continue
        k, v = line.split("=", 1)
        k, v = k.strip(), v.strip().strip('"').strip("'")
        if k.startswith("export "): k = k[7:].strip()
        os.environ.setdefault(k, v)

def env(name, required=True):
    v = os.environ.get(name, "").strip()
    if required and not v:
        die(f"{name} is not set. Add it to your shell profile and open a new terminal.")
    return v

# ---------- script parsing ----------
def parse_front_matter(text):
    """Optional leading block:
    ---
    title: YSG funder update
    summary: one line
    source: https://notion.so/...
    slug: 2026-09-25-ysg-funder-update
    voice: VOICE_ID
    ---
    """
    meta = {}
    m = re.match(r"^---\s*\n(.*?)\n---\s*\n", text, re.S)
    if not m: return meta, text
    for line in m.group(1).splitlines():
        if ":" in line:
            k, v = line.split(":", 1); meta[k.strip().lower()] = v.strip().strip('"')
    return meta, text[m.end():]

def parse_script(path):
    text = open(path, encoding="utf-8").read()
    _, text = parse_front_matter(text)
    sections = {}
    current = "MAIN BRIEFING"
    buf = []
    for line in text.splitlines():
        m = re.match(r"^##\s+(.+?)\s*$", line)
        if m:
            if buf: sections[current] = "\n".join(buf).strip()
            current, buf = m.group(1).strip().upper(), []
        else:
            buf.append(line)
    if buf: sections[current] = "\n".join(buf).strip()
    main = sections.get("MAIN BRIEFING") or sections.get(next(iter(sections)))
    short = sections.get("SHORT CUT")
    if not main: die("No script text found.")
    return clean(main), (clean(short) if short else None)

def clean(t):
    t = re.sub(r"https?://\S+", "", t)                 # never read URLs aloud
    t = re.sub(r"[*_`#>\[\]]", "", t)                  # stray markdown
    t = re.sub(r"[ \t]+", " ", t)
    t = re.sub(r"\n{3,}", "\n\n", t)
    return t.strip()

def chunk(text, limit=CHUNK_CHARS):
    paras = [p.strip() for p in text.split("\n\n") if p.strip()]
    chunks, cur = [], ""
    for p in paras:
        if len(p) > limit:                              # split an oversized paragraph on sentences
            for s in re.split(r"(?<=[.!?])\s+", p):
                if len(cur) + len(s) + 1 > limit and cur:
                    chunks.append(cur); cur = ""
                cur = (cur + " " + s).strip()
            continue
        if len(cur) + len(p) + 2 > limit and cur:
            chunks.append(cur); cur = ""
        cur = (cur + "\n\n" + p).strip()
    if cur: chunks.append(cur)
    return chunks

# ---------- ElevenLabs ----------
def tts(text, voice_id, model_id, api_key, prev=None, nxt=None):
    url = f"https://api.elevenlabs.io/v1/text-to-speech/{voice_id}?output_format={OUTPUT_FORMAT}"
    body = {"text": text, "model_id": model_id,
            "voice_settings": {"stability": 0.5, "similarity_boost": 0.75, "style": 0.0, "use_speaker_boost": True}}
    if prev: body["previous_text"] = prev[-600:]
    if nxt:  body["next_text"] = nxt[:600]
    req = urllib.request.Request(url, data=json.dumps(body).encode(), method="POST",
        headers={"xi-api-key": api_key, "Content-Type": "application/json", "Accept": "audio/mpeg"})
    try:
        with urllib.request.urlopen(req, timeout=180) as r:
            return r.read()
    except urllib.error.HTTPError as e:
        die(f"ElevenLabs {e.code}: {e.read()[:400].decode(errors='ignore')}")

def render(text, voice_id, model_id, api_key, out_path):
    parts = chunk(text)
    print(f"  {len(parts)} chunk(s), {len(text):,} chars")
    blobs = []
    for i, p in enumerate(parts):
        prev = parts[i-1] if i > 0 else None
        nxt = parts[i+1] if i+1 < len(parts) else None
        print(f"  rendering chunk {i+1}/{len(parts)} …")
        blobs.append(tts(p, voice_id, model_id, api_key, prev, nxt))
    if len(blobs) == 1 or not shutil.which("ffmpeg"):
        with open(out_path, "wb") as f:
            for b in blobs: f.write(b)
    else:
        with tempfile.TemporaryDirectory() as td:
            names = []
            for i, b in enumerate(blobs):
                n = os.path.join(td, f"p{i:03d}.mp3"); open(n, "wb").write(b); names.append(n)
            lst = os.path.join(td, "list.txt")
            open(lst, "w").write("".join(f"file '{n}'\n" for n in names))
            subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-f", "concat", "-safe", "0",
                            "-i", lst, "-c", "copy", out_path], check=True)
    size = os.path.getsize(out_path)
    return size, int(size * 8 / BITRATE_BPS)

# ---------- Supabase ----------
def sb_headers(key, extra=None):
    h = {"apikey": key, "Authorization": f"Bearer {key}"}
    if extra: h.update(extra)
    return h

def upload(path_in_bucket, data, content_type, key):
    url = f"{SUPABASE_URL}/storage/v1/object/{BUCKET}/{path_in_bucket}"
    req = urllib.request.Request(url, data=data, method="POST",
        headers=sb_headers(key, {"Content-Type": content_type, "x-upsert": "true", "Cache-Control": "max-age=300"}))
    try:
        with urllib.request.urlopen(req, timeout=300) as r: r.read()
    except urllib.error.HTTPError as e:
        die(f"Supabase upload {e.code}: {e.read()[:400].decode(errors='ignore')}")
    return f"{SUPABASE_URL}/storage/v1/object/public/{BUCKET}/{path_in_bucket}"

def upsert_episode(row, key):
    url = f"{SUPABASE_URL}/rest/v1/{TABLE}?on_conflict=slug"
    req = urllib.request.Request(url, data=json.dumps(row).encode(), method="POST",
        headers=sb_headers(key, {"Content-Type": "application/json",
                                 "Prefer": "resolution=merge-duplicates,return=minimal"}))
    try:
        with urllib.request.urlopen(req, timeout=60) as r: r.read()
    except urllib.error.HTTPError as e:
        die(f"Supabase upsert {e.code}: {e.read()[:400].decode(errors='ignore')}")

def list_episodes(key):
    url = f"{SUPABASE_URL}/rest/v1/{TABLE}?select=*&order=published_at.desc&limit=200"
    req = urllib.request.Request(url, headers=sb_headers(key))
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.loads(r.read())

def rfc2822(iso):
    d = dt.datetime.fromisoformat(iso.replace("Z", "+00:00"))
    return d.strftime("%a, %d %b %Y %H:%M:%S %z")

def build_feed(episodes):
    base = f"{SUPABASE_URL}/storage/v1/object/public/{BUCKET}"
    items = []
    for e in episodes:
        audio = f"{base}/{e['audio_path']}"
        dur = int(e.get("duration_seconds") or 0)
        items.append(f"""
    <item>
      <title>{escape(e['title'])}</title>
      <description>{escape(e.get('summary') or e['title'])}</description>
      <guid isPermaLink="false">{escape(e['slug'])}</guid>
      <pubDate>{rfc2822(e['published_at'])}</pubDate>
      <enclosure url="{escape(audio)}" length="{int(e.get('bytes') or 0)}" type="audio/mpeg"/>
      <itunes:duration>{dur}</itunes:duration>
      <itunes:explicit>false</itunes:explicit>{f'''
      <link>{escape(e['source_ref'])}</link>''' if (e.get('source_ref') or '').startswith('http') else ''}
    </item>""")
    return f"""<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0" xmlns:itunes="http://www.itunes.com/dtds/podcast-1.0.dtd" xmlns:atom="http://www.w3.org/2005/Atom">
  <channel>
    <title>{escape(FEED_TITLE)}</title>
    <link>{FEED_LINK}</link>
    <language>en-au</language>
    <description>{escape(FEED_DESC)}</description>
    <atom:link href="{base}/feed.xml" rel="self" type="application/rss+xml"/>
    <itunes:author>{escape(FEED_AUTHOR)}</itunes:author>
    <itunes:owner><itunes:name>{escape(FEED_AUTHOR)}</itunes:name><itunes:email>{FEED_EMAIL}</itunes:email></itunes:owner>
    <itunes:image href="{base}/cover.png"/>
    <itunes:explicit>false</itunes:explicit>
    <itunes:block>Yes</itunes:block>
    <itunes:category text="Business"/>
    <lastBuildDate>{rfc2822(dt.datetime.now(dt.timezone.utc).isoformat())}</lastBuildDate>{''.join(items)}
  </channel>
</rss>
"""

def slugify(s):
    s = re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")
    return s[:60]

# ---------- main ----------
def publish_one(script_path, title, slug, summary, source, voice, model, outdir, cover, dry_run, el_key, sb_key):
    os.makedirs(outdir, exist_ok=True)
    main_text, short_text = parse_script(script_path)
    jobs = [(slug, title, main_text)]
    if short_text: jobs.append((f"{slug}-short", f"{title} (short cut)", short_text))

    published = []
    for s, t, text in jobs:
        out = os.path.join(outdir, f"{s}.mp3")
        print(f"Rendering: {t}")
        size, dur = render(text, voice, model, el_key, out)
        print(f"  {out}  {size/1e6:.1f} MB  ~{dur//60}m{dur%60:02d}s")
        if dry_run: continue
        path = f"episodes/{s}.mp3"
        url = upload(path, open(out, "rb").read(), "audio/mpeg", sb_key)
        upsert_episode({"slug": s, "title": t, "summary": summary or None, "source_ref": source or None,
                        "audio_path": path, "bytes": size, "duration_seconds": dur, "voice_id": voice,
                        "published_at": dt.datetime.now(dt.timezone.utc).isoformat()}, sb_key)
        published.append((t, url))

    if dry_run:
        print("Dry run: nothing published."); return published

    if cover and os.path.exists(cover):
        upload("cover.png", open(cover, "rb").read(), "image/png", sb_key)
    feed_url = upload("feed.xml", build_feed(list_episodes(sb_key)).encode(), "application/rss+xml", sb_key)
    print("\nPublished:")
    for t, u in published: print(f"  {t}\n  {u}")
    print(f"\nFeed: {feed_url}")
    return published

def main():
    load_env_file()
    here = os.path.dirname(os.path.abspath(__file__))
    ap = argparse.ArgumentParser()
    ap.add_argument("--script", help="one ear-script .md to publish")
    ap.add_argument("--inbox", help="publish every .md in this folder that has no .published marker (watch mode)")
    ap.add_argument("--title")
    ap.add_argument("--slug")
    ap.add_argument("--summary", default="")
    ap.add_argument("--source", default="", help="URL or name of the source document")
    ap.add_argument("--voice", default=os.environ.get("BRIEFING_VOICE_ID", "").strip())
    ap.add_argument("--model", default=DEFAULT_MODEL)
    ap.add_argument("--outdir", default=os.path.join(here, "audio"))
    ap.add_argument("--cover", default=os.path.join(here, "cover.png"))
    ap.add_argument("--dry-run", action="store_true", help="render mp3 locally, do not publish")
    a = ap.parse_args()
    if not a.script and not a.inbox: die("Pass --script FILE or --inbox DIR.")

    el_key = env("ELEVENLABS_API_KEY")
    sb_key = None if a.dry_run else env("SUPABASE_SERVICE_KEY")
    today = dt.date.today().isoformat()

    if a.script:
        meta, _ = parse_front_matter(open(a.script, encoding="utf-8").read())
        title = a.title or meta.get("title") or os.path.splitext(os.path.basename(a.script))[0]
        voice = a.voice or meta.get("voice")
        if not voice: die("No voice: pass --voice, set BRIEFING_VOICE_ID, or add voice: to the front matter.")
        slug = a.slug or meta.get("slug") or f"{today}-{slugify(title)}"
        publish_one(a.script, title, slug, a.summary or meta.get("summary", ""), a.source or meta.get("source", ""),
                    voice, a.model, a.outdir, a.cover, a.dry_run, el_key, sb_key)
        return

    # Inbox mode: called by launchd whenever the folder changes.
    inbox = a.inbox
    pending = sorted(f for f in os.listdir(inbox) if f.endswith(".md") and not f.startswith(".")
                     and not os.path.exists(os.path.join(inbox, f + ".published")))
    if not pending:
        print("Inbox: nothing to publish."); return
    for f in pending:
        p = os.path.join(inbox, f)
        # iCloud/Cowork may still be writing: skip files modified in the last 5 seconds.
        if dt.datetime.now().timestamp() - os.path.getmtime(p) < 5:
            print(f"Inbox: {f} still being written, will retry on next trigger."); continue
        try:
            meta, _ = parse_front_matter(open(p, encoding="utf-8").read())
            title = meta.get("title") or os.path.splitext(f)[0]
            voice = meta.get("voice") or a.voice
            if not voice: die("No voice: set BRIEFING_VOICE_ID in the env file.")
            slug = meta.get("slug") or f"{today}-{slugify(title)}"
            pub = publish_one(p, title, slug, meta.get("summary", ""), meta.get("source", ""),
                              voice, a.model, a.outdir, a.cover, a.dry_run, el_key, sb_key)
            with open(p + ".published", "w") as m:
                m.write(dt.datetime.now().isoformat() + "\n" + "\n".join(u for _, u in pub) + "\n")
            print(f"Inbox: published {f}")
        except SystemExit as e:
            with open(p + ".failed", "a") as m:
                m.write(dt.datetime.now().isoformat() + " exit " + str(e.code) + "\n")
            print(f"Inbox: FAILED {f} (see {f}.failed)")

if __name__ == "__main__":
    main()
