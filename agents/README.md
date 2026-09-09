# Agents — inventory, overlaps, and the streamlining plan

Captured 9 Sep 2026 from the live Cowork Routines (`routines/`, one file
per routine, prompts verbatim) after Jonathan's brain dump with ChatGPT
(`DESIGN-NOTES-2026-09-09.md`). This file is the map. Nothing has been
refactored yet; the migration rule is copy first, then review together,
then refactor shared logic into `context/`.

## 1. What runs today

| # | Routine | Schedule (Brisbane) | Status | Reads | Writes | Job in one line |
|---|---|---|---|---|---|---|
| 1 | **Morning brief** | weekdays 07:00 | live | repo, Google Calendar (primary only), Gmail/Superhuman (generic), Todoist, Notion, Granola | HTML artifact | One-day plan across all worlds via the generic `/morning` skill |
| 2 | **Donna — Processor v2** | weekdays 10:00 to 18:00, 2-hourly | live | repo, Granola, Otter, Calendar, Gmail, Notion, Todoist | Todoist tasks, Gmail drafts, Notion Donna Log and Run History | Meeting notes into commitments and follow-up drafts |
| 3 | **Donna — End of Day (audio)** | daily 18:15 | **disabled 6 Sep** | repo, Todoist, Gmail, Notion, ElevenLabs | Todoist completions, Gmail draft with audio link, Notion Run History | Reconcile the day's loops and read a 90-second summary |
| 4 | **Weekly AAR** | Saturday 06:00 | live | repo, Calendar, Todoist, Notion, Granola, Otter | Notion AAR db, email, proposed context updates | Blunt weekly retrospective, drift check against goals |
| 5 | **Monthly Claude directions diff** | 1st, 14:00 | live | Notion Sessions db, Gmail, Calendar, Todoist | Report | Are the skills and standing instructions still what he actually does |
| 6 | **Watch for Allianz reply** | daily 09:00 | live | Gmail personal (via Superhuman acting_email) | Report | One low-volume inbox, one thread, until the claim closes |
| 7 | **AI Signal Benchmark** | 1st and 15th, 06:00 | live | Cloudflare KV, repo code | Benchmark output | Product pipeline, not personal ops |
| 8 | Donna — Processor (hourly) | hourly | dead since 24 Jul | | | Superseded by #2 |
| 9 | Donna — End of Day (email) | daily 17:00 | dead, never ran | | | Superseded by #3 |
| 10 | OPPO subscriber question drafter | every 4 h | dead, never ran | | | OPPO's own Cloudflare app handles this |
| 11 | EthicalJobs applicant intake | weekdays 23:00 | dead since Jul | | | Hire done (Alex Linton) |

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
- No feedback loop for "important". The AAR's context-updates section is
  the nearest thing and it runs weekly, not daily.

## 4. Streamlining plan (proposed, not applied)

**Delete now** (dead, superseded, or job finished): #8, #9, #10, #11.
Their prompts are preserved in `routines/`, so nothing is lost.

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

**Rebuild one thing**: the Morning brief becomes the **Morning Chief of
Staff**. It reads `context/accounts.md`, scans every registered mailbox
(Superhuman `acting_email` per account) for the last 72 hours plus
anything unread or pending, reads all seven calendars and deduplicates,
looks seven days ahead, reads Donna's overnight block instead of the raw
meeting notes, and outputs: what matters today, what it is at risk of
missing, one to three moves for open blocks, what is coming, the accounts
it checked, and the accounts with nothing to worry about. The Allianz
watch then becomes a line in the registry ("watch this thread"), not a
routine.

**Decide one thing**: End of Day. Either re-enable it as the evening
specialist once audio delivery works, or move its reconciliation into the
Processor's last run of the day and drop it. Two summaries a day plus a
weekly one is one too many unless the evening one is spoken.

**Then**: the platform-neutral repo the notes ask for is this one.
`agents/` holds definitions; `context/` holds shared context and rules;
`context/accounts.md` is the registry. Output schemas and adapters come
after the Chief of Staff rebuild, not before.

## 5. How to use this directory

- `routines/<name>.md`: one file per Cowork Routine, frontmatter metadata,
  prompt verbatim. Re-capture after any prompt change in Cowork.
- `DESIGN-NOTES-2026-09-09.md`: the brain dump this plan answers.
- When a routine prompt is rewritten, rewrite it here first, then paste
  into Cowork. The repo is the source of truth; Cowork is the runtime.
