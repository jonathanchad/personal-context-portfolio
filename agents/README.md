# Agents — inventory, overlaps, and the streamlining plan

Captured 9 Sep 2026 from the live Cowork Routines (`routines/`, one file
per routine, prompts verbatim) after Jonathan's brain dump with ChatGPT
(`DESIGN-NOTES-2026-09-09.md`). This file is the map. Nothing has been
refactored yet; the migration rule is copy first, then review together,
then refactor shared logic into `context/`.

## 1. What runs today

| # | Routine | Schedule (Brisbane) | Status | Reads | Writes | Job in one line |
|---|---|---|---|---|---|---|
| 1 | **Morning Chief of Staff** (rebuilt 9 Sep, was "Morning brief") | weekdays 06:00 | live | repo incl. accounts.md, all 8 registered mailboxes via Superhuman, 7 Google Calendars, Todoist, Charlotte Timeline & Priorities (Notion) | HTML artifact | Scans every mailbox and calendar, reports what it checked and what's clear, 7-day look-ahead, 1-3 moves for open blocks |
| 2 | **Donna — Processor v2** (importance gate added 13 Sep) | weekdays 10:00 to 18:00, 2-hourly | live | repo, Granola, Otter, Calendar, Gmail, Notion, Todoist | Todoist tasks (gated), Gmail drafts, Notion Donna Log and Run History (every extracted item, gated or not) | Meeting notes into commitments; only genuinely important ones become Todoist tasks, everything is logged either way |
| 3 | **Donna — End of Day (audio)** | daily 18:15 | **retired 9 Sep; rebuild from scratch later** | repo, Todoist, Gmail, Notion, ElevenLabs | Todoist completions, Gmail draft with audio link, Notion Run History | Reconcile the day's loops and read a 90-second summary |
| 4 | **Weekly AAR** | Saturday 06:00 | live | repo, Calendar, Todoist, Notion, Granola, Otter | Notion AAR db, email, proposed context updates | Blunt weekly retrospective, drift check against goals |
| 5 | **Monthly Claude directions diff** | 1st, 14:00 | live | Notion Sessions db, Gmail, Calendar, Todoist | Report | Are the skills and standing instructions still what he actually does |
| 6 | **Watch for Allianz reply** | daily 09:00 | live | Gmail personal (via Superhuman acting_email) | Report | One low-volume inbox, one thread, until the claim closes |
| 7 | **AI Signal Benchmark** | 1st and 15th, 06:00 | live | Cloudflare KV, repo code | Benchmark output | Product pipeline, not personal ops |
| 12 | **Charlotte Project Manager** (rebuilt 13 Sep on real PM discipline) | Mon and Thu, 05:30 | **created but not yet functional — see below** | repo worlds/charlotte.md, Charlotte Timeline & Priorities (Notion: Objectives/Milestones/Priorities/RAID log/Decision log/Action register), jonathan@charlotteproject.au, Charlotte calendar, Todoist | Notion tracker (writes state, not reports) | Backward-plans every milestone, runs a RAID log + decision log + action register, reports one RAG status, feeds the Morning Chief of Staff |
| 8 | Donna — Processor (hourly) | hourly | **deleted 9 Sep** | | | Superseded by #2; prompt kept in `routines/` |
| 9 | Donna — End of Day (email) | daily 17:00 | **deleted 9 Sep** | | | Superseded by #3; prompt kept |
| 10 | OPPO subscriber question drafter | every 4 h | **deleted 9 Sep** | | | Never ran; OPPO's own app handles replies; prompt kept |
| 11 | EthicalJobs applicant intake | weekdays 23:00 | **deleted 9 Sep** | | | Hire done (Alex Linton); prompt kept |

Other automation that is not a Cowork Routine but competes for the same
ground: the `morning-briefing` skill (a second, older morning brief that
triggers on "hey" in a session), `session-tracker` and
`client-time-tracker` (Notion logging at session start and end),
`tool-documentation`, `weekly-aar-spoken-edition`, the OPPO tracker's own
daily brief emails (Cloudflare), and Eytan's DailyDigest pattern (Fly.io)
that the audio work keeps borrowing from.

