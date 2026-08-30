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
  **Known issue:** this cloud environment's network egress is proxied
  through a domain allowlist that returns 403 on `api.elevenlabs.io` (also
  `api.openai.com`, `api.cartesia.ai`). Expect a direct REST call to fail
  and fall back to the `read-aloud` skill's offline HTML player until that
  allowlist changes.

---
_Seeded from the live prompts of the Donna and Weekly AAR routines._
