# source register and ingestion queue

status labels: identified = official publication located; extracted = structured data independently checked; pending = not yet checked.

| id | source | coverage | status | url |
| --- | --- | --- | --- | --- |
| src-europol-tesat-2026 | europol, eu te-sat 2026 | eu, reference year 2025 | identified | https://op.europa.eu/en/publication-detail/-/publication/51f6ac4d-c326-11f1-bfcb-01aa75ed71a1/language-en |
| src-europol-tesat-2025 | europol, eu te-sat 2025 | eu, reference year 2024 | identified | https://op.europa.eu/en/publication-detail/-/publication/a8035d30-5241-11f0-a9d0-01aa75ed71a1/language-en |
| src-europol-series | europol, eu te-sat editions | historical eu reporting, scope varies | identified | https://www.europol.europa.eu/publications-events/main-reports/tesat-report |
| src-europol-ectc | europol european counter terrorism centre | european cross-border context | identified | https://www.europol.europa.eu/about-europol/european-counter-terrorism-centre-ectc |
| src-uk-home-office | uk home office terrorism statistics | united kingdom, especially post-2020 | pending | https://www.gov.uk/government/collections/operation-of-police-powers-under-the-terrorism-act-2000 |

## next ingestion steps

1. retrieve each annual eu te-sat edition for reference years 2015–2025 and transcribe category totals with precise page citations.
2. audit each edition's territorial and category definitions; track uk inclusion before and after eu departure.
3. obtain primary uk, norway, iceland and liechtenstein statistics for uncovered years; do not interpret missing reporting as zero incidents.
4. reconcile country-level cases and deduplicate cross-border plots across the fixed 31-country area.
5. create incident and actor records only with traceable primary documentation.
6. review and publish the first statistical comparison after independent checks.

## initial cross-check, eu only, 2025

europol te-sat 2026 reports 45 total completed/failed/foiled attacks, of which 24 jihadist, 12 left-wing/anarchist and 5 right-wing; remaining 4 other categories. this is a preliminary source-level summary, not a validated 2015–2025 series or a 31-country total.

## 2026-11-18 incident verification update

- [Full TE-SAT 2026](https://www.europol.europa.eu/cms/sites/default/files/documents/EU-TE-SAT-2026.pdf), DOI 10.2813/5264545, pp. 5, 18–20, 27, 29–30, 47. Keep the existing Executive Summary identifier for its distinct edition.
- [2025 incident reconciliation and publication gaps](2025_INCIDENT_RECONCILIATION.md).
- [Structured 2025 verification sources](data/jihadist_2025_sources.csv).
