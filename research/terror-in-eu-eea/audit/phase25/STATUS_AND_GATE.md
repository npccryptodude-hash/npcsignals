# phase 25 — source presentation and visual production checkpoint

date: 18 november 2026
status: **partial implementation; publication blocked**

## completed

1. created [an English reader-facing source guide](SOURCE_GUIDE.md) linking all eleven annual TE-SAT editions from the versioned dataset, with printed-page locators and a claim-to-evidence map for c01–c20.
2. created [an English 2019–2020 geographic comparison SVG](figures/01_2019_2020_geography.svg) showing 119, 55, 57 and the separately labelled later official revision 56. the arithmetic 119 − 64 = 55 was checked against the annual dataset and c03.
3. created [an English accessible text alternative](figures/01_2019_2020_geography_ALT.md).
4. translated [phase 23 figure captions](../phase23/FIGURES.md) and [phase 24 text alternatives](../phase24/TEXT_ALTERNATIVES.md) to English while retaining the numerical observations and caveats.
5. updated [the English editorial report](../phase24/EDITORIAL_REPORT_DRAFT.md) to link to the new figure and source guide.

## independently checked within this session

- the branch matched the phase 24 head before phase 25 edits.
- annual dataset values for 2019 and 2020 agree with the new figure and source guide.
- the existing figure 01 ends in 2019, so the new panel addresses a genuine editorial mismatch.
- the existing phase 24 figure inspection warns that labels are too small at 360 px for comfortable standalone reading.

## outstanding defects and constraints

**language:** the phase 23 captions and phase 24 text alternatives have now been translated to English. however, portions of [the phase 23 SVG generator](../phase23/build_figures.py) and inherited SVG assets contain Norwegian labels or prose. the original [phase 23 research report](../phase23/REPORT.md) also remains in Norwegian. these inherited materials require controlled English remediation and numerical regression checks. do not imply that the repository is now entirely English.

**figure validation:** the new SVG includes a title, description and explicit numbers, but no actual 360 px raster/export inspection was completed in this session. final mobile versions of all main figures are not yet approved. the new SVG is a static evidence graphic, not a generated output from the existing deterministic figure builder; add a reproducible builder and exact-value tests before production use.

**citation completeness:** annual report links and page locators were transcribed from the versioned dataset; not every external PDF was reopened in phase 25. some judicial and institutional entries still lack verified direct reader-facing URLs. the source guide is a citation map, not a completed source-verification audit.

**editorial signoff:** no independent human editorial review has occurred. no final-format export or full privacy/harm assessment has been completed.

## next controlled tasks

1. translate inherited SVG assets, their generator and remaining Norwegian research prose to English without altering statistics or evidentiary qualifications.
2. make the new geographic SVG reproducible from the versioned annual dataset; test exact values, zero-based comparisons, source labels and accessibility.
3. create mobile-specific figure exports, visually inspect at the intended width, and test that captions and caveats remain attached.
4. verify direct judicial and institutional source URLs, all c01–c20 citation placements, and external edition links against the original documents.
5. conduct an independent human editorial review, then a final publication gate assessment.

**publication verdict:** blocked. no merge, public deployment, contact with subjects, or modification of main is authorized.
