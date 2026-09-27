# Context Desk

Added 27 Sep 2026, at Jonathan's request: "an interface where I can more
easily edit the various pieces of this shared tooling... go in and just
see all the different context pieces in a nice interface."

**Live at:** https://claude.ai/artifact/5baN9qbUMPt6AjfTsSjRFM (private
to Jonathan). A Claude Artifact page — browse and edit every file under
`context/` and `agents/routines/` from a phone or laptop browser, no
Claude Code session required to *read* or *draft* an edit.

## Why it isn't a direct-commit tool (yet)

The obvious design — the page calls the GitHub API straight from the
browser and commits — needs a **GitHub connector attached to Jonathan's
claude.ai account** (Settings → Connectors). Checked 27 Sep: it isn't
there. What *is* there is the separate "Claude GitHub App" under Claude
Code's own repo-access settings — that's what lets Claude Code sessions
(this one included) clone and push this repo, but it is not exposed to
a published Artifact page. `SearchMcpRegistry` also turned up no
standalone GitHub connector in the directory at all. So a page's `mcp`
capability has nothing to call.

**If that changes** (a GitHub connector becomes available and Jonathan
connects it), this page can be upgraded to commit directly: declare
`capabilities: {mcp: {servers: [{server: "GitHub", tools: [...]}]}}`
and replace the save handler below with real commits, dropping the
sync step entirely. Worth revisiting next time this file is touched.

## How it works today

The page declares the `db` capability (a small JSON store attached to
the artifact itself, shared across whoever opens it — see
`ArtifactData`/`artifact-capabilities` if extending this). One document
per tracked file, in the `files` collection:

```
{ path: "context/worlds/charlotte.md",   // real repo path
  content: "...",                         // full file text
  pending: true|false,                    // edited here, not yet committed
  updatedAt: "<ISO timestamp>" }
```

Document id = the path with `/` replaced by `__` (e.g.
`context__worlds__charlotte.md`) — plain `/` isn't a legal single path
segment for the store.

Jonathan browses and edits in the page; **Save** writes the doc with
`pending: true`. Nothing reaches the repo until someone runs the sync
step below — the page's own banner shows a "sync pending edits" button
with the exact instruction to paste into a Claude Code session,
including which files changed.

## Sync procedure (what "sync context edits" / "sync Context Desk" means)

Any Claude Code session working on this repo, when asked to sync:

1. `ArtifactData` → `action: "query"`, `url: "https://claude.ai/artifact/5baN9qbUMPt6AjfTsSjRFM"`,
   `collection: "files"`, `query: {"where": [["pending", "eq", true]]}`.
2. For each returned doc: `Write` its `data.content` to `data.path` in
   this repo (the path is relative to the repo root, exactly as stored).
3. `git add` those paths, commit, push — same as any other repo change.
4. Once pushed, `ArtifactData` → `action: "batch"` with one `update` per
   synced doc: `{pending: false, updatedAt: "<push time, ISO>"}`. Pin
   each with `if_version` from the query results to avoid clobbering a
   newer edit made while syncing.
5. Tell Jonathan which files synced.

There's no scheduled/automatic version of this yet — it's a manual "ask
a session to sync" step, by design, until the direct-commit path above
is possible. A Cowork Routine that polls and auto-syncs is a plausible
future upgrade, but wasn't built now: it would need its own repo
checkout and write access, and a manual step that works today beats an
automated one that's unproven.

## Re-seeding after repo-side changes

If `context/` or `agents/routines/` change from elsewhere (a routine's
own "Context updates" applied by a session, a manual edit) and you want
Context Desk to reflect it, re-run the same seed as a batch `set` per
file (path → doc id, `/` → `__`, `pending: false`, fresh `updatedAt`).
A `set` overwrites unconditionally, so only do this for files with no
un-synced edit pending in the page — check `pending` first or you'll
silently discard someone's draft.

## Scope

Only `context/**/*.md` and `agents/routines/*.md` — 32 files as of
27 Sep 2026. Deliberately excludes the rest of the repo (README files,
`tools/`, `GETTING-STARTED.md`) per Jonathan's own scope choice: this is
for the pieces he actually corrects day to day, not a general file
browser.
