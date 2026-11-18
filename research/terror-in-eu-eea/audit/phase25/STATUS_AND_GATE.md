# phase 25 — source presentation and visual production checkpoint

date: 18 november 2026
status: **English figure copies complete; final mobile and source-verification gates blocked**

## completed

1. created [an English reader-facing source guide](SOURCE_GUIDE.md) linking all eleven annual TE-SAT editions from the versioned dataset, with printed-page locators and a claim-to-evidence map for c01–c20.
2. created [an English 2019–2020 geographic comparison SVG](figures/01_2019_2020_geography.svg) showing 119, 55, 57 and the separately labelled later official revision 56. the arithmetic 119 − 64 = 55 was checked against the annual dataset and c03.
3. created [an English accessible text alternative](figures/01_2019_2020_geography_ALT.md).
4. translated [phase 23 figure captions](../phase23/FIGURES.md) and [phase 24 text alternatives](../phase24/TEXT_ALTERNATIVES.md) to English while retaining the numerical observations and caveats.
5. updated [the English editorial report](../phase24/EDITORIAL_REPORT_DRAFT.md) to link to the new figure and source guide.

6. added six English SVG copies in [phase 25 figures](figures/), preserving the original SVG geometry, coordinates and numeric text labels. a [versioned translation manifest](figure_translations.json) and [deterministic rebuild/check script](../build_english_figures.py) were added. the original phase 23 SVGs remain untouched.
7. recorded selected direct primary-source checks and explicit unresolved items in [the verification ledger](DIRECT_SOURCE_VERIFICATION.md).
8. updated the editorial report to link to the English copies.

## independently checked within this session

- the branch matched the phase 24 head before phase 25 edits.
- annual dataset values for 2019 and 2020 agree with the new figure and source guide.
- the existing figure 01 ends in 2019, so the new panel addresses a genuine editorial mismatch.
- the existing phase 24 figure inspection warns that labels are too small at 360 px for comfortable standalone reading.

## outstanding defects and constraints

**language:** the reader-facing figure set, figure captions and text alternatives now have English versions. original historical files, including the phase 23 SVG generator and report, retain Norwegian and remain in the repository as preserved audit evidence. a separate repository-wide English-only remediation remains necessary if the requirement applies retroactively to all historical files.

**figure validation:** six English copies have text-only translations and a committed byte-for-byte rebuild script, plus a dataset-value check for the new lead figure. the checks were not executed in a checked-out repository in this session; source/translated geometry was compared in the GitHub tool workflow. no actual 360 px raster/export inspection was completed. final mobile versions remain unapproved. the lead figure is a static source-controlled graphic with dataset-value validation, not yet generated from a complete deterministic drawing routine.

**citation completeness:** selected primary sources were reopened and compared in the [direct-source ledger](DIRECT_SOURCE_VERIFICATION.md), including Europol 2026 and Bundestag 21/4296. the 2019 PDF was too large for retrieval and the BGH page returned access denied; other source links remain unverified. this is a partial source audit, not a completed claim-by-claim verification.

**editorial signoff:** no independent human editorial review has occurred. no final-format export or full privacy/harm assessment has been completed.

## next controlled tasks

1. execute the deterministic figure check in a clean repository checkout; inspect exported English graphics at 360 px and resolve any label overflow. preserve the original historical assets as audit evidence.
2. add a fully generated version of the new geographic SVG or document its controlled static production process, and run its dataset validation and accessibility checks.
3. create mobile-specific figure exports, visually inspect at the intended width, and test that captions and caveats remain attached.
4. complete remaining direct judicial and institutional source checks, all c01–c20 citation placements, and external edition links against the original documents.
5. conduct an independent human editorial review, then a final publication gate assessment.

**publication verdict:** blocked. no merge, public deployment, contact with subjects, or modification of main is authorized.
