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

## Next build, once the context package is signed off

Daily audio brief with a real mp3 attached. The ElevenLabs MCP connector
can generate speech but the bytes never reach the routine; direct REST
is blocked from remote sessions. Jonathan's call, 5 Sep: wire it up with
ElevenLabs or something else, and a small Fly.io service is acceptable
(the pattern in Eytan's DailyDigest). Design the service around the
routine output in this repo, not around a new prompt.

## How to update

Tell any Claude Code session the correction; it edits `context/`, appends
to `memory/log.md` where the change matters, and pushes to `main`. The
routines pick it up on their next run. The Weekly AAR will also propose
updates every Friday in its "Context updates" section.

## Tips

- Specific, not aspirational. Agents need ground truth.
- Short beats long. A world file is one screen, not five.
- Update `context/`, never the routine prompts.
