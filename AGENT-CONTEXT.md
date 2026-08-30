# Agent Context — Read This First

This repo is Jonathan Schleifer's personal, git-based shared context — the
single source of truth any agent or automation acting on his behalf should
read before doing its job. It exists so facts about who he is, what he's
working on, what tools connect where, and how he wants things done live in
**one place** instead of being copy-pasted and drifting across a dozen
separate automation prompts.

This is for personal use. Not a product, not licensed out.

## Where things live

- `context/identity.md` — who Jonathan is
- `context/current-projects.md` — active clients, campaigns, products.
  **This is the file to update when a client/project starts, ends, or
  changes status** — not the individual automation prompts.
- `context/tools-and-systems.md` — what connects to what, plus known
  quirks (e.g. the ElevenLabs egress block)
- `context/preferences-and-constraints.md` — hard rules any agent acting
  as/for Jonathan must respect
- `templates/`, `examples/`, `wiring/`, `interview-protocol/` — the
  original template-portfolio material this repo started as. Kept for
  reference; not yet cleaned up for personal-only use.

## How an automation should use this

1. On every run, pull the current version of this repo before doing
   anything else (`git clone` or `git pull`). It's git-based specifically
   so the same fetch works whether the agent is Claude Code, Cowork, or
   whatever comes next.
2. Read the `context/` files relevant to the job at hand.
3. If a fact here conflicts with something hardcoded elsewhere in your
   prompt, **this repo wins** — it's the canonical, most-recently-updated
   version.
4. Don't fabricate anything that isn't in these files. If you need a fact
   that isn't here, say so rather than guessing.

## Wired-in automations (Cowork Routines)

- **Morning brief**
- **Donna — Processor v2** (meeting notes → tasks)
- **Donna — End of Day** (reconcile + audio email)
- **Weekly After Action Review (AAR)**

Each of these now starts with a context-sync step pointing here instead of
carrying its own copy of Jonathan's identity and client list. Update the
files above, not the individual routine prompts, when something changes.
