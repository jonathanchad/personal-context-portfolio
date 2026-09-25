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

**Likely supersedes the "rebuild the daily audio routine from scratch"
item in `GETTING-STARTED.md`.** The session's `audio-briefing` skill
description — "Turn any document... into a well-explained spoken
briefing rendered with ElevenLabs and published to Jonathan's private
podcast feed" — matches this script's job exactly. Not confirmed end
to end from a cloud session (it can't run here — ElevenLabs and
Supabase aren't reachable from the sandboxed environment, same
constraint the script's own comment names for "the cloud workspace").
**Needs Jonathan to confirm**: is this pipeline actually live and
tested, does the `audio-briefing` skill call it or something else, and
does the old End of Day audio rebuild agenda in `GETTING-STARTED.md`
still apply or should it be retired in favour of this.

See the script's own docstring for full usage. Not modified — copied
verbatim.

**`cover.png`** replaced 25 Sep 2026 with a photo Jonathan supplied
directly (converted from the uploaded .webp to PNG, 2000×2000, square).
