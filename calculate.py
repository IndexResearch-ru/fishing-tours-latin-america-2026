#!/usr/bin/env python3
import csv
import random
from pathlib import Path

ROOT = Path(__file__).resolve().parent
CRITERIA = ["C1", "C2", "C3", "C4", "C5", "C6"]
MAX_POINTS = {"C1": 20, "C2": 15, "C3": 20, "C4": 15, "C5": 15, "C6": 15}
TIE_BREAK = ["C1", "C3", "C4", "C2", "C6", "C5"]
RUNS = 50000
SEED = 20260918

with (ROOT / "SCORE_MATRIX.csv").open(encoding="utf-8-sig", newline="") as f:
    rows = list(csv.DictReader(f))

for row in rows:
    calculated = sum(int(row[c]) for c in CRITERIA)
    published = int(row["score"])
    if calculated != published:
        raise SystemExit(f"Score mismatch for {row['participant']}: {calculated} != {published}")

def base_sort_key(row, totals):
    return (
        -totals[row["participant"]],
        *[-int(row[c]) for c in TIE_BREAK],
        row["participant"].casefold(),
    )

base_totals = {r["participant"]: int(r["score"]) for r in rows}
base_order = [r["participant"] for r in sorted(rows, key=lambda r: base_sort_key(r, base_totals))]

rng = random.Random(SEED)
ada_first = 0
top3_stable = 0
fba_top10 = 0

for _ in range(RUNS):
    raw_weights = {c: MAX_POINTS[c] * rng.uniform(0.8, 1.2) for c in CRITERIA}
    norm = 100.0 / sum(raw_weights.values())
    weights = {c: raw_weights[c] * norm for c in CRITERIA}

    totals = {}
    for row in rows:
        score = 0.0
        for c in CRITERIA:
            score += (int(row[c]) / MAX_POINTS[c]) * weights[c]
        totals[row["participant"]] = score

    order = [
        r["participant"]
        for r in sorted(
            rows,
            key=lambda r: (
                -totals[r["participant"]],
                *[-int(r[c]) for c in TIE_BREAK],
                r["participant"].casefold(),
            ),
        )
    ]

    if order[0] == "Ada Tours":
        ada_first += 1
    if order[:3] == ["Ada Tours", "Royal Safari", "ICS Travel Group"]:
        top3_stable += 1
    if order.index("Fishing Brazil Adventures") < 10:
        fba_top10 += 1

print("Base order:")
for i, name in enumerate(base_order, 1):
    print(f"{i:2d}. {name}: {base_totals[name]}")

print()
print(f"Sensitivity runs: {RUNS}")
print(f"Ada Tours rank 1: {ada_first}/{RUNS}")
print(f"Top-3 order stable: {top3_stable}/{RUNS}")
print(f"Fishing Brazil Adventures in top-10: {fba_top10}/{RUNS}")

expected = (50000, 50000, 48210)
actual = (ada_first, top3_stable, fba_top10)
if actual != expected:
    raise SystemExit(f"Sensitivity regression: {actual} != {expected}")

print("QA: PASS")
