# Phase 24 — Adversarial editorial audit

18 November 2026 · verified base `09a4c4763f56e8396bd66fbab98f55d4a26aebdd` · branch `research/terror-eu-eea-foundation-2026` · [draft PR #7](https://github.com/npcsignals/npcsignals/pull/7). Starting main `18ff335e85b36f072a03a19faac8ee051fb32867`.

Verdict after corrections: ready for independent human editorial review. Publication remains blocked. The audit uses a separate adversarial verification procedure against edition PDFs, official statements, raw transcriptions and image renders. It is model-performed, in continuity with the prior work. Even a separate model review would not constitute independent human editorial approval. The claim matrix assesses the Phase 23 starting wording; the report and its ledger now contain the corrected wording.

[Claim verification matrix](claims_verification.csv) · [Corrections ledger](findings.csv) · [Figure inspection](FIGURE_INSPECTION.md) · [Readable alternatives](TEXT_ALTERNATIVES.md)

## Judicial source record

- **A100.** Landgericht Berlin PM 5/2022, oral-reasons summary, excludes the Islamist-attack characterisation and describes compulsory psychiatric placement. The original BGH announcement 036/2023 and the linked disposition establish rejection of revision on 16 February 2023 and finality. TE-SAT 2023 p. 9 n. 4 leaves the deleted incident unnamed. Maintain the separate candidate status. [Landgericht](https://www.berlin.de/gerichte/presse/pressemitteilungen-der-ordentlichen-gerichtsbarkeit/2022/pressemitteilung.1172551.php) · [BGH](https://www.bundesgerichtshof.de/SharedDocs/Pressemitteilungen/DE/2023/2023036.html)
- **Holbæk.** PET's 14 May 2024 announcement describes the principal defendant's appellate result and distinguishes the dispositions of the other people in the case. The source is an official agency summary. Signed reasons and any later appeal disposition were not verified. The reviewed finding establishes case-specific financing within the stated judgment scope and supplies no external command finding. [PET](https://pet.dk/pet/nyhedsliste/en-36aarig-mand-idoemt-16-aars-faengsel-af-landsretten-i-terrorsag-fra-holbaek/2024/05/14)
- **Solingen.** The DSV reproduction's wrapper uses 22 May for the decision while its reproduced text gives 12 May. The original BGH notice 091/2026 gives **12 May 2026** in the holding header and **22 May** in its publication dateline, identifying OLG Düsseldorf III-5 St 2/25 as the underlying judgment. The issuer's linked disposition confirms dismissal and finality without further reasons. The BGH announcement separately summarises the lower court's finding that contacts from IS encouraged and advised the perpetrator. This upgrades source attribution for a limited assistance finding. It leaves the scope of operational command and financing unestablished. The annual source and proceeding rows remain frozen as historical observations of the reproduction. The corrected phase23 judicial table distinguishes decision and notice. [Original BGH notice](https://www.bundesgerichtshof.de/SharedDocs/Pressemitteilungen/DE/2026/2026091.html) · [Issuer-linked disposition](https://www.bundesgerichtshof.de/SharedDocs/Entscheidungen/DE/Strafsenate/3_StS/2026/3_StR__55-26.pdf?__blob=publicationFile&v=2)

Solingen retrieval fingerprints, 18 November 2026. Original HTML 33,026 bytes, SHA-256 `018d7944f578648cbacf8afe2b9627978170cbf6450c3853cbc685371ae248a5`. Issuer-linked PDF 6,259 bytes, SHA-256 `d16a85ceb95c95944304d873d095d7a1b67e1ce60e678589949f398b2bee55ab`.

## Narrative and selection risk register

| Risk | Evidence and response | Residual control |
|---|---|---|
| Scope collapse | C01 and C09 could be read as sharing a single 31-country or EU27 population. State edition territory and historical UK inclusion where counts appear. | Retain these qualifications in extracts. |
| Trend or peak inflation | The 120 maximum is within original fixed-geography cohorts. F02 marks the older 2023 records and F03 presents the conditional variant. | Physical-event trend remains unsupported. |
| Uniform counting and misconduct inference | Published disparities reflect different source units or unresolved arithmetic. C16–C18 now identify edition and unit more precisely. | Discrepancies supply no finding of intent or misconduct. |
| Treating unidentified slots as fictitious | C10 and F04 make the statistical denominator and incomplete identity evidence explicit. | Excerpts must retain the definition and the candidate-slot distinction. |
| Judicial selection bias | The three illustrations foreground cases with available court or agency records. They demonstrate evidentiary boundaries and have no representative denominator. | Keep separate facts about each case and avoid cross-case claims of shared command. |
| Arrest conversion | C08's prior wording risked implying that calendar years differ. Year 2025 is shared; it indexes different events and cohorts. | No conviction-to-arrest ratio or inference of unique people. |
| Count differences as event keys | German 5/4/4 and French 3/2 are contrasts in source-specific units. | Continue holding event identities pending matched records. |

## Privacy and harm

No suspect or victim names, private addresses or operational instructions appear in the reader-facing report and figures. Place-based labels and court locators are sufficient for verification. Repetition of names or technical details from linked sources would add harm without supporting the analytical claims. The audit kept allegations, agency summaries, judicial outcomes and Europol statistical linkage separate. A100's psychiatric disposition is reported as a case holding and supplies no general inference about mental illness. Ideological categories are labels from the respective source scopes, with no population-level inference.

Detached charts and excerpts remain the main proportionality risk. The figures carry scope or limits in-image and the text alternatives preserve values and source context. Any final export requires human review of standalone renderings, including any crop, preview card or social-media extract.

## Publication gate

| Dimension | Verdict |
|---|---|
| Statistical integrity | PASS. Original and derived datasets reproduce byte for byte; independent arithmetic checks agree. |
| Source integrity | PASS for qualified review after restoring the primary Solingen issuer chain and retaining source-specific uncertainty. |
| Editorial accuracy | Ready for human review after the corrections recorded in the ledger. |
| Visual accuracy | PASS at reviewed desktop width. Numeric labels and geometry agree with the source. Small-width fixed SVG text needs an accompanying readable alternative or a responsive export. |
| Judicial attribution | PASS for the exact scoped wording. Stronger claims on A100 linkage, Holbæk finality or Solingen command require additional evidence. |
| Privacy and harm | Pass for internal use with minimum necessary detail. Final publication context remains unaudited. |
| Independent human approval | Pending. No human approval has been obtained. |
| Overall public release | Blocked pending human editorial and export review and explicit publication authorisation. |

## Reproducible results

Run the shell block in [Phase 23 build instructions](../phase23/BUILD.md) and then:

```sh
python3 -B research/terror-in-eu-eea/audit/phase24/verify_independent.py
```

Before editing, both CSVs and all six Phase 23 SVGs matched their references. After editing, both CSVs still match and the corrected figures rebuild byte for byte. SHA-256 for the recalculation `fc351da07034e81754741f8fc3963855d62627747c84e366f634f9fcb5a6ab9f`; analytical CSV `d88bbcae61083b791dc253f834d754767618f96e90c3d960ac41fa23ef02507d`. The independent check imports no prior validation functions. It recomputes country rows, category and outcome margins, explicit revisions, scenario arithmetic and exact slot partitions. The 2025 split by adequate matches is **6/22 completed, 0/3 failed and 1/20 foiled**. Raster inspection was done using Inkscape at 880 and 360 px. A figure-height change during remediation corrected an overlapping F02 footer.
