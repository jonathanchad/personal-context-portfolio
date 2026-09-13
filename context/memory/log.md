# Context log

Newest first. Format: `YYYY-MM-DD — entry` with a source in brackets.

- 2026-09-13 — **Charlotte PM rebuilt on real PM discipline.** Jonathan
  pushed back that the first version (12 Sep) tracked status but didn't
  manage anything. Researched what a PM actually does (RAID logs,
  decision logs, action registers, RAG status reporting) and rebuilt
  the Notion tracker: added Assumption, Issue, Decision and Action row
  types alongside Objective/Milestone/Priority/Risk/Note, added Owner
  and Severity properties, reclassified the unconfirmed paid-media
  proposal from a Priority into an Issue, seeded 3 Assumptions, 4
  Decisions and 5 Actions from `worlds/charlotte.md`, and added a single
  "Charlotte overall status (RAG)" rollup row with explicit criteria for
  what flips it. The routine's prompt now runs the RAID log, the
  decision log and the action register each fire, and the Morning Chief
  of Staff leads with the RAG row rather than re-deriving Charlotte
  priority itself. Full citations in
  `agents/routines/charlotte-pm.md`'s "Design basis" section. [this
  session, responding to Jonathan: "The PM's responsibility should be
  actually project management... identify what an agentic PM would do"]

