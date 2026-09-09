---
name: "Morning brief"
trigger_id: trig_01BZdfHczNrNwrooRuEXtW61
platform: Cowork Routine (Claude)
schedule_utc: "0 21 * * 0-4"
schedule_local: "weekdays 07:00 Brisbane"
enabled: false
superseded: 2026-09-09 by morning-chief-of-staff.md (same trigger_id, prompt replaced)
model: claude-opus-5
last_run: 2026-09-08T21:02:13.628960236Z ROUTINE_RUN_STATUS_SUCCEEDED
captured: 2026-09-09
---

# Morning brief

Captured verbatim from the live Cowork Routine on 9 Sep 2026. **Superseded the same day**: the routine (same trigger_id) now runs the Morning Chief of Staff prompt in `morning-chief-of-staff.md`. Kept for the record; the generic `/morning` skill this prompt invoked only ever read one calendar and had no account registry. Metadata above; the prompt
below is untouched. Purpose, inputs and outputs are summarised in
`agents/README.md`.

## Prompt (verbatim)

```
/morning

CONTEXT SYNC (before anything else, once /morning loads): git clone or pull https://github.com/jonathanchad/personal-context-portfolio and read AGENT-CONTEXT.md, then context/identity.md, context/goals-and-priorities.md, context/worlds/README.md and every file in context/worlds/ (charlotte, breakthrough-tools, consulting, personal). This is Jonathan's canonical, up-to-date context — if it conflicts with anything below, the repo wins.

ONE DAY, NOT FOUR: Jonathan's day blends across parenting, school and the P&C, Charlotte, clients and the tools. Plan a single timeline with all of it prioritised together — never separate sections that pretend the other worlds don't exist. Carry constraints across worlds (a squad run or school commitment constrains a client call; a funder deadline constrains P&C time) and say so when they collide. The guardrails in context/worlds/personal.md and context/preferences-and-constraints.md hold regardless.

Write the brief in English (Australian English spelling).

Role context: not-for-profit, advocacy and consulting. Treat client work, campaign deadlines, pipeline conversations and commercial questions (pricing, pilots, founding-member terms) as first-order — see context/worlds/consulting.md for the client roster and shorthand, and context/goals-and-priorities.md for what today should serve. Surface any drafted-but-unsent proposal, SOW or invoice as a priority-one close, ahead of new opportunities.

Gather from the connected tools: Google Calendar, Gmail/Superhuman, Todoist, Notion, Granola. Render the brief as the styled HTML artifact and deliver it.
```
