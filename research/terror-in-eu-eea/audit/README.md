# Independent audit of the 2015–2025 foundation

18 November 2026 · baseline `3280084` · internal quality review.

- [Recalculated statistical series](recalculated.csv) and [validation script](recalculate.py)
- [Source integrity and legal evidence](EVIDENCE.md)
- [Report retrieval ledger](source_integrity.csv) and [2025 arrest rows](arrests_2025.csv)
- [Discrepancies and corrections](DISCREPANCIES.md)
- [Publication decisions and remediation](PUBLICATION_READINESS.md)

## Statistical controls

From the repository root run `python3 research/terror-in-eu-eea/audit/recalculate.py`. For deterministic replication, redirect stdout to a temporary CSV and compare it to `recalculated.csv`. An issue is emitted to stderr and causes a nonzero exit. The calculation sums country/category or country/outcome inputs first, then tests the existing consolidated summary. A dash in the 2025 source table is represented as zero inside a reported cell. An absent country row remains absent.

All eleven attack and arrest totals reconcile to the operative rows. The script verifies crosswalk totals by country, joint cells when available, the two separate annex margins where appropriate, the confidence partition, and 31-country grid membership. Category totals are tallied in edition terminology. The 2023 annex combines other and unspecified even though the crosswalk distinguishes two observations within it. The 2024 crosswalk and annex use different names for the same separatist category. Neither recoding changes source data.

For 2015–2019 the independently summed non-UK rows yield 108/66/98/69/55 attacks and 943/853/807/783/723 arrests. The included UK rows are 103/76/107/60/64 attacks and 134/149/412/273/281 arrests. The differences agree with non-UK sums. A UK contribution of zero in the EU27-era series represents reporting scope. Separate Northern Ireland statistics were excluded from the calculation. TE-SAT 2021 p. 12 provides the later fixed-geography attack comparisons for 2018 and 2019 (69 and 55); these are a geographic restatement. See the annual geography notes for dataset-specific Northern Ireland coverage.

The outcome columns count the country/category allocations. For example, the 2016 crosswalk allocates ten completed, while Europol's headline explicitly counts 47 completed overall. Its unresolved allocations can include completed, failed and foiled events. Use the published complete outcome margin where it exists. The audit does not infer zero original failed attacks from a zero in an allocated column.

The provenance ledger yields later official historical totals of 56 for 2020 and 18 for 2021. The analytical occurrence-year assumptions are applied separately: one removal in 2020, three late right-wing entries and four reallocated separatist records in 2021, 22 reallocated to 2022 and 26 removed from the 2023 cohort. This gives 56/22/50/94 for 2020–2023. The 26 transferred records net to zero across those years. A zero adjustment for other years records the lack of a keyed adjustment in this ledger, with no assertion of perfect occurrence-year coverage. The 193 chart value is held outside all these calculations.

## Crosswalk integrity and detection limits

- Across the original edition baselines, the partitions sum to 168 adequate, 35 candidate and 926 unidentified slots out of 1,129. This diagnostic sum includes the historical UK rows and known retrospective reporting. It measures database allocation coverage.
- For 2015–2022 the script checks linked incident ID uniqueness across cells and the country, category, outcome and ascertainable year for linked records. For 2023–2024 it reconstructs confidence counts from case rows using country/category/outcome, since no explicit key is carried in each cell. Phase 6's 2025 allocation is checked against the two country inputs and the 18 positive country/category/outcome cells. The 2025 source text and allocation descriptions do not constitute an event-keyed official return.
- The 2015 Paris November series and 2022 Spain series demonstrate that the number of physical acts can differ from the number of statistical entries. The original 2015 record links the series with a minimum supported allocation and leaves detailed grouping unverified. The 2022 p. 79 annex and pp. 59–60 narrative support one Spanish slot for six connected acts. The 2023 Duisburg count likewise requires preserving the two physical acts in the one adjudicated case. An ID uniqueness test cannot detect two aliases for a physical event or two explicit reporting entries later grouped into a single case.
- Three French completed jihadist candidates compete for two 2025 slots. The 7/17/21 partition is coherent and the 18 possible candidate identities do not add a slot. Named Europol examples support specific identifications, such as Munich, Bielefeld and Villach. France's two names, Essen's statistical match and event-level duplicate testing for the retrospective cohorts still require keyed evidence. No confidence class changed.
- All years have 31 geographic research rows. Judicial, national and historical incident coverage remains incomplete. See the [limitations and decision rules](PUBLICATION_READINESS.md).