- 2026-09-13 — **Calendar naming convention adopted; no separate
  Scheduler agent.** Jonathan drafted a detailed convention (tag
  register, meeting-title pattern, 25/50-minute durations, travel-time
  buffers) — filed as `context/calendar-conventions.md`. Decided this
  is a standing rule any agent applies at event-creation time, not a
  scheduled routine; the Weekly AAR's existing drift check now also
  spot-checks compliance (Step 1.6) instead of a new job being built.
  Rationale in `context/maintenance.md`. [this session, responding to
  Jonathan: "i drafted these calendar directions - do we need a
  separate Scheduler agent?"]

- 2026-09-13 — Resend connector added (transactional/bulk email). Not
  yet wired into any routine; noted in `tools-and-systems.md` as
  available for a future EDM-sending flow. [Jonathan]

- 2026-09-12 — **Charlotte Project Manager built — pilot for per-project
  PMs.** Jonathan's design thought: agents that hold a project's
  timeline and objectives, check whether today's work serves them, and
  keep a maintained active priority list, feeding the Morning Chief of
  Staff instead of reporting to Jonathan directly. Built a Notion
  database "Charlotte Timeline & Priorities" (under Charlotte — Hub;
  data source `collection://a8c5654c-0cf1-4416-9447-419d0efd42d1`),
  seeded from `worlds/charlotte.md`: 3 Objectives, 12 dated Milestones
  through Mar 2027, 7 ranked Priority rows (each stating which milestone
  it Serves), 5 Risks. Created the Cowork trigger
  (`trig_01JgLDQF5roRynHpNzHDtzty`, Mon/Thu 05:30 Brisbane) and wired
  the Morning Chief of Staff to read the tracker's top priorities and
  any at-risk milestone for Charlotte specifically. **Not yet
  functional**: the trigger has zero MCP connectors because it was
  created from a Claude Code session with none to pass through, and a
  follow-up update didn't fix it — needs manual connector attachment in
  the claude.ai Routines UI before its first fire (Mon 14 Sep). See
  `GETTING-STARTED.md` and `context/maintenance.md`. If the pattern
  works, Breakthrough Tools gets a portfolio variant next; a standalone
  Breakthrough Strategies PM was judged unnecessary given Donna, the
  Morning CoS and `client-time-tracker` already cover that ground.
  [this session, responding to Jonathan's design thought about
  per-project chiefs of staff]

- 2026-09-10 — **Feedback loop lightened.** The 9-10 Sep round trip
  (print the brief, mark it up by hand, a separate session verifies
  against mailbox and writes a git patch, upload the patch) was more
  machinery than the job needs. New standard: correct any session in
  plain English; if the correction needs checking against a real thread
  or event, that happens in whichever session has the access; either way
  the output is a plain "Context updates" block (same pattern the Weekly
  AAR already used weekly), pasted into a Claude Code session to apply.
  The Morning Chief of Staff now proposes its own "Context updates"
  section daily (Step 6) instead of only via the weekly AAR. Git patches
  still work as a fallback but aren't the expected path. Open question
  to test: whether a Cowork/Desktop session can push a PR directly via
  the GitHub connector and remove the paste step too. See
  `context/maintenance.md`. [this session, responding to Jonathan: "the
  am JCS brief was great! what is next in improving this tool"]

- 2026-09-10 — Jonathan lifted the blanket "never name the sons" rule for
  internal agent output. Owen and Jacob can be named in the morning brief and
  similar internal work; they stay out of client-facing and published
  material. `worlds/personal.md` updated. Reason: attribution matters for
  planning — the brief mis-assigned Owen's 5:15 swim squad to Jonathan and
  Owen's UQ Transition Meet to Jonathan's Pan Pacs preparation, and unnamed
  boys made both errors easy to miss. [Jonathan]

- 2026-09-10 — Charlotte calendar access widened from free/busy to full detail.
  It now returns titles, attendees and response status. Still not visible to
  the connector: any P&C, Rackley or Masters calendar, and the Charlotte weekly
  leadership hour, which does not appear on the Charlotte calendar. [Jonathan]

- 2026-09-10 — **Morning brief feedback, marked up by Jonathan on the printed brief.**
  Corrections that must change future runs, not just that day's report:
  - **Check the counterparty thread before calling anything "quiet".** The brief
    said ACBF had gone quiet and told him to chase before the 15 Sep Senate
    vote. Wrong: Marguerite replied 6 Sep saying she lacks bandwidth for INFM
    right now, and Jonathan replied 7 Sep parking it himself — "Focus everything
    on the 15th... Let's pick it up the week of the 21st." The thread is
    labelled `[Superhuman]/AI/Waiting` with a reminder set. A 72-hour inbox
    sweep plus a stale line in `consulting.md` is not enough; search the
    counterparty by name and read their thread before asserting silence.
  - **A draft still in the folder is not an open loop.** Jonathan marked several
    of the nine unsent drafts "HANDLED in mtg". Drafts get overtaken by
    meetings and calls and are never deleted. Report a draft as an unsent close
    only after checking whether the substance moved by another route.
  - **Name which product.** "Daily Brief" is ambiguous across at least three
    things: the CapacityAI in-app Today page, the OPPO email brief, and 25G
    Daily Clips. Always say which.
  - **Attribute family commitments to the right person.** The 5:15 swim is his
    son's session; Jonathan goes to the gym. The UQ Transition Meet is his
    son's, not Jonathan's Pan Pacs preparation. Do not fold the boys'
    activities into Jonathan's own training.
  - **Don't assign work that is not his.** The LAN AEC disclosure return is
    signed by Paul, not Jonathan.
  - **Drop the dramatic headline.** "Two things are quietly on fire" — his note:
    "too much." Lead with the day, not a hook.
  - **Format:** the five-minute cluster should be a discrete list, not a
    paragraph.
  - Confirmed good catches, keep this class of finding: the stale "Sydney —
    booked" hold, the Becky Corbett unsent role email ("Good catch!"), the
    Safina time-capsule cutoff, the Kiera document access, the open block.
  - Already handled before the brief ran, so old news by the time he read it:
    the 2pm/4pm Tradie Shift time question, and soccer cover (Katie had it).

- 2026-09-10 — Stale calendar entries Jonathan flagged for deletion: Aqualicious
  masters squad Sunday 8:30 ("no more"), and the Saturday 6:00am squad, which
  is now a 6:30 birthday party. [Jonathan]

- 2026-09-05 — Hand-off prompt written: prompts/nura-country-assessment.md
  (finish the Middle Powers Australian country assessment from the 1 Sep
  draft, using the ALP research, the "Understanding Australia" memo,
  polling on hand, Erso/OPPO/AI Signal; Dione note first). [this session]
- 2026-09-09 — Personal world file: added Jonathan's Rackley Swim Team
  Centenary Race Volunteer Organiser role as a commitment to protect,
  and an explicit rule never to name the sons. Confirm list closed;
  GETTING-STARTED now just tracks watching the Chief of Staff's first
  run. [this session]
- 2026-09-09 — Jonathan deleted the five duplicate Notion Organisations
  rows (AISNSW, PIE, Soul Freedom Movement, STEF, The Safer Air Project)
  by hand in Notion. Confirmed gone by query. Client list reconciliation
  is now fully closed out, in the repo and in Notion. [Jonathan]
- 2026-09-09 — Two spellings confirmed and corrected: 89 Degrees East's
  Annie O'Rourke is Founder & Chief Creative Officer (was flagged
  against a mis-heard "Ann O'Reilly"; CEO Alister Jordan added).
  ACTU's contact is Dan Sherrell, not "Dan Cheryl". [Jonathan; 89degreeseast.com]
- 2026-09-09 — Morning Chief of Staff moved from 07:00 to 06:00 Brisbane;
  Jonathan sometimes works that early. [Jonathan]
- 2026-09-09 — Morning brief rebuilt as the Morning Chief of Staff. Same
  Cowork Routine (trig_01BZdfHczNrNwrooRuEXtW61), new prompt: scans all 8
  registered mailboxes via Superhuman acting_email, reads all 7 Google
  Calendars, 7-day look-ahead, reports what was checked and what's
  clear, suggests 1-3 moves for open blocks. Superhuman Mail connector
  attached to the routine for the first time. Old prompt kept at
  agents/routines/morning-brief.md, marked superseded. [Jonathan]
- 2026-09-09 — Your Shout Gas admin account linked. All 8 registry
  accounts now linked to the Superhuman connector. Account registry
  complete; the morning scan can reach every mailbox. [Jonathan]
- 2026-09-09 — LAN operations account linked to the Superhuman
  connector. 7 of 8 registry accounts now linked. [Jonathan]
- 2026-09-09 — P&C President account linked to the Superhuman connector.
  6 of 8 registry accounts now linked. [Jonathan]
- 2026-09-09 — Rackley Swim Team account linked to the Superhuman
  connector. 5 of 8 registry accounts now linked. [Jonathan]
- 2026-09-09 — Corrected the Rackley address: .com.au, not .com. [Jonathan]
- 2026-09-09 — Final mailbox list from Jonathan, replacing the earlier
  draft: 8 accounts with named roles (BTS CEO/principal, Charlotte
  CEO/Founder, personal, P&C President, AFAE Maintenance x2 — flagged,
  same label on two different domains — Your Shout Gas admin, and
  Rackley Swim Team Centenary race volunteer organiser, which replaces
  the earlier swim-club guess). Written into accounts.md verbatim.
  [Jonathan]
- 2026-09-09 — Mailbox scan set settled: add Your Shout Gas admin (active
  campaign, Jonathan wants eyes on it); keep Andrew's LAN mailbox out
  (not his to triage). 8 of 11 addresses in scope once linked. Jonathan
  will add the missing accounts to Superhuman himself. [Jonathan]
- 2026-09-09 — Full mailbox list from Jonathan's Superhuman screenshot
  (11 addresses) written into accounts.md; 4 linked to the connector.
  Proposed scan set: BTS, Charlotte, gmail, P&C president, swim club,
  AFAE ops, LAN operations. Jonathan: "I don't need all of those";
  awaiting his cut. [Jonathan]
- 2026-09-09 — End of Day (audio) retired, to be rebuilt from scratch in
  a dedicated session with the wiring verified first. Agenda in
  GETTING-STARTED. [Jonathan]
- 2026-09-09 — Four dead routines deleted from Cowork at Jonathan's
  instruction: Donna Processor (hourly), Donna End of Day (email), OPPO
  subscriber question drafter, EthicalJobs applicant intake. Prompts
  remain in agents/routines/. Seven routines remain, six live plus the
  disabled End of Day (audio). [Jonathan]
- 2026-09-09 — Agent inventory. Jonathan's ChatGPT brain dump (Morning
  Chief of Staff, account registry, specialists feeding a cross-domain
  decider, platform-neutral repo) saved to agents/DESIGN-NOTES. All 11
  Cowork Routines captured verbatim into agents/routines/. Findings: 6
  live, 4 dead, Donna End of Day disabled 6 Sep; the generic /morning
  skill reads one calendar and no account list; four mailboxes wired via
  Superhuman, P&C, LAN ops and Rackley not connected. context/accounts.md
  started. Plan in agents/README.md, not yet applied. [this session]
