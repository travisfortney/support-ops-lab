# Support Ops Lab

Small support-ops experiments using fake data: scoring models, triage helpers, QA rubrics, and reporting ideas.

This repo is intentionally simple. It is a sandbox for turning support instincts into small, testable tools without using real customer data.

## What's inside

- `data/sample_tickets.csv` - synthetic ticket data for demos and tests
- `scripts/score_support_health.py` - a tiny scoring script for support workload/health signals
- `docs/scoring-model.md` - the first scoring model notes
- `tests/test_score_support_health.py` - regression tests for the scoring script

## Run it

```bash
python3 scripts/score_support_health.py data/sample_tickets.csv
python3 -m unittest discover -s tests
```

## Why this exists

Support work has a lot of patterns hiding in plain sight: aging replies, high-friction tickets, missed follow-ups, uneven load, and quality signals. This repo is where I can model those patterns with fake data and keep the useful parts reusable.

## Data policy

All data here is fake or synthetic. No customer data, private company data, credentials, exports, or internal notes belong in this repo.
