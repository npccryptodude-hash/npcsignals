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

## Second pass: 2016 injury discrepancy traced to source fields (20 November 2026)

Directly reopened `2016/statistics.csv`, `2016/incidents.csv` and `METHODOLOGY.md` on the research branch.

**Reproducible arithmetic from the registered values:**
- `BRU-INJ` = **340** (Europol combined Brussels sites, 22 March 2016).
- `FR16-NIC.injuries` = **201** (Europol contemporary Nice value).
- `DE16-BER.injuries` = **56** (Europol contemporary Berlin value).
- **340 + 201 + 56 = 597**, whereas `ALL-INJ` = **379** (EU28 all-ideologies 2016 total), and `J-INJ` = **374** (EU28 jihadist total).

**Confirmed finding:** The apparent 597-versus-379 discrepancy is reproducible from **different fields of the same registered Europol edition**, not merely from later revised Nice/Berlin victim totals. The individual-site figures cannot be naively aggregated as the same population and definition as the annual total. This is a **source-level scope/definition conflict requiring original TE-SAT page and footnote verification**, not an arithmetic error to “fix” by replacing 379 with 597.

**Additional control:** The `2016/incidents.csv` Nice injuries value 201 is contemporary, whereas the separate `NIC-LATE-I` value 458 is a later national research figure. Combining 458 with contemporary 340/56 would create another mixed-scope total. The Brussels 340 is already combined across both airport and metro; it must not be added separately to each Brussels event. The annual 379 and 374 remain recorded as source claims with unresolved harmonisation.

**Dataset policy:** Preserve original figures and qualifiers, add an explicit cross-scope arithmetic warning before figures are used in prose or charts. Recheck the original TE-SAT 2017 printed pp. 10, 23–24 and 49 and its statistical reference period before determining whether the discrepancy arises from reporting-year versus attack-year population, a table correction, casualty definitions or another cause. **No cause has yet been proven.**

## Second pass: 2016 register row classification

A direct row count of the inspected `2016/incidents.csv` text gives **23 incident records** (excluding header): **20 adequate**, **2 candidate**, **1 outside_scope** (based on the displayed confidence column; independently verify with a CSV parser before using in any publication). More importantly, the specific rows `DE16-HAN` and `DE16-DUS` are candidates and `GB16-COX` is explicitly outside original attack count; the file is **not** a 23-attack denominator. The row count is an audit inventory, not a Europol total.

## Second pass: reader-facing attribution claims

`part-2/ATTRIBUTION_COMPARISON.md` was reopened. Its ten examples distinguish (a) judicially supported ideology, (b) official reports of claims, (c) agency assessments, (d) pretrial custody and (e) final court outcomes. No direct assertion that the 2016 Italian FAI/FRI-labelled claim proves perpetrator identity was found in this inspected comparison. Remaining risk: the comparison's `Germany, Solingen, 2024` row uses a final BGH summary to support membership, but the document expressly withholds an inference of operational command; retain that caveat. This is a **document-specific check**, not an exhaustive audit of all Part 2 prose.

**Next:** verify counts programmatically, inspect the original TE-SAT 2017 tables, then inspect each remaining Part 2 profile against the event-ID crosswalk.
