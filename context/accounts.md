# Accounts and calendars registry

The list an agent reads so Jonathan never has to ask "which inbox have I
forgotten?" Every morning scan reports against this list: checked, what
matters, nothing to worry about. Started 9 Sep 2026; incomplete rows are
marked and are the first thing to fix.

## Mailboxes

**Final list, Jonathan, 9 Sep 2026** — replaces every earlier draft in
this file. Eight accounts, each with the role he gave it. All eight are
in scope for the morning scan. 5 of 8 linked as of 9 Sep; 3 remain
(P&C President, LAN operations, Your Shout Gas admin).

| # | Account | Role (Jonathan's words) | World | In Superhuman | Linked to agent connector |
|---|---|---|---|---|---|
| 1 | jonathan@breakthroughstrategies.co | CEO and principal consultant, includes Breakthrough Tools | consulting, tools | yes | yes |
| 2 | jonathan@charlotteproject.au | CEO and Founder | charlotte | yes | yes |
| 3 | jonathanchad@gmail.com | Personal | personal | yes | yes |
| 4 | jonathan.schleifer@icsspandc.com | P&C President | personal | no | no |
| 5 | operations@afae.net.au | AFAE Maintenance | consulting | yes | yes |
| 6 | operations@liberalsagainstnuclear.au | AFAE Maintenance *(as given; flagged below)* | consulting | yes | no |
| 7 | admin@yourshoutgas.com.au | added, active campaign | consulting | no | no |
| 8 | Centenary.race@rackleyswimteam.com.au | Race Volunteer Organiser | personal | yes | **yes, linked 9 Sep** |

**Flag, not silently corrected:** rows 5 and 6 both say "AFAE
Maintenance" in Jonathan's list, but row 6's address is
liberalsagainstnuclear.au, a different entity (LAN, winding down —
see `worlds/consulting.md`). Recorded verbatim; ask Jonathan whether
row 6 is actually AFAE-related mail routed through the LAN domain, or
whether "AFAE Maintenance" was meant for row 5 only and row 6 should
read "LAN wind-down" as before.

**Dropped from the previous draft:** swimclubVC1@icsspandc.com (P&C
swim club) is not on this final list; Centenary.race@rackleyswimteam.com.au
(Rackley Swim Team, Centenary — race volunteer organising) replaces it
as the swimming-world address. contact@liberalsagainstnuclear.au,
admin@liberalsagainstnuclear.au, andrew@liberalsagainstnuclear.au and
oppo@breakthroughstrategies.co are out of scope, per the 9 Sep decision.

Once Jonathan adds an account to Superhuman, an agent session confirms
it in `list_accounts` and flips its "linked" column to yes.

## Calendars (Google Calendar connector, 9 Sep 2026)

| Calendar | Id | World | Notes |
|---|---|---|---|
| jonathan@breakthroughstrategies.co | same | consulting, tools | the "primary" the generic morning skill reads |
| jonathan@charlotteproject.au | same | charlotte | separate at source; keep it that way |
| JCS - Personal | jonathanchad@gmail.com | personal | |
| SchleifCon Family Calendar | 6f6d4a75…1422@group.calendar.google.com | personal | family commitments, squad |
| Todoist | c_d0a523…1c61e@group.calendar.google.com | all | task due dates mirrored; deduplicate against Todoist itself |
| CANA Brown Bag Lunches | c_707f6n23cg2on8d0nlun06lm2c@group.calendar.google.com | consulting | low priority |
| Holidays in Australia | en.australian#holiday | all | context only |

Not visible to the connector: any P&C calendar, any Rackley or Masters
Swimming calendar, the Charlotte leadership meeting series if it lives
elsewhere. Confirm.

## Rules

- **Scan every row, report every row.** A mailbox with nothing in it
  gets a line under "nothing to worry about", so the check is visible.
- **Calendars stay separate at source.** Unify the view, never the
  calendars. Deduplicate the same meeting across calendars and
  invitations.
- **Look back 72 hours plus anything unread or pending; look ahead 7
  days.**
- **Importance signals** (from Jonathan, 9 Sep): a direct question or
  request to him; someone waiting on him; deadlines; money, invoices, tax
  or finance admin; legal or governance; family, school or parenting;
  project decisions or dependencies; anything that creates a problem if
  ignored. Corrections go into `memory/log.md` and this file, so the
  definition of important gets more his over time.
- Adding an account means adding a row here first. Routines read this
  file; they do not carry their own list.
