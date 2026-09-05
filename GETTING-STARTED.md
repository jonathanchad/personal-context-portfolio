# Getting Started — what's still open

The structure is in place and four routines read from it. What remains is
confirming the parts that were pattern-matched rather than stated.

## Confirm (highest value first)

1. **`people.md`** — any role still marked *?*.
2. **`worlds/consulting.md`** — the Notion "Current Client" list looks
   stale (Lock the Gate, BZE, Independent Schools NSW, ECF) — confirm.
3. **`goals-and-priorities.md`** — date of the P&C time capsule event.
4. **`communication-style.md`** — signature phrases; whether the register
   shifts by audience.
5. **`worlds/personal.md`** — P&C title (executive, which office?);
   anything else agents should protect.

## How to update

Tell any Claude Code session the correction; it edits `context/`, appends
to `memory/log.md` where the change matters, and pushes to `main`. The
routines pick it up on their next run. The Weekly AAR will also propose
updates every Friday in its "Context updates" section.

## Tips

- Specific, not aspirational. Agents need ground truth.
- Short beats long. A world file is one screen, not five.
- Update `context/`, never the routine prompts.
