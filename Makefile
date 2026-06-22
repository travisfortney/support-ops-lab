test:
	python3 -m unittest discover -s tests

run:
	python3 scripts/score_support_health.py data/sample_tickets.csv
