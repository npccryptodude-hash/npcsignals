"""Build six deterministic, accessible SVG figures from versioned CSVs."""
import argparse
import csv
from html import escape
from pathlib import Path

HERE = Path(__file__).resolve().parent
LEGAL_SOURCE = "BGH original notice 091/2026 and disposition 3 StR 55/26"
SOURCE_COMMIT = "d1f675eb785db712655c6952e43f3a57dd31f66c"
INK = "#162436"
BLUE = "#235886"
TEAL = "#17746b"
AMBER = "#9b4c14"
GREY = "#c9d3df"
WIDTH = 880


def read(path):
    with path.open(newline="", encoding="utf-8") as stream:
        return list(csv.DictReader(stream))


class Figure:
    def __init__(self, title, description, height):
        self.height = height
        self.parts = [
            f'<svg xmlns="http://www.w3.org/2000/svg" width="{WIDTH}" height="{height}" '
            f'viewBox="0 0 {WIDTH} {height}" role="img" aria-labelledby="title description">',
            f'<title id="title">{escape(title)}</title>',
            f'<desc id="description">{escape(description)}</desc>',
            f'<metadata>NPCsignals internal review. Source commit {SOURCE_COMMIT}.</metadata>',
            '<g font-family="sans-serif">',
        ]
        self.rect(0, 0, WIDTH, height, "#ffffff")
        self.label(30, 39, title, size=24, bold=True)

    def label(self, x, y, value, size=14, anchor="start", bold=False):
        weight = ' font-weight="bold"' if bold else ""
        self.parts.append(
            f'<text x="{x}" y="{y}" font-size="{size}" text-anchor="{anchor}" '
            f'fill="{INK}"{weight}>{escape(str(value))}</text>'
        )

    def rect(self, x, y, width, height, fill):
        self.parts.append(
            f'<rect x="{x:.2f}" y="{y:.2f}" width="{width:.2f}" height="{height:.2f}" fill="{fill}"/>'
        )

    def grid(self, left, top, right, bottom, maximum, step, percent=False):
        for value in range(0, maximum + 1, step):
            y = bottom - (bottom - top) * value / maximum
            self.rect(left, y, right - left, 1, GREY)
            self.label(left - 9, round(y + 4, 2), f"{value}%" if percent else value, 12, "end")

    def bars(self, rows, keys, top, bottom, maximum, step, colors, unit):
        self.label(30, top - 13, unit, 13, bold=True)
        self.grid(68, top, 846, bottom, maximum, step)
        group_width = 770 / len(rows)
        width = min(28, (group_width - 12) / len(keys))
        for i, row in enumerate(rows):
            center = 72 + group_width * (i + 0.5)
            self.label(round(center, 2), bottom + 23, row["reference_year"], 12, "middle")
            for j, (key, color) in enumerate(zip(keys, colors, strict=True)):
                value = int(row[key])
                height = (bottom - top) * value / maximum
                x = center + (j - len(keys) / 2) * width
                self.rect(x, bottom - height, width - 2, height, color)
                self.label(round(x + width / 2, 2), round(bottom - height - 5, 2),
                           value, 12, "middle")

    def save(self, output, filename):
        self.label(30, self.height - 16, "npcsignals · internt utkast · kildegrunnlag d1f675e", 11)
        (output / filename).write_text("\n".join([*self.parts, "</g>", "</svg>", ""]), encoding="utf-8")


