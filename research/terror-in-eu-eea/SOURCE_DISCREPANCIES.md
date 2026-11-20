# source revision discrepancy — 2020 and 2021

date: 2026-11-18
status: unresolved; review required before cross-edition comparisons

eu council historical infographic reports 2020=57 and 2021=15. the europol te-sat 2023 executive summary retrospectively says 2020=56 and 2021=18. these figures are inconsistent across editions/summaries and should not be silently harmonised.

- council: https://www.consilium.europa.eu/en/infographics/terrorism-eu-facts-figures/
- europol te-sat 2023 executive summary: https://www.europol.europa.eu/cms/sites/default/files/documents/TE-SAT%202023%20-%20Executive%20Summary.pdf

the historical totals csv currently uses council 57/15 and must be treated as a source-specific reported series, not a single definitive reconciled series. determine whether changes arise from later revisions, category reclassification, editorial inconsistency or different reporting definitions. preserve original edition values and page references in separate rows if confirmed. no publication-ready claim about the magnitude of 2020-to-2021 change until resolved.

the 2023 country map was also rendered inconsistently by text extraction tools. do not ingest country values from that map until visual/manual verification against the source.


## 2024 category-versus-outcome reconciliation (2026-11-18)

The full Europol TE-SAT 2025 annex page 62 has now been independently extracted into two distinct CSVs:
- data/eu_2024_attacks_by_country_ideology.csv
- data/eu_2024_attack_outcomes_by_country.csv

Both total 58 and reconcile by country. Ideology totals: jihadist 24, right-wing 1, left-wing/anarchist 21, separatist 4, other 8. Outcome totals: completed 34, failed 5, foiled 19.

Important: these are two separate marginal tables. It is **not possible** to derive each country's ideology-by-outcome intersections from the two tables alone.

Primary full-report copy: https://tpcoe.gov.pl/download/10/4691/EUTE-SAT2025.pdf (Europol TE-SAT 2025, p. 62).
