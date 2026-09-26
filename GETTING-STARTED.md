# Getting Started — what's still open

The structure is in place. See `agents/README.md` for the full,
current routine inventory (14 entries as of 25 Sep, several deleted or
retired) — this file only tracks what's still open.

## Open: Kiera's review reminder still needs connectors

Zero-connector bug (see `context/maintenance.md`'s "Known limitation"
note) also hit **"Check for Kiera's review (day 3)"**
(`trig_01N9kagMTCy81UM1KS2myUym`) — a one-off AFAE-contract check-in,
not a full routine, so it needs a much smaller fix than Charlotte PM
did: just **Gmail** and **Superhuman_Mail** attached by hand in the
Routines UI. Flagged 17 Sep, not yet confirmed done. Its last scheduled
check is 22 Sep; if that's passed with no fix, the check-in chain has
already silently died and someone needs to ask Jonathan whether Kiera
ever replied.

## Closed 17-25 Sep

- **Charlotte Project Manager's connectors**, fixed 17 Sep — five days
  with zero connectors after two failed API-side attempts, resolved by
  Jonathan attaching them by hand in the Routines UI. Confirmed live.
  See `agents/README.md`.
- **Two undocumented routines captured**, 25 Sep — "Nura Fund reply
  check" and "Monthly billing reconstruction — BTS" existed, fully
  connected, doing real work, with no record in this repo. Now captured
  verbatim in `agents/routines/` per the standard "copy first" rule;
  see `agents/README.md`'s inventory table (rows 13-14). Neither has
  been reviewed for streamlining or overlap with anything else yet —
  the billing reconstruction routine in particular reads a `memory`
  project file this repo doesn't own
  (`/projects/019d9b46-a3e0-74ca-b872-86d6feafe901/rate_card.md`) and
  flags a real unresolved YSG billing-basis conflict worth checking
  against `worlds/consulting.md`.

## Watch

