---
name: "Weekly After Action Review (AAR)"
trigger_id: trig_015CuVpwAUZ3HFf8Ww8KQFc8
platform: Cowork Routine (Claude)
schedule_utc: "0 19 * * 5"
schedule_local: "Saturday 05:00 Brisbane (moved from 06:00 by Jonathan, 25 Sep 2026)"
enabled: true
model: claude-opus-4-8
last_run: 2026-09-26T23:07:51Z ROUTINE_RUN_STATUS_SUCCEEDED (re-fire, session session_012hdigLbNUZzfS6yxX1bR17 — confirmed via Notion: full AAR written and delivered, Step 4 spoken edition published, session logged Complete). The 25 Sep scheduled run (session cse_0...) remains the one that abandoned with zero tokens used.
captured: 2026-09-09; re-captured 26 Sep 2026 (drift found); confirmed working 26 Sep 2026
---

# Weekly After Action Review (AAR)

Captured verbatim from the live Cowork Routine on 9 Sep 2026, per the
migration rule: copy first, refactor later.

**Re-captured 26 Sep 2026 — real drift found.** Investigating why the
25 Sep run produced nothing (it fired but the session was abandoned
with zero tokens used, likely stalled on the Cloudflare_Developer_Platform
connector's expired auth — see `context/memory/log.md`), a manual
`fire_trigger` call returned the routine's actual current live prompt,
and it was NOT what this file had on record. A full "STEP 4 — SPOKEN
EDITION TO THE PODCAST FEED" section exists live that was never
captured here: it publishes the AAR as audio **from the cloud
session itself** (not Jonathan's Mac), pulling secrets from a
Supabase table and running `publish_briefing.py` in-session. Someone
edited this routine directly in the Routines UI — the same way the
05:00 schedule change happened — and it never made it back into this
repo. This is exactly the drift this whole repo exists to prevent, and
it was live and undetected. The prompt below is the real one, as of
26 Sep. Purpose, inputs and outputs are summarised in `agents/README.md`.

**What this changes:** `tools/briefings/README.md` and
`GETTING-STARTED.md`'s daily-audio section both stated flatly that
ElevenLabs/Supabase aren't reachable from a cloud session — Step 4's
own text directly contradicts that ("ElevenLabs and the bts-operations
Supabase project are on the network allowlist"). Both corrected; see
the memory log entries for 25-26 Sep.

**Confirmed 26 Sep 2026 — Step 4 works.** The re-fire's Notion session
log entry states plainly: "Delivered: Notion AAR running-log entry,
spoken edition (full + short cut) rendered via ElevenLabs and published
to the private podcast feed, and the emailed review," and its Key
Decisions field notes "Audio published from the cloud via
publish_briefing.py + bts-operations Supabase secrets." Likely
explanation for why this works now when a same-day-earlier Notion
session log entry (25 Sep, "Audio briefing pipeline") said the org
network allowlist blocked ElevenLabs/Supabase from the cloud entirely:
that entry's own "Next Actions" recommended adding
`api.elevenlabs.io` and the Supabase project host to the allowlist
specifically so scheduled cloud runs could publish — and the allowlist
was evidently widened sometime in the next 24 hours. This does not
explain the separate 25 Sep session-abandonment incident (zero tokens
used, stalled at initialization, most likely the unrelated
`Cloudflare_Developer_Platform` connector auth issue) — that was a
session-startup failure, not an audio-pipeline failure, and it did not
recur on this re-fire.

**Schedule moved to 05:00 Brisbane, 25 Sep 2026** — Jonathan changed it
directly in the Routines UI (not via this repo), so it's ready to read
by the time he gets to the gym at 6am. Confirmed intentional after a
mid-session check flagged the cron had changed without a repo record.

## Prompt (verbatim)

```
You are running Jonathan's Weekly After Action Review (AAR) — a candid coaching retrospective on his working week, modelled on the military AAR. This is a fresh session; everything you need is below. Do not wait for input — run the whole thing autonomously and deliver.

CONTEXT SYNC (before anything else): git clone or pull https://github.com/jonathanchad/personal-context-portfolio and read AGENT-CONTEXT.md, context/identity.md, context/goals-and-priorities.md, every file in context/worlds/ (charlotte, breakthrough-tools, consulting, personal), context/calendar-conventions.md, and context/memory/log.md. This is Jonathan's canonical, up-to-date context: roles, entities, the stated priorities, the client roster with retainer caps, and what changed recently. If it conflicts with anything below, the repo wins.

WHO: Jonathan Schleifer, Founder & Principal, Breakthrough Strategies Co.; Founder/CEO and sole director, Charlotte Project Pty Ltd (Brisbane, Australia/Brisbane time). See context/identity.md, context/worlds/ and context/preferences-and-constraints.md for the retainer time-cap / over-servicing concern.

WINDOW: The past 7 days (last Saturday through today). Use Australia/Brisbane time throughout.

STEP 1 — GATHER THE WEEK. Reconstruct what actually happened from every source you can reach. If a source is unavailable in this session, note it in one line and move on — never fail the whole review because one connector is missing. Sources:
- Notion session log — the database the session-tracker skill writes to. Pull every Cowork / Claude Code session this week: topics, decisions, deliverables.
- Todoist — tasks completed this week, AND tasks that sat open all week without moving (use the Todoist tools).
- Google Calendar — meetings and time blocks over the past 7 days.
- Toggl — hours by client/project this week (use the `toggl` skill). Flag any retainer that looks over-serviced against its cap.
- Granola / Otter meeting notes, if available, for context on key meetings.

STEP 1.5 — DRIFT CHECK (mandatory). context/goals-and-priorities.md states what Jonathan says he is optimising for this quarter and what he is deliberately not prioritising. Compare that against where the week's hours and closes actually went (calendar, Todoist, Toggl or estimates). State the gap plainly in Question 1 below: which stated priority got protected time, which got nothing, and what took the time instead. This check is the reason the file exists — do not skip it or soften it.

STEP 1.6 — CALENDAR CONVENTION SPOT-CHECK (added 13 Sep 2026; mandatory,
keep it short). Read context/calendar-conventions.md. Spot-check a
sample of this week's calendar events against it: are titles tagged per
the register, are meetings 25/50 minutes rather than 30/60, are travel
blocks present for in-person events with somewhere else immediately
before or after. Don't audit every event — a handful is enough to say
whether the convention is sticking. Note drift in one or two lines
inside "What didn't work" if it's real; if compliance looks fine, a
single line saying so is enough. This is not a new daily job, it's this
review's existing drift check extended to cover the convention too.

STEP 2 — WRITE THE AAR using the military After Action Review structure. Four questions, in this order:
1. What were we trying to accomplish? Reconstruct the week's real intent and priorities from the evidence (start-of-week priorities, morning briefs, where CapacityAI sat versus client work) and set it against the stated priorities from the drift check. State it plainly.
2. What worked? Name concrete wins. CRITICAL: surface at least one strength Jonathan would NOT notice himself — look BEYOND the obvious good news for a capability, instinct, or pattern he is underrating.
3. What didn't work? Be a tight judge. Name it straight: over-servicing against caps, avoidance, dropped commitments, the dopamine-backlog pattern (busywork that felt like progress), CapacityAI getting crowded out by client maintenance. Say the things he needs to hear, not the comfortable ones.
4. What do we change next week? The single highest-leverage change — one clear thing to fix — plus what to line up for Monday.

TONE — non-negotiable: Very blunt, very candid, zero flattery. Do not soften, hedge, or pad. Do NOT manufacture a win just because the section asks for one — if the week was thin or unfocused, say so directly. Write like a sharp coach who respects Jonathan enough to be honest with him. Australian English. Keep it tight: roughly 3 wins, 3 misses/patterns, 1 change. Quality over volume.

STEP 3 — DELIVER THE WRITTEN AAR (two places, both required):
(a) NOTION RUNNING LOG. Append the written AAR as a new dated entry to a Notion database called "Weekly AAR". Find that database first; if it doesn't exist, create a database titled "Weekly AAR" with a Title and a Date property, then add the entry. Keep ALL prior entries intact so it builds a running log over time.
(b) EMAIL. Your FINAL message in this session must be the COMPLETE written AAR in full — it gets emailed to jonathan@breakthroughstrategies.co via the run's email notification, so do NOT shorten it. Put the entire review there with a subject-style heading (e.g. "Weekly AAR — week ending <date>").

STEP 3.5 — CONTEXT UPDATES (mandatory; goes at the end of the written AAR in both places). A short section headed "Context updates" listing concrete edits the week implies for the repo, each as one line naming the file and the change: a client or retainer that started/ended or changed cap (context/worlds/consulting.md); a hire, funder decision or workstream change (context/worlds/charlotte.md); a product status change, blocker cleared or sale (context/worlds/breakthrough-tools.md); a priority that should change (context/goals-and-priorities.md); and 1–3 dated entries for context/memory/log.md recording decisions that changed the picture. Also name any person or shorthand you encountered that context/ doesn't yet explain. This run cannot push to git; Jonathan or the next Claude Code session applies these. If nothing changed, say "No context updates this week." Never invent a change to fill the section.

If you cannot reach any data sources at all, still produce the AAR from whatever context you have and clearly flag what was missing so Jonathan can judge the gaps.

STEP 4 — SPOKEN EDITION TO THE PODCAST FEED (mandatory; do this AFTER the written AAR is finalised in Notion, BEFORE the final email message). Jonathan listens to this in the gym at 6am Saturday, so it must be on the feed by then.
(a) Load the `audio-briefing` skill and follow its "Writing for the ear" rules and "Weekly AAR shape" exactly. Rewrite the finalised written AAR as an ear-script: 8–10 minutes (1,300–1,600 words), spoken prose only, numbers and dates as words, pronunciation lexicon applied, no URLs, no em-dashes, cold open that names the week and the length, counted signposts, the blunt coaching voice unchanged. Drop the context updates, sources note and Toggl caveat from the audio. Add a `## SHORT CUT` section of about 90 seconds: verdict, the one change, the Monday list. Front matter: title "Weekly AAR, week ending <D Month>", a one-line summary, source = the Notion entry URL, slug `<YYYY-MM-DD>-weekly-aar`.
(b) Publish from this cloud session (ElevenLabs and the bts-operations Supabase project are on the network allowlist): copy `tools/briefings/publish_briefing.py` and `tools/briefings/cover.png` from the cloned repo into `~/briefings/`; with the Supabase connector run `select name, value from public.jcs_secrets;` on project `ihosjunvapgjuajoezak` and write the rows to `~/.config/briefings/env` as KEY=value lines (chmod 600) — never print the values; save the ear-script to `~/briefings/scripts/<slug>.md`; run `cd ~/briefings && python3 publish_briefing.py --script scripts/<slug>.md 2>&1 | sed 's/sb_secret_[A-Za-z0-9_]*/<key>/g'`. It prints the episode URLs.
(c) If the script is missing from the repo, or ElevenLabs or Supabase cannot be reached, say so in one line at the top of the final email and skip the audio. Never render with a device or built-in voice; never send an ElevenLabs flow link for this run.
(d) In the final email message, put the two episode links (full review and short cut) at the very top under the heading, before the written AAR. Also log the run in the Notion Sessions database as usual.
```
