# Personal Context Portfolio

Every AI agent, tool, and automation I use needs to know who I am. Without
this, I re-explain myself from scratch every time — role, projects,
preferences, constraints. It's the most repetitive, highest-friction part
of working with AI, and it gets worse as the number of agents in my life
grows from one to ten to fifty.

This repo fixes that. It's a structured set of markdown files that
together represent me as a context package — something any agent, any
tool, any automation can read and immediately understand who it's working
for.

It's not a resume. It's not a profile. It's the operating manual every
agent working for me reads first — see `AGENT-CONTEXT.md`.

This is personal infrastructure, not a product. Not licensed out, not
built for anyone else to fork.

## What's In It

- **`AGENT-CONTEXT.md`** — the entry point. Any agent or automation reads
  this first.
- **`context/`** — the real, populated files: identity, current
  projects/clients, tools & systems, preferences & constraints. This is
  the canonical source every automation syncs from.
- **`templates/`** — empty templates + the interview questions for filling
  in the rest (team-and-relationships, communication-style,
  goals-and-priorities, domain-knowledge, decision-log — not yet promoted
  to `context/`).
- **`wiring/`** — guides for connecting this to the tools I actually use
  (Claude Projects, MCP, system prompts).
- **`examples/`** — three persona examples, kept as format reference.

| File | What It Captures |
|------|-----------------|
| `identity.md` | Who I am in one page — the file an agent reads if it can only read one |
| `role-and-responsibilities.md` | What my weeks actually look like |
| `current-projects.md` | Active workstreams, clients, status, priority |
| `team-and-relationships.md` | Key people, how I interact, what they need from me |
| `tools-and-systems.md` | My stack, what connects to what |
| `communication-style.md` | How I write, how I want things written for me |
| `goals-and-priorities.md` | What I'm optimizing for and deliberately ignoring |
| `preferences-and-constraints.md` | Hard rules any agent should respect |
| `domain-knowledge.md` | What I know that a general-purpose AI doesn't |
| `decision-log.md` | How I make decisions, with real examples |

## Design Principles

**Markdown-first.** Every AI system can read markdown. Not JSON, not
PDFs, not databases. Human-readable and machine-readable.

**Modular, not monolithic.** Separate files for separate domains. An
agent prepping a meeting doesn't need my full life story — it needs team
and current-project context. Modularity lets agents grab what's relevant.

**Living, not static.** This isn't written once. `context/` updates as
clients and priorities change — automations read the current version on
every run, so a stale file here means stale output everywhere.

**Portable across everything.** Works with Claude Code, Cowork, or
whatever comes next. No vendor lock-in. It's just files in git.

## Filling In the Rest

`context/` has the load-bearing files. The rest of `templates/` isn't
populated yet — team-and-relationships, communication-style,
goals-and-priorities, domain-knowledge, decision-log. Same approach that
built `context/`: open a template from `/templates`, hand it to Claude,
say "let's do this one," work through the interview questions embedded in
it, and promote the finished file into `context/`.

## Wired-in

Four Cowork Routines currently sync from `context/` on every run: Morning
brief, Donna — Processor v2, Donna — End of Day, and the Weekly AAR. See
`AGENT-CONTEXT.md` for how that sync works and what to update when
something changes. `wiring/` has guides for the other ways to connect
this — Claude Projects, MCP, system-prompt patterns — for tools not
already wired.

## Repo Structure

```
personal-context-portfolio/
├── README.md                    ← you are here
├── GETTING-STARTED.md           ← how to fill in what's left
├── AGENT-CONTEXT.md             ← entry point every agent/automation reads first
├── context/                     ← the real, populated files
│   ├── identity.md
│   ├── current-projects.md
│   ├── tools-and-systems.md
│   └── preferences-and-constraints.md
├── templates/                   ← empty templates + interview protocols, for the rest
├── examples/                    ← persona examples, kept as format reference
│   ├── knowledge-worker/
│   ├── executive/
│   └── entrepreneur/
├── wiring/                      ← guides for connecting this to other AI tools
└── interview-protocol/
    └── agent-system-prompt.md   ← interview format used to build context/ files
```
