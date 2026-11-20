# Judicial decision–incident crosswalk: Greece and Italy

Research checkpoint: 20 November 2026. This crosswalk joins **specific repository incident IDs** to court records only when the event, date and procedural scope can be supported. It does not add incidents to annual totals or replace existing proceedings files.

## Join definitions

- **DIRECT_EVENT_JUDGMENT:** the court's decision identifies the same event and adjudicates relevant conduct; the specific operative holding and finality still need to be recorded.
- **CONTEXTUAL_EVENT_REFERENCE:** a court decision mentions an event or investigation but has not been shown to adjudicate the conduct attributed to the incident row.
- **ORGANISATIONAL_HISTORY_ONLY:** a court document discusses a group or persons but cannot be joined to the dated event.
- **NO_VERIFIED_JOIN:** no event-specific judicial connection established.
- **OUTSIDE_WINDOW:** a historical case occurred outside 2015–2025 and cannot become a new attack row.

## Greek event-level crosswalk

| Existing incident ID | Event | Candidate judgment | Join status | Reason and required next check |
|---|---|---|---|---|
| GR16-PRO | October 2016, Athens prosecutor residence | Areios Pagos 1333/2018; 442/2021; 1223/2024 | NO_VERIFIED_JOIN | Existing Europol attribution to CCF; no demonstrated judicial identity between the event and any cited decision |
| GR16-MEX | July 2016, Mexican embassy | Same decisions | NO_VERIFIED_JOIN | No court-event correspondence established |
| GR16-FRA | November 2016, French embassy | Same decisions | NO_VERIFIED_JOIN | No court-event correspondence established |
| GR17-JAN | 10 January 2017, Athens | Areios Pagos 1223/2024 | NO_VERIFIED_JOIN | Decision's 2017 letter-bomb context alone cannot identify this specific January event |
| GR17-NOV | 6 November 2017, Athens | Areios Pagos 1223/2024 | NO_VERIFIED_JOIN | Event-specific correspondence not established |
| GR17-PAP | May 2017, Athens | Areios Pagos 1223/2024 | NO_VERIFIED_JOIN | Date and target require checking against full judgment |
| GR17-BAN | 19 April 2017, Athens | Areios Pagos 1223/2024 | NO_VERIFIED_JOIN | Do not equate a 2017 letter-bomb reference with this incident without recipient/date confirmation |
| GR17-APP | 22 December 2017, Athens | Areios Pagos 1223/2024 | NO_VERIFIED_JOIN | Court judgment's factual history not mapped to this incident |

**Judicial-document findings independent of incident linkage:** Areios Pagos 1333/2018 and 442/2021 provide organisational/defendant history. Areios Pagos 1223/2024 partially quashed the appellate disposition on mitigation and sentence, not the entire conviction; subsequent sentence unknown. These are **judgment-level findings** but **not verified joins** to the eight rows above.

## Italian event-level crosswalk

| Existing incident ID | Event | Candidate judgment | Join status | Reason and required next check |
|---|---|---|---|---|
| IT16-CIV | January 2016 Civitavecchia courthouse | Fossano/Cospito-Beniamino Cassation history | NO_VERIFIED_JOIN | Distinct 2006 event and location; FAI/FRI label is insufficient |
| IT16-PAR | June 2016 EFSA Parma parcel | Fossano/Cospito-Beniamino Cassation history | NO_VERIFIED_JOIN | No defendant-to-event judicial correspondence |
| IT16-BIO | June 2016 biotech company parcel | Fossano/Cospito-Beniamino Cassation history | NO_VERIFIED_JOIN | No defendant-to-event judicial correspondence |
| IT16-BOL | 2016 Bologna Carabinieri station | Fossano/Cospito-Beniamino Cassation history | NO_VERIFIED_JOIN | Different date and incident; common anarchist classification not enough |
| IT22-ROM | 27 June 2022 Rome foiled event | US 2025 FAI/FRI alias designation; Fossano proceedings | NO_VERIFIED_JOIN | Augusto Masetti alias is administratively listed but no Italian judicial responsibility finding matched to the 2022 act |

**Outside-window historical anchors:** Fossano 2006 and Adinolfi 2012 are **OUTSIDE_WINDOW** for the attack dataset. The Torino prosecutor-general's 2025 report supports the Fossano procedural outcome, but it does not connect that case to any listed 2016 or 2022 incident. Speziale's reported acquittal is also **not an incident-level link** to these rows without original case documents.

## Original sources requiring event matching

- [Greek Supreme Court 1333/2018](https://www.areiospagos.gr/nomologia/apofaseis_DISPLAY.asp?apof=1333_2018&cd=ZSFD5EMZYDNB7AERPCS8ZTMB4EA8O2&info=%EF%BF%BD).
- [Greek Supreme Court 442/2021](https://www.areiospagos.gr/nomologia/apofaseis_DISPLAY.asp?apof=442_2021&cd=CTRUXZM9XNV2644MP3Q7SKHVBMGMDY&info=%EF%BF%BD).
- [Greek Supreme Court 1223/2024](https://areiospagos.gr/nomologia/apofaseis_DISPLAY.asp?apof=1223_2024&cd=B08I1WMEC4SX8ILMY6IIMIQB1YM8RL&info=%EF%BF%BD).
- [Torino prosecutor-general 2025 report](https://pg-torino.giustizia.it/cmsresources/cms/documents/RELAZIONE%20PROCURATORE%20GENERALE.pdf).
- [Europol TE-SAT 2017](https://www.europol.europa.eu/tesat/2017/4.LEFT-WING_AND_ANARCHIST_TERRORISM.html) and [TE-SAT 2023](https://publications.europa.eu/resource/cellar/1694f1b5-9a38-11ee-b164-01aa75ed71a1.0001.01/DOC_1).

**Verification limitation:** The cited Greek decision URLs could not be reopened by the available public web reader in this pass. Their case-level descriptions here derive from the already checked-in organisation profile, not from an independent fresh reading of their full text. Accordingly, **no direct incident–judgment join is asserted**. Before upgrading any row, retrieve the full original judgment and extract its precise event date, target, place, defendants, operative findings, and finality.

## Next actions

1. Retrieve and inspect complete Greek judgment texts; search target and date in Greek and align to the specific incident rows.
2. Search Greek national court/prosecutor records for the October 2016 prosecutor-residence device and 2017 incidents separately.
3. Retrieve original Italian national judgments for Civitavecchia, Parma, Bologna and June 2022 Rome rather than joining them to Fossano by organisational label.
4. Add proceedings relationship records only after a DIRECT_EVENT_JUDGMENT join is verified; preserve existing CSVs meanwhile.
