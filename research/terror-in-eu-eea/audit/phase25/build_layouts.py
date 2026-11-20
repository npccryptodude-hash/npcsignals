"""Generate the lead desktop figure and all seven readable mobile layouts."""
from html import escape
import csv
from pathlib import Path
from textwrap import wrap

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
SOURCE = "d1f675eb785db712655c6952e43f3a57dd31f66c"


def read(path):
    with path.open(newline="", encoding="utf-8") as stream:
        return list(csv.DictReader(stream))


def text(x, y, value, size=14, bold=False):
    weight = ' font-weight="bold"' if bold else ""
    return f'<text x="{x}" y="{y}" font-size="{size}"{weight}>{escape(str(value))}</text>'


def svg(width, height, title, description, items):
    return "\n".join([
        f'<svg xmlns="http://www.w3.org/2000/svg" xml:lang="en" width="{width}" height="{height}" '
        f'viewBox="0 0 {width} {height}" role="img" aria-labelledby="title desc">',
        f'<title id="title">{escape(title)}</title>',
        f'<desc id="desc">{escape(description)}</desc>',
        f'<metadata>NPCsignals internal review. Statistical source commit {SOURCE}.</metadata>',
        '<rect width="100%" height="100%" fill="#fff"/>',
        '<g font-family="DejaVu Sans, sans-serif" fill="#162436">',
        *items, "</g>", "</svg>", "",
    ])


def lead(years):
    a, b = years[4:6]
    values = [a["original_attacks"], a["fixed_eu27_attacks"],
              b["original_attacks"], b["later_official_attack_revision"]]
    descriptors = ["2019 · original EU28", "2019 · fixed EU27",
                   "2020 · original EU27", "2020 · later official revision"]
    rows = list(zip(descriptors, values, strict=True))
    title = "2019–2020: geography changes the comparison"
    uk = a["included_uk_attacks"]
    note = f"2019 UK contribution: {uk} entries ({values[0]} − {uk} = {values[1]})."
    limit = "Fixed geography retains national reporting and classification differences."
    qualification = "The later official revision is shown separately from the original cohort."
    attribution = "TE-SAT 2020 p. 84 · TE-SAT 2021 pp. 12, 99 · TE-SAT 2023 p. 9 n. 4."
    boundary = "Reported statistical entries. Physical attack frequency cannot be inferred."
    items = [text(35, 48, title, 26, True), text(35, 79, "Reported attack entries")]
    for i, (label, value) in enumerate(rows):
        y = 103 + i * 72
        length = 4 * int(value)
        color = ["#235886", "#17746b", "#17746b", "#c9d3df"][i]
        items += [text(35, y + 27, label, 16),
                  f'<rect x="290" y="{y}" width="{length}" height="40" fill="{color}"/>',
                  text(305 + length, y + 27, value, 22, True)]
    items.extend(text(35, 405 + i * 22, line, 14)
                 for i, line in enumerate((note, limit, qualification, attribution, boundary)))
    items.append(text(35, 522, "NPCsignals · internal draft · statistical source checkpoint d1f675e", 12))
    desc = "; ".join(f"{label}: {value}" for label, value in rows) + ". " + boundary
    return svg(900, 540, title, desc, items), title, rows, (note, limit, qualification, attribution, boundary)


def mobile(title, rows, notes):
    items = []
    y = 23
    for line in wrap(title, 27, break_long_words=False):
        items.append(text(16, y, line, 19, True))
        y += 24
    y += 8
    for key, value in rows:
        left = [line for part in key.splitlines() for line in wrap(part, 19, break_long_words=False)]
        right = wrap(value, 22, break_long_words=False)
        height = max(len(left), len(right)) * 18 + 10
        items.append(f'<rect x="12" y="{y-16}" width="336" height="{height-2}" fill="#eef3f7"/>')
        items.extend(text(18, y + 18*i, line, 13, True) for i, line in enumerate(left))
        items.extend(text(178, y + 18*i, line, 13) for i, line in enumerate(right))
        y += height
    y += 8
    for note in (*notes, "NPCsignals · internal draft · d1f675e"):
        for line in wrap(note, 43, break_long_words=False, break_on_hyphens=False):
            items.append(text(16, y, line, 13))
            y += 18
        y += 6
    description = " | ".join(f"{key}: {value}" for key, value in rows) + ". " + " ".join(notes)
    return svg(360, y, title, description, items)


