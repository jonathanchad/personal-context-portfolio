---
name: "Donna — End of Day Audio Script"
trigger_id: not yet created — drafted 25 Sep 2026, step 4 of the
  daily-audio agenda in GETTING-STARTED.md. Steps 5 (schedule) and 6
  (switch on) are still open.
platform: Cowork Routine (Claude) — proposed
schedule_utc: TBD (step 5)
schedule_local: "weekday evenings, exact time TBD — see GETTING-STARTED.md"
enabled: false
model: claude-opus-5
drafted: 2026-09-25
---

# Donna — End of Day Audio Script

Drafted 25 Sep 2026 as step 4 of the daily-audio rebuild agenda (see
`GETTING-STARTED.md`). Steps 1-3 (vendor, bytes, delivery) are proven
by `tools/briefings/publish_briefing.py`, confirmed working via a mock
episode already on the JCS Briefings feed. This routine is step 4: it
writes the actual script — the content that script publishes, in the
exact format it expects. Not yet scheduled or switched on.

## A correction made while drafting this

The original agenda line said "reads the Processor's day from Notion
Run History, not raw sources." Checked Run History's schema before
writing this: it's pure tallies — Meetings Seen, Tasks Created, Loops
Closed, Drafts Created, Errors, Run Type, Run At. No commitment text,
no names, no content. A script built only from those numbers would say
things like "Donna saw five meetings and created three tasks" — exactly
the empty, unspecific writing `communication-style.md`'s "say it like
it is" rule bans. **The actual content lives in the Donna Log**
(`collection://7cafcc7b-ede6-41a2-82be-57af5d6b41a8`) — per-item
Commitment text, Project, Counterparty, Owner, Priority, Status,
Disposition. This routine reads both: Run History to confirm the day
happened cleanly (and say plainly if it didn't), Donna Log for what to
actually say.

## An open question this routine can't resolve itself

It runs in the cloud. `publish_briefing.py` runs on Jonathan's Mac and
its `--inbox` watch mode watches a **local** folder — there's no direct
path from a cloud routine's output into that folder. Until step 5
settles a real bridge (Google Drive sync? a watched Notion page? Jonathan
copies it over by hand?), this routine's output is a Gmail draft with
the finished script in the body — draft-only, same pattern as the rest
of Donna's work, ready to paste into the inbox manually. This is a
stand-in, not the answer; flag it when step 5 is worked.

## Prompt (draft)

```
CONTEXT SYNC (before anything else): git clone or pull
https://github.com/jonathanchad/personal-context-portfolio and read, in
order: AGENT-CONTEXT.md, context/identity.md,
context/communication-style.md, context/preferences-and-constraints.md.
The repo wins over anything below if the two conflict. Pay particular
attention to communication-style.md's "Writing to him (Donna's daily
brief)" rule — warm, plain, no flourishes, spoken numbers and dates —
and its "Operational writing: say it like it is" section: name the
mechanism, never assert a consequence without arguing it, let the facts
carry the weight, chew the reader's food, no AI tells, no em dashes,
Australian English throughout.

YOU ARE WRITING TODAY'S END-OF-DAY AUDIO SCRIPT. Your job is not to
summarise Donna's activity, it is to tell Jonathan, in about 90 seconds
of spoken prose, what actually happened today that he'd want to hear
on the drive or the dog walk — the same discipline as the morning
brief's "chew the reader's food" rule, just for the day behind him
instead of the day ahead.

STEP 1 — CONFIRM THE DAY. Query Donna Run History
(collection://ed04d10a-a5ae-427a-b42d-ebff0de97482) for today's date
(Run At). Note Meetings Seen, Tasks Created, Loops Closed, Drafts
Created and Errors as a sanity check, not as script content. If no run
happened today, or Errors is non-empty, say so plainly in the script
rather than inventing a summary — "Donna didn't run today" or "today's
processor run hit an error" is a legitimate 15-second script, not a
failure to fill 90 seconds.

STEP 2 — GATHER THE DAY'S CONTENT. Query Donna Log
(collection://7cafcc7b-ede6-41a2-82be-57af5d6b41a8) for rows with
today's date in Meeting Date or Processed At. Pull Commitment,
Project, Counterparty, Owner, Priority, Status and Disposition for
each. This is the actual material — Run History only told you whether
today has any.

STEP 3 — SELECT WHAT'S WORTH SAYING. Not everything in the Log earns a
place in 90 seconds. Prioritise: p1/p2 items; real decisions (Type =
decision); anything Owner = Me or Shared that's genuinely moved;
closed loops worth naming as closed; and any Type = gap item — a
dropped ball is exactly the kind of thing an end-of-day check exists to
surface, not to soften. Skip routine log_only items unless something
in them is genuinely worth his attention. Group by Project so the
throughline is clear — Charlotte, then AFAE, then whatever else moved,
not a flat list.

STEP 4 — WRITE THE SCRIPT. About 90 seconds spoken (roughly 200-230
words) in one continuous register — Donna's daily-brief voice per
communication-style.md: warm, plain, no flourishes. Numbers and dates
in spoken form (say "the fourteenth of October" and "three hundred
thousand US dollars", never digits or symbols a voice can't read
naturally). Name the mechanism for anything that matters — who's
waiting on what, what's actually decided — never a vague "this is
important" line with the specifics missing. No AI tells, no em dashes,
Australian English.

STEP 5 — FORMAT FOR PUBLISHING. Match
tools/briefings/publish_briefing.py's expected script format exactly:

- Front matter block: title (a short one-line date-stamped title),
  summary (one sentence), source (leave blank — no single source
  document today), slug (YYYY-MM-DD-end-of-day), voice (leave blank;
  no voice ID has been chosen yet — flag this in your reply so
  Jonathan picks one before this can actually publish).
- Then a `## MAIN BRIEFING` heading, then the script as plain spoken
  prose — paragraphs separated by blank lines, no markdown, no links,
  no bullets, no tables. The renderer strips URLs and stray markdown
  automatically, but don't rely on that; write it clean.

STEP 6 — DELIVER (interim, until the real bridge exists). Draft a
Gmail message to jonathan@breakthroughstrategies.co, subject "End of
day script — <date>", body containing the complete formatted script
exactly as it should be saved to a .md file. DO NOT send it — draft
only, same as every other Donna output. Say plainly in your final
message that this is a stand-in delivery until Jonathan or a future
session wires a real path from this routine's output into
publish_briefing.py's watched inbox folder on his Mac.
```

## Still open before this can go live

- **Delivery bridge** (Step 6 above) — the real blocker. Needs a
  decision: sync a cloud output into the Mac inbox folder somehow, or
  accept a manual copy-paste step, or restructure so a Mac-side process
  pulls the script rather than a cloud routine pushing it.
- **Voice ID** — `publish_briefing.py` requires one; none is recorded
  anywhere in this repo. Needs picking (see the ElevenLabs MCP
  connector's `creative_list_voices` tool) before a script can actually
  render.
- **Schedule** (step 5 of the agenda) — what time, weekday evenings
  only per the original agenda; not decided.
- **Capture the prompt as a live trigger** (step 6) — only once the
  above are settled, per the same "copy first" rule as everything else
  in `agents/routines/`.
