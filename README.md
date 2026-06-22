# Support Ops Lab

Fake data, small scripts, and support-ops ideas worth testing before they turn into anything bigger.

This is a sandbox for the kind of support patterns that show up again and again: stale replies, messy handoffs, follow-up pressure, uneven ticket load, and tickets that feel louder than they look in a normal queue.

## What's here

- `data/sample_tickets.csv` - made-up tickets for demos and tests
- `scripts/score_support_health.py` - a tiny scoring script for ticket risk
- `docs/scoring-model.md` - notes on the first scoring model
- `tests/test_score_support_health.py` - tests so the model does not drift by accident

## Run it

```bash
python3 scripts/score_support_health.py data/sample_tickets.csv
python3 -m unittest discover -s tests
```

## Why this exists

Support work has a lot of useful signals hiding in plain sight. The trick is turning those signals into something readable without pretending a person, a team, or a week of work can be reduced to one magic number.

This repo is for rough models, fake examples, and small tools that can be reused elsewhere if they prove useful.

## Data rules

Everything here should be fake or synthetic. No real customer data, private company data, credentials, exports, or internal notes belong in this repo.
