# Getting Started — what's still open

The structure is in place. Six routines read from it live: Morning Chief
of Staff, Donna Processor v2, Weekly AAR, Monthly directions diff, the
Allianz watch, and the AI Signal benchmark. What remains is small.

## Fix before Monday: Charlotte Project Manager has no connectors

Built 12 Sep as the pilot for per-project PMs (see
`agents/routines/charlotte-pm.md`, `agents/README.md`). Its Notion
tracker ("Charlotte Timeline & Priorities", under the Charlotte — Hub
page) is seeded and ready. **The Cowork trigger itself
(`trig_01JgLDQF5roRynHpNzHDtzty`, Mon/Thu 05:30 Brisbane, next fire
Mon 14 Sep) has zero MCP connectors attached** — it was created from a
Claude Code session that had none to pass through, and a follow-up
update didn't fix it. As it stands it will fire Monday and fail with
nothing to work with.

**Fix, before Monday:** open the Routine in the claude.ai Routines UI
and attach Notion, Superhuman_Mail, Google_Calendar, Todoist and Gmail —
or ask a Cowork session (one that already holds those connectors, not a
remote Claude Code session like this one) to attach them. See
`context/maintenance.md`'s "Per-project PMs" section for why this
happened.

## Watch

1. **First Morning Chief of Staff run happened 10 Sep and Jonathan marked
   it up on paper.** The corrections are folded into
   `context/accounts.md` ("Importance signals — refinements from
   Jonathan") and `context/memory/log.md`: verify a counterparty thread
   before calling it quiet, treat unsent drafts as candidates not
   findings, name which "Daily Brief" product, check task ownership
   before assigning it to Jonathan, attribute Owen's and Jacob's own
   commitments to them rather than folding them into Jonathan's, and
   drop dramatic headlines. Keep watching the next few runs against this
   list — see `agents/README.md`.
2. **The feedback loop itself got lighter, 10 Sep.** No more printing
   and marking up: reply in plain English to whatever session you're
   correcting, it drafts a "Context updates" block (verified against the
   real inbox/calendar if the correction depends on one), and you paste
   that block into a Claude Code session to apply. The Morning Chief of
   Staff now proposes its own "Context updates" daily (Step 6) instead
   of waiting for the weekly AAR. See `context/maintenance.md`. Open
   question worth testing next time: can a Cowork/Desktop session push a
   PR directly via the GitHub connector and skip the paste step
   entirely?
3. **Once the Charlotte PM has connectors and has run a few times**,
   check: is Mon/Thu the right cadence, or should it run right after the
   Monday leadership hour instead; does the Morning Chief of Staff
   actually lean on the tracker for Charlotte's priorities or keep
   re-deriving them from the mailbox; is the priority list staying short
   (5-8 rows) rather than turning into a task list. See
   `agents/routines/charlotte-pm.md`'s "Open questions" section.

## Next build: daily audio, rebuilt from scratch (session to be scheduled)

Jonathan, 9 Sep: retire the old End of Day audio routine and rebuild it
from scratch in a working session, verifying every link before it goes
live. Walk in with this agenda:

1. **Decide the vendor and the path.** ElevenLabs via the MCP connector
   (works for generation, returns a hosted flow link, no mp3 bytes) or a
   small Fly.io service with open egress (DailyDigest pattern; Fish Audio
   or ElevenLabs REST). Fly.io is acceptable.
2. **Prove the bytes.** One test run that produces an mp3 file we can
   open, before any prompt is written.
3. **Prove delivery.** Gmail draft with the mp3 attached, or a player
   page the phone can open in one tap. Never a link that says "attached".
4. **Then the script.** 90 seconds, spoken-friendly, one register,
   reads the Processor's day from Notion Run History, not raw sources.
5. **Then the schedule.** Weekday evenings only; confirm the time.
6. **Only then** switch it on, and capture the prompt into
   `agents/routines/`.

Old prompt, for reference: `agents/routines/donna-end-of-day-reconcile-audio-email.md`.

## Smaller follow-ons noted in `agents/README.md`

- Donna should produce a clean dated "overnight" block the Morning Chief
  of Staff can read, instead of the Chief of Staff re-reading raw
  meeting notes.
- The Allianz watch is still its own routine rather than a line in
  `accounts.md`; folding it in would lose its guaranteed daily check on
  one thread, so it stays separate for now.
- Whether the Monthly directions diff should fold into the first-Saturday
  AAR run instead of its own schedule.

## How to update

Tell any Claude Code session the correction; it edits `context/`, appends
to `memory/log.md` where the change matters, and pushes to `main`. The
routines pick it up on their next run. The Weekly AAR will also propose
updates every Friday in its "Context updates" section.

## Tips

- Specific, not aspirational. Agents need ground truth.
- Short beats long. A world file is one screen, not five.
- Update `context/`, never the routine prompts.
