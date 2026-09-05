# Personal Context Portfolio

Every AI agent, tool, and automation I use needs to know who I am, what
I'm working on, and how I want things done. Without this I re-explain
myself from scratch every time, and each routine carries its own slowly
drifting copy of the facts.

This repo fixes that. It's the operating manual every agent working for me
reads first — see `AGENT-CONTEXT.md`. Personal infrastructure, not a
product. Not licensed out, not built for anyone else to fork.

## How it's organised

Not the generic "ten files about me" template this started as. I operate
in several distinct worlds at once, the facts in them change at different
speeds, and my own weekly reviews say I won't hand-maintain ten files. So:

- **Slow facts** — `context/identity.md`, `preferences-and-constraints.md`,
  `communication-style.md`, `tools-and-systems.md`. Change rarely; I edit them.
- **Worlds** — `context/worlds/`: `charlotte.md`, `breakthrough-tools.md`,
  `consulting.md`, `personal.md`. Each world carries its own people, rules,
  status and shorthand. Change weekly; agents propose the edits.
- **Goals** — `context/goals-and-priorities.md`. What I say I'm optimising
  for. The Weekly AAR reads it every Friday and reports where the hours
  actually went. That drift check is the point.
- **Memory** — `context/memory/`: where the running record lives (the
  Weekly AAR database in Notion is the real decision log) plus a short
  dated log of changes to this context.
- **Maintenance** — `context/maintenance.md`: who keeps which file
  current, and the weekly loop that makes it live rather than static.

Four Cowork Routines sync from `context/` on every run: Morning brief,
Donna — Processor v2, Donna — End of Day, Weekly AAR.

## Repo structure

```
personal-context-portfolio/
├── README.md
├── AGENT-CONTEXT.md             ← entry point every agent reads first
├── GETTING-STARTED.md           ← what's still open
├── context/
│   ├── identity.md
│   ├── preferences-and-constraints.md
│   ├── communication-style.md
│   ├── goals-and-priorities.md
│   ├── tools-and-systems.md
│   ├── maintenance.md
│   ├── worlds/
│   │   ├── charlotte.md
│   │   ├── breakthrough-tools.md
│   │   ├── consulting.md
│   │   └── personal.md
│   └── memory/
│       ├── README.md
│       └── log.md
├── templates/                   ← original generic template, reference only
├── examples/                    ← persona examples, reference only
├── wiring/                      ← Claude Projects / MCP / system-prompt guides
└── interview-protocol/          ← interview format, reference only
```
