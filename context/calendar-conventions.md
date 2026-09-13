# Calendar naming convention

**Status:** active
**Owner:** JCS
**Applies to:** all Google Calendar events created by Jonathan or by Claude on his behalf
**Adopted:** 13 Sep 2026, drafted by Jonathan. This is a standing rule any
agent or session consults at the moment it creates or edits an event —
not a scheduled routine. See `maintenance.md`'s note on why this didn't
become a separate "Scheduler" agent: the Weekly AAR spot-checks
compliance on its existing cadence instead of a new one.

---

## The rule

Every event title opens with a bracketed context tag, then the title.

```
[TAG] Title — optional detail
```

The tag goes first so the context is legible in month view, in a notification, and on a watch face, where the title itself is usually truncated.

**Correct**

```
[Owen] Boys Trial — RiverCity Water Polo
[CP] Board papers due
[CP] Nicky Ison x JCS | Resilience scoping
```

**Incorrect**

```
Boys Trial [Owen]          ← tag trailing
Boys Trial (Owen)          ← round brackets
[owen] Boys Trial          ← inconsistent case
Boys Trial                 ← no tag
```

---

## Meetings

Meetings take a fixed shape:

```
[TAG] Their name x JCS | TOPIC
```

- The tag is the project or client the meeting belongs to. Use `[MTG]` only where the meeting sits under no project.
- `x JCS` marks it as a two-way. For three or more, name the group instead of listing everyone: `[CP] Comms working group | Q4 plan`.
- The pipe separates who from what. Topic in caps or sentence case, consistent within a calendar.
- External attendees can read the title, so keep internal shorthand out of the topic.

```
[CP] Nicky Ison x JCS | Resilience scoping
[BZE] Board chair x JCS | Fundraising plan
[MTG] Dion McMurtrie x JCS | Summer season
```

---

## Modality

The leading tag carries the **project**, not how the meeting happens. Modality is already on the event — the location field, the video link, the attendee list — and Google surfaces it on the chip and in the notification. What can't be recovered at a glance is which workstream the hour belongs to, and that's what gets filtered, totalled and billed.

Where modality is worth stating, it trails:

```
[CP] Nicky Ison x JCS | Resilience scoping · ZM
[BZE] Board chair x JCS | Fundraising plan · call
```

Markers: `· ZM` (Zoom), `· Meet`, `· call`, `· IRL`.

**Exception.** Events with no project behind them take a modality or activity tag in the bracket, because there's nothing to filter by:

```
[Coffee] Dave
[Gym]
[Travel] Home → Valley Pool
```

---

## Formatting rules

1. Square brackets, no space inside: `[CP]`, not `[ CP ]`.
2. One space after the closing bracket.
3. Tags are written exactly as the register lists them. Project tags are uppercase; people tags are name case (`[Owen]`, `[Katie]`).
4. One tag by default. A second tag is allowed only where it adds something the first doesn't — normally a work tag plus an event-type tag: `[CP] [MTG] Comms sync`.
5. Keep the whole title under about 40 characters. Detail after an em dash is fine; it just gets truncated first.
6. Venue goes in the location field, not the title.
7. Sources, links and notes go in the description, not the title.

---

## Tag register

### Confirmed

| Tag | Meaning |
|---|---|
| `[CP]` | Charlotte Project |
| `[MTG]` | Meeting |
| `[Owen]` | Owen — school, sport, appointments |
| `[O/J]` | Owen and Jacob together |

### Proposed — client and workstream

| Tag | Meaning |
|---|---|
| `[YSG]` | Your Shout Gas |
| `[AFAE]` | Australians for Affordable Energy |
| `[BE]` | Boundless Earth |
| `[SFC]` | Solutions for Climate Australia |
| `[BZE]` | Beyond Zero Emissions |
| `[CDA]` | Climate Defenders Australia |
| `[1MW]` | One Million Women |
| `[AFMH]` | Australians for Mental Health / Youth Unmuted |
| `[LAN]` | LAN retainer |

