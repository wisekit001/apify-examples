"""Check whether ChatGPT and Perplexity recommend your brand, and print the
mention rate, citation rate and share of voice.

    pip install "apify-client>=3"
    export APIFY_TOKEN=...
    python ai_visibility_weekly.py --demo     # free, fictional brand, no AI calls
    python ai_visibility_weekly.py            # real check: about $0.35 for 5 prompts x 2 engines
"""
import json
import os
import sys

from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])
run_input = (
    {"brandName": "demo", "demoMode": True}
    if "--demo" in sys.argv
    else {
        "brandName": "YourBrand",
        "brandDomain": "yourbrand.com",
        "category": "project management tool",
        "competitors": ["CompetitorA", "CompetitorB"],
        "engines": ["chatgpt", "perplexity"],
        "monitorName": "weekly",
    }
)
run = client.actor("wisekit/ai-search-visibility-tracker").call(run_input=run_input)
summary = client.key_value_store(run.default_key_value_store_id).get_record("SUMMARY")
value = (summary.get("value") if isinstance(summary, dict) else getattr(summary, "value", None)) if summary else None
print(json.dumps(value or {}, indent=2, default=str)[:4000])
