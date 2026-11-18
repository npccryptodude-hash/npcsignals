"""Verify claim-to-report parity, core numeric statements and accessible SVG metadata."""
import re
from xml.etree import ElementTree

from build_figures import HERE, SOURCE_COMMIT, read


def main():
    rows = read(HERE.parents[1] / "data" / "phase22_annual_analysis.csv")
    years = {int(row["reference_year"]): row for row in rows}
    claims = read(HERE / "claims.csv")
    report = (HERE / "REPORT.md").read_text(encoding="utf-8")
    bodies = re.findall(r"^\*\*(C\d+)\*\* (.+)$", report, re.MULTILINE)
    assert bodies == [(claim["claim_id"], claim["exact_wording"]) for claim in claims]
    assert len({claim["claim_id"] for claim in claims}) == len(claims)
    assert {int(claim["section"]) for claim in claims} == set(range(1, 13))
    assert all(all(claim.values()) for claim in claims)

    def values(field, *reference_years):
        return [int(years[year][field]) for year in reference_years]

    assert values("original_attacks", 2019, 2020, 2021) == [119, 57, 15]
    assert values("fixed_eu27_attacks", 2019, 2020, 2022, 2023, 2024, 2025) == [55, 57, 28, 120, 58, 45]
    assert max(int(row["fixed_eu27_attacks"]) for row in rows) == 120
    assert values("included_uk_attacks", 2019) == [64]
    assert values("later_official_attack_revision", 2020, 2021) == [56, 18]
    assert values("occurrence_sensitivity_attacks", 2022, 2023) == [50, 94]
    assert values("fixed_eu27_arrests", 2015, 2022, 2025) == [943, 380, 486]
    for field, count, last in (
        ("original_attacks", 1129, 45),
        ("adequate_slots", 168, 7),
        ("candidate_slots", 35, 17),
        ("unidentified_slots", 926, 21),
    ):
        assert sum(int(row[field]) for row in rows) == count
        assert values(field, 2025) == [last]
    assert values("unexplained_later_chart", 2015) == [193]
    assert values("original_arrests", 2023) == [426]
    assert values("later_retrospective_arrest_annex_sum", 2023) == [431]
    assert values("jihadist_arrest_age_footnote_denominator", 2025) == [344]
    assert "jihadist=347" in years[2025]["arrest_categories_original_scope"].split(";")

    ids = {claim["claim_id"] for claim in claims}
    for source in ("institutional_counts.csv", "judicial_chain.csv"):
        assert all(row["claim_id"] in ids and row["source_locator"] for row in read(HERE / source))
    assert [int(row["count"]) for row in read(HERE / "institutional_counts.csv")] == [5, 4, 4, 3, 2]
    namespace = "{http://www.w3.org/2000/svg}"
    figures = sorted((HERE / "figures").glob("*.svg"))
    assert len(figures) == 6
    for path in figures:
        svg = ElementTree.parse(path).getroot()
        assert svg.attrib["role"] == "img"
        assert svg.findtext(namespace + "title") and svg.findtext(namespace + "desc")
        assert SOURCE_COMMIT in svg.findtext(namespace + "metadata")
    print(f"Verified {len(claims)} claims, 12 sections and {len(figures)} figure documents.")


if __name__ == "__main__":
    main()
