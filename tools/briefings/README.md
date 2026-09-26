# JCS Briefings — audio publishing pipeline

Added 25 Sep 2026. Jonathan supplied `publish_briefing.py` and
`cover.png` directly (uploaded to a Claude Code session; the script's
own docstring says it "runs on the Mac" since "the cloud workspace
cannot reach ElevenLabs or Supabase" — **corrected 26 Sep, see below,
this is no longer accurate for at least one live routine**).

**What it is**, per the script's own docstring: renders a spoken-
briefing script with ElevenLabs, uploads the mp3 to Supabase Storage,
and publishes/updates a private podcast RSS feed ("JCS Briefings",
`itunes:block: Yes` — not publicly listed). Designed to run on
Jonathan's Mac via `launchd` watching an inbox folder of script files,
or one-off via `--script`. Standard library only, no dependencies.

**Confirmed 25 Sep: the pipeline works.** Jonathan confirmed there's a
mock (test) episode already on the JCS Briefings feed.

**Correction, 26 Sep: it also runs from a cloud session, at least for
the Weekly AAR.** Investigating why the AAR hadn't produced anything,
`fire_trigger` surfaced its actual live prompt — a "STEP 4" section not
captured anywhere in this repo until now (see
`agents/routines/weekly-after-action-review-aar.md`) that runs this
exact script **from inside the Cowork session itself**: copies it and
`cover.png` from the cloned repo into `~/briefings/`, pulls the
ElevenLabs/Supabase keys from a Supabase table (`public.jcs_secrets`
on project `ihosjunvapgjuajoezak`) rather than a local env file, and
runs it there. Its own text: "ElevenLabs and the bts-operations
Supabase project are on the network allowlist." So the "runs on the
Mac only" framing above is wrong for at least this environment — no
delivery-bridge problem exists for a routine willing to pull its own
keys from Supabase per-run instead of relying on a local
`~/.config/briefings/env` file. **Whether this actually works is still
unconfirmed** — the 25 Sep run never got far enough to reach Step 4
(it stalled and was abandoned before doing anything), and a re-fire
was in progress when this was written.

**What this means for the daily-audio agenda in
`GETTING-STARTED.md`:** the "no delivery bridge" blocker on step 5 may
already be solved, by copying this same cloud-side pattern rather than
inventing a new one. Still unconfirmed whether this session's
`audio-briefing` skill calls this exact script or a separate
implementation of the same idea — worth checking once Step 4's success
is confirmed.

See the script's own docstring for full usage. Not modified — copied
verbatim.

**`cover.png`** replaced 25 Sep 2026 with a photo Jonathan supplied
directly (converted from the uploaded .webp to PNG, 2000×2000, square).