1. **First Morning Chief of Staff run happened 10 Sep and Jonathan marked
   it up on paper.** The corrections are folded into
   `context/accounts.md` ("Importance signals — refinements from
   Jonathan") and `context/memory/log.md`: verify a counterparty thread
   before calling it quiet, treat unsent drafts as candidates not
   findings, name which "Daily Brief" product, check task ownership
   before assigning it to Jonathan, attribute Owen's and Jacob's own
   commitments to them rather than folding them into Jonathan's, and
   drop dramatic headlines. Keep watching the next few runs against this
   list — see `agents/README.md`.
2. **The feedback loop itself got lighter, 10 Sep.** No more printing
   and marking up: reply in plain English to whatever session you're
   correcting, it drafts a "Context updates" block (verified against the
   real inbox/calendar if the correction depends on one), and you paste
   that block into a Claude Code session to apply. The Morning Chief of
   Staff now proposes its own "Context updates" daily (Step 6) instead
   of waiting for the weekly AAR. See `context/maintenance.md`. Open
   question worth testing next time: can a Cowork/Desktop session push a
   PR directly via the GitHub connector and skip the paste step
   entirely?
3. **Once the Charlotte PM has connectors and has run a few times**,
   check: is Mon/Thu the right cadence, or should it run right after the
   Monday leadership hour instead; does the Morning Chief of Staff
   actually lean on the tracker for Charlotte's priorities or keep
   re-deriving them from the mailbox; is the priority list staying short
   (5-8 rows) rather than turning into a task list; does the RAG status
   actually stay honest (recomputed with real evidence, not left on
   whatever it was last); does "Owner: Jonathan" on most RAID rows
   spread out once hiring closes. See `agents/routines/charlotte-pm.md`'s
   "Open questions" section.
4. **Calendar naming convention, adopted 13 Sep** (`context/calendar-
   conventions.md`) — watch whether Claude sessions actually apply the
   tag/duration/travel-block rules when creating events, and whether the
   Weekly AAR's new spot-check (Step 1.6) catches real drift or just
   says "looks fine" every week without checking hard enough to matter.

## Daily audio — pipeline proven, content and schedule still open

**Update, 25 Sep:** confirmed with Jonathan — there's a mock (test)
episode already on the JCS Briefings feed. So the mechanics of
`tools/briefings/publish_briefing.py` (see `tools/briefings/README.md`)
are proven: it can render, upload and publish for real. Against the
original 9 Sep agenda below, that closes steps 1-3. What's still open
is 4-6 — there's no real daily content flowing into it yet, and no
schedule or routine driving it.

**Correction, 26 Sep — the "no delivery bridge" blocker may already be
solved, just not where this file could see it.** Investigating why the
Weekly AAR hadn't produced anything, `fire_trigger` surfaced its actual
live prompt: a "STEP 4" section, never captured in this repo until
today, that runs `publish_briefing.py` **from inside the cloud
session** — pulling ElevenLabs/Supabase keys from a Supabase table per
run instead of a local Mac env file. See
`agents/routines/weekly-after-action-review-aar.md` and
`tools/briefings/README.md`. If that pattern actually works (still
unconfirmed as of this writing — the run that would have proven it
stalled before reaching Step 4, see the "Open: investigate" item
below), the end-of-day script drafted below should copy it rather than
fall back to a Gmail draft.

**Remaining agenda:**

4. **The script — drafted 25 Sep**, not yet live. See
   `agents/routines/donna-end-of-day-audio-script.md`. One correction
   made while drafting: Run History turned out to be pure tallies
   (meetings seen, tasks created — no content), so the routine actually
   sources content from the **Donna Log** (the per-item commitment
   data) and only uses Run History to confirm the day happened cleanly.
   Two things this step surfaced as still unresolved and blocking:
   - **Delivery bridge** — drafted with a Gmail-draft fallback; revisit
     against the AAR's cloud-side Supabase-secrets pattern above once
     that's confirmed working.
   - **No voice ID is recorded anywhere** in this repo — needed before
     any script can actually render.
5. **The schedule.** Weekday evenings only; confirm the time. Still
   open.
6. **Only then** switch it on — create the live trigger from the
   drafted prompt, same "copy first" rule as everything else here.

Old prompt, for reference: `agents/routines/donna-end-of-day-reconcile-audio-email.md`.

## Open: investigate why the 25 Sep Weekly AAR produced nothing

Fired 26 Sep at Jonathan's request as a diagnostic
(`trig_015CuVpwAUZ3HFf8Ww8KQFc8`, new session
`cse_012hdigLbNUZzfS6yxX1bR17`) — outcome not yet known as of this
writing. The 25 Sep scheduled run fired correctly (matching the new
05:00 Brisbane time) but the resulting session was abandoned with zero
tokens used, roughly a minute after creation. Leading hypothesis: this
session has repeatedly been told the `Cloudflare_Developer_Platform`
connector needs re-authorization and can't complete that OAuth flow
unattended; the AAR trigger has that connector attached (almost
certainly inherited automatically, not something the AAR uses), and an
unattended session trying to initialize with an unauthorized connector
attached could stall exactly like this. **Needs Jonathan to
re-authorize that connector in claude.ai's connector settings** — only
he can do that. Check the 26 Sep re-fire's outcome next session; if it
stalled the same way, that's further evidence; if it succeeded, this
was likely transient and can be closed.

## Smaller follow-ons noted in `agents/README.md`

- Donna should produce a clean dated "overnight" block the Morning Chief
  of Staff can read, instead of the Chief of Staff re-reading raw
  meeting notes.
- The Allianz watch is still its own routine rather than a line in
  `accounts.md`; folding it in would lose its guaranteed daily check on
  one thread, so it stays separate for now.
- Whether the Monthly directions diff should fold into the first-Saturday
  AAR run instead of its own schedule.

## How to update

Tell any Claude Code session the correction; it edits `context/`, appends
to `memory/log.md` where the change matters, and pushes to `main`. The
routines pick it up on their next run. The Weekly AAR will also propose
updates every Friday in its "Context updates" section.

## Tips

- Specific, not aspirational. Agents need ground truth.
- Short beats long. A world file is one screen, not five.
- Update `context/`, never the routine prompts.