- 2026-09-05 — Voice rule added: clarity, storytelling, humour; "chew
  the reader's food for them". Never presume shared context, inside
  jokes or prior analysis. Concise is not the same as truncated.
  [Jonathan]
- 2026-09-05 — Notion Organisations corrected to match consulting.md:
  Funder/Ally/Remove options added; 30 rows updated; Nura Fund, Meliore,
  GSCC, 89 Degrees East created; Solutions for Climate renamed CANA;
  Sunrise Foundation renamed The Sunrise Project. Five rows marked
  Remove for Jonathan to delete. [this session]
- 2026-09-05 — Pan Pacs = Pan Pacific Masters Games, Gold Coast, 6 to
  15 Nov 2026, swimming 12 to 14 Nov; events 50 free, 50 fly, mixed 100
  and 200 free. Rebecca Chew and Kajute at Boundless; TradieShift team
  is Alex Vitlin, Jonny, Liana, Jess Miller (independent consultants
  under one brand); Gianni Sottile is Boundless's contractor running
  Solar Sharer; ACTU is an ally, contact Dan Cheryl. Voice sign-offs
  written from sent mail. Next build: daily audio, Fly.io acceptable.
  [Jonathan]
- 2026-09-05 — Nura item identified from Mary Fitzgerald's 14 Aug
  "analysis request": the Australian country assessment for Nura Fund's
  Middle Powers climate comms strategy, EUR 500 honorarium, due end Aug,
  overdue. Boundless cleared use of the ALP research on 4 Sep; Dione
  wants the specific points first. [Gmail]