### Proposed — products

| Tag | Meaning |
|---|---|
| `[CAI]` | CapacityAI |
| `[OPPO]` | OPPO |
| `[SIG]` | AI Signal |
| `[ERSO]` | Erso |

### Proposed — business

| Tag | Meaning |
|---|---|
| `[BTS]` | Breakthrough internal — admin, finance, tooling |
| `[BD]` | Business development, pipeline conversations |
| `[FMC]` | Fundraising Masterclass and coaching delivery |

### Proposed — event type (second tag only)

| Tag | Meaning |
|---|---|
| `[MTG]` | Meeting |
| `[CALL]` | Phone or video call |
| `[DL]` | Deadline — no attendees, blocks nothing |
| `[FOCUS]` | Protected work block |
| `[Travel]` | Travel leg — always its own event, see Travel time |

### Proposed — personal

| Tag | Meaning |
|---|---|
| `[Owen]` | Owen |
| `[Jacob]` | Jacob |
| `[O/J]` | Both kids — joint commitments |
| `[Katie]` | Katie |
| `[FAM]` | Whole-family commitments |
| `[P&C]` | Ithaca Creek State School P&C |
| `[HOME]` | House, trades, maintenance |

### Proposed — no project behind it

| Tag | Meaning |
|---|---|
| `[Coffee]` | Catch-up with no work attached |
| `[Gym]` | Training |
| `[Travel]` | Travel leg |
| `[Admin]` | Personal admin — forms, renewals, appointments |

Cut what you won't use. A register nobody can recall from memory stops getting applied, and half-tagged calendars are worse than untagged ones.

---

## Durations

Default meeting lengths are **25 and 50 minutes**, not 30 and 60.

The five or ten minutes at the end is what makes the next thing start on time. Back-to-back full-hour meetings have no recovery in them, so a single overrun propagates through the whole day.

**Rules**

1. A meeting Jonathan schedules is 25 or 50 minutes. Full-hour and half-hour blocks are for things that genuinely need the whole slot.
2. The short end goes at the finish, not the start. A 10:00 meeting starts at 10:00 and ends at 10:25.
3. Meetings other people organise arrive at whatever length they chose. Don't edit their event; absorb it in the gap after.
4. A 90-minute or longer session takes a break block rather than running straight through.

**Set it once.** Google Calendar → Settings → General → Event settings → **Speedy meetings**. It ends 30-minute events five minutes early and longer events ten minutes early, for every event created in the UI. Events created by an agent set the end time explicitly.

---

## Travel time

Any event at a physical location gets its own travel event when the previous or next commitment is somewhere else. Travel is never folded into the meeting's own start time — a 10am meeting starts at 10am, and the trip to it is a separate block.

```
[Travel] Home → Somerville House          10:00–10:30
[Owen] Boys Trial — RiverCity Water Polo  10:30–12:00
```

15 min door to door, plus 5 to park and walk in, plus the standing 5. No return leg — nothing follows it that day.

**Rules**

1. Title is `[Travel] Origin → Destination`. Use place names people recognise, not street addresses — the address goes in the location field.
2. Busy, no attendees, no notification.
3. Origin is the location of the preceding event that day. Where the preceding event is virtual or there isn't one, origin is home — 21 Leslie St, Bardon.
4. Return leg only where something follows that he has to be somewhere for, or where the return itself eats a working block.
5. Add arrival buffer on top of door-to-door time — parking, walking in, finding the room. Five minutes suburban, fifteen for the CBD, thirty for the airport.
6. Then add a further five minutes, always. Jonathan runs late; the standing buffer is what makes him on time. It is not optional and it is not trimmed to make a tight day fit — if the day only works without it, the day is overcommitted.
7. Round out to the nearest five minutes.
8. No travel events for virtual meetings.
9. No routing tool is connected. Estimate from the defaults below, state the estimate and what it assumes (driving, time of day) in the event description, and never present an estimate as a lookup.

