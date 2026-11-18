# phase 25 — direct-source verification ledger

review date: 18 november 2026
scope: selected high-impact assertions in the reader-facing report. this is a partial, explicit source check, not verification of every source.

## directly inspected

| claim | direct source | verified observation | result |
|---|---|---|---|
| c01–c02 methodological framing | [europol, EU TE-SAT 2026, introduction p. 5](https://www.europol.europa.eu/cms/sites/default/files/documents/EU-TE-SAT-2026.pdf) | member states supply attack/arrest data; eurojust supplies judicial data; national legislation and case classifications may differ. | confirmed for methodological framing, not for the complete 2015–2025 dataset |
| c04, c07, c17, 2025 totals | [EU TE-SAT 2026 pp. 6, 18–20, 47–49](https://www.europol.europa.eu/cms/sites/default/files/documents/EU-TE-SAT-2026.pdf) | 45 reported attacks, 486 arrests, 22 completed, 3 failed, 20 foiled; jihadist 24 attacks and 347 arrests. | confirmed |
| c08 | [EU TE-SAT 2026 p. 23](https://www.europol.europa.eu/cms/sites/default/files/documents/EU-TE-SAT-2026.pdf) | eurojust reports 406 convictions and 99 acquittals in proceedings concluded in 2025; some decisions are not final. | confirmed, with finality caveat |
| c06 | [EU TE-SAT 2026 annex pp. 47–48, notes 44–45](https://www.europol.europa.eu/cms/sites/default/files/documents/EU-TE-SAT-2026.pdf) | 70 french separatist entries reported in the 2023 cohort, consisting of four 2021, 22 2022 and 44 2023 occurrences. | confirmed for 26 older entries; the conditional scenario is NPCsignals' calculation, not a publisher observation |
| c14 | [German Bundestag response 21/4296 p. 18, question 29](https://dserver.bundestag.de/btd/21/042/2104296.pdf) | lists Munich (13 Feb), Berlin (21 Feb), Bielefeld (18 May), and Essen (5 Sep) 2025. question 28 explains that incident classification can require individual review and delay. | confirmed for four named federal locations; does not verify NRW's separate five |
| c15 | [EU TE-SAT 2026 pp. 19–20](https://www.europol.europa.eu/cms/sites/default/files/documents/EU-TE-SAT-2026.pdf) | two completed french jihadist attack entries and four completed german jihadist entries. | confirmed for europol counts; PNAT's three not independently reopened |
| c17 | [EU TE-SAT 2026 p. 27 note 36](https://www.europol.europa.eu/cms/sites/default/files/documents/EU-TE-SAT-2026.pdf) | age note uses 344 jihadist arrests, while the report's principal count is 347. | confirmed unresolved discrepancy |
| c17 2023 arrests | [EU TE-SAT 2026 p. 49 and subsequent country annexes](https://www.europol.europa.eu/cms/sites/default/files/documents/EU-TE-SAT-2026.pdf) | main type-level table totals 426 in 2023. | confirmed for 426; the separate 431 sum was not independently recalculated in this session |

## not yet directly verified

- **c03 2019 geography:** the cited TE-SAT 2020 PDF was not accessible to the web retrieval service because of a size limit. the 119/64/55 values remain supported by the versioned, previously audited dataset but were not re-verified against that PDF in this session.
- **c05 official revisions:** the TE-SAT 2023 footnote was not reopened in this session; 56 and 18 remain previously audited values.
- **c11–c13 judicial sources:** the BGH 091/2026 page returned an access-denied response to the web retrieval service. the A100 and PET original notices were not reopened. do not label them independently re-verified.
- **c14 NRW, c15 PNAT, c16 injuries, c18 Corsica:** original documents were not reopened in this session.
- **c09–c10 identification coverage:** arithmetic and the project crosswalk are internal research measurements, not observations that Europol can independently attest.
- **c19–c20:** bounded interpretations rely on the overall methodology and completeness audit; no stronger external factual claim is asserted.

## source quality notes

- source access failure is **not** evidence that a document does not exist or that its contents are false.
- direct web retrieval of a PDF verifies only the inspected passages. it does not validate every page, claim, calculation or the full external link set.
- retain precise printed-page references in the [source guide](SOURCE_GUIDE.md), but distinguish inherited audited locators from passages directly reopened here.
- do not clear publication until the outstanding direct-source checks and a human editorial review are completed.

**verdict: partial verification, not an independent source-completeness pass.**
