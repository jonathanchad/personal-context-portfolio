# Accounts and calendars registry

The list an agent reads so Jonathan never has to ask "which inbox have I
forgotten?" Every morning scan reports against this list: checked, what
matters, nothing to worry about. Started 9 Sep 2026; incomplete rows are
marked and are the first thing to fix.

## Mailboxes

Eleven addresses live in Jonathan's Superhuman (screenshot, 9 Sep 2026).
Only four are linked to the Superhuman MCP connector that agents use, so
"scan" below means "should scan once linked". Jonathan, 9 Sep: "I don't
need all of those." The Scan column is the proposal; he corrects it.

| Account | World | In Superhuman | Linked to the agent connector | Scan in the morning brief? | Watch for |
|---|---|---|---|---|---|
| jonathan@breakthroughstrategies.co | consulting, tools | yes (primary) | **yes** | **yes** | everything |
| jonathan@charlotteproject.au | charlotte | yes | **yes** | **yes** | funders, team, Boundless |
| jonathanchad@gmail.com | personal | yes | **yes** | **yes** | Allianz claim 6210520873, family and school admin, Rackley squad |
| jonathan.schleifer@icsspandc.com | personal (P&C President) | yes | no | **yes, once linked** | Jodie Painter, time capsule RSVPs, website, P&C executive |
| swimclubVC1@icsspandc.com | personal (ICSS Sharks Swim Club, race timing) | yes | no | **yes, once linked** | meet entries, timing duties. *Confirm this is the "Rackley / race timing" account from the 9 Sep notes* |
| operations@afae.net.au | consulting (AFAE ops) | yes | **yes** | **yes** | payroll, Xero, supplier invoices, Margo |
| operations@liberalsagainstnuclear.au | consulting (LAN wind-down) | yes | no | **yes, once linked** | Ripple Legal, insurance, shutdown admin |
| contact@liberalsagainstnuclear.au | consulting (LAN) | yes | no | no | public inbox; skim only if the wind-down needs it |
| admin@liberalsagainstnuclear.au | consulting (LAN) | yes | no | no | |
| andrew@liberalsagainstnuclear.au | consulting (LAN) | yes | no | **no, kept out** | someone else's mailbox; Jonathan's call, 9 Sep: keep it out |
| admin@yourshoutgas.com.au | consulting (Your Shout Gas) | yes | no | **yes, once linked** | active campaign; Jonathan wants eyes on it, 9 Sep |
| oppo@breakthroughstrategies.co | tools | no (app sends from it) | no | no | subscriber replies, handled by the OPPO app |

To link a mailbox to the connector: Superhuman connector, add account.
Jonathan, 9 Sep: he will add the missing accounts himself. Once each is
added, an agent session confirms it shows up in `list_accounts` and
flips its row here to "yes" / "linked".

**Settled scan set, 9 Sep 2026 (8 of 11):** breakthroughstrategies.co,
charlotteproject.au, jonathanchad@gmail.com, P&C president
(jonathan.schleifer@icsspandc.com), swim club (swimclubVC1@icsspandc.com),
AFAE ops, LAN operations, Your Shout Gas admin. Excluded: LAN contact,
LAN admin, Andrew's LAN mailbox, the OPPO sender address.

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
