# Memory

Where the running record lives. Agents read this to find what happened;
they don't reconstruct history from scratch.

## Canonical (Notion — agents write here already)

| Record | Where | Written by |
|---|---|---|
| **Weekly AAR** — the decision log. Dated, candid, running. | Notion database "Weekly AAR" (data source `f3e0c2e7-0c39-4b6d-a9d5-1d9c98d2f22d`) | Weekly AAR routine, Fridays |
| **Run History** — every Donna processor / end-of-day run | Notion data source `ed04d10a-a5ae-427a-b42d-ebff0de97482` | Donna |
| **Donna Log** — every surfaced commitment | Notion data source `7cafcc7b-ede6-41a2-82be-57af5d6b41a8` | Donna |
| **Cowork Session Log** — every Claude session, topics, decisions | Notion, via `session-tracker` | Every session |
| **Client Retainers** — hours against caps | Notion, via `client-time-tracker` | Session wrap-up |

## In-repo (`memory/log.md`)

A short, dated log of decisions and changes that alter this context —
new client, retainer ended, hire made, blocker cleared, a rule changed.
Not a diary. One line to a paragraph per entry. Append; never rewrite.

Who appends: Claude Code sessions directly; the Weekly AAR proposes
entries in its "Context updates" section (routines can't push to git),
and the next session applies them. See `maintenance.md`.
