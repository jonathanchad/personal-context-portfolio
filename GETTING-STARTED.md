# Getting Started

`context/identity.md`, `current-projects.md`, `tools-and-systems.md`, and
`preferences-and-constraints.md` are done and wired into live automations
(see `AGENT-CONTEXT.md`). What's left is the rest of the ten-file set —
team-and-relationships, communication-style, goals-and-priorities,
domain-knowledge, decision-log — still sitting as empty templates in
`/templates`.

---

## Filling in what's left

Work through the templates with an AI build partner (Claude Code, Cowork,
whatever's on hand).

1. Open a template file from `/templates`.
2. Copy the entire file and paste it to the build partner.
3. Say "let's do this one."
4. It reads the interview protocol embedded in the template and starts
   asking questions.
5. When it has enough, it drafts the file. Read the draft and correct
   what's wrong.
6. Save the final version into `context/` (promote it from `templates/`),
   so it's on the same footing as the files already wired into
   automations.

**Suggested order:**

1. `team-and-relationships.md`
2. `communication-style.md`
3. `goals-and-priorities.md`
4. `preferences-and-constraints.md` (already started — extend it)
5. `domain-knowledge.md`
6. `decision-log.md`

---

## Wiring a new file or tool in

`context/` files already sync into four Cowork Routines automatically
(see the "Wired-in automations" section of `AGENT-CONTEXT.md` for how).
For anything else — a new Routine, Claude Projects, MCP, or another tool
entirely — `wiring/` has guides for:

- Exposing this repo as an MCP resource
- Using it in Claude Projects
- Copy-paste patterns for system prompts
- Building an API layer (only if something needs to query this
  programmatically — most things don't)

Start with whatever tool the new context needs to reach.

---

## Tips

- **Be specific, not aspirational.** Describe how I actually work, not
  how I wish I worked. Agents need ground truth.
- **Don't skip the reaction pass.** Read every draft and find what's
  wrong. The corrections are where the real signal is.
- **Short is better than long.** One page beats five. Agents perform
  better on dense, high-signal context than sprawling documents.
- **Update `context/`, not individual automation prompts.** That's the
  whole point of the wiring — one edit here should be enough. A portfolio
  that's stale gives every agent confident but wrong context.
