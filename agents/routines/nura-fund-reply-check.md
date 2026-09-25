---
name: "Nura Fund reply check"
trigger_id: trig_01AueKLvU8RCJGBmM7F1aUKH
platform: Cowork Routine (Claude)
schedule_utc: "0 22 * * *"
schedule_local: "daily 08:00 Brisbane"
enabled: true
model: claude-sonnet-5
mcp_connections: Todoist, Xero, Supabase, Cloudflare_Developer_Platform, Canva, Gmail, Superhuman_Mail, Resend, Otter, Google_Calendar, ElevenLabs, Granola, Google_Drive, Invideo, Notion, Claude_Code_Remote
captured: 2026-09-25
found: 2026-09-17 (not created by any session tracked in this repo)
---

# Nura Fund reply check

Discovered 17 Sep 2026 while checking a connector fix on a different
routine — it exists, is enabled, and is fully connected, but was never
captured here. Captured verbatim 25 Sep 2026 per the "copy first,
refactor later" migration rule (see `agents/README.md`). Nobody has
reviewed whether it should be streamlined; it's recorded as-is.

**What it watches:** a single Gmail/Superhuman thread on Charlotte
Project's Nura Fund grant application (Meliore Foundation, USD
$300,000), waiting on a reply that unblocks a stuck "Invited Amount"
field in the SmartSimple portal. Runs once a day; only speaks up when
something actually changes — silence is not itself reported.

## Prompt (captured verbatim, 25 Sep 2026)

```
Check whether Meliore Foundation (Matt Gould and team) has replied to Charlotte Project's Nura Fund grant application status update (SmartSimple ref 2609-4252).

Use the Superhuman Mail MCP tools with acting_email set to jonathan@charlotteproject.au. Find the thread titled "Charlotte-Nura Fund-2609-4252-Grant Application" (thread_id 1a07b0e0d481c200 as of Sep 2026 — confirm via list_threads if that id has changed) and check for any new incoming messages from matt.gould@climatecomms.org or other Meliore/CommsHub staff (David Turnbull, Wyclife Ouma, Claraluz Keiser, Tonnia Johanson, Meliore Operations) since Jonathan's last outgoing message in that thread, which asked why the "Invited Amount" field is blank/locked in the SmartSimple portal, blocking submission.

If there IS a new reply from Meliore/Matt Gould's side: this run is noteworthy. Summarize what they said in plain terms, especially anything about the Invited Amount field, an invite number, or next steps to submit — this is what Jonathan is waiting on to unblock a USD $300,000 grant request. Do not draft or send any email — Jonathan reviews and sends everything himself, no exceptions.

If there is NO new reply yet: this run is not noteworthy. Just note briefly that there's still no response — no need to alert Jonathan for silence, only when something actually changes.

Context for the fresh session: Charlotte Project Pty Ltd, Jonathan Schleifer's climate advocacy org, separate from Breakthrough Strategies Co. This is a live, time-sensitive funding blocker, not routine inbox triage — stay narrowly focused on this one thread.
```

## Notes for whoever picks this up

- **Overlaps the Nura Fund thread already referenced in
  `prompts/nura-country-assessment.md`** (a different, unrelated Nura
  Fund engagement — Mary Fitzgerald's Middle Powers country assessment,
  not this grant application). Same funder name, two separate pieces of
  work; don't conflate them.
- Once the grant either lands or is confirmed dead, this routine should
  be disabled rather than left running indefinitely on a closed thread
  — nobody has set an end condition for it yet.
- Fully connected already (16 connectors); no connector fix needed here,
  unlike Charlotte PM and Kiera's review check.
