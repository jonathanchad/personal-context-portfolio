# Getting Started — what's still open

The structure is in place and four routines read from it. What remains is
confirming the parts that were pattern-matched rather than stated.

## Confirm (highest value first)

1. **Notion Organisations**: five rows are marked "Remove" (AISNSW, PIE,
   Soul Freedom Movement, STEF, The Safer Air Project). The connector
   cannot delete pages; delete them in Notion.
2. **`people.md`**: confirm "Dan Cheryl" (ACTU) and "Annie O'Rourke" vs
   "Ann O'Reilly" (89 Degrees East) spellings.
3. **`worlds/personal.md`**: anything else agents should protect.

## Agent streamlining (from the 9 Sep brain dump)

`agents/README.md` has the inventory and the plan. Decisions Jonathan
owes: delete the four dead routines; keep or fold the monthly directions
diff; re-enable or retire Donna End of Day; confirm the P&C, LAN and
Rackley mailbox addresses for `context/accounts.md`. Then the morning
brief is rebuilt as the Morning Chief of Staff.

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

## How to update

Tell any Claude Code session the correction; it edits `context/`, appends
to `memory/log.md` where the change matters, and pushes to `main`. The
routines pick it up on their next run. The Weekly AAR will also propose
updates every Friday in its "Context updates" section.

## Tips

- Specific, not aspirational. Agents need ground truth.
- Short beats long. A world file is one screen, not five.
- Update `context/`, never the routine prompts.
