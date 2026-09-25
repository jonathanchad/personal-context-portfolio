---
name: "Monthly billing reconstruction — BTS"
trigger_id: trig_01XbPYfNpnUzY6JaRPCQsHd8
platform: Cowork Routine (Claude)
schedule_utc: "0 22 1 * *"
schedule_local: "2nd of the month, 08:00 Brisbane"
enabled: true
model: claude-opus-5
mcp_connections: Todoist, Xero, Supabase, Cloudflare_Developer_Platform, Canva, Gmail, Superhuman_Mail, Resend, Otter, Google_Calendar, ElevenLabs, Granola, Google_Drive, Invideo, Notion, Claude_Code_Remote
captured: 2026-09-25
found: 2026-09-17 (not created by any session tracked in this repo)
---

# Monthly billing reconstruction — BTS

Discovered 17 Sep 2026 while checking a connector fix on a different
routine — it exists, is enabled, and is fully connected, but was never
captured here. Captured verbatim 25 Sep 2026 per the "copy first,
refactor later" migration rule (see `agents/README.md`). Nobody has
reviewed whether it should be streamlined; it's recorded as-is.

**What it does:** the problem statement in its own prompt says it
plainly — Jonathan under-records his own time, the Notion Sessions
ledger is never complete enough to invoice from (one cited month showed
2.0 recorded billable hours against ~13.6 hours of documented work, and
he judged the real figure higher again). Once a month it sweeps six
separate evidence sources (Donna Log, Granola, Otter, Calendar, Gmail
sent mail, Todoist completions), reconciles them into the Notion
Sessions ledger, applies a detailed set of per-client billing rules,
flags rate/cap conflicts against source-of-truth documents rather than
trusting Notion's own retainer notes, and produces an invoice-ready
`.xlsx` schedule. It never invoices or contacts a client itself —
Jonathan raises every invoice by hand.

## Prompt (captured verbatim, 25 Sep 2026)

```
Run the monthly billing reconstruction for Breakthrough Strategies Co. (Jonathan Schleifer, Brisbane, Australia/Brisbane timezone). Target period is THE MONTH JUST ENDED — work out the dates from today, don't assume.

Australian English. Be concise in chat; the deliverable carries the detail.

## Why this exists
Jonathan under-records his own time and works in many places that never get tracked formally. The Notion Sessions ledger is never complete enough to invoice from — in August 2026 it showed 2.0 billable hours for the whole month against ~13.6 hours of documented work, and he judged the real figure far higher again. Your job is to sweep every system that holds evidence of work, reconstruct the month, correct the ledger, and hand him an invoice-ready schedule. He raises the invoices himself.

## Step 1 — What the ledger claims
Notion Sessions: `collection://ff762165-db5c-4b9e-a398-7ca33980de7b`. Query all rows dated in the target month. Note rows with no Hours and rows that look mis-flagged on Billable.

Notion Client Retainers: `collection://f354ddc1-3078-4877-a731-789ff70a9c2a`. Pull rate, retainer type, Active, budget cap, monthly hours target, billing entity and sensitivity for every client. See the warning in Step 5 before trusting any of it.

## Step 2 — Sweep every evidence source
Work through ALL of these. Each catches work the others miss.

1. **Donna Log** — `collection://7cafcc7b-ede6-41a2-82be-57af5d6b41a8`. This is the richest source: Donna already reconciles Granola, Otter and Calendar into one row per commitment, decision or action item, with a Project field naming the client, a Meeting Date, a Sources field (granola/otter/calendar) and a Note Link. Query the target month. Every meeting represented here is work that happened. Cross-check against Donna Run History (`collection://ed04d10a-a5ae-427a-b42d-ebff0de97482`) for runs that found meetings, and Donna Routing (`collection://ce6638b0-19ce-4352-9cef-e2958cf4caf0`) for the domain/keyword → project rules if a client attribution is unclear.
2. **Granola** — list meetings for the month directly. Donna may have missed runs or had gaps.
3. **Otter** — search the month. It catches meetings Granola didn't record.
4. **Google Calendar** — all events. Filter out personal and family items: dog park, squad, [gym], school runs and pickups, kids' activities and sport, meals, flights, [Travel] blocks.
5. **Gmail** — sent mail in the target month is evidence of work. Search for substantial client correspondence he sent, per client, and treat a dense run of drafting or negotiation as billable work even where no meeting exists.
6. **Todoist** — completed tasks in the month, by project. Use find-completed-tasks and find-activity with his own initiatorId. Completed work with no corresponding session row is unrecorded time.

Deduplicate hard: the same meeting will appear in Donna, Granola, Otter and Calendar. Count it once, and prefer the actual duration from Calendar or Granola over an estimate.

