---
name: "AI Signal Benchmark"
trigger_id: trig_01T8LKzHw5xDtJjYRg6kwTfY
platform: Cowork Routine (Claude)
schedule_utc: "0 20 1,15 * *"
schedule_local: "1st and 15th, 06:00 Brisbane"
enabled: true
model: claude-sonnet-4-6
last_run: 2026-09-01T20:09:02.229811517Z ROUTINE_RUN_STATUS_SUCCEEDED
captured: 2026-09-09
---

# AI Signal Benchmark

Captured verbatim from the live Cowork Routine on 9 Sep 2026, per the
migration rule: copy first, refactor later. Metadata above; the prompt
below is untouched. Purpose, inputs and outputs are summarised in
`agents/README.md`.

## Prompt (verbatim)

```
You are running the AI Signal benchmark pipeline. This is an automated run.

Steps:
1. Install dependencies: `npm install`
2. Fetch API keys from Cloudflare KV using the Cloudflare MCP. The keys are stored in the AUTH_KV namespace (KV namespace ID can be found in wrangler.toml) under the key `api_keys` as a JSON object. Use the Cloudflare MCP tool `kv_namespace_get` to read this key. Then write a `.env` file in the project root with the key-value pairs (one per line, format: KEY=value). The JSON contains: ANTHROPIC_API_KEY, GOOGLE_AI_STUDIO_API_KEY, OPENAI_API_KEY, RESEND_API_KEY.
3. Run the full benchmark: `node scripts/run-benchmark.js`
4. If the benchmark succeeds, export the static site: `node scripts/export-static.js`
5. Deploy to Cloudflare Pages: `npx wrangler pages deploy dist/ --project-name=ai-signal`
6. Send the results email: `node scripts/send-report.js`

If any platform fails the health check, the benchmark will abort. Report which platforms failed and why.

IMPORTANT: Do NOT skip any steps. Run them in order. If a step fails, report the error and stop.
```
