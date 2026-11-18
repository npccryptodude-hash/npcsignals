# Phase 22 — Controlled historical analysis, 2015–2025

Internal draft · 18 November 2026 · [PR #7](https://github.com/npcsignals/npcsignals/pull/7)

Verified starting head `50243a0e811420810616bd7a345559fdef05afcd` on `research/terror-eu-eea-foundation-2026`. Main was at `18ff335e85b36f072a03a19faac8ee051fb32867`. This analysis uses the existing annual registers and [Phase 18](README.md), [Phase 19](PHASE_19_REMEDIATION.md), [Phase 20](PHASE_20_EVENT_LINKAGE.md) and [Phase 21](PHASE_21_REPORTING_MECHANISMS.md) reviews.

## What the counts support

| Reference year | Original attacks | Fixed EU27 | Later official | Occurrence-year sensitivity | Original arrests | Fixed EU27 arrests |
|---|---:|---:|---:|---:|---:|---:|
| 2015 | 211 | 108 | — | 108 | 1,077 | 943 |
| 2016 | 142 | 66 | — | 66 | 1,002 | 853 |
| 2017 | 205 | 98 | — | 98 | 1,219 | 807 |
| 2018 | 129 | 69 | — | 69 | 1,056 | 783 |
| 2019 | 119 | 55 | — | 55 | 1,004 | 723 |
| 2020 | 57 | 57 | 56 | 56 | 449 | 449 |
| 2021 | 15 | 15 | 18 | 22 | 388 | 388 |
| 2022 | 28 | 28 | — | 50 | 380 | 380 |
| 2023 | 120 | 120 | — | 94 | 426 | 426 |
| 2024 | 58 | 58 | — | 58 | 449 | 449 |
| 2025 | 45 | 45 | — | 45 | 486 | 486 |

The [analytical CSV](../data/phase22_annual_analysis.csv) includes source locators, the original UK contribution, category counts in edition terminology and confidence percentages. Blank numeric fields indicate unavailable or inapplicable observations. A zero in a UK contribution field from 2020 onwards records UK exclusion from the EU aggregate. A zero sensitivity adjustment records that the chosen scenario applies no change. Neither describes national incident counts. Category fields are semicolon-separated key/value pairs from the audited margins. A missing key is left implicit and should not be converted into zero across editions. For example, TE-SAT 2026 p. 19 independently documents zero *verified reported* separatist attacks in its 2025 scope.

- **Geography.** In 2015–2019 removing the documented UK rows reduces attacks by 103, 76, 107, 60 and 64 respectively. The 2019–2020 step changes from **119 → 57** in the original series (−62) to **55 → 57** (+2) on fixed EU27 geography, or **55 → 56** (+1) with the documented official correction. The apparent large fall across that boundary depends on mixing geographic scopes.
- **Retrospective entries.** The original 2020 and 2021 attack figures are 57 and 15. A later edition gives 56 and 18. The 2020 removal's identity remains unverified. The sensitivity scenario uses those adjustments and moves the 26 earlier French separatist records to their occurrence years (+4 to 2021, +22 to 2022, −26 from 2023). The transfers net to zero. Scope-complete matching and overlap across event IDs remain unavailable.
- **Magnitude under both EU27 scenarios.** The 2022–2023 rise is +92 in the original cohort and +44 under the stated sensitivity. The 2023–2024 fall is −62 and −36 respectively. The direction survives this particular reassignment; the magnitude is strongly cohort-dependent. The 2023 peak is 120 in the fixed-geography baseline; the sensitivity series peaks at 108 in 2015 and places 2023 at 94. The 2024–2025 step is 58 → 45 in both. These are arithmetic observations about reported entries.
- **Outcomes.** The published 2024 and 2025 margins move from 34 to 22 completed, five to three failed, and 19 to 20 foiled. Edition outcome margins are often more complete than country/category allocations. In 2016 Europol reported 47 completed overall while the joint allocation in the audit identifies 10 completed and leaves 130 outcomes unallocated across cells. Do not interpret an allocation zero as an official failed or foiled zero.
- **Arrests.** Fixed EU27 arrests fall from 943 in 2015 to 380 in 2022 and reach 486 in 2025. From 2019 to 2020 they fall by 274 after holding geography fixed, compared with 555 in the original editions. The subsequent 2022–2025 rise is +106. The later annex sum of 431 would change the 2022–2023 step from +46 to +51 and 2023–2024 from +23 to +18 if substituted in a clearly labelled check. The operative series uses 426. Geography alone cannot identify the causes of changes in arrests.

The 193 graphic observation is retained outside the four series. No inference of a common physical attack-frequency trend follows from the series, including over the whole 2015–2025 span. National coding, grouping, enforcement and documentation vary, and the 31-country grid contains gaps. Comparisons by motive require the [category matrix](phase22_category_comparability.csv).

## Incident identification coverage

| Reference year | Adequate | Candidate | Unidentified |
|---|---:|---:|---:|
| 2015 | 4.27% | 1.42% | 94.31% |
| 2016 | 14.08% | 0.70% | 85.21% |
| 2017 | 13.17% | 0.49% | 86.34% |
| 2018 | 17.05% | 0.00% | 82.95% |
| 2019 | 20.17% | 0.84% | 78.99% |
| 2020 | 26.32% | 0.00% | 73.68% |
| 2021 | 93.33% | 6.67% | 0.00% |
| 2022 | 42.86% | 10.71% | 46.43% |
| 2023 | 7.50% | 0.83% | 91.67% |
| 2024 | 15.52% | 12.07% | 72.41% |
| 2025 | 15.56% | 37.78% | 46.67% |

Denominator is the original edition's slots per year, with the UK included through 2019. Percentages round independently. The pooled diagnostic is 168/1,129 adequate (14.88%), 35/1,129 candidate (3.10%) and 926/1,129 unidentified (82.02%). It weights slots equally across heterogeneous cohorts. The 2021 percentage is 14 of 15 adequate and one candidate; it excludes later additions because they were outside the frozen original cohort. In 2023 the original cohort includes all 70 French separatist slots, while the exact French assignments remain incomplete. In 2025 three French event alternatives compete for two slots, and 18 candidate identities across the edition correspond to 17 candidate slots.

Named publisher narratives and dated court records make high-profile completed events easier to anchor. For 2025, 6 of 22 completed slots have adequate matches versus 1 of 20 foiled and 0 of 3 failed, from the [frozen outcome cells](../2025_INCIDENT_IDENTIFICATION_PHASE6.md). Small denominators, publication selection and investigative confidentiality limit interpretation. Unnamed interventions, pooled series, vague place/time descriptions and judicial proceedings spanning multiple acts are harder to join. This is a documentation pattern in the research record, with no estimated probability of observation for underlying physical incidents. An unidentified slot represents an observed statistical entry with no supported identity; it provides no basis to deny occurrence.

## Readiness and validation

See the [arrest and judicial measures report](PHASE_22_ARREST_AND_JUDICIAL_MEASURES.md), [visualisation specification](PHASE_22_VISUALISATION_SPEC.md) and [current publication-readiness matrix](PUBLICATION_READINESS.md#phase-22-analytical-readiness). This phase prepares internal analysis and design only.

From the repository root:

```sh
set -e
root=research/terror-in-eu-eea
audit_tmp=$(mktemp)
analysis_tmp=$(mktemp)
python3 "$root/audit/recalculate.py" > "$audit_tmp"
cmp "$audit_tmp" "$root/audit/recalculated.csv"
python3 -B "$root/audit/build_phase22.py" > "$analysis_tmp"
cmp "$analysis_tmp" "$root/data/phase22_annual_analysis.csv"
sha256sum "$audit_tmp" "$analysis_tmp"
rm "$audit_tmp" "$analysis_tmp"
```

The established output was reproduced before and after edits, SHA-256 `fc351da07034e81754741f8fc3963855d62627747c84e366f634f9fcb5a6ab9f`. The builder draws categories directly from the independent annual audit logic and joins versioned source metadata and reconciliation fields on reference year. The original annual registers and all confidence assignments are preserved.
