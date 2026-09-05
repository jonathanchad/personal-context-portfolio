# Getting Started — what's still open

The structure is in place and four routines read from it. What remains is
confirming the parts that were pattern-matched rather than stated.

## Confirm (highest value first)

1. **`worlds/consulting.md`** — client shorthand ("BE"), whether CDA is
   still active, who Moira / Margo / Jonno are, and the AFAE hire outcome.
2. **`worlds/charlotte.md`** — roles for Larissa, Mike, Nicky, Casey,
   Simon, Locke.
3. **`goals-and-priorities.md`** — the "Tradeoffs" section: is the
   meetings-over-closes pattern something to counterbalance, or how you
   actually want to work?
4. **`communication-style.md`** — the three open questions at the bottom.
5. **`worlds/personal.md`** — P&C role; anything else agents should protect.

## How to update

Tell any Claude Code session the correction; it edits `context/`, appends
to `memory/log.md` where the change matters, and pushes to `main`. The
routines pick it up on their next run. The Weekly AAR will also propose
updates every Friday in its "Context updates" section.

## Tips

- Specific, not aspirational. Agents need ground truth.
- Short beats long. A world file is one screen, not five.
- Update `context/`, never the routine prompts.