def outputs():
    a = read(ROOT / "data/phase22_annual_analysis.csv")
    desktop, title, rows, notes = lead(a)
    yield "01_2019_2020_geography.svg", desktop
    yield "mobile/01_2019_2020_geography.svg", mobile(title, rows, notes)
    yield "mobile/01_geography_en.svg", mobile(
        "EU28 and fixed EU27", [(r["reference_year"], f'{r["original_attacks"]} / {r["fixed_eu27_attacks"]}') for r in a[:5]],
        ("Reported entries: original EU28 / fixed EU27. UK rows excluded from the fixed series.",
         "UK rows: 103 / 76 / 107 / 60 / 64. The 193 chart value for 2015 remains unresolved; the annual total is 211.",
         "Sources: TE-SAT 2016–2020 annexes. Fixed geography retains national reporting differences."))
    yield "mobile/02_eu27_series_en.svg", mobile(
        "Reported counts at fixed EU27", [(r["reference_year"], f'{r["fixed_eu27_attacks"]} / {r["fixed_eu27_arrests"]}') for r in a],
        ("Each row: reported attack entries / reported arrests. From 2020 the UK is outside the original series.",
         "2023 contains 26 older attack entries; arrests 426 versus later annex sum 431. The 2015 chart value 193 and 2025 age denominator 347/344 remain unresolved.",
         "Sources: TE-SAT 2016–2026. The series does not measure physical attack frequency."))
    yield "mobile/03_revisions_en.svg", mobile(
        "Revisions and conditional sensitivity", [(r["reference_year"], " / ".join(
            (r["fixed_eu27_attacks"], r["later_official_attack_revision"] or "—", r["occurrence_sensitivity_attacks"]))) for r in a[5:9]],
        ("Fixed EU27 / later official / conditional. A dash means no later official marker.",
         "The scenario adds four older entries to 2021 and 22 to 2022, taking 26 from 2023. It also includes the official revisions. Individual joins and overlap remain unresolved.",
         "The 193 chart value for 2015 is unresolved and outside this comparison. Sources: TE-SAT 2023 p. 9 n. 4; TE-SAT 2024 p. 51 n. 75."))
    yield "mobile/04_coverage_en.svg", mobile(
        "Identification of statistical entries", [(f'{r["reference_year"]} (n={r["original_attacks"]})', " / ".join(
            r[k] for k in ("adequate_slots", "candidate_slots", "unidentified_slots"))) for r in a],
        ("Adequately identified / candidate / unidentified. Each denominator is the original annual cohort: EU28 through 2019, EU27 from 2020.",
         "2025: 17 candidate entries and 18 possible identities. These counts cannot establish physical incident coverage.",
         "Source: NPCsignals frozen crosswalk and Phase 22 annual analysis."))
    issuers = {"Bundesregierung": "Federal government"}
    institutions = read(ROOT / "audit/phase23/institutional_counts.csv")
    yield "mobile/05_institutions_en.svg", mobile(
        "Institutional counts, 2025", [(f'{r["country"]} · {issuers.get(r["issuer"], r["issuer"])}', f'{r["count"]} · {r["unit"]}') for r in institutions],
        ("Different units; no common event key or missing incident is established.",
         "Sources: NRW 2025 pp. 28, 216; Bundestag 21/4296 p. 18; PNAT bundle p. 27; TE-SAT 2026 pp. 19, 47."))
    court = read(ROOT / "audit/phase23/judicial_chain.csv")
    yield "mobile/06_judicial_en.svg", mobile(
        "Judicial and organizational evidence", [(f'{r["case"]}\n{r["date"]}',
            f'{r["stage"]}: {r["evidence"]}') for r in sorted(court, key=lambda r: (r["case"], r["date"]))],
        ("A100 linkage to the deleted Europol entry remains a candidate. The cases do not establish common operational command.",
         "Sources: LG Berlin 5/2022; BGH 036/2023; PET 14 May 2024; TE-SAT 2025; BGH 3 StR 55/26 and notice 091/2026." ))
