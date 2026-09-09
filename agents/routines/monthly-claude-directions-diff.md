---
name: "Monthly Claude directions diff"
trigger_id: trig_01FM98hWh5naTiTW6isAzXo3
platform: Cowork Routine (Claude)
schedule_utc: "0 4 1 * *"
schedule_local: "1st of month 14:00 Brisbane"
enabled: true
model: claude-opus-5
last_run: 2026-09-01T04:05:56.623685035Z ROUTINE_RUN_STATUS_SUCCEEDED
captured: 2026-09-09
---

# Monthly Claude directions diff

Captured verbatim from the live Cowork Routine on 9 Sep 2026, per the
migration rule: copy first, refactor later. Metadata above; the prompt
below is untouched. Purpose, inputs and outputs are summarised in
`agents/README.md`.

## Prompt (verbatim)

```
Run the monthly Claude directions drift check for Jonathan Schleifer (Breakthrough Strategies Co.). This is an unattended scheduled run — make reasonable calls and report, don't ask questions.

WHAT TO DO

1. Query the Notion Sessions database (data source ff762165-db5c-4b9e-a398-7ca33980de7b) for all sessions in the last 60 days. Group by the Project multi-select, and note each project's session count and most recent session date.

2. Compare that picture against Jonathan's current Cowork directions (his personal preferences, visible in your system context). Specifically check:
   - Does the "Live workstreams" list still match where the sessions actually are? Flag any workstream with 10+ sessions in the window that isn't named, and any named workstream with zero sessions in the window.
   - Do any instructions reference a workflow that a connected MCP now does natively? The known failure mode is telling Claude to hand Jonathan an export file when the tool could write directly (Todoist, Notion, Gmail, Calendar, Drive, Xero, Supabase are all connected).
   - Do any instructions reference file paths, databases, or skills that no longer exist? Verify before claiming — check the filesystem, list the skills, query Notion.
   - Are there skills in ~/.claude/skills that do work the directions describe manually, or that aren't named in the directions at all?

3. Write up the findings as a short markdown file: what changed, what to retire, what to add, and exact replacement wording for anything that needs rewriting. Keep it tight — this is a maintenance check, not a full audit. If nothing material has drifted, say so in three lines and stop.

4. Deliver the file to Jonathan and add a p2 Todoist task to the "Claude directions refresh" section of the SystemsCleanUp2026 project (id 6g6wX8hRFhfCfqmc) if anything needs his action.

CONTEXT

The baseline is the audit run on 27 July 2026, which found: the Todoist CSV export rule was obsolete (MCP writes directly), the /mnt/user-data/outputs path didn't exist, the BFF "offer to log at the end" rule should be "log as you go", the handoff-document rule duplicated the session-tracker and tool-documentation skills, and the projects list was five months stale — it named six dormant projects and omitted BE YSG (92 sessions that year) and OPPO entirely.

Write in Australian English. Be concrete and evidence-based — cite session counts and dates, not impressions.
```
