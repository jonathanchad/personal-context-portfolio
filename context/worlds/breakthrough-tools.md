# World: Breakthrough Tools

The software products built under Breakthrough Strategies Co. Not a
separate company. Authoritative list:
[tools.breakthroughstrategies.co](https://tools.breakthroughstrategies.co/)

## Products

| Product | Status | What it does |
|---|---|---|
| **CapacityAI** | LIVE — capacityai.io | Persuasion platform for advocacy organisations. Applies research-backed persuasion science to generate, evaluate and improve strategic communications — media releases, talking points, social content. **Named primary focus.** |
| **AI Signal** | BETA | Tracks how an organisation shows up in AI answers: whether LLMs name you and adopt your arguments on the policy questions that matter, and how that shifts over time. |
| **Erso** | BETA | Predicts how industry will respond to a scenario — policy announcement, geopolitical shock, court ruling. Returns a structured intelligence report: who moves, what they ask for, early-warning signals. |
| **OPPO** | BETA | Monitors opposition paid advertising via Meta's Ad Library. Captures every ad, analyses messaging and veracity, tracks themes and coordination across advertisers. Has its own brand guide (`oppo-brand` skill). |

**Never came to fruition (not products):** Zoltar, VibeMentor. The
`tool-documentation` skill still lists Zoltar — that reference is stale.

## Targets to December 2026 (Jonathan, 5 Sep)

Revenue is the goal: enough paying users to justify further development.
CapacityAI 2–3 paying users (JCN already a client). OPPO 2–3 paying
users. AI Signal: land one. (The ~$30k 89 Degrees East measurement idea
is not a client relationship, per Jonathan's 5 Sep worksheet; if it
proceeds, Sunrise is the counterparty.)
Erso: **no revenue target** (Jonathan, 5 Sep 2026). It stays in beta; agents
should not propose Erso pitches or Erso build work as a route to revenue.

## Current state (as of late Aug 2026)

- **CapacityAI** — JCN (Basya Vorchheimer, Jarred) is a paying client;
  onboarding done Jul 2026. **Update, 26 Sep:** Basya's 16 features
  shipped to production (PR #205) — but this is a build milestone, not
  a delivery one: JCN's feature flags are still off and the client
  email announcing it is still a Gmail draft, so none of it is visible
  to JCN yet. The Weekly AAR calls this out by name: "built" got ticked,
  "live for the client" didn't. Flip the flags and send the email before
  counting this as done.
- **AI Signal** — went from dormant/zero revenue to ~AUD 30k of scoped
  measurement work around 89 Degrees East's Sunrise campaign (Scott
  Gamble, Annie O'Rourke; 89DE itself is **not a client**, Sunrise would
  be the payer) by offering to
  *measure* whether their Sunrise work lands, rather than pitching software.
  **Update, 26 Sep:** pivoted to per-purpose crawler-access measurement
  after a Cloudflare change (15 Sep); added a free all-org monitor;
  corrected 11 orgs' reports (including Climate Council) that had been
  wrongly showing as AI-blocked.
- **OPPO** — led with an OPPO report (not a demo) to Environment Victoria.
  **ACBF is now a live paying customer** — see `consulting.md`'s current
  clients table; Campaign tier, 2 seats, provisioned, pending final
  budget sign-off from their Lyndon. This is the first real revenue
  against the OPPO target. **Sunrise**: asked for a Victorian election
  proposal that includes OPPO. **Together (ASU)** is a CapacityAI
  prospect (Alex Scott). CEC and Fortescue (Louisa Ross) added as
  report recipients/prospects; Daniel Hurst (GSCC) and Louisa Ross now
  on the OPPO daily brief. Build, 26 Sep: all 162,686 ads fully
  analysed; the in-brief report generator shipped; an off-topic-brief
  output gate and a real-database CI (84 migrations) went in.
  **Risk:** the Meta ad-sweep token expired 24–25 Sep (sweeps failed);
  the replacement also expires ~24 Nov — inside the Pan Pacs fortnight
  and just before the 28 Nov Victorian election. The permanent fix (a
  non-expiring System User token) is written up as a task but still
  open; do it before it becomes a race-week outage on a product that
  now has paying customers.

## Go-to-market pattern (Jonathan's own, from the AAR)

The tools sell as **an instrument held up to the buyer's own work, not as
a platform**. Offer to measure; let the number do the selling. This has
worked twice (AI Signal, OPPO) and is not yet run deliberately on
CapacityAI. Agents helping with any product pitch should default to this
framing. Erso is excluded: no revenue target.

## Documentation and brand

- `tool-documentation` skill maintains ARCHITECTURE / LOGIC / USER_GUIDE /
  STRESS_TEST per tool and logs changes to each tool's Notion page.
- `commercial-readiness` skill: the hardening playbook (patterns proven on
  CapacityAI, Jul 2026).
- Brand: `breakthrough-brand-skills` (BSC identity); `oppo-brand` (OPPO).
