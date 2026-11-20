# Part 2 — Evidence integrity audit

Audit initiated: 20 November 2026. Scope: source-to-incident-to-organisation-to-proceeding claims in Part 2, with a non-destructive comparison to the 2015–2025 baseline. This document is an audit ledger, not a replacement for source records or a publication clearance.

## Evidence relationship types

- **COURT_EVENT_HOLDING**: original merits judgment matches event date, place, target and operative count. Record defendant, scope and finality separately.
- **REPORTED_EVENT_VERDICT**: credible reporting of a specific verdict; original operative text or finality not verified.
- **COURT_CONTEXT**: original judgment mentions the incident without deciding that incident's responsibility.
- **OFFICIAL_EVENT**: primary police, intelligence, prosecutorial or parliamentary report confirms the occurrence.
- **OFFICIAL_ATTRIBUTION**: agency assessment of actor responsibility; not itself a court finding.
- **REPORTED_CLAIM**: a claim is reported, not necessarily authenticated as the perpetrator's.
- **IDEOLOGICAL_AFFINITY**: shared ideas, references or solidarity; not operational control.
- **ADMINISTRATIVE_DESIGNATION**: legally effective designation and named aliases; not a criminal conviction or event-level command.
- **NO_VERIFIED_JOIN**: no adequately evidenced relationship for the precise event.
- **OUTSIDE_WINDOW**: event before 2015 or after 2025; historical context only.

Each row must preserve source provenance, original source text or exact locator, relevant time period, date of judicial act, uncertainty, and whether the relationship is about an individual, cell, organisation or ideology. Never collapse these into a single “linked” boolean.

## Initial adversarial findings

| ID | Register item / claim | What was checked directly | Issue | Severity | Resolution gate |
|---|---|---|---|---|---|
| EIA-001 | GR17-PAP, 25 May 2017 | Existing 2017 event crosswalk and its original-court versus contemporary-report separation | 2023 first-instance attack conviction is **reported**, while Areios Pagos 1223/2024 is **contextual in a different weapons case**; finality not established | High | Do not encode as final court-event conviction; obtain attack trial operative text and later appeal status |
| EIA-002 | IT16-CIV / IT16-PAR / IT16-BIO | Original Italian government reports and crosswalk, 2016 incidents.csv | Original sources support 12 January Civitavecchia, 7 June Parma and 9 June Milan, but incident CSVs retain month-only dates and IT16-BIO locality “Italy” | Medium | Check row/source provenance and schema contract before a narrowly scoped CSV correction; do not change attack totals |
| EIA-003 | Scripta Manent 38184/2022 | Institutional legal summaries in crosswalk | Full Cassation judgment not obtained; individual counts **cannot** be declared exhaustively reviewed; count F relates to Fossano **2006** | High | Retrieve complete judgment; count-by-count adjudication, dates and named defendants |
| EIA-004 | IT16-CIV / PAR / BIO versus FAI/FRI | Crosswalk official event and attribution distinctions | A responsibility claim for Civitavecchia cannot be transferred to **unclaimed** Parma and Milan parcels; probable common campaign is an intelligence assessment | High | Keep separate event claim/agency assessment/court judgment columns |
| EIA-005 | NRM dissolution / US designations | Organisation verification matrix | Finnish association-law dissolution and US administrative designation are distinct from criminal conviction | High | Check all prose for legal-category drift |
| EIA-006 | IS German AK 100–106/23 and StB 50/25 | Organisation verification matrix | Pretrial detention decisions are not verdicts; some alleged IS links are support or contact rather than membership or command | High | Check individual claim scope against original BGH orders |
| EIA-007 | 2016 injury totals | Earlier consolidated research checkpoint | Previously identified mismatch between baseline 379 and selected large-incident summed 597; no reconciliation verified in this pass | High | Reopen baseline methodology, source-year scope and casualty definitions; do not silently fix either number |
| EIA-008 | 2016 national and European event population | 2016/incidents.csv | Rows mix adequate, candidate and explicitly outside-scope context (e.g. GB16-COX); summing all rows as official attack totals would be invalid | High | Confirm inclusion logic in scripts and published figures |
| EIA-009 | GR16-PRO, MEX, FRA; IT16-BOL; IT22-ROM | Existing crosswalk | No direct event-specific merits judgment established; historical group identity and aliases are insufficient | Medium | Maintain NO_VERIFIED_JOIN until event-specific primary evidence appears |

## Structural audit — first pass

- `2016/incidents.csv` was inspected on the research branch: Rows include both adequately linked events and non-adequate or out-of-scope flags; exact aggregate counts were not independently computed in this pass. The substantive issue is mixed evidence and inclusion status, not the row count.
- `2016/proceedings_relationships.csv` contains confirmed, reported and not-final relationships; no Greek/Italian incident-specific proceedings rows were present in the inspected file. This is consistent with the conservative gate.
- `part-2/JUDGMENT_INCIDENT_CROSSWALK.md` contains both historical status text and dated updates. Earlier statements that Papademos attack proceedings were pending are explicitly superseded for **current** procedural status by the reported November 2023 trial outcome. During editorial cleanup, add temporal labels rather than deleting the historical procedural fact.
- `part-2/ORGANISATION_PROFILE_VERIFICATION.md` is a cumulative matrix with later dated corrections. The initial table is **not** an up-to-date summary on its own. Before publication, consolidate it into a current-status table and a dated evidence-change log.
- No statistical denominator or original evidence file has been changed by this audit.

## Audit decisions and next work

1. Extract every organisation/event link in Part 2 and check the exact relationship type, source and direction of inference. **Pending.**
2. Verify 2016 original source locators, source IDs, and all five Italian/Greek event dates; only then consider minimal CSV factual corrections. **Pending.**
3. Trace the 2016 injury discrepancy back to the original baseline table and its source period. **Pending.**
4. Run the repository's existing deterministic verification commands, recording command, exit status and file hashes. **Pending; no build run claimed.**
5. Independent human editorial review remains a publication gate. No publication, merge or main-branch edits authorised.

**Provisional verdict: NOT READY FOR PUBLICATION.** This is a research-quality control status, not a conclusion about any investigated organisation or defendant.
