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

## Trial-file separation and appeal-status check (20 November 2026)

A closer reading of [Kathimerini's 24 November 2023 courtroom report](https://www.kathimerini.gr/society/562746274/katadiki-gia-to-dema-vomva-ston-loyka-papadimo/) resolves an important potential conflation:

1. **Weapons/explosives possession proceeding:** An earlier first-instance 11-year sentence was reportedly reduced **on appeal in April 2023 to a two-year suspended sentence**. This is the distinct proceedings track relevant to the background in Areios Pagos 1223/2024.
2. **2017 parcel-bomb attack proceeding:** A **separate first-instance judgment on 23 November 2023** imposed an **11-year sentence with suspended effect** for the attack against Loukas Papademos. The panel split 2–1; one judge favoured acquittal. The report says the court adopted a lesser legal characterisation of an explosion endangering people instead of attempted murder.

**Do not transfer the April 2023 appeal outcome to the November 2023 attack conviction.** Both happen to involve an 11-year first-instance sentence in different proceedings. The exact court file number and operative written 2023 attack judgment remain unverified.

The [official Greek Supreme Court criminal-case search](https://www.areiospagos.gr/poiniko_search.asp) requires a challenged judgment number/year or hearing date, which is not yet established for the 2023 attack case. A targeted public-source search did not locate a later appeal or cassation disposition by 20 November 2026. This **does not prove** no appeal was filed or no later judgment exists.

**Event join status remains** REPORTED_ATTACK_TRIAL_CONVICTION, **not** final original-court judgment. CCF membership/operational direction is **not adjudicated by this report**. The separate final acquittal on membership described in AP 1223/2024 must not be overwritten by the later attack conviction.

## Original Italian parliamentary source: IT16-CIV (20 November 2026)

[Italian Ministry of Interior, *Relazione al Parlamento — Anno 2016*, presented to the Senate 15 January 2018, Doc. XXXVIII no. 5, vol. I, printed pp. 11–12](https://www.senato.it/service/PDF/PDFServer/DF/335766.pdf), expressly describes the **12 January 2016** explosion at an ENEL electrical cabin beside the perimeter wall of the **Civitavecchia courthouse**. It reports limited damage to the structure and nearby parked vehicles, and a **27 January 2016 online responsibility claim** signed **“Comitato pirotecnico per un anno straordinario, F.A.I/F.R.I.”**. The report's footnote quotes the claim and describes its anti-court/prison rationale.

**Join:** IT16-CIV -> Italian Ministry of Interior 2016 parliamentary report = **DIRECT_OFFICIAL_EVENT_REPORT + REPORTED_RESPONSIBILITY_CLAIM**. This is stronger incident-level source corroboration than a general organisational classification, but **not a judicial conviction**, authenticated author identity, or proven organisational command. The report also describes Italian–Greek ideological alignment; ideological solidarity is not operational direction.

**Exact source locator:** PDF text lines 194–210, printed pp. 11–12, especially lines 200–205 and footnote 4. The document was directly reopened and its event description inspected on 20 November 2026.

**Greek Papademos court-number search:** Contemporary [Kathimerini report](https://www.kathimerini.com.cy/gr/ellada/katadiki-gia-to-dema-bomba-ston-loyka-papadimo-%E2%80%93-neo-yliko-apo-tis-kameres-asfaleias) identifies the trial court, decision date and defendant, but does not supply an operative judgment number. The [Greek Supreme Court criminal-case search](https://www.areiospagos.gr/poiniko_search.asp) requests a challenged judgment number/year or a hearing date. A verified attack-trial judgment number and subsequent finality were **not obtained** in this search. Do not infer absence of appeal.

## Original Italian intelligence report: exact 2016 incident joins (20 November 2026)

[Italian government, *Relazione sulla politica dell'informazione per la sicurezza 2016*, Doc. XXXIII no. 4, communicated to Parliament 24 February 2017, printed pp. 69–70](https://www.senato.it/service/PDF/PDFServer/BGT/1021660.pdf) was reopened and its relevant text reviewed.

| Incident ID | Original report's exact date and place | Event and attribution | Evidence join |
|---|---|---|---|
| IT16-CIV | **12 January 2016**, Civitavecchia courthouse | Low-yield device; later claim signed Comitato pirotecnico per un anno straordinario, FAI/FRI | DIRECT_OFFICIAL_EVENT_REPORT; REPORTED_RESPONSIBILITY_CLAIM |
| IT16-PAR | **7 June 2016**, European Food Safety Authority, Parma | Explosive parcel intercepted by security staff | DIRECT_OFFICIAL_EVENT_REPORT; **no authenticated direct responsibility claim** |
| IT16-BIO | **9 June 2016**, biotechnology company's registered office, **Milan** | Parcel exploded; office-holder slightly injured | DIRECT_OFFICIAL_EVENT_REPORT; **no authenticated direct responsibility claim** |

The government report explicitly says the Parma and Milan attacks were **not claimed**, but assesses they **probably** belonged to the same anti-harm campaign linked to the *Nucleo Danaus plexippus*-FAI/FRI statement delivered to food/biotechnology companies on 7–9 June. This is an **official intelligence assessment of thematic/possible actor linkage**, not a conviction, authenticated perpetrator or command relationship. Its identification of Milan improves the geographical precision of the generic `IT16-BIO` incident description, but the structured CSV is intentionally unchanged until the event-to-source audit and controlled edit.

The report also describes September 2016 *Scripta Manent* detention measures against seven suspects and investigative reconstruction of the FAI/FRI network. **No defendant-to-IT16-PAR/IT16-BIO conviction is established by this source.** The report's account of Greek CCF ideological ties and a 2016 Athens judge-residence attack likewise does not prove cross-border operational direction.

**Locator:** printed pp. 69–70, PDF extracted lines 1331–1350; CCF Greece discussion printed p. 71, lines 1357–1359. This is an additional original government source alongside the separately reviewed Italian Interior Ministry 2016 report for IT16-CIV.

**Current evidence status:** three **official event joins**, zero **verified event-specific judicial conviction joins** from this source. No alteration to 2016 incident counts, casualty allocations or proceedings relationships.

## Scripta Manent: Italian judicial training institution's case-number evidence (20 November 2026)

The [Scuola Superiore della Magistratura, *Le varie realtà dell'anarco-insurrezionalismo*](https://www.scuolamagistratura.it/documents/20126/cf14a1bc-bad4-73e5-d69d-5b9b25bf7e87), original institutional legal-training paper, was opened and read. It identifies the **Torino prosecutor investigation 15577/2012**, **Torino Court of Assize of Appeal judgment 6/2020 (24 November 2020)** and **Court of Cassation, second criminal section, judgment 38184/2022 (6 July 2022)**. These are actionable original-case identifiers, not yet the full judgments themselves.

Its footnote 19 lists acts for which convictions had become final, including explosive parcels to Bologna's mayor and Torino recipients in **2005–2006**, the **5 March 2007** Torino Crocetta devices, and associated explosives offences. It also describes the **2006 Fossano** attack in the case history. None is the same dated act as **IT16-CIV (12 January 2016)**, **IT16-PAR (7 June 2016)**, or **IT16-BIO (9 June 2016)**. **Do not join these convictions to the 2016 rows on the strength of a shared FAI/FRI label.**

The paper distinguishes the investigative/prosecutorial reconstruction of informal anarchist currents from adjudicated findings. Its historical claim that FAI/FRI developed transnational links with Greek CCF in 2011 is an **institutional author's assessment**, not a court finding that the Greek group commanded specific Italian incidents. It identifies earlier programme statements as source leads, but their provenance and authenticity are not independently reviewed here.

**Document hierarchy:** This is an original publication by a judicial training institution summarising proceedings, **not** the complete operative text of Cassation judgment 38184/2022. Confirm each count, defendant, conviction, acquittal and finality from that decision before creating any event-specific judicial relationship. The police [6 September 2016 Scripta Manent release](https://www.poliziadistato.it/articolo/3857ce8d5e3c1fa164926365) independently specifies that the arrest-operation allegations concerned **Fossano 2006** and **Torino Crocetta 2007** explosives, not a demonstrated judicial link to the June 2016 parcel incidents.

**Research status:** new **case identifiers verified**; no new DIRECT_EVENT_JUDGMENT for 2016 incident rows.

## Targeted retrieval of Cassation 38184/2022 and separate Italian case registers (20 November 2026)

**Full-text retrieval outcome: NOT OBTAINED.** The exact Cassation decision is **Second Criminal Section no. 38184/2022, hearing 6 July 2022, deposited 11 October 2022**. Searches of public Cassation materials and legal repositories found original downstream court documents and the Supreme Court's institutional analysis, but **not the complete text of decision 38184/2022**. Do not describe its individual charges as exhaustively inspected.

**Original judicial substitutes actually inspected:**
- [Italian Supreme Court's *Rassegna della giurisprudenza di legittimità penale 2022*, volume I](https://www.cortedicassazione.it/resources/cms/documents/Rassegna_penale_anno_2022_VOLUME_I.pdf), section IV on political versus ordinary *strage*, specifically analyses **count F** (Fossano Carabinieri school, 2006) and mentions **count L** (three devices in Torino within a year). It is an **institutional analytical summary**, not the full judgment or a count-by-count disposition.
- [Italian Constitutional Court judgment 94/2023](https://www.cortecostituzionale.it/scheda-pronuncia/2023/94) confirms that Cassation partially annulled the appellate ruling as to **count F legal classification**, from article 422 to article 285, remitting **sentence determination**. It expressly dates the Fossano event to **2 June 2006**. This is an **original court judgment about the remittal**, not the complete 38184/2022.
- [Torino Court of Assize of Appeal order, 19 December 2022, RG 18/22](https://www.giurisprudenzapenale.com/wp-content/uploads/2023/01/ORDINANZA-19.12.2022.pdf) identifies the same Cassation number and remittal proceeding.
- [Court of Cassation judgment 13258/2023](https://www.giurisprudenzapenale.com/wp-content/uploads/2023/03/cospito-cassazione.pdf) is a **different judgment** concerning detention conditions; it refers to the 2022 case but must not be mistaken for 38184/2022.

**Count-to-register gate:** Count F = **OUTSIDE_WINDOW** (Fossano, 2 June 2006). Count L = **historical Torino 2007 context**, pending full count text and disposition; not a match to IT16-CIV, IT16-PAR, IT16-BIO or IT16-BOL. All other counts in 38184/2022 = **NOT_EXTRACTED**; no assertion of exhaustive verification. The full 2022 decision is required before marking each count reviewed.

### Separate national-source checks

| Incident | Newly checked national source | Result | Judicial gap |
|---|---|---|---|
| IT16-CIV | [Italian National Anti-Mafia/Anti-Terrorism Directorate report for July 2015–June 2016](https://www.avvisopubblico.it/home/wp-content/uploads/2017/06/RELAZIONE-DNA-1.7.2015-30.6.2016.pdf) | Prosecutorial institutional report independently records the January 2016 device near Civitavecchia court and says FAI/FRI claimed it | No case docket, named defendants or final merits judgment established |
| IT16-PAR | [Parma police headquarters annual address, 10 April 2017](https://questure.poliziadistato.it/it/Parma/articolo/96658eb85222b571378756506) | Original territorial police statement records June 2016 intercepted explosive parcel to EFSA and describes anarchist authorship as **probable** | No case docket, named defendants or final merits judgment established |
| IT16-BIO | [Italian 2016 intelligence report](https://www.senato.it/service/PDF/PDFServer/BGT/1021660.pdf) (previously inspected) | Confirms Milan biotechnology recipient and injury; no distinct national prosecution record newly found | No case docket, named defendants or final merits judgment established |

**Status of national register access:** Public-source searches did not provide a case-number lookup or complete prosecution file for these three incidents. Do not infer that the investigations were closed or that no prosecution occurred. The publicly documented original police/prosecutor sources are **event verification**, not judicial attribution.

**Next retrieval route:** Search Italian Supreme Court public judgment search by exact **38184/2022**, or request document access through authorised legal databases or court archives; if a copy becomes available, extract each lettered charge, event date/location, accused persons, adjudicated result and finality. Independently seek Parma, Milano and Civitavecchia prosecutor case numbers; do not map by FAI/FRI alias alone.
