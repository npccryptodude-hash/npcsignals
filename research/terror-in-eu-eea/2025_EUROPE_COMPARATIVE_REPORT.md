# Terrorism in 2025 — 31-country coverage and comparative audit

Review cutoff: 18 November 2026. Baseline: draft PR #7 at 9452f3c. The fixed study area includes EU27 and GB, NO, IS and LI. This pass establishes a complete country roster and a verified EU source transcription. National investigation and incident identification remain incomplete.

- [31-country coverage matrix](data/terror_2025_coverage.csv)
- [Country and EU statistics](data/terror_2025_country_statistics.csv)
- [Incident supplement](data/terror_2025_incident_supplement.csv) and [existing jihadist records](data/jihadist_2025_incidents.csv)
- [Procedural and relationship updates](data/terror_2025_judicial_relationship_updates.csv)
- [Additional sources](data/terror_2025_additional_sources.csv) and [existing source keys](data/jihadist_2025_sources.csv)

## Source-bounded EU comparison

[Europol TE-SAT 2026](https://www.europol.europa.eu/cms/sites/default/files/documents/EU-TE-SAT-2026.pdf), pp. 18–20 and 47. The linkage of category to outcome uses the explicit p. 19 narrative. The two marginal tables alone would not establish every joint cell.

| Ideology | Completed | Failed | Foiled | Total |
|---|---:|---:|---:|---:|
| Jihadist | 9 | 0 | 15 | 24 |
| Right-wing | 1 | 0 | 4 | 5 |
| Left-wing and anarchist | 11 | 1 | 0 | 12 |
| Ethno-nationalist and separatist | 0 | 0 | 0 | 0 |
| Other or unspecified | 1 | 2 | 1 | 4 |
| All | 22 | 3 | 20 | 45 |

The six fatalities comprise five in jihadist attacks and one in a right-wing attack. The report specifies 81 jihadist injuries and separately six injuries in reported other/unspecified stabbings. It reports no victims for left-wing/anarchist attacks. An all-category injury total and an event-by-event victim allocation are not derived. A zero in this table means no event or victim reported in that source category as applicable.

| EU member state in the annex | Completed | Failed | Foiled | Total |
|---|---:|---:|---:|---:|
| France | 3 | 0 | 11 | 14 |
| Italy | 10 | 1 | 0 | 11 |
| Austria | 1 | 0 | 6 | 7 |
| Germany | 4 | 0 | 0 | 4 |
| Belgium | 0 | 0 | 2 | 2 |
| Greece | 1 | 1 | 0 | 2 |
| Ireland | 1 | 0 | 1 | 2 |
| Malta | 0 | 1 | 0 | 1 |
| Netherlands | 1 | 0 | 0 | 1 |
| Spain | 1 | 0 | 0 | 1 |

France reports the most cases in this EU source (14), mainly foiled (11). Italy reports the most completed cases (10). The other 17 EU countries have no attack row in the report. The four non-EU countries are outside its statistical scope. A 31-country sum or rate cannot be constructed from these series.

## Classification and discrepancy register

| Issue | Evidence and treatment |
|---|---|
| France | PNAT separately counts three completed jihadist-inspired events, compared with two in TE-SAT. The October DNRT lead and the unresolved individual matching remain in the [French audit](FRANCE_2025_PNAT_VS_EUROPOL_DISCREPANCY.md). PNAT identifies Puget-sur-Argens as a completed ultra-right attack, consistent with the single French right-wing completed cell. The June 2025 formal investigation is reported by Le Monde, with disputed motive and judgment unavailable (fr-pnat, fr-puget, fr-puget26). |
| Germany | Essen remains provisional pending submission or age-reference clarification. TE-SAT p. 33 includes a German right-wing case example while p. 20 has no German right-wing attack count. The text dates arrests and does not make this an annex entry. The German prosecutor identifies a broader investigation in 2026 and JPD reports a November 2026 trial of two alleged supporters, docket 3 St 2 BJs 190/26. Match the conduct charged, incident date and any decision before creating an event link (de-lvw, de-lvw26). |
| Italy and Greece | Italy has ten completed and one failed left-wing/anarchist events. The 18 January travel-agency example and the 31 March Narni case are traceable in the report. The Narni failed outcome remains inferred, and the parliament transcript establishes locality rather than a judgment. Hellenic Train is explicitly described in TE-SAT p. 39 and Hellenic Police's same-day release. The separate failed Greek other/unspecified incident remains unidentified (it-narni, gr-pol). Claims are not judicial attribution. The US NCTC also attributes Hellenic Train to the claimant group (gr-odni). |
| Netherlands | Prosecutors described five injuries and alleged terrorist intent after the Dam attack; the Jan. 2026 entry is a procedural hearing. The single Dutch other/unspecified completed cell is consistent with this case. The public aggregate of six injuries from other/unspecified stabbings spans the category and does not settle this match (nl-om, nl-om26, eu-full). |
| Ireland | TE-SAT p. 35 illustrates the November plot also reported in Galway court coverage. Three defendants were sentenced after guilty pleas on 30 October 2026, with reported terms of 10½, 8 and 8 years and the final year suspended in each. The presiding judge described a leadership role. The source does not establish the fourth accused's ultimate outcome or appeal status. The existing Dublin stabbing/arson distinction remains (ie-galway, ie-galway-sentence). |
| Poland and Portugal | Polish ABW reports interrupting alleged preparations on 30 November and referral to court in 2026. In Portugal, six arrests in June 2025 led to a nine-defendant indictment in June 2026. DCIAP says all were referred for trial on 1 October, with financing, recruiting and group offences among the charges. This is not a financing finding. Neither country appears in the EU attack table. The domestic measures include preparatory activity; whether an individual event qualified for or was submitted to TE-SAT was not established (pl-attack, pt-pj, pt-dciap, pt-malinstr). |
| Norway and Portugal | PST explicitly reports no completed extreme-Islamist attack in Norway since 2022; RASI explicitly reports no Islamist terrorist attack in Portugal through 2025. Both zeros are ideology-specific. Threat assessments do not supply all-category failed or foiled data (no-pst, pt-rasi). |
| Iceland and Liechtenstein | Iceland's April assessment measures threat, with no verified full-year attack census. Liechtenstein reports one recorded police offence under Terrorismus. The annual table does not identify an attack outcome, ideology, case or victims (is-risk, li-pol). |
| UK and Northern Ireland | CTP declared the Manchester synagogue attack a terrorist incident. Judicial inquests cover two victim deaths; attribution of individual deaths and injuries needs the inquest record. In the separate Shrivenham case, the sentencing court found joint terrorist preparation and a decision not to proceed, imposing life with minimum 16 years and 135 days on Bashir. CPS reports no evidence presented of his involvement in the synagogue attack. NI reports zero in the narrower national-security attack series, with 12 bombings and nine shootings in separate calendar-year metrics. Frankland is retained as an assault lead with terrorism classification unresolved (gb-ctp, gb-inq, gb-bashir, gb-cps, gb-ni, gb-frankland). |

## Source-quality, missing-data and progress audit

- The CSV matrix contains 31 country rows, comprising 10 TE-SAT attack rows, 17 EU absences and four countries outside the statistical scope. The national source status distinguishes annual reports located, scoped zeros, case-specific evidence, other metrics and unsuccessful searches. Locating a report does not imply extracting or validating an attack census. Missing national figures for cases, ideology, victims, outcomes, or definitions remain blank or explicitly unresolved.
- At this report’s baseline, the supplement recorded 12 events or preparatory leads and retains national and TE-SAT labels separately. Confirmed qualifies the source-supported event or official action; the match and evidence-stage columns govern the EU link and allegations. Preparation-only flags carry no completed, failed or foiled aggregate weight without a source-specific outcome. Confirmed EU statistics are independently reconciled to the source-specific provisional country margins. Historic files and the ten jihadist incident records retain their original classifications.
- Immediate evidence priorities: identify the remaining Italian cases and the separate Greek and Maltese failed entries; verify the Dutch case match and Dutch trial outcome; identify Belgium's other/unspecified foiled case and independently check the Antwerp submission. Obtain individual French right-wing foiled entries and the original Irish judgment, fourth accused's disposition and subsequent appeal evidence. Verify the Portuguese and Polish merits dockets.
- Next country pass: extract the national reports identified but not ingested into comparable totals, find equivalent or clearly marked national statistics where missing, and check case-level GB coverage against official calendars. Seek the Icelandic full-year series and Liechtenstein offence definition and case type. Revisit underlying national definitions before claiming a zero or comparing source counts. Continue the [jihadist evidence queue](2025_EVIDENCE_FOLLOW_UP_2026-11-18.md) alongside these tasks. Full incident census and publication-level independent verification remain open.
