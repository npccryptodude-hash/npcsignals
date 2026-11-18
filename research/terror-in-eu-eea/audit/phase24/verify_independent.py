"""Check raw transcriptions and rendered-SVG data independently of Phase 23 code."""
import csv
from pathlib import Path
import re
from xml.etree import ElementTree as ET

ROOT = Path(__file__).resolve().parents[2]
FIGURES = ROOT / "audit/phase23/figures"
NS = {"s": "http://www.w3.org/2000/svg"}
OUTCOMES = ("completed", "failed", "foiled")


def read(path):
    with (ROOT / path).open(newline="", encoding="utf-8") as stream:
        return list(csv.DictReader(stream))


def sums(rows, *fields):
    return [sum(int(row[field]) for row in rows) for field in fields]


def totals(path):
    rows = read(path)
    return sums(rows, "total")[0], sums(
        [row for row in rows if row["country_iso2"] != "GB"], "total"
    )[0]


def labels(index):
    path, = FIGURES.glob(f"{index:02}_*.svg")
    return [e.text for e in ET.parse(path).findall(".//s:text", NS)]


def main():
    original = [totals(f"{year}/attacks.csv") for year in range(2015, 2024)]
    assert original[4:6] == [(119, 55), (57, 57)]
    assert original[6:9] == [(15, 15), (28, 28), (120, 120)]
    outcomes24 = sums(read("data/eu_2024_attack_outcomes_by_country.csv"), *OUTCOMES)
    rows25 = [row for row in read("data/terror_2025_country_statistics.csv")
              if row["source_system"] == "TE-SAT 2026" and len(row["country_iso2"]) == 2]
    outcomes25 = [sum(int(row["value"]) for row in rows25 if row["measure"] == outcome)
                  for outcome in OUTCOMES]
    assert outcomes24 == [34, 5, 19] and outcomes25 == [22, 3, 20]
    original.extend((sum(outcomes), sum(outcomes)) for outcomes in (outcomes24, outcomes25))
    assert max(pair[1] for pair in original) == 120

    provenance = {row["adjustment_id"]: int(row["affected_records"]) for row in read("2021/provenance.csv")}
    deletion, added, earlier21, earlier22 = (
        provenance[key] for key in ("DE20-JIH-REMOVE", "FR21-RW-LATE",
                                    "FR-COR-2021-RETRO", "FR-COR-2022-RETRO")
    )
    assert [57 - deletion, 15 + added] == [56, 18]
    assert [57 - deletion, 15 + added + earlier21, 28 + earlier22, 120 - earlier21 - earlier22] == [56, 22, 50, 94]
    assert [120 - 28, (120 - earlier21 - earlier22) - (28 + earlier22)] == [92, 44]

    fixed_arrests = [totals(f"{year}/arrests.csv")[1] for year in range(2015, 2025)]
    fixed_arrests.append(totals("audit/arrests_2025.csv")[1])
    assert [fixed_arrests[i] for i in (0, 7, 8, 10)] == [943, 380, 426, 486]
    assert sums(read("audit/arrests_2025.csv"), "jihadist") == [347]
    assert sums(read("2023/arrests.csv"), "right_wing") == [26]
    assert 426 + (12 - 4) - 2 - 1 == 431
    assert 340 + 201 + 56 == 597

    names = ("adequate", "candidate", "unidentified")
    partitions = [sums(read(f"{year}/crosswalk.csv"), *names) for year in range(2015, 2025)]
    narrative = (ROOT / "2025_INCIDENT_IDENTIFICATION_PHASE6.md").read_text()
    cells = re.findall(r"^\| [^|]+ (completed|failed|foiled) \| (\d+) \| (\d+) \| (\d+) \| (\d+) \|", narrative, re.M)
    assert [sum(int(cell[2]) for cell in cells if cell[0] == outcome) for outcome in OUTCOMES] == [6, 0, 1]
    partitions.append([sum(int(cell[column]) for cell in cells) for column in (2, 3, 4)])
    assert list(map(sum, zip(*partitions))) == [168, 35, 926]
    assert sum(sum(partition) for partition in partitions) == 1129

    yearly = read("data/phase22_annual_analysis.csv")
    for i, counts in enumerate(partitions):
        n = sum(counts)
        assert n == original[i][0]
        for key, count in zip(names, counts, strict=True):
            assert abs(float(yearly[i][key + "_slot_pct"]) - 100 * count / n) <= 0.005001
        assert f"n={n}" in labels(4)
        assert "/".join(map(str, counts)) in labels(4)

    for index, values in ((1, [n for pair in original[:5] for n in pair]),
                          (2, [pair[1] for pair in original] + fixed_arrests),
                          (3, [57, 15, 28, 120, 56, 22, 50, 94, 18]),
                          (5, [5, 4, 4, 3, 2])):
        assert all(str(value) in labels(index) for value in values)
    assert "2026-05-12" in labels(6) and "2026-05-22" in labels(6)
    print("PASS: raw-data arithmetic, country scope, 11 confidence partitions, 2025 outcome coverage, and SVG labels.")


if __name__ == "__main__":
    main()
