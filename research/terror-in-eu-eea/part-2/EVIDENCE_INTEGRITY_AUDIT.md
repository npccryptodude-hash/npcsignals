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

## Third pass: direct verification against Europol TE-SAT 2017 (20 November 2026)

**Original primary PDF reopened:** [Europol, *European Union Terrorism Situation and Trend Report 2017*](https://www.europol.europa.eu/sites/default/files/documents/tesat2017.pdf). This is a **same-edition, directly verified internal numerical incompatibility**, not an inference from later national casualty revisions.

| Source location (printed page) | Original statement / number | Audit result |
|---|---|---|
| p. 10, general overview | **379** injured; **142** victims killed; **142** attacks reported | Confirmed as original headline |
| p. 49, Annex 1 | **374 out of 379** casualties in religiously inspired category; **135 out of 142** deaths | Confirmed original annex wording |
| p. 24, Brussels narrative | **340** injured across Zaventem and Maelbeek, combined | Confirmed; **do not duplicate across both sites** |
| p. 23, Nice narrative | **201** injured | Confirmed |
| p. 23, Berlin narrative | **56** injured | Confirmed |

**Arithmetic:** 340 + 201 + 56 = **597**, exceeding the report's 379 by **218**. Even the two-event sum Brussels + Nice = **541**, exceeding 379 by **162**. All three events are described by the report as 2016 attacks in the EU. **Therefore the narrative figures and the headline cannot be treated as one consistent, additive injury population.** The underlying cause (definition, correction, temporal cutoff, editorial error or another issue) is **not established** by the checked pages. Do not assign one.

**Editorial restriction:** No graph, comparative injury-rate calculation or prose may use the 379 as a reconciled sum of these individual incidents. Present it only as *Europol's published aggregate* with an explicit inconsistency flag until an official correction or defensible methodology is found. Preserve original values in `2016/statistics.csv` and `2016/incidents.csv`; any later harmonised series must have a separate metric and source protocol.

**Independent cross-check:** The PDF's Annex 1 also shows the **142** attacks split by country and affiliation; it does not provide incident-specific injury allocations that would resolve this mismatch. The original narrative directly supports the 340/201/56 values; the original headline and annex directly support 379/374.

**Verification status:** Original-source arithmetic conflict = **CONFIRMED**. Explanation = **UNKNOWN**. Official corrigendum = **NOT YET CHECKED**. Dataset changes = **NONE**.

## Fourth pass: contemporary independent warning and official correction search (20 November 2026)

A contemporary independent public-sector review identified **the exact same numerical conflict**: Government of Catalonia's security blog, [*The number of terrorist attacks falls, the threat remains*, 26 July 2017](https://notesdeseguretat.blog.gencat.cat/2017/07/26/the-number-of-terrorist-attacks-falls-the-threat-remains/), footnote 1, states that 201 + 56 + 340 already exceeds the published 374 jihadist injury count. This is a **2017 secondary-source criticism**, not a correction issued by Europol.

**Primary-source web-version comparison:** Europol's [TE-SAT 2017 §1.1](https://www.europol.europa.eu/tesat/2017/1.1.TERRORIST_ATTACKS_AND_SUSPECTS_ARRESTED.html) retains **379**; [Annex 1](https://www.europol.europa.eu/tesat/2017/ANNEX_1.html) retains **374 of 379**; [§2.1](https://www.europol.europa.eu/tesat/2017/2.1.TERRORIST_ATTACKS_AND_SUSPECTS_ARRESTED_IN_THE_EU.html) retains **340** for Brussels and **56** for Berlin (and the report narrative gives 201 for Nice). Thus the inconsistency persists in the accessible official HTML edition as well as the PDF. The [official report landing page](https://www.europol.europa.eu/publications-events/main-reports/eu-terrorism-situation-and-trend-report-te-sat-2017) displays a **6 December 2021** update date but **does not identify a numerical correction**. The [EU Publications Office 2017 edition](https://op.europa.eu/en/publication-detail/-/publication/a4fe72c9-b541-11e7-837e-01aa75ed71a1) and [EU open-data catalogue](https://data.europa.eu/data/datasets/european-union-terrorism-situation-and-trend-report-2017?locale=en) were checked for version/corrigendum pointers; no explicit correction was located in this pass.

**Methodology test:** [Europol Annex 4](https://www.europol.europa.eu/tesat/2017/ANNEX_4.html) says statistics exclusively reflect incidents reported as terrorism by Member States, while the narrative can discuss extremism outside those statistical data. The three selected major attacks are discussed as jihadist terrorism, so this caveat **alone does not resolve the conflict**. The report says Member State returns were cross-checked and validated; that describes collection protocol, not a verified explanation for the discrepancy.

**Corrigendum verdict:** **No official corrigendum found in the sources searched**, not proof that none exists. **Cause remains unknown.** Do not attribute it to deliberate manipulation or claim 597 is the correct 2016 annual injury count.

**Trend-series consequence:** 2016 `ALL-INJ` and `J-INJ` are **SOURCE_REPORTED_UNRECONCILED**. Comparisons of injuries across 2015–2025 that require a harmonised 2016 count must be held or marked non-comparable. Attack-count and death-count series are not invalidated by this injury-specific arithmetic discrepancy without separate evidence; each has independent verification gates.

**Next verification route:** obtain an official Europol clarification/corrigendum through published records, or find a published national-to-Europol injury reconciliation. No outreach is authorised. Independently inspect injury definitions in neighbouring TE-SAT editions before making longitudinal comparisons.

## Fifth pass: cross-chapter organisation-attribution review (20 November 2026)

Reopened **all five thematic Part 2 chapters** and `ORGANISATIONS.md` on the research branch. This is a complete **chapter-level claim scan**, not a complete primary-source re-verification of every linked national record.

| Chapter | Tested attribution boundary | Finding | Follow-up |
|---|---|---|---|
| `LEFT_WING_AND_ANARCHIST.md` | 2022 Rome claim, 2024/25 Greek RCS assessment | **PASS WITH OPEN EVIDENCE:** distinguishes Europol claim, NCTC attribution and absent judicial proof. The 2022 Rome statistical match is not treated as proof of FAI/FRI command. | Validate referenced 2022/2024/2025 incident IDs and sources before any aggregate group count. |
| `RIGHT_WING_NETWORKS_AND_INFLUENCE.md` | Swedish NMR association, Slovak Terrorgram influence, French 2025 projects | **PASS WITH OPEN EVIDENCE:** no automatic membership or direction from reported links/influence; French proceedings not described as convictions. | Obtain original national judgments/prosecutor records for selected cases. |
| `JIHADIST_NETWORKS_AND_INDIVIDUALS.md` | Solingen membership, Holbæk assistance, Westbahnhof purported contact | **PASS WITH OPEN EVIDENCE:** membership, reported contact and operational direction kept separate. | Reopen underlying case decisions for finality and specific charge scope. |
| `SEPARATIST_AND_ETHNONATIONALIST.md` | Corsica 2023 cohort; Northern Ireland mixed reporting | **PASS WITH OPEN EVIDENCE:** retrospective Corsican 4/22/44 occurrence-year allocation not presented as 70 attacks in 2023; NI entries not assigned to a named organisation. | Verify all country/year denominators against original editions. |
| `ORGANISATIONS.md` | Organisation index | **PASS:** explicitly rejects equating profile count with active organisation count; identifies sources as selected cases. | Audit each linked profile individually. |

**No chapter-level attribution inflation was identified in these inspected passages.** This is a limited negative finding: absence of an observed overclaim in five chapters does not certify the underlying case records or all profile appendices.

**Cross-cutting material risk:** Source-derived 2016 injury totals remain inconsistent in the original edition, and the separatist 2023 reporting-year cohort differs from occurrence-year distribution. These are **different** comparability issues and must not be combined into one correction.

**Next queue:** audit the five organisation profiles in full; validate cross-referenced incident IDs and original-source locators; inspect 2016 casualty trend figures and run deterministic repository checks.

## Sixth pass: all five organisation profiles, dated consistency audit (20 November 2026)

Reopened the complete repository content of `organisations/FAI_FRI.md`, `REVOLUTIONARY_CLASS_SELF_DEFENSE.md`, `CONSPIRACY_OF_CELLS_OF_FIRE.md`, `ISLAMIC_STATE.md` and `NORDIC_RESISTANCE_MOVEMENT.md`. This pass checks **internal consistency and attribution boundaries**; it does not claim independent re-reading of every linked primary document.

**Verified internal inconsistencies corrected on the research branch:**
1. **NRM:** Opening narrative and 2020 chronology previously stated Finnish judgment had not been independently checked, despite later section citing the verified **official Supreme Court summary KKO:2020:68**. Corrected to distinguish the reviewed official summary from the full Finnish-language judgment not yet reviewed.
2. **RCS:** Initial US-designation section still described Federal Register verification as outstanding despite the later original-notice section. Updated to reflect primary FTO/SDGT notices and preserve the Greek judicial gap.
3. **CCF:** Clarified that missing original event-specific judicial proof concerns **October 2016 prosecutor-residence incident**, not all Greek cases. The Papademos 2017 first-instance verdict remains **reported**, not original-judgment-verified or final.

**No text change required in this pass:** FAI/FRI profile consistently distinguishes US alias designation, 2016 Europol attribution, Italian historical Fossano proceedings and the separate 2022 Rome claim; IS profile separates final Solingen membership finding from detention orders in AK 100–106/23 and StB 50/25. Both still have original-judgment/document gaps explicitly identified.

**Unresolved:** The FAI/FRI opening narrative describes the two 2016 parcels as attributed to a named cell in Europol, while the original Italian intelligence report's stronger nuance is that Parma and Milan were **unclaimed** and a shared campaign was assessed as probable. These propositions can coexist only with careful source attribution: a Europol-reported cell attribution is not a perpetrator-authenticated claim or a judicial finding. Before publication, align the event-specific wording with both original documents and preserve the differing confidence levels.

**Scope of edits:** Four sequential commits to three existing organisation profiles; no incident data, statistics, legal relationship CSVs or primary evidence changed. The five-profile internal consistency check is **completed with residual source-verification gaps**, not a full substantive clearance.

**Next queue:** cross-reference all profile incident IDs with CSV source identifiers; inspect deterministic validation scripts and run them in an appropriate reproducible environment; resolve the Italian event wording where original texts support a precise correction.

## Seventh pass: exact 2016 event-ID and source-ID check; FAI/FRI correction (20 November 2026)

Directly reopened `2016/incidents.csv`, `2016/sources.csv`, `part-2/organisations/FAI_FRI.md` and `part-2/JUDGMENT_INCIDENT_CROSSWALK.md`.

**Inventory:** The CSV has **23 data rows**, of which **20** have `confidence=adequate`, **2** `candidate` and **1** `outside_scope`. The 23-row inventory is not an official 2016 attack total; `GB16-COX` is contextual and `DE16-HAN` / `DE16-DUS` are alternative or candidate German event links.

**Direct incident-ID joins:** `IT16-CIV`, `IT16-PAR`, `IT16-BIO` and `IT16-BOL` exist in `2016/incidents.csv` and the judgment crosswalk. The 2016 register uses `EU16` as its source ID for all four; `EU16` exists in `2016/sources.csv` and resolves to the archived TE-SAT 2017 PDF with a recorded SHA-256. The additional original Italian intelligence and Ministry of Interior sources are cited in the crosswalk but **not yet assigned dedicated `2016/sources.csv` source IDs**. This is a traceability enhancement to address before editing the structured dates/localities.

**Corrected `organisations/FAI_FRI.md`:** The June 2016 Parma and Milan entries now explicitly distinguish (1) original Italian report's **unclaimed** parcel attacks; (2) intelligence assessment of a probable common campaign linked to *Nucleo Danaus plexippus* communication; (3) Europol's FAI/FRI-cell attribution. Civitavecchia's later FAI/FRI-labelled claim is a separate claim. No event-specific merits judgment has been verified for any of these three.

**Remaining controlled-data task:** Add the Italian primary documents to the source register with stable source IDs, then amend `IT16-CIV`, `IT16-PAR`, `IT16-BIO` dates and `IT16-BIO` locality using those source IDs; retain original Europol source and classification. Do not change incident totals or proceedings relationships.

**Verification gate:** Crosswalk existence and source-ID existence above were manually inspected; a **whole-repository automated foreign-key check has not yet run**. This is not a claim of complete validation.

## Eighth pass: controlled Italian CSV corrections and read-back (20 November 2026)

Two original Italian government sources were added to `2016/sources.csv`:
- `IT16-INTEL`: 2016 intelligence report, Senate Doc. XXXIII no. 4, printed pp. 69–70; source URL in register.
- `IT16-INTERIOR`: Ministry of Interior parliamentary report, Doc. XXXVIII no. 5 vol. I, printed pp. 11–12; source URL in register.

The following **only** fields were amended in `2016/incidents.csv`: `IT16-CIV.event_date=2016-01-12` and source IDs `EU16;IT16-INTEL;IT16-INTERIOR`; `IT16-PAR.event_date=2016-06-07` and `EU16;IT16-INTEL`; `IT16-BIO.event_date=2016-06-09`, `locality=Milan`, and `EU16;IT16-INTEL`. Original Europol source ID, confidence, category, outcome, death and injury cells, event IDs and row counts were retained.

**Post-edit remote read-back:** Both CSV files were fetched again from the branch. The three event rows and both new source rows match the intended values. `2016/incidents.csv` still has **23** records and `2016/sources.csv` has **25** records (excluding headers). This verifies the remote edit landed and basic row count preservation; **no deterministic repository build, CSV parser, foreign-key scan or whole-repo test has been executed in this pass**.

**Scope:** Research branch only. No merge, main modification, publication, external contact or legal attribution change. Publication gate remains NOT READY.
