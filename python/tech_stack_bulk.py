"""Find the CMS, analytics, hosting and email provider of a list of websites
and save it as CSV.

    pip install "apify-client>=3"
    export APIFY_TOKEN=...
    python tech_stack_bulk.py sites.txt out.csv     # one domain or URL per line
    python tech_stack_bulk.py --demo                # free run on fictional sites
"""
import csv
import os
import sys

from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])
if "--demo" in sys.argv:
    run_input, out_path = {"urls": ["example.com"], "demo": True}, "demo.csv"
else:
    with open(sys.argv[1], encoding="utf-8") as f:
        urls = [line.strip() for line in f if line.strip()]
    run_input, out_path = {"urls": urls, "includeEmailProvider": True}, sys.argv[2]

run = client.actor("wisekit/tech-stack-detector").call(run_input=run_input)
rows = list(client.dataset(run.default_dataset_id).iterate_items())

flat = []
for row in rows:
    flat.append({k: (", ".join(map(str, v)) if isinstance(v, list) else v)
                 for k, v in row.items() if not isinstance(v, dict)})
fields = sorted({k for r in flat for k in r})
with open(out_path, "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=fields)
    w.writeheader()
    w.writerows(flat)
print(f"{len(flat)} rows written to {out_path}")