**Default door-to-door estimates — from Bardon, driving, off-peak**

| Trip | Estimate |
|---|---|
| Within the inner west (Paddington, The Gap, Ashgrove, Red Hill) | 10 min |
| Bardon → CBD | 20 min |
| Bardon → South Brisbane / West End | 20 min |
| Bardon → Fortitude Valley / Newstead | 20 min |
| Bardon → south side (Woolloongabba, Greenslopes) | 25 min |
| Bardon → Brisbane Airport | 35 min |

**Known anchors** — measured or confirmed, use these before the table above:

| From → To | Time |
|---|---|
| Home (Bardon) → Sunset Park (dog park) | 5 min |

Add a row here each time a real trip disproves an estimate. Over a few months this replaces the table.

Add 50% in the weekday peaks — roughly 7:30–9:00 and 16:00–18:00. Correct any figure that proves wrong in practice; this table is a starting point, not a measurement.

**Agent behaviour.** Before creating any in-person event, check the adjacent events for location, work out the trip, and create the travel block in the same pass. Don't wait to be asked.

---

## Edge cases

**Invitations from other people.** Don't retag an event where Jonathan is an attendee rather than the organiser — in Google Calendar the title change either fails or notifies the whole guest list. Leave it and rely on the organiser's name.

**Events Jonathan organises with external attendees.** The tag is visible to them. Use a tag the attendee would read as neutral (`[MTG]`, `[CP]`) and keep internal shorthand out of it.

**Recurring events.** Tag the series, not the instance.

**All-day events.** Same rule. `[Travel] Sydney — AEGN` reads better than a bare city name.

**No tag fits.** Create the event untagged rather than forcing one, then add the tag to this register if the category recurs.

---

## Machine-readable register

```yaml
calendar_tag_convention:
  position: prefix
  delimiter: "[]"
  max_tags: 2
  second_tag_role: event_type
  meeting_pattern: "[TAG] Their name x JCS | TOPIC"
  title_target_length: 40
  tags:
    confirmed: [CP, MTG, Owen, "O/J"]
    client: [YSG, AFAE, BE, SFC, BZE, CDA, 1MW, AFMH, LAN]
    product: [CAI, OPPO, SIG, ERSO]
    business: [BTS, BD, FMC]
    event_type: [MTG, CALL, DL, FOCUS, Travel]
    personal: [Owen, Jacob, "O/J", Katie, FAM, "P&C", HOME]
    unprojected: [Coffee, Gym, Travel]
  modality:
    position: trailing
    markers: ["· ZM", "· Meet", "· call", "· IRL"]
  durations:
    default_short_minutes: 25
    default_long_minutes: 50
    short_end_at: finish
    google_setting: speedy meetings
  travel:
    separate_event: true
    title_pattern: "[Travel] Origin → Destination"
    origin_default: preceding event location, else home (21 Leslie St, Bardon QLD)
    buffer_minutes: {suburban: 5, cbd: 15, airport: 30}
    standing_buffer_minutes: 5  # always, on top of the arrival buffer
    skip_for_virtual: true
  rules:
    - Tag precedes the title, always.
    - Project tags uppercase; people tags name case.
    - Do not retag events where the user is an attendee, not the organiser.
    - Venue to location field; links and notes to description.
```

---

## Instruction for agents

> When creating or editing a Google Calendar event for Jonathan, prefix the title with the matching bracketed tag from the register in `calendar-conventions.md`. Tag first, then the title. Never append the tag. If no tag fits, leave the event untagged and flag the gap. For meetings use `[TAG] Their name x JCS | TOPIC`. Default meeting length is 25 or 50 minutes, with the gap at the end. Before creating any in-person event, check the adjacent events, work out door-to-door travel, and create a separate `[Travel] Origin → Destination` block in the same pass.
