# Getting Started — what's still open

The structure is in place. See `agents/README.md` for the full,
current routine inventory (14 entries as of 25 Sep, several deleted or
retired) — this file only tracks what's still open.

## Open: Kiera's review reminder still needs connectors

Zero-connector bug (see `context/maintenance.md`'s "Known limitation"
note) also hit **"Check for Kiera's review (day 3)"**
(`trig_01N9kagMTCy81UM1KS2myUym`) — a one-off AFAE-contract check-in,
not a full routine, so it needs a much smaller fix than Charlotte PM
did: just **Gmail** and **Superhuman_Mail** attached by hand in the
Routines UI. Flagged 17 Sep, not yet confirmed done. Its last scheduled
check is 22 Sep; if that's passed with no fix, the check-in chain has
already silently died and someone needs to ask Jonathan whether Kiera
ever replied.

## Closed 17-25 Sep

- **Charlotte Project Manager's connectors**, fixed 17 Sep — five days
  with zero connectors after two failed API-side attempts, resolved by
  Jonathan attaching them by hand in the Routines UI. Confirmed live.
  See `agents/README.md`.
- **Two undocumented routines captured**, 25 Sep — "Nura Fund reply
  check" and "Monthly billing reconstruction — BTS" existed, fully
  connected, doing real work, with no record in this repo. Now captured
  verbatim in `agents/routines/` per the standard "copy first" rule;
  see `agents/README.md`'s inventory table (rows 13-14). Neither has
  been reviewed for streamlining or overlap with anything else yet —
  the billing reconstruction routine in particular reads a `memory`
  project file this repo doesn't own
  (`/projects/019d9b46-a3e0-74ca-b872-86d6feafe901/rate_card.md`) and
  flags a real unresolved YSG billing-basis conflict worth checking
  against `worlds/consulting.md`.

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
   (5-8 rows) rather than turning into a task list; does the RAG status
   actually stay honest (recomputed with real evidence, not left on
   whatever it was last); does "Owner: Jonathan" on most RAID rows
   spread out once hiring closes. See `agents/routines/charlotte-pm.md`'s
   "Open questions" section.
4. **Calendar naming convention, adopted 13 Sep** (`context/calendar-
   conventions.md`) — watch whether Claude sessions actually apply the
   tag/duration/travel-block rules when creating events, and whether the
   Weekly AAR's new spot-check (Step 1.6) catches real drift or just
   says "looks fine" every week without checking hard enough to matter.

## Daily audio — likely already solved, needs Jonathan to confirm

**Update, 25 Sep:** Jonathan supplied a working audio pipeline —
`tools/briefings/publish_briefing.py` — that renders a script with
ElevenLabs, uploads to Supabase Storage, and publishes a private
podcast feed. This session's `audio-briefing` skill description
matches its job description closely enough that it's likely the same
pipeline, or calls it. See `tools/briefings/README.md`. This probably
answers most of the agenda below (vendor decided: ElevenLabs REST +
Supabase, not Fly.io; delivery proven: a podcast feed, arguably better
than the Gmail-attachment or player-page options considered). Not
confirmed end to end — can't run from a cloud session (needs Mac-local
keys). **Before anyone works this agenda again: ask Jonathan whether
this pipeline is live and tested, and whether it retires this whole
section.**

## Original agenda, 9 Sep (superseded above pending confirmation)

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
