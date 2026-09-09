---
name: "EthicalJobs applicant intake — AFAE Comms Lead"
trigger_id: trig_014UjeWWKzY5fDtxYEHb1z9L
platform: Cowork Routine (Claude)
schedule_utc: "0 13 * * 0-4"
schedule_local: "weekdays 23:00 Brisbane"
enabled: false
deleted: 2026-09-09 (routine removed from Cowork; prompt kept for the record)
model: claude-opus-5
last_run: never 
captured: 2026-09-09
---

# EthicalJobs applicant intake — AFAE Comms Lead

Captured verbatim from the live Cowork Routine on 9 Sep 2026, per the
migration rule: copy first, refactor later. Metadata above; the prompt
below is untouched. Purpose, inputs and outputs are summarised in
`agents/README.md`.

## Prompt (verbatim)

```
Run the EthicalJobs applicant intake for Jonathan's AFAE Communications Lead role (job 567172).

Invoke the `ethicaljobs-applicant-intake` skill and follow it end to end. This is an unattended scheduled run, so:

- Do NOT wait for approval before downloading. The skill's Step 3 approval gate is waived for this run — treat "just go" as given. Still show the new names and count in your final report.
- Go all the way through: read the roster, diff against processed.json, download each new applicant's documents, file them into per-applicant folders, write the batch manifest, update the ledger, then invoke the applicant analyser skill on the batch.
- Follow the skill's selection-verification discipline strictly. Confirm the detail pane actually changed to the intended applicant before every download. A stuck pane produces duplicate files under correct-looking names, which is worse than an obvious failure — if the pane won't advance after a couple of tries, stop the run.
- Leave the "Move to" dropdown and the Shortlist / Not Suitable buttons alone. Downloading is read-only; stage moves are Jonathan's call after he's read the analysis.
- If more than about twenty applicants are new, download the twenty most recent, say clearly in your report that you capped it and how many are still waiting, and stop there.

If you can't get in — Chrome isn't reachable, the browser extension isn't connected, the device bridge to Jonathan's Mac is unavailable, or the dashboard shows a login screen — stop immediately. Do not attempt to authenticate and do not go looking for saved credentials. Report plainly what you tried and what blocked it, so Jonathan knows the batch is still sitting there. Don't retry in a loop.

Report at the end: how many were new, who they are, what documents came down, where the batch is filed, what the analyser said, and anything that needs a human eye (applicants with no documents, failed downloads, possible resubmissions).

Australian English. Write like a person — no AI flourishes.
```
