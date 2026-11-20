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
| GR17-PAP | 25 May 2017, Athens: letter-bomb explosion injuring former PM Loukas Papademos and vehicle occupants | Areios Pagos 1223/2024; Athens three-member felony appeals court reported 23 November 2023 | REPORTED_ATTACK_TRIAL_CONVICTION + CONTEXTUAL_EVENT_REFERENCE | Contemporary Kathimerini reports Giagtzoglou convicted at first instance (11 years; suspended effect); original trial judgment and later finality unverified. AP 1223/2024 is separate weapons proceedings and does not itself adjudicate the attack |
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

## Direct original-text review: Areios Pagos 1223/2024 (20 November 2026)

The full published Greek judgment was accessible through the [Supreme Court's original page](https://www.areiospagos.gr/nomologia/apofaseis_DISPLAY.asp?apof=1223_2024&cd=B08I1WMEC4SX8ILMY6IIMIQB1YM8RL&info=%EF%BF%BD). It expressly identifies (a) 15 March 2017 letter-bomb delivery to the German Finance Ministry, (b) 16 March 2017 delivery to the IMF office in Paris, (c) eight devices intercepted at Kryoneri postal sorting centre on 20 March 2017, and (d) the 25 May 2017 explosion in former PM Loukas Papademos's vehicle. The court recites these as **police investigation context**. The underlying Athens appeal proceeding reviewed in 1223/2024 concerns weapons/explosives possession and related allegations, not adjudication of the Papademos bombing. The court records that a defendant was already **irrevocably acquitted of CCF membership**, and that proceedings concerning the Papademos bombing were separately pending at the time described.

**Verified join:** GR17-PAP -> 1223/2024 = CONTEXTUAL_EVENT_REFERENCE (date and target explicitly match). **Not verified:** a final Papademos-attack conviction, CCF command, or defendant-specific responsibility for that attack. Do not add a trial-verdict relationship to the structured 2017 proceedings register. The 2017 Paris IMF incident is a separate French event and cannot be silently merged with GR17-PAP or added as a new Greek row.

The full [442/2021 judgment](https://www.areiospagos.gr/nomologia/apofaseis_DISPLAY.asp?apof=442_2021&cd=CTRUXZM9XNV2644MP3Q7SKHVBMGMDY&info=%EF%BF%BD) has also been reopened. It includes a charged period of alleged CCF membership between early January 2014 and arrest on 28 February 2015, plus events from 2013. The date of the arrest does **not** turn those earlier acts into 2015 attacks. The operative findings and finality of individual counts need a separate full-length extraction before event joining.

The [1333/2018 judgment](https://www.areiospagos.gr/nomologia/apofaseis_DISPLAY.asp?apof=1333_2018&cd=ZSFD5EMZYDNB7AERPCS8ZTMB4EA8O2&info=%CE%A0%CE%9F%CE%99%CE%9D%CE%99%CE%9A%CE%95%CE%A3+-++%CE%95) was reopened through its official full-text search result. It discusses a 10 August 2012 Paros bank robbery and organisational allegations; no exact event match to the selected 2016/2017 rows has been established. **Historical context only** pending operative review.

### Extraction ledger for the verified contextual join

| Field | GR17-PAP / AP 1223/2024 |
|---|---|
| Date | 25 May 2017 |
| Location | Athens / vehicle of former PM (street not established here) |
| Target / victims | Former PM Loukas Papademos; driver and accompanying passenger described as injured |
| Defendants in reviewed separate weapons case | Anonymised initials K. G. and Th. D. in Supreme Court publication; do not infer identity of Papademos attacker |
| Court's finding relevant to this join | Attack recited as investigative context; separate proceedings described |
| Finality of attack-specific proceedings | Not verified; pending at time of court's narrative |
| Organisational membership | Judgment records irrevocable acquittal of K. G. on CCF membership allegation |
| Join classification | CONTEXTUAL_EVENT_REFERENCE, not DIRECT_EVENT_JUDGMENT |

## Subsequent disposition discovered: GR17-PAP (20 November 2026)

[Kathimerini, 24 November 2023](https://www.kathimerini.gr/society/562746274/katadiki-gia-to-dema-vomva-ston-loyka-papadimo/) reports that on **23 November 2023** the Athens three-member felony appeals court, sitting at first instance for the attack case, convicted **Konstantinos Giagtzoglou** in relation to the **25 May 2017** letter-bomb explosion against former PM Loukas Papademos. It reports an **11-year custodial sentence with suspended effect**, a **2–1 majority**, and the court's acceptance of a lesser explosion-endangerment characterisation instead of attempted murder. [Dnews, 24 November 2023](https://www.dnews.gr/eidhseis/politikes-eidhseis/450710/me-6-xronia-kathysterisi-i-katadiki-tis-tromokratikis-epithesis-me-vomva-dema-ston-l-papadimo) independently reports the outcome.

**Join:** This is an **event-specific, contemporaneously reported first-instance conviction** and therefore a stronger link than AP 1223/2024's contextual reference. **Not yet original-judgment verified:** case number, exact counts in the operative decision, appeal, cassation or finality. Do not label it final or use it to prove CCF membership/command. The earlier statement that attack-specific proceedings were still pending refers to the time recounted in the Supreme Court's separate case and is superseded as a current-status claim by the November 2023 trial report.

**Dataset policy:** Keep `2017/incidents.csv` unchanged. Add a proceedings relationship only after documenting the court's case number/operative text or explicitly accepting a **reported non-final trial disposition** as a separate evidence tier under the existing register policy.