## 2. Where they overlap

- **Three things summarise the day back to Jonathan**: morning brief,
  End of Day, Weekly AAR. Two of them try to produce audio. None of them
  consumes the others' output; each re-reads the sources.
- **Todoist is read by four routines** (1, 2, 3, 4) and written by two
  (2, 3). The Processor and End of Day both close loops; the rule
  "conservative on evidence" is copied into both prompts.
- **Two drift checks**: the AAR checks the week against goals; the
  monthly diff checks the skills against session history. Same idea,
  different cadence, no shared definition of drift.
- **Meeting notes are read three times**: Processor (every 2 h), AAR
  (weekly), morning brief (via Granola, for context). Only the Processor
  should read them raw; the others should read the Processor's Notion
  output.
- **Prompts still carry context that now lives in the repo**: the
  Processor and End of Day prompts embed client shorthand, email
  identities and rules that `context/` owns. Repo wins by rule, but the
  duplication is where drift starts.

## 3. Gaps against the Chief of Staff design

The 9 Sep notes describe a morning Chief of Staff that checks every
registered inbox and calendar, reports what it checked, says what is
safe to ignore, looks seven days ahead, and suggests one to three things
for open blocks. Today's morning brief does none of the account-level
parts:

- The `/morning` skill fetches **one calendar, today only**, and treats
  email generically. It has no idea four mailboxes exist. The Allianz
  routine exists precisely because a low-volume inbox was being missed.
- No account registry existed until today (`context/accounts.md`). Four
  mailboxes are wired through Superhuman; the P&C, LAN operations and
  Rackley timing accounts are not connected anywhere.
- No "accounts checked" or "nothing to worry about" section.
- No seven-day look-ahead, no conflict or landmine detection.
- No open-block recommendations.
- ~~No feedback loop for "important".~~ **Fixed 10 Sep**: the Morning
  Chief of Staff now ends with its own daily "Context updates" section
  (Step 6), and the print-and-patch round trip from its first real run
  has been replaced with a plain-English reply → verify if needed →
  "Context updates" block → paste into Claude Code. See
  `context/maintenance.md`.
- **New 12 Sep: no agent checked whether today's work actually served a
  project's timeline** — only whether the inbox was current. Jonathan's
  design thought: a per-project PM that holds the timeline and
  objectives, backward-plans from them, and maintains an active priority
  list, feeding the Morning Chief of Staff rather than reporting to
  Jonathan directly. Charlotte is the pilot; see below.

## 4. Streamlining plan (proposed, not applied)

**Deleted 9 Sep 2026** (Jonathan's call): #8, #9, #10, #11. Their prompts
are preserved in `routines/` with `enabled: false` in the frontmatter.

**Keep as specialists** (they understand one domain):

- Donna Processor v2: meeting notes to commitments. Strip the embedded
  context; point it at `context/`. Add one output the Chief of Staff can
  read: a dated "overnight" block in Notion Run History.
- Weekly AAR: keep. It is the feedback loop the notes ask for; extend
  its "Context updates" to include importance corrections for the
  morning scan.
- AI Signal Benchmark: keep, it is product infrastructure. Move it out of
  the personal-ops list mentally.
- Monthly directions diff: fold into the AAR as a first-Saturday extra
  step, or keep if the monthly cadence matters. One drift definition.

**Rebuilt 9 Sep 2026.** The Morning brief is now the Morning Chief of
Staff (`morning-chief-of-staff.md`, same trigger_id as the old routine).
It reads `context/accounts.md` fresh every run, scans all 8 registered
mailboxes via Superhuman `acting_email`, reads all 7 Google Calendars and
deduplicates, looks 7 days ahead, and outputs: what matters today, what
it is at risk of missing, one to three moves for open blocks, what is
coming, every account and calendar it checked, and which of them had
nothing needing attention. Not yet done: it still reads raw meeting
notes rather than Donna's overnight output (Donna doesn't produce a
dated overnight block yet — a follow-on improvement), and the Allianz
watch is still its own routine rather than a registry line, since
folding it in would drop its daily-scan guarantee for one thread.