def annual_figures(output, rows):
    fig = Figure("eu28 og fast eu27, 2015–2019",
                 "To stolper per år. Originalserien inkluderer Storbritannia; fast EU27 trekker fra den britiske raden.", 435)
    fig.label(30, 69, "venstre: original eu28 · høyre: fast eu27", 14)
    fig.bars(rows[:5], ["original_attacks", "fixed_eu27_attacks"], 108, 300, 250, 50,
             [BLUE, TEAL], "rapporterte angrepsposter")
    fig.label(30, 356, "britiske poster trukket fra: " + " / ".join(r["included_uk_attacks"] for r in rows[:5]), 13)
    fig.label(30, 376, "2015: figurobservasjonen 193 har uavklart grunnlag; 211 er originalt årstall.", 12)
    fig.label(30, 395, "fast geografi beholder nasjonal rapporteringspraksis.", 12)
    fig.save(output, "01_geography.svg")

    fig = Figure("rapporterte tall ved fast eu27-geografi",
                 "Elleve år med angrepsposter og pågripelser i to separate paneler med nullbaserte akser.", 655)
    fig.bars(rows, ["fixed_eu27_attacks"], 91, 245, 150, 30, [BLUE], "angrepsposter")
    fig.bars(rows, ["fixed_eu27_arrests"], 330, 485, 1000, 200, [TEAL], "rapporterte pågripelser")
    fig.label(30, 538, "fra 2020: britisk rad er ute av originalserien; fast eu27 bruker samme geografi gjennom perioden.", 13)
    fig.label(30, 561, "2023: 26 eldre poster i angrepskohorten; 426 pågripelser mot senere tabellsum 431.", 13)
    fig.label(30, 584, "2015: 193 er en separat figurobservasjon · 2025: aldersnevneren 347/344 er uavklart.", 12)
    fig.label(30, 606, "rapporterte kohorter; faktisk hendelsesfrekvens kan ikke utledes.", 12)
    fig.save(output, "02_eu27_series.svg")

    selected = rows[5:9]
    fig = Figure("offisielle revisjoner og betinget følsomhet",
                 "Fast EU27 mot analytisk scenario for 2020–2023. To separate markører viser dokumenterte revisjoner.", 490)
    fig.label(30, 68, "venstre: fast eu27 · høyre: betinget scenario · oransje markør: senere offisielt tall", 13)
    fig.bars(selected, ["fixed_eu27_attacks", "occurrence_sensitivity_attacks"],
             108, 315, 150, 30, [BLUE, TEAL], "rapporterte eller omfordelte angrepsposter")
    for i, row in enumerate(selected):
        revision = row["later_official_attack_revision"]
        if revision:
            x = 72 + 770 / len(selected) * (i + 0.5) + 56
            y = 315 - (315 - 108) * int(revision) / 150
            fig.rect(x, y - 4, 8, 8, AMBER)
            fig.label(x + 11, round(y + 4, 2), revision, 12)
    fig.label(30, 372, "senere offisielle tall: 56 (2020) og 18 (2021); øvrige markører mangler.", 13)
    fig.label(30, 398, "scenario: offisielle revisjoner og omfordeling av 26 eldre poster til 2021 (+4) og 2022 (+22).", 12)
    fig.label(30, 424, "2015, utenfor panelet: 193 i senere figur har uavklart grunnlag.", 12)
    fig.label(30, 450, "omfordelingen er betinget; enkelthendelser og mulig overlapp er uavklart.", 12)
    fig.save(output, "03_revisions.svg")

    fig = Figure("identifikasjon av statistiske poster",
                 "Tre stablede andeler for hvert år. Total og eksakte klassetall står under hver stolpe.", 500)
    fig.label(30, 70, "nederst: tilstrekkelig · midten: kandidat · øverst: uidentifisert", 14)
    fig.grid(68, 104, 846, 319, 100, 25, percent=True)
    for i, row in enumerate(rows):
        center = 104 + i * 70
        total = int(row["original_attacks"])
        counts = [int(row[f"{key}_slots"]) for key in ("adequate", "candidate", "unidentified")]
        bottom = 319
        for count, color in zip(counts, [BLUE, AMBER, GREY], strict=True):
            height = 215 * count / total
            if count:
                fig.rect(center - 18, bottom - height, 36, height, color)
            bottom -= height
        fig.label(center, 343, row["reference_year"], 12, "middle", True)
        fig.label(center, 363, f"n={total}", 11, "middle")
        fig.label(center, 383, "/".join(map(str, counts)), 10, "middle")
    fig.label(30, 420, "original geografi: eu28 til og med 2019; eu27 fra 2020.", 13)
    fig.label(30, 442, "i 2025 svarer 17 kandidatposter til 18 mulige identiteter.", 12)
    fig.label(30, 464, "den fysiske hendelsesdekningen kan ikke utledes av disse andelene.", 12)
    fig.save(output, "04_coverage.svg")


def qualitative_figures(output):
    institutions = read(HERE / "institutional_counts.csv")
    fig = Figure("institusjonelle tellinger, 2025",
                 "Fem rader viser særskilte institusjonelle enheter i Tyskland og Frankrike.", 350)
    units = {
        ("DE", "NRW"): "jihadistisk motiverte angrep i hele tyskland",
        ("DE", "Bundesregierung"): "navngitte steder i føderalt svar",
        ("FR", "PNAT"): "fullførte jihadistisk inspirerte angrep",
    }
    for i, row in enumerate(institutions):
        y = 103 + i * 34
        fig.rect(30, y - 22, 820, 30, "#eef3f7" if i % 2 == 0 else "#ffffff")
        fig.label(45, y, row["country"], 14, bold=True)
        fig.label(100, y, row["issuer"])
        fig.label(280, y, row["count"], 16, bold=True)
        fig.label(325, y, units.get((row["country"], row["issuer"]), "fullførte jihadistiske europolposter"))
    fig.label(30, 293, "kildene oppgir ulike telleenheter; de publiserte radene har ingen felles hendelsesnøkkel.", 13)
    fig.save(output, "05_institutions.svg")

    events = read(HERE / "judicial_chain.csv")
    fig = Figure("rettslige og organisatoriske beviskjeder",
                 "Daterte rader viser initial vurdering, dom og rettskraft i A100, PETs oppsummering for Holbæk og flere kildetyper for Solingen.", 490)
    labels = {
        "initial assessment": "innledende mistanke om islamistisk angrep",
        "first instance": "domstolen avviser klassifisering og beslutter plassering",
        "finality": "BGH forkaster revisjonen; avgjørelsen er rettskraftig",
        "appeal reported": "PET oppgir ankefunn om terrorforsøk og finansiering",
        "official assessment published": "Europol omtaler kommunikasjon og oppmuntring",
        "court summary published": "BGH gjengir oppmuntring og råd fra IS-kontakter",
    }
    for i, row in enumerate(sorted(events, key=lambda item: (item["case"], item["date"]))):
        y = 103 + i * 39
        fig.rect(30, y - 23, 820, 34, "#eef3f7" if i % 2 == 0 else "#ffffff")
        fig.label(44, y, row["case"], 14, bold=True)
        fig.label(145, y, row["date"], 13)
        label = ("BGH forkaster revisjonen; draps- og medlemskapsdommen er rettskraftig"
                 if row["case"] == "Solingen" and row["stage"] == "finality" else labels[row["stage"]])
        fig.label(255, y, label, 13)
    fig.label(30, 405, "A100: kobling til slettet europolpost står som kandidat.", 13)
    fig.label(30, 428, "sakene gir ikke grunnlag for å fastslå en felles operativ kommandostruktur.", 12)
    fig.label(30, 452, LEGAL_SOURCE, 12)
    fig.save(output, "06_judicial.svg")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=HERE / "figures")
    output = parser.parse_args().output
    output.mkdir(parents=True, exist_ok=True)
    annual_figures(output, read(HERE.parents[1] / "data" / "phase22_annual_analysis.csv"))
    qualitative_figures(output)


if __name__ == "__main__":
    main()
