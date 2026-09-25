# JCS Briefings — audio publishing pipeline

Added 25 Sep 2026. Jonathan supplied `publish_briefing.py` and
`cover.png` directly (uploaded to a Claude Code session; they live on
his Mac under iCloud Drive, not reachable from any cloud session).

**What it is**, per the script's own docstring: renders a spoken-
briefing script with ElevenLabs, uploads the mp3 to Supabase Storage,
and publishes/updates a private podcast RSS feed ("JCS Briefings",
`itunes:block: Yes` — not publicly listed). Runs on Jonathan's Mac via
`launchd` watching an inbox folder of script files, or one-off via
`--script`. Standard library only, no dependencies. Keys live in
`~/.config/briefings/env` on the Mac, outside iCloud — never in this
repo.

**Confirmed 25 Sep: the pipeline works.** Jonathan confirmed there's a
mock (test) episode already on the JCS Briefings feed — it has
actually rendered, uploaded and published, not just been written.
Against the daily-audio agenda in `GETTING-STARTED.md`, that proves
steps 1-3 (vendor, bytes, delivery). Still open: a real script (step 4
— nothing generates daily content for it yet), a schedule (step 5 —
the `--inbox` watch mode exists but no routine feeds it), and actually
switching it on (step 6). Still unconfirmed: whether this session's
`audio-briefing` skill calls this exact script or a separate
implementation of the same idea.

See the script's own docstring for full usage. Not modified — copied
verbatim.

**`cover.png`** replaced 25 Sep 2026 with a photo Jonathan supplied
directly (converted from the uploaded .webp to PNG, 2000×2000, square).
