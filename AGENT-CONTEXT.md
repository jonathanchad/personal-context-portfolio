# Agent Context — Read This First

This repo is Jonathan Schleifer's personal, git-based shared context — the
single source of truth any agent or automation acting on his behalf reads
before doing its job. Facts about who he is, the worlds he operates in,
what tools connect where, what he's optimising for, and how he wants
things done live in **one place** instead of drifting across a dozen
routine prompts.

Personal infrastructure. Not a product, not licensed out.

## Structure

Slow facts, per-world state, and a running memory — kept current by
agents wherever possible (see `context/maintenance.md`).

| Path | What it is | Read it when |
|---|---|---|
| `context/identity.md` | Who Jonathan is: roles, entities, background, family (one line) | Always |
| `context/preferences-and-constraints.md` | Hard rules, verification rules, what not to over-explain | Always |
| `context/goals-and-priorities.md` | What he's optimising for and deliberately not doing. **The Weekly AAR checks the week against this.** | Planning, prioritising, reviewing |
| `context/worlds/README.md` | Why the worlds are lenses on one life, and how they lean on each other | Before planning or prioritising across them |
| `context/worlds/charlotte.md` | Charlotte Project Pty Ltd: entity, Stage 2, the pitch, people | Anything Charlotte |
| `context/worlds/breakthrough-tools.md` | CapacityAI, AI Signal, Erso, OPPO: status, blockers, go-to-market pattern | Product work, pitches |
| `context/worlds/consulting.md` | Client retainers, caps, pipeline, counterparties, routing shorthand | Client work, Donna routing, billing |
| `context/worlds/personal.md` | Family, community roles, scheduling constraints | Scheduling, anything touching personal time |
| `context/people.md` | Who he works with, by organisation, tagged by world; points at the Notion CRM | Drafting to someone, meeting prep, routing |
| `context/communication-style.md` | Voice — points at the canonical writer skills | Writing as Jonathan |
| `context/tools-and-systems.md` | Connectors, data sources, known quirks (egress block, MCP path) | Wiring, debugging |
| `context/memory/README.md` | Where the running record lives (Notion AAR db, Run History, Donna Log) | Finding what happened |
| `context/memory/log.md` | Dated log of decisions that changed this context | Before proposing a change |
| `context/maintenance.md` | Who keeps each file current, and the weekly loop | Before editing anything here |

`templates/`, `examples/`, `wiring/`, `interview-protocol/` are the
original generic template this repo started from — reference only.

## How an automation uses this

1. **Sync first.** `git clone` or `git pull` this repo before anything
   else. Git-based so the same fetch works in Claude Code, Cowork, or
   whatever comes next.
2. **Read what the job needs** (table above). Identity and preferences
   always; the relevant `worlds/` file for the task.
3. **The repo wins.** If a fact here conflicts with something hardcoded
   in your prompt, use this.
4. **Don't fabricate.** If a fact isn't here, say so and propose the line
   to add. Routines end with a "Context updates" section for exactly this;
   the next Claude Code session applies it and pushes.
5. **Charlotte is an entity, not a person.**
6. **Worlds are lenses, not silos.** Jonathan's day blends across
   parenting, the P&C, Charlotte, clients and the tools. Plan one day;
   carry constraints across; keep the guardrails. See
   `context/worlds/README.md`.

## Wired-in automations (Cowork Routines)

| Routine | Reads | Writes back |
|---|---|---|
| **Morning brief** (weekday mornings) | identity, goals, worlds/*, personal | — |
| **Donna — Processor v2** (weekdays, 2-hourly) | identity, tools, preferences, worlds/consulting + charlotte | Todoist, Notion Donna Log / Run History |
| **Donna — End of Day** (daily 18:15) | identity, tools, preferences, worlds/consulting | Todoist, Gmail draft, Notion Run History |
| **Weekly AAR** (Fridays) | identity, goals, worlds/*, memory/log | Notion AAR db; **proposes context updates** |

Update the files here, not the routine prompts, when something changes.
