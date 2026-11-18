# 31-country coverage register — first pass

status: methodology and availability register, not a complete dataset. coverage is not equivalent to zero incidents.

## fixed study area

eu27: at be bg hr cy cz dk ee fi fr de gr hu ie it lv lt lu mt nl pl pt ro sk si es se.
additional: gb is li no.

## annual record rules

- reported_in_tesat_annex: country-level row in the annual source.
- not_listed_in_attacks_table: no attack row; not automatically a verified zero.
- supplement_needed: national source required for 31-country coverage.
- verified_zero: authoritative source explicitly confirms zero for the exact metric and period.
- unverified: not yet checked.

## 2024 source coverage

eu te-sat 2025 annex page 62 lists 14 member states reporting 58 attacks in 2024. country outcome rows are transcribed in data/eu_2024_attack_outcomes_by_country.csv. arithmetic check: 34 completed, 5 failed, 19 foiled, 58 total.

the other 13 eu countries are not entered as verified zeros by this extract. uk and three non-eu eea states require supplementation. no 31-country total yet.

## 2023 caution

eu te-sat 2024 reports 120 eu attacks. its map labels require manual country verification before per-country transcription. prefer tabular annex.

## next steps

create full 31-country by 11-year matrix (341 country-years), with missingness explicit; verify source coverage and definitions per year; retrieve 2025 country outcomes from the official 2026 annex; add uk/no/is/li national sources.

primary source: https://www.europol.europa.eu/cms/sites/default/files/documents/EU_TE-SAT_2025.pdf

## 2025 coverage update — 2026-11-18

See the [31-country matrix](data/terror_2025_coverage.csv) and [comparative audit](2025_EUROPE_COMPARATIVE_REPORT.md). This dated extraction supplements the historical coverage matrix. An absent TE-SAT attack row is kept distinct from scoped national zeros and from national sources using other metrics.
