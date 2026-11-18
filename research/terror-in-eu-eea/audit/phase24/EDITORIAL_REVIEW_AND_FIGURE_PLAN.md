# editorial narrative review and figure plan

internal working note · 18 november 2026 · following phase 24 · not approved for publication

## reviewed sources

- [reader-facing draft](EDITORIAL_REPORT_DRAFT.md)
- [original report with 20 audited claims](../phase23/REPORT.md) and [claim register](../phase23/claims.csv)
- [phase 24 audit](AUDIT.md), [figure inspection](FIGURE_INSPECTION.md), [figure captions](../phase23/FIGURES.md), and [accessible alternatives](TEXT_ALTERNATIVES.md)

this is an editorial review of existing evidence and assets, not a new primary-source investigation. independent human editorial approval has not been obtained.

## narrative assessment

**editorial focus:** what europol's terrorism statistics measure, how they are reported, and how geography, reporting cohorts and institutional counting units shape interpretation. do not claim an overall change in the actual terrorism threat.

**strength:** the 2019–2020 geographic comparison is a concrete opening. retrospective entries explain why the reporting year may differ from the occurrence year. identification coverage demonstrates the limits of the investigation's public event-linkage evidence.

**main risks:** readers may mistake the conditional sensitivity scenario for an official revised series, or interpret 926 unidentified statistical entries as attacks for which europol has no internal documentation. retain the qualifications in the body, captions, previews and standalone extracts.

**balance:** do not characterize cross-institutional count differences as evidence of suppression, misconduct or error. treat them as source-specific differences in definitions, scope and counting units unless stronger evidence emerges.

## figure selection and placement

| placement | figure | editorial decision | required control |
|---|---|---|---|
| 1 | f01 geography + f02 eu27 series | **paired lead illustration**. f01 ends in 2019 and cannot alone support the 2019–2020 comparison. | preferably produce a dedicated three-value panel for 2019 original 119, 2019 fixed eu27 55, and 2020 eu27 57. if the later official 56 is shown, label it separately. this panel has not been produced. |
| 2 | f03 revisions and sensitivity | **primary illustration**. | show 56 and 18 as official revisions and 56/22/50/94 as a conditional scenario. missing official revision values are not zero. |
| 3 | f04 identification coverage | **primary illustration**. | retain 168/35/926 of 1,129, the mixed original eu28/eu27 denominator and the distinction from europol's internal evidence. |
| 4 | f05 institutional counts | **supplementary illustration** adjacent to the institutional reporting discussion. | each number retains its country, issuer, source scope and unit; do not imply a verified common event roster. |
| appendix | f06 judicial evidence chains | **evidence appendix** with an in-text link. | retain source classes, judicial stages and distinct decision/publication dates. |
| appendix / context | f02 complete eu27 series | **retain the full series** even if its 2020 data point also supports the lead comparison. | separate attack and arrest panels; no causal inference. |

## source presentation

the reader-facing draft uses c01–c20 as internal cross-references. **these are not yet reader-friendly source citations.** before publication, each supported assertion needs a source display with document title, edition, precise page or paragraph, and direct link where available. editorial review must confirm that each claim reference maps to the appropriate entry in the existing claim register. a bare csv link is not a sufficient presentation for general readers.

judicial examples should use direct court or agency links with accurate source type. the a100 deletion link remains a candidate; holbæk is attributed to pet's summary; solingen distinguishes the decision on 12 may 2026 from the announcement on 22 may.

## accessibility and export

phase 24 identified small labels at 360 px. the current svg files are therefore **not approved as standalone mobile graphics**. review the actual release format at mobile size, including numbers, caveats, captions and screen-reader alternatives. cropping or preview generation must not remove critical qualifications.

## recommended article structure

1. open with the geographic comparison.
2. explain retrospective reporting and official revisions.
3. contrast institutional counting units.
4. explain identification and event-linkage limitations.
5. provide a short judicial illustration, with extended evidence in an appendix.
6. preserve unresolved discrepancies.
7. conclude with explicitly bounded findings.
8. attach a source and methods appendix with the complete annual table and all six figures.

## release gates

- independent human editorial approval: **pending**.
- final export, mobile rendering and accessibility: **pending**.
- privacy and harm assessment of the actual release context: **pending**.
- explicit authorization to publish: **pending**.
- main, pull request state and public deployment: **must remain unchanged**.

**editorial verdict:** suitable for independent human review with three lead illustrations and a documented evidence appendix. not cleared for publication.