**Decided 9 Sep**: End of Day stays off and will be rebuilt from scratch
in a dedicated session, with the wiring verified end to end before it is
switched on. The Processor's last run of the day covers reconciliation
until then. Agenda for that session is in `GETTING-STARTED.md`.

**Then**: the platform-neutral repo the notes ask for is this one.
`agents/` holds definitions; `context/` holds shared context and rules;
`context/accounts.md` is the registry. Output schemas and adapters come
after the Chief of Staff rebuild, not before.

**Built 12 Sep 2026, pilot: Charlotte Project Manager.** Runs Mon/Thu
05:30 Brisbane. Reads the sprint's milestones and objectives (now a
Notion database, "Charlotte Timeline & Priorities", seeded from
`worlds/charlotte.md`), checks Charlotte's real activity since last run,
backward-plans each milestone against today's date, and maintains a
short ranked active priority list — each row stating which milestone it
actually serves. Writes state to Notion; doesn't email Jonathan except
one exception (a near-term milestone just went Blocked). The Morning
Chief of Staff reads the tracker's top priorities and any at-risk
milestone as its source of truth for Charlotte, instead of re-deriving
Charlotte priority from the mailbox alone. Full design and prompt:
`agents/routines/charlotte-pm.md`.

**Not yet functional — needs a manual fix before its first run
(Mon 14 Sep 05:30 Brisbane).** The Cowork trigger
(`trig_01JgLDQF5roRynHpNzHDtzty`) was created from a Claude Code session
that holds no connector grants to pass through, so it stores zero MCP
connectors — it can't reach Notion, Superhuman, the Charlotte calendar
or Todoist yet. Same underlying limitation the account already worked
around once for the Morning Chief of Staff, but this time it needs a
direct fix: open the Routine in the claude.ai Routines UI and attach
Notion, Superhuman_Mail, Google_Calendar, Todoist and Gmail, or ask
Claude to do it from a session that already holds those connectors
(a Cowork session, not this remote one). Until that's done the routine
will fire and fail with nothing to work with.

**If this pattern earns its keep**: Breakthrough Tools next, as a
portfolio variant (CapacityAI, AI Signal, Erso, OPPO each get a status
row rather than a separate PM). Hold off on a standalone Breakthrough
Strategies (consulting) PM — Donna, the Morning Chief of Staff and
`client-time-tracker` already cover most of that ground; strengthen
`consulting.md`'s deliverables detail first.

**Rebuilt again 13 Sep 2026** after Jonathan pushed back that the first
version tracked status without managing anything. Researched actual PM
discipline (RAID logs, decision logs, action registers, RAG status
reporting) and rebuilt the tracker and routine around it — see
`agents/routines/charlotte-pm.md`'s "Design basis" section for what
changed and why, with citations.

**Does the Charlotte PM replace Donna? No — different jobs.** Jonathan
asked, hoping the PM pattern could fix Donna's over-eager Todoist
writing. It can't, directly: Donna extracts commitments from meeting
notes (a transcription job, cross-cutting every world); the Charlotte
PM backward-plans one project's timeline against its milestones (a
judgement job, Charlotte-specific). What Donna actually needed was the
same discipline the PM already has — an explicit bar before something
earns a task rather than "everything mentioned becomes one" — so that
got fixed directly in Donna's own prompt (Step 2.6, "The Importance
Gate," 13 Sep): a task now needs to clear the same importance signals
as everywhere else in this repo, or it's logged (never lost) but not
put in front of Jonathan in Todoist.

## 5. How to use this directory

- `routines/<name>.md`: one file per Cowork Routine, frontmatter metadata,
  prompt verbatim. Re-capture after any prompt change in Cowork.
- `DESIGN-NOTES-2026-09-09.md`: the brain dump this plan answers.
- When a routine prompt is rewritten, rewrite it here first, then paste
  into Cowork. The repo is the source of truth; Cowork is the runtime.
