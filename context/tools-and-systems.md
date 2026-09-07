# Tools & Systems

## Task / commitment tracking

- **Todoist** — source of truth for Donna's task tracking. Labels:
  `donna` (own commitment), `donna-processed` (dedup marker),
  `donna-needs-routing` (unclear owner/routing).

## Meetings

- **Granola** — preferred meeting-notes source; canonical over Otter/Calendar
  when a meeting appears in more than one.
- **Otter** — secondary meeting transcript source.
- **Google Calendar** — meeting/time-block source.

## Comms

- **Gmail / Superhuman** — connector is DRAFT ONLY. Automations must never
  send email on Jonathan's behalf, only create drafts for him to send.

## Notion

- Session log — written by the `session-tracker` skill.
- Run History — data source `ed04d10a-a5ae-427a-b42d-ebff0de97482`.
- Donna Log — data source `7cafcc7b-ede6-41a2-82be-57af5d6b41a8`.
- "Weekly AAR" database — running log of every weekly review.

## Time tracking

- **Toggl** — hours by client/project, checked against retainer time caps.

## Voice / audio

- **ElevenLabs** — text-to-speech for Donna's audio briefing and the AAR
  spoken edition.
  **Confirmed (30 Aug 2026, tested live via curl):** raw REST egress from
  this environment is blocked by *organization policy*, not a
  vendor-specific allowlist — `api.elevenlabs.io`, `api.openai.com`, and
  `api.fish.audio` all return `connect_rejected` identically. This isn't
  fixable from inside a Routine's prompt.
  **What actually works:** the ElevenLabs **MCP connector**
  (`creative_generate_speech` etc.) runs server-side on ElevenLabs'
  infrastructure and bypasses this block entirely — Donna's End of Day
  already uses it successfully for generation. The real remaining gap is
  narrower than "can't reach ElevenLabs": the MCP tool returns a hosted
  flow URL, not raw downloadable mp3 bytes, so there's no file to attach
  to a Gmail draft yet. Weekly AAR's raw-REST-first approach was the wrong
  path from the start — it should use the MCP tool like Donna does, not
  fall back past it to a blocked direct call.
- **Fish Audio** (`api.fish.audio`) — the TTS vendor Eytan's `DailyDigest`
  repo actually uses (not ElevenLabs, despite the name similarity in past
  conversations here). Runs as a persistent Fly.io service with normal
  unrestricted egress, which is *why* its direct-REST approach works —
  not a technique portable into this sandboxed environment. Worth
  borrowing vendor-agnostic: its voice-script system-prompt contract
  (280–320 words, no markdown, anonymous narrator, spoken-friendly text
  normalization for acronyms/numbers/%) and its player-page aesthetic
  (dark gradient background, white rounded card, speed controls).

## Connector quirks found 5 Sep 2026

- **Xero connector is linked to Charlotte Project Pty Ltd**, not
  Breakthrough Strategies Co. It sees the Charlotte invoices only. BTS
  invoices have to be read from Xero's emailed copies in Gmail
  (`from:messaging-service@post.xero.com`), which started July 2026;
  before that BTS used Thriday. Gaps in the BTS invoice number sequence
  are deleted mistakes, not missing customers.
- **Notion Organisations** (data source e51e1250-24c1-43b8-80fe-e7e9ccc733bd)
  now carries Client Type = Current Client / Prospect / Past Client /
  Funder / Partner / Ally / Remove, matching `worlds/consulting.md`.
  The connector cannot delete pages; rows marked Remove wait for a manual
  delete. Each page update is one tool call, so bulk changes prompt per
  row unless the session is in auto mode.
- **Google Calendar semantic search** misses plain event titles; search
  Gmail for the event name instead.
- **Egress** also blocks mastersgames.com.au; use WebSearch for public
  facts when a fetch is refused.

---
_Seeded from the live prompts of the Donna and Weekly AAR routines._
