"""Emit the Phase 22 annual analytical table as CSV on stdout."""
import csv
from pathlib import Path
import sys

from recalculate import annual, issues

ROOT = Path(__file__).resolve().parents[1]
CAVEATS = {
    2015: "193 alternate figure; French overview/annex conflict; partial outcome allocation",
    2016: "379/374 injuries versus 597 across three narratives; partial outcome allocation",
    2017: "UK attack subcategories partly available; Northern Ireland casualty exclusions",
    2018: "Dutch annex duplicate and distinct Hague judicial outcome; Belgium arrest coding",
    2019: "UK included; additional Northern Ireland arrests outside operative total",
    2020: "57 original, 56 later official; withdrawn case identity unverified",
    2021: "15 original, 18 later official; conditional transfer adds four further entries",
    2022: "22 earlier occurrences published in the 2023 cohort; sensitivity assumes transfer",
    2023: "26 earlier occurrences included; 426 arrests versus later annex sum 431",
    2024: "Other/unspecified completion conflict; operative six completed corroborated",
    2025: "347 jihadist arrests versus age footnote 344; France and Essen mappings unresolved",
}


def index(path):
    with (ROOT / path).open(newline="") as source:
        return {int(row["reference_year"]): row for row in csv.DictReader(source)}


def main():
    baseline = index("data/eu_statistical_reconciliation_2015_2025.csv")
    sources = index("audit/source_integrity.csv")
    rows = []
    for year in range(2015, 2026):
        row = baseline[year]
        source = sources[year]
        counts = annual(year)
        slots = int(row["original_attacks"])
        if slots != counts["attacks"] or slots != sum(
            int(row[f"{confidence}_slots"])
            for confidence in ("adequate", "candidate", "unidentified")
        ):
            raise ValueError(f"Slot denominator mismatch for {year}")
        shares = {
            f"{confidence}_slot_pct": f"{100 * int(row[f'{confidence}_slots']) / slots:.2f}"
            for confidence in ("adequate", "candidate", "unidentified")
        }
        rows.append({
            **row,
            "edition": source["edition"],
            "source_id": source["source_id"],
            "source_url": source["source_url"],
            "statistical_printed_pages": source["statistical_printed_pages"],
            "attack_categories_original_scope": counts["attack_categories"],
            "arrest_categories_original_scope": counts["arrest_categories"],
            **shares,
            "slot_confidence_scope": "frozen original edition cohort",
            "aggregate_comparability": "qualified reported cohorts; fixed geography only",
            "category_comparability": "edition labels; see category comparability matrix",
            "known_caveats": CAVEATS[year],
            "later_retrospective_arrest_annex_sum": 431 if year == 2023 else "",
            "jihadist_arrest_age_footnote_denominator": 344 if year == 2025 else "",
        })
    if issues:
        raise ValueError("\n".join(issues))
    writer = csv.DictWriter(sys.stdout, fieldnames=list(rows[0]), lineterminator="\n")
    writer.writeheader()
    writer.writerows(rows)


if __name__ == "__main__":
    main()
