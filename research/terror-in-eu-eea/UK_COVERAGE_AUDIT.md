# coverage and comparability audit — 2026-11-18

status: primary-source review; not publication ready

## key finding: uk counting systems

the uk is included in the fixed 31-country study area throughout 2015–2025. europol te-sat 2017 annex 1 reports 76 uk incidents in 2016, all under separatist terrorism, and 142 total eu incidents. the narrative identifies those uk incidents as northern ireland-related terrorism. its general overview also cautions that the uk did not provide disaggregated attack data permitting a precise ranking across all affiliations. retain both statements; do not infer that the 76 cases represent all forms of terrorism in the uk.

source: https://www.europol.europa.eu/tesat/2017/ANNEX_1.html
source: https://www.europol.europa.eu/tesat/2017/1.1.TERRORIST_ATTACKS_AND_SUSPECTS_ARRESTED.html

## important distinction: great britain vs united kingdom

the uk house of commons library briefing of 2026-05-20 explicitly says most of its terrorism statistics cover great britain (england, wales, scotland), not northern ireland, owing to differing legislation and counting rules. it should not be used alone as a uk-wide incident count. northern ireland requires a separate primary source and reconciliation.

source: https://commonslibrary.parliament.uk/research-briefings/cbp-7613/

## data integration rules

1. country_iso2 = gb denotes united kingdom; retain subnational area: england, wales, scotland, northern ireland or unknown.
2. source coverage must include territory and measurement definition: attacks vs police arrests vs deaths vs convictions.
3. do not add great britain and northern ireland datasets until time periods, counting rules and duplicate cases are reconciled.
4. do not add uk numbers to historical europol eu totals for years when uk data were already included.
5. do not treat missing post-brexit uk cases in europol eu totals as zero.
6. keep all 31 countries in the fixed-scope output; label unavailable values null and mark completeness.
7. the 2016 annex row is a source-reported subset and is not a comprehensive uk-wide ideology breakdown.

## source-checked eu baselines

- 2016: 142 attacks, 76 uk northern ireland-related; 13 classified as religiously inspired, 99 separatist, 27 left-wing, 1 right-wing, 2 unspecified.
- 2023: 120 eu attacks: 98 completed, 9 failed, 13 foiled; 14 jihadist and 70 separatist.
- 2024: 58 eu attacks: 34 completed, 5 failed, 19 foiled; 24 jihadist and 21 left-wing/anarchist.

sources:
- https://www.europol.europa.eu/tesat/2017/ANNEX_1.html
- https://www.europol.europa.eu/cms/sites/default/files/documents/TE-SAT%202024%20-%20Executive%20Summary%20-%20EN.pdf
- https://www.europol.europa.eu/cms/sites/default/files/documents/TE-SAT%202025%20-%20Summary%20-%20EN.pdf

## next research priorities

- obtain primary northern ireland security statistics and event-level methodology.
- identify post-2020 uk-wide incident-level records; reconcile against great britain-only releases.
- expand annual eu te-sat country-level annexes; document whether counts refer to current or historical eu membership.
- review the existing 2016 csv against this audit before using it in public charts.
