#!/usr/bin/env python3
import csv
import sys
from collections import defaultdict

PRIORITY_WEIGHT = {
    "low": 0,
    "normal": 1,
    "high": 2,
    "urgent": 3,
}


def row_risk(row):
    risk = 0
    age_hours = float(row["age_hours"])
    replies = int(row["replies"])
    follow_up_due_hours = float(row["follow_up_due_hours"])
    priority = PRIORITY_WEIGHT.get(row["priority"].lower(), 1)
    status = row["status"].lower()
    waiting_on_customer = row["waiting_on_customer"].lower() == "true"
    csat_raw = row.get("csat", "").strip()

    if status != "solved":
        risk += 10
    risk += min(age_hours / 6, 10)
    risk += min(replies, 10) * 0.7
    risk += priority * 3

    if follow_up_due_hours <= 2 and not waiting_on_customer:
        risk += 8
    elif follow_up_due_hours <= 8 and not waiting_on_customer:
        risk += 4

    if waiting_on_customer:
        risk -= 3

    if csat_raw:
        csat = int(csat_raw)
        if csat <= 2:
            risk += 10
        elif csat == 3:
            risk += 5
        elif csat >= 5:
            risk -= 2

    return max(0, round(risk, 1))


def risk_band(score):
    if score >= 30:
        return "red"
    if score >= 18:
        return "yellow"
    return "green"


def summarize(rows):
    by_owner = defaultdict(lambda: {"tickets": 0, "risk": 0.0, "red": 0, "yellow": 0, "green": 0})
    scored_rows = []

    for row in rows:
        score = row_risk(row)
        band = risk_band(score)
        row = dict(row)
        row["risk_score"] = score
        row["risk_band"] = band
        scored_rows.append(row)

        owner = row["owner"]
        by_owner[owner]["tickets"] += 1
        by_owner[owner]["risk"] += score
        by_owner[owner][band] += 1

    return scored_rows, by_owner


def print_summary(scored_rows, by_owner):
    print("Support health summary")
    print("======================")
    for owner in sorted(by_owner):
        item = by_owner[owner]
        avg = item["risk"] / item["tickets"]
        print(f"{owner}: tickets={item['tickets']} avg_risk={avg:.1f} red={item['red']} yellow={item['yellow']} green={item['green']}")

    print("\nHighest risk tickets")
    print("====================")
    for row in sorted(scored_rows, key=lambda item: item["risk_score"], reverse=True)[:5]:
        print(f"{row['ticket_id']}: {row['owner']} {row['risk_band']} score={row['risk_score']} topic={row['topic']}")


def main(path):
    with open(path, newline="") as handle:
        rows = list(csv.DictReader(handle))
    scored_rows, by_owner = summarize(rows)
    print_summary(scored_rows, by_owner)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: score_support_health.py data/sample_tickets.csv", file=sys.stderr)
        sys.exit(64)
    main(sys.argv[1])
