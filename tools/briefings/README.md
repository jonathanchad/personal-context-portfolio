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
`~/.config/briefings/env` file.

**Confirmed 26 Sep 2026: it works.** The re-fired AAR's Notion session
log entry states "spoken edition (full + short cut) rendered via
ElevenLabs and published to the private podcast feed," with the Key
Decisions field crediting "publish_briefing.py + bts-operations
Supabase secrets" run from the cloud. Likely explanation for the
contradiction: an earlier Notion session log entry (25 Sep, "Audio
briefing pipeline") recorded the org network allowlist as blocking
ElevenLabs/Supabase from the cloud entirely, and recommended adding
`api.elevenlabs.io` and the Supabase project host to it precisely so
scheduled cloud runs could publish. That was evidently done sometime
in the next day — the AAR's Step 4 text (written after that change)
assumes the allowlist is open, and the 26 Sep run proves it is.

**What this means for the daily-audio agenda in
`GETTING-STARTED.md`:** the "no delivery bridge" blocker on step 5 is
solved — copy this same cloud-side pattern (pull keys from
`public.jcs_secrets` on Supabase project `ihosjunvapgjuajoezak`, run
`publish_briefing.py` in-session) into
`agents/routines/donna-end-of-day-audio-script.md` instead of its
current Gmail-draft interim. Still worth checking whether this
session's `audio-briefing` skill calls this exact script or a separate
implementation of the same idea.

See the script's own docstring for full usage. Not modified — copied
verbatim.

**`cover.png`** replaced 25 Sep 2026 with a photo Jonathan supplied
directly (converted from the uploaded .webp to PNG, 2000×2000, square).
