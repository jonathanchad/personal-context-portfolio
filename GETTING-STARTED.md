# Getting Started — what's still open

The structure is in place. Six routines read from it live: Morning Chief
of Staff, Donna Processor v2, Weekly AAR, Monthly directions diff, the
Allianz watch, and the AI Signal benchmark. What remains is small.

## Confirm (highest value first)

1. **Notion Organisations**: five rows are marked "Remove" (AISNSW, PIE,
   Soul Freedom Movement, STEF, The Safer Air Project). The connector
   cannot delete pages; delete them in Notion.
2. **`people.md`**: confirm "Dan Cheryl" (ACTU) and "Annie O'Rourke" vs
   "Ann O'Reilly" (89 Degrees East) spellings.
3. **`worlds/personal.md`**: anything else agents should protect.
4. **Watch the first Morning Chief of Staff run** (next weekday, 06:00
   Brisbane). It's new and unproven: check the report length, whether
   the "nothing to worry about" section reads as reassuring rather than
   padding, and whether all 8 mailboxes actually came back. Tune from
   there — see `agents/README.md`.

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
