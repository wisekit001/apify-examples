# Apify examples: job feeds, tech stacks and AI visibility

Copy-and-run examples for calling [Wisekit's Apify Actors](https://apify.com/wisekit) from n8n, Python or curl. Every example has a **free demo mode** that returns fictional sample data, so you can try the whole flow without spending anything.

*Disclosure: we built these Actors. The examples are MIT-licensed; the Actors are paid per result on Apify.*

| Example | What it does | Actor | Price |
|---|---|---|---|
| [`n8n/ats-new-jobs-to-slack.json`](n8n/ats-new-jobs-to-slack.json) | Every morning, posts new jobs from Greenhouse, Lever and Ashby boards to a Slack channel | [ATS Job Feed](https://apify.com/wisekit/ats-job-feed) | $0.001 per job + $0.002 per board |
| [`python/new_jobs_daily.py`](python/new_jobs_daily.py) | Prints new and closed jobs since the last run | [ATS Job Feed](https://apify.com/wisekit/ats-job-feed) | same |
| [`python/tech_stack_bulk.py`](python/tech_stack_bulk.py) | CMS, analytics, hosting and email provider for a list of sites, saved as CSV | [Tech Stack Detector](https://apify.com/wisekit/tech-stack-detector) | $2 per 1,000 sites |
| [`python/ai_visibility_weekly.py`](python/ai_visibility_weekly.py) | Whether ChatGPT and Perplexity mention and cite your brand vs competitors | [AI Visibility Tracker](https://apify.com/wisekit/ai-search-visibility-tracker) | $0.02–$0.10 per check |

Failed or blocked results are free in all three Actors.

## Before you start

1. Create a free [Apify account](https://console.apify.com/sign-up) and copy your API token from **Settings → API & Integrations**.
2. Never commit the token. The examples read it from the `APIFY_TOKEN` environment variable (Python) or an n8n credential.

## n8n: new jobs to Slack every morning

1. In n8n, go to **Workflows → Import from file** and choose `n8n/ats-new-jobs-to-slack.json`.
2. Open **Run ATS Job Feed (Apify)** and create a **Header Auth** credential with name `Authorization` and value `Bearer <your Apify API token>`.
3. Replace the `companies` with real job boards: `greenhouse:board`, `lever:board`, `ashby:board`, or full board URLs such as `https://boards.greenhouse.io/yourcompany`. To test for free, use `{"companies": ["demo"], "demoMode": true}`.
4. Paste a Slack [incoming webhook](https://api.slack.com/messaging/webhooks) URL into **Post to Slack**, or swap that node for Google Sheets, email or a database.
5. Activate the workflow.

The first run saves every open job as the baseline and posts nothing. From the next morning on, only new jobs reach Slack. The call waits up to 5 minutes for the run; for long company lists, split them over several workflows.

## Python

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=...           # PowerShell: $env:APIFY_TOKEN="..."
python python/new_jobs_daily.py --demo
python python/tech_stack_bulk.py --demo
python python/ai_visibility_weekly.py --demo
```

Drop `--demo` and edit the inputs at the top of each script to run on real data.

## curl

```bash
curl -s -X POST "https://api.apify.com/v2/acts/wisekit~ats-job-feed/run-sync-get-dataset-items" \
  -H "Authorization: Bearer $APIFY_TOKEN" -H "Content-Type: application/json" \
  -d '{"companies": ["demo"], "demoMode": true}'
```

## AI agents (MCP)

Each Actor is also a tool on Apify's MCP server, for Claude, Cursor and other MCP clients:
`https://mcp.apify.com?tools=wisekit/ats-job-feed,wisekit/tech-stack-detector,wisekit/ai-search-visibility-tracker`

## Questions

Open an issue here or on the Actor's **Issues** tab on Apify. The ATS Job Feed is not affiliated with Greenhouse, Lever, Ashby or Workable; the AI Visibility Tracker is not affiliated with OpenAI, Perplexity, Google or Anthropic.
