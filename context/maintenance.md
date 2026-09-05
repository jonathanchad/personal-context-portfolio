# Maintenance — who keeps what current

The failure mode this repo is designed against is staleness. Jonathan's
own AARs say the admin doesn't get closed, so the living parts must be
kept current by agents, not by hand.

| File | Changes how often | Kept current by | Trigger |
|---|---|---|---|
| `identity.md` | Rarely | Jonathan, in a Claude Code session | Life/entity change |
| `preferences-and-constraints.md` | Rarely | Jonathan | A rule changes or an agent gets something wrong |
| `communication-style.md` | Rarely | Jonathan; points at skills | Voice guidance changes in a skill |
| `tools-and-systems.md` | Occasionally | Whoever changes wiring | New connector, routine, or known-issue |
| `goals-and-priorities.md` | Quarterly | Jonathan sets; **Weekly AAR reports drift** every Friday | Quarter start; AAR flags stated-vs-actual gap |
| `worlds/charlotte.md` | Weekly-ish | Weekly AAR proposes; next Claude Code session applies | Hire, funder decision, workstream change |
| `worlds/breakthrough-tools.md` | Weekly-ish | Same; `tool-documentation` skill for product docs | Status change, blocker cleared, sale |
| `worlds/consulting.md` | Weekly | Weekly AAR proposes; Donna's routing rules consume it | Client starts/ends, cap changes, counterparty confirmed |
| `worlds/personal.md` | Rarely | Jonathan | Family/community change |
| `memory/log.md` | Every notable change | Claude Code sessions append; AAR proposes | Any decision that changes context |

## The loop

1. **Friday:** Weekly AAR clones the repo, reads `goals-and-priorities.md`
   and `worlds/`, reports where the week's hours went versus the stated
   priorities, and ends with a **"Context updates"** section — concrete
   proposed edits (new client, retainer ended, hire made, blocker cleared,
   memory entries).
2. **Next Claude Code session** (or Jonathan): applies those edits to
   `context/` and pushes. Routines can't push to git from their
   environments, so this step is human/session-driven for now.
3. **Every morning:** Morning brief reads the updated `worlds/` and
   `personal.md` and plans against current state.
4. **All day:** Donna routes commitments using `worlds/consulting.md` and
   `worlds/charlotte.md` for client shorthand and counterparties.

## Rule

If a fact isn't in `context/`, an agent says so rather than guessing —
and proposes the line to add. That proposal is how the repo grows.