- 2026-09-05 — INV-0002 and INV-0010 were never real: gaps in the Xero
  sequence from deleted mistakes, not missing customers. Dropped from
  the open list. [Jonathan]
- 2026-09-05 — Corrections after the worksheet: "prospects, not
  pending" (no contracts); GSCC funded Your Shout Gas; Reliability Watch
  is a coal-emissions reporting tool, PMO is the Prime Minister's Office
  (subject and partner), neither a funder; 89 Degrees East is a polling
  and research firm Jonathan works with, Rebecca Huntley key; AFAE role =
  Solar Sharer leadership plus operations (no CEO there); LAN billed to
  CANA; Nura is owed a political-environment summary (BTS work); SCEC
  (Sunshine Coast Environment Council) past, paid by ELF, contact Steph.
  [Jonathan]
- 2026-09-05 — Client Reconciliation Worksheet returned annotated.
  consulting.md rewritten into Funders (Boundless Earth, CANA, Nura,
  Meliore) / Current (AFAE, JCN, Lock the Gate, LAN) / Pending (ACBF
  OPPO $3k/mo, Sunrise, Environment Victoria, Footy, ISNSW, GSCC under
  BE, Together as CapacityAI prospect) / Not clients (89DE, Reliability
  Watch, PMO, COP31 Epic, Politiv, Lockslie, Surfers) / Past (1MW via
  ELA, CDA, BZE, ECF, Meliore, the Notion past list). Open: INV-0002 and
  INV-0010, Nura "report on AMS", ACTU. [Jonathan, worksheet scan]
- 2026-09-05 — Client list pass: Lock the Gate occasional; BZE not a
  client; Independent Schools NSW dormant, course again next year; Footy
  for Climate light (board survey; fundraising training coming); ECF
  unknown to Jonathan, mark former. ACBF is a live OPPO prospect
  (proposal sent 31 Aug, mail). Sunrise asked for a Victorian election
  proposal including OPPO. [Jonathan + Gmail]
- 2026-09-05 — Jonathan is President of the Ithaca Creek State School
  P&C; duties per the Constitution (in the pandc-compliance skill). Two
  big P&C priorities: icsspandc.com live, and the time capsule event.
  Added to identity, personal.md, goals Tradeoffs, people.md. [Jonathan]
- 2026-09-05 — Time capsule event fixed: Sun 25 Oct 2026, 10am, ICSS
  school hall, 49 Lugg St Bardon. [Jonathan]
- 2026-09-05 — Tradeoffs stated: protect the P&C time capsule event
  (big priority this month); consulting retainer hours can slide;
  LinkedIn and pitch work can definitely slide; everything else still
  has to find time. Written into goals Tradeoffs and personal.md.
  [Jonathan]
