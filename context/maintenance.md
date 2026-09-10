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
| `people.md` | Weekly | Donna and the AAR propose new/changed people; Notion Contacts stays the CRM | New counterparty appears in meetings or mail |
| `memory/log.md` | Every notable change | Claude Code sessions append; AAR proposes | Any decision that changes context |
| `accounts.md` | Rarely | Jonathan; the morning scan reports against it | A mailbox or calendar is added or dropped |
| `../agents/` | When a routine changes | Claude Code session re-captures the prompt verbatim; Jonathan decides what runs | Any edit to a Cowork Routine |

## The loop

1. **Any routine or session that makes a judgment call ends with a
   "Context updates" section** — concrete proposed lines, not prose —
   whenever it catches its own miscall or Jonathan corrects it. Not just
   the Weekly AAR: the Morning Chief of Staff does this daily now (see
   `agents/routines/morning-chief-of-staff.md` Step 6), and any Cowork or
   Desktop session should when a correction needs verifying against a
   real inbox or calendar thread before it's trusted.
2. **Jonathan corrects in plain English** — a reply, a message in any
   session — not a printed markup and not a git patch. If the correction
   needs checking against source data (was a thread actually quiet?),
   that happens in whichever session has the mailbox/calendar access;
   the output is still a plain "Context updates" block.
3. **Next Claude Code session applies it and pushes.** Paste or attach
   the block; a Claude Code session has git push access, Cowork sessions
   don't, so this hand-off stays for now. A git patch still works if one
   shows up (9-10 Sep did it that way) but isn't the expected path —
   it's more machinery than the job needs.
4. **Every morning:** the Morning Chief of Staff reads the updated
   `accounts.md`, `worlds/` and `personal.md` and plans against current
   state, including whatever the previous day's correction added.
5. **All day:** Donna routes commitments using `worlds/consulting.md` and
   `worlds/charlotte.md` for client shorthand and counterparties.

**Open question, worth testing:** whether a Cowork/Desktop session can
push a branch or open a PR directly via the GitHub connector, which
would remove the "paste into Claude Code" hand-off entirely. Untested as
of 10 Sep 2026 — try it next time a correction comes through and note
the result here.

## Rule

If a fact isn't in `context/`, an agent says so rather than guessing —
and proposes the line to add. That proposal is how the repo grows.
