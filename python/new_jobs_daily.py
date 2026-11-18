"""Print every job that is new (or closed) since the last run on a list of
Greenhouse, Lever, Ashby and Workable job boards.

Run it once a day (cron, Task Scheduler, GitHub Actions). The first run saves a
baseline; later runs print only the changes.

    pip install "apify-client>=3"
    export APIFY_TOKEN=...            # https://console.apify.com/settings/integrations
    python new_jobs_daily.py          # add --demo for a free run on fictional data
"""
import os
import sys

from apify_client import ApifyClient

COMPANIES = [
    "greenhouse:yourcompany",
    "lever:anothercompany",
    "ashby:thirdcompany",
]

client = ApifyClient(os.environ["APIFY_TOKEN"])
run_input = (
    {"companies": ["demo"], "demoMode": True}
    if "--demo" in sys.argv
    else {
        "companies": COMPANIES,
        "keywords": ["engineer"],
        "monitorName": "daily-jobs",
        "onlyChanges": True,
        "includeDescription": False,
    }
)
run = client.actor("wisekit/ats-job-feed").call(run_input=run_input)

for row in client.dataset(run.default_dataset_id).iterate_items():
    if row.get("type") == "job":
        print(f'{row.get("changeType", ""):9} {row["company"]:20} {row["title"]} {row["jobUrl"]}')
    else:
        print(f'{"(board)":9} {row.get("input", "")}: {row.get("status")} {row.get("message", "")}')
