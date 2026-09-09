---
name: "Watch for Allianz reply — claim 6210520873"
trigger_id: trig_01NTdSE4MBj5pQPaau8FzHh2
platform: Cowork Routine (Claude)
schedule_utc: "0 23 * * *"
schedule_local: "daily 09:00 Brisbane"
enabled: true
model: claude-opus-5
last_run: 2026-09-08T23:11:23.957303747Z ROUTINE_RUN_STATUS_SUCCEEDED
captured: 2026-09-09
---

# Watch for Allianz reply — claim 6210520873

Captured verbatim from the live Cowork Routine on 9 Sep 2026, per the
migration rule: copy first, refactor later. Metadata above; the prompt
below is untouched. Purpose, inputs and outputs are summarised in
`agents/README.md`.

## Prompt (verbatim)

```
Check Jonathan's personal email (jonathanchad@gmail.com, via the Superhuman Mail MCP — use acting_email to target that account) for any new correspondence about Allianz home insurance claim 6210520873, policy 621S618381DMP, for 21 Leslie St, Bardon QLD 4065.

Background: this is a hail damage claim from 5 December 2025. Allianz cash-settled at $41,467.66 less a $1,000 excess ($40,467.66 net), based on a Pattersons Insurebuild scope (quote IB042489) that repairs only 31 m² of a 260 m² roof. Jonathan has rejected that and written back asking that the roof component be settled at not less than $34,150 including GST — the cost of full replacement quoted by Roo Roofing on 4 August 2026 ($25,940 replacement, $4,970 anti-condensation blanket, $3,240 approvals and certification) — with no deduction for depreciation. He also asked that, failing agreement, the matter be treated as a request for a final response under internal dispute resolution so he can refer it to AFCA. Under ASIC RG 271 an insurer has 30 calendar days to give an IDR response to a standard complaint.

Check for messages received in the last 24 hours from allianz.com.au addresses (including internalassessing52@allianz.com.au, the assessor Nila Akbari, and staff writing on her behalf such as Rebecca), and from Pattersons Insurebuild. Also check for anything from AFCA.

If there is nothing new, do not notify Jonathan — just end quietly.

If there is something new: read it in full, including any attachments you can access, and send him a short summary covering
- who wrote and when
- whether they have moved on the money, and if so the new figure and how it compares to both the $40,467.66 already offered and the $34,150 roof ask
- whether they have accepted, rejected or ignored the full-replacement argument
- whether they have raised depreciation, the six-month repair-commencement provision in the PDS, or asked him to obtain further quotes
- whether they have issued a final response under internal dispute resolution, and if so the date, since that starts the clock on referring the matter to AFCA
- what he should do next, in one or two lines

Keep it brief and factual. Do not reply to Allianz or draft anything on his behalf unless he asks.
```