- 2026-09-05 — Charlotte 30-day priority: build the team AND assemble a
  bench of support consultants and creatives in parallel (no time to
  sequence); get experiments off the ground; content as soon as
  possible. Victorian election (28 Nov 2026) is a milestone, not the
  launch. Les White and Simon Hobbs definite and on payroll; Moira is a
  potential adviser only. [Jonathan]
- 2026-09-05 — Tools goal made concrete: 2–3 paying users each for
  CapacityAI (JCN already) and OPPO; land one for AI Signal. Erso has
  no revenue target and stays in beta. Purpose is revenue to justify
  further development. [Jonathan]
- 2026-09-05 — Goals set by Jonathan: (1) crush Charlotte's first three
  months and deliver on the promise; (2) Pan Pacs: sub-30 50 free, PB 50
  fly; (3) keep momentum on the Breakthrough tools. Charlotte sprint
  spine written into charlotte.md from Boundless Schedule 1, the
  Yajilarra outcomes paper and Leadership Meeting 1. Yajilarra is a
  funder, not a MEL partner (earlier guess corrected). [this session]

- 2026-09-05 — Jonathan set the voice: friendly, funny (self-deprecating,
  Ryan Reynolds register), concise; no AI tells ever; no em dashes ever;
  email = context, ask, explanation if needed, ask again. Written into
  `communication-style.md` and as a hard rule in preferences. [this session]

- 2026-09-05 — Jonathan: Mike = Mike Cannon-Brookes (BE funder); Simon is
  a paid Charlotte consultant; Think Big FG (Sally Hurst) is the BTS
  bookkeeper; Sentiment Agency = influencer-focused digital/campaign shop;
  Nidhi Bolar = go-to graphic designer (India); Dave Rood introduced by
  Eytan; Moira = former PMO staffer with Katie, introduced by Austin
  Phillips, possible Charlotte consultant. [this session]
- 2026-09-05 — Built `people.md` from 60 days of calendar, Granola, sent
  mail, Notion Contacts/Organisations and the Charlotte outreach sheet.
  Resolved: LAN = Liberals Against Nuclear (winding down); CDA = Climate
  Defenders Australia; "Locke" = Les White (Lockslie Consulting); TS3 =
  TradieShift (Jess Miller); AFAE Comms Lead hired = Alex Linton. [this session]
- 2026-09-05 — Jonathan: "BE" = Boundless Earth; CDA no longer active;
  Margot is director of AFAE; Jonno La Nauze is CEO of Environment
  Victoria. Asked for a much fuller people directory pulled from email,
  calendar, Granola and the Charlotte contacts spreadsheet. [this session]

- 2026-09-05 — Jonathan: the old ten-file system "divided my life up too
  much"; worlds are lenses on one blended day, guardrails stay. Added
  `worlds/README.md` and rule 6 in AGENT-CONTEXT.md; Morning brief told
  to plan one timeline. [this session]

- 2026-08-30 — Restructured `context/` from the generic 10-file template
  to worlds/ + goals + memory + maintenance. Wired Morning brief, Donna
  (Processor v2, End of Day) and Weekly AAR to sync from this repo.
  Confirmed: Zoltar and VibeMentor never came to fruition; Breakthrough
  Tools = CapacityAI, AI Signal, Erso, OPPO. [this session]
- 2026-08-30 — Confirmed raw REST egress to ElevenLabs / OpenAI / Fish
  Audio is blocked by org policy from routine environments; the ElevenLabs
  MCP connector is the working path. [tested live]
- 2026-08-06 — Charlotte "Mike" three-pillar deck delivered to Larissa,
  ~10 days ahead of the 17 Aug meeting. [Weekly AAR, 8 Aug]
- 2026-08-03 — AFAE Comms Lead: eight decline emails sent, individually
  signed. Second interview round then run (Alex Linton, Ben Manassah,
  Bibi Bello); finalists Alex vs Ben. Retainer over-servicing flagged for
  the third week. [Weekly AAR, 8 Aug]
- 2026-08 (week of 3 Aug) — AI Signal turned from dormant to ~AUD 30k of
  scoped work with 89 Degrees East by offering measurement of their
  Sunrise campaign rather than a software pitch. Named in the AAR as the
  repeatable go-to-market pattern. [Weekly AAR, 8 Aug]
- 2026-07-30 — Charlotte Project Pty Ltd registration confirmed;
  constitution accepted. [Notion entity page]