NOTE ON CLAUDE CONVERSATIONS: there is no tool that searches Jonathan's Claude conversation history, so you cannot mine it. The Notion Sessions database is the closest proxy — the session-tracker skill logs Cowork and Claude Code sessions there. Treat any Sessions row with a real title but no Hours as a session that happened and needs a duration estimate, and say plainly in your reply that this part is estimated.

## Step 3 — Correct the ledger
Write the reconstruction back into Notion Sessions so it matches what gets billed:
- Create Quick Log rows (Status "Complete") for documented work with no row.
- Fix Hours and Billable on rows that are wrong.
- In the Summary field, name the source: "Reconstructed from Donna Log" / "from calendar" / "from Granola" / "from sent mail" / "estimate — no contemporaneous record".
Never silently inflate. An estimate stays labelled an estimate everywhere it appears.

## Step 4 — Billing rules
- AFAE: ALL AFAE time bills to AFAE — comms lead interviews, Gianni Sottile check-ins and Alex Linton check-ins included. Settled; don't re-litigate.
- Charlotte: Jonathan's own entity. Not billable to a client.
- BTS Internal, CapacityAI, Erso, OPPO, VibeMentor, AI Signal: internal R&D, not billable.
- Ithaca Creek P&C: volunteer, unpaid.
- Client Development: BD, not billable.
- Coalition participation (e.g. the Diesel Group fortnightly) is not billable client time.
- Boundless Earth work that is Charlotte-related is not billable consulting.
If a workstream doesn't clearly fit, ask rather than guess.

## Step 5 — Verify caps and rates before trusting them
The Notion Client Retainers fields are Jonathan's own notes, not contracts, and they have been wrong.
- BE YSG: Notion says $350/hr with a $20,000 cap. The "YSG Budget" sheet in Google Drive says Breakthrough Strategies is allocated $30,000 ex-GST for Phase 1 on a $1,000/day basis, with a Phase 2 management line at $450/hour. As at September 2026 this was UNRESOLVED — check the Todoist task "Resolve YSG billing basis before invoicing August" in the BE Your Shout Gas project before billing any YSG time.
- Also check `/projects/019d9b46-a3e0-74ca-b872-86d6feafe901/rate_card.md` in memory for current rates by client.
- For project-based clients, compute cumulative billed-to-date and flag anything past 80% of cap, or any month that would breach it.
- LAN: the 20 hrs/month target ran Apr–Jun 2026 with a July review. Confirm the engagement is live before invoicing.

## Step 6 — Deliverable
Build an .xlsx billing schedule: a Summary tab (client, billing entity, hours, rate, fees ex-GST, GST at 10%, total inc GST), one line-detail tab per billable client with the evidence source named on each line, and a cap tracker for any capped client. Arial throughout, real formulas not hardcoded results, recalculated so there are no formula errors. Read the xlsx skill before building. Save to /mnt/user-data/outputs/ and deliver with SendUserFile.

Add a "Possible unbilled work" section listing evidence you found but could not confidently attribute or price — don't drop it silently. On the Summary tab, list every flag he needs before sending: estimates, cap positions, lapsed retainers, rate conflicts, possible double-billing against project-based invoices.

## Step 7 — Hand off
Invoices are raised in the Breakthrough Strategies Co. Xero org, which is NOT the Xero org connected to these sessions (that one is Charlotte Project Pty Ltd). Do not create invoices. Do not send anything to any client — no email, no messages, under any circumstances. Produce the schedule, give him the totals per client, and stop.

If something material is ambiguous and nobody answers, make the conservative choice, state the assumption plainly at the top of your reply, and carry on.
```

## Notes for whoever picks this up

- **Reads and writes far more of the stack than any other routine in
  this repo**: six separate evidence sources reconciled against two
  Notion databases, plus a `memory` project file
  (`/projects/019d9b46-a3e0-74ca-b872-86d6feafe901/rate_card.md`) this
  repo has no record of and doesn't own. Worth understanding where that
  file actually lives before touching this routine.
- **The YSG billing-basis conflict it flags (Notion vs the Google Drive
  budget sheet) is a real, unresolved discrepancy** as of its own
  prompt text — check whether `context/worlds/consulting.md` reflects
  the same conflict; if not, that's a gap worth closing.
- **Reconfirm the Xero org warning is still accurate** (BTS invoices
  live in a different Xero org than the one connected to these
  sessions, which is Charlotte's) against
  `context/tools-and-systems.md`'s connector-quirks section, which
  already documents this from the other direction.
- Only reads/writes Notion, never touches Xero directly despite Xero
  being in its connector list — worth confirming that's intentional
  (a defence against accidentally creating invoices) rather than an
  oversight, next time this routine is reviewed.
