# phase 25 — final figure and source validation

Review date: 18 November 2026. Verified starting checkpoint `cdd3572e8232ee1e1615b0ce48c01e80fd5fd26f` on `research/terror-eu-eea-foundation-2026`, draft PR #7. Starting main `18ff335e85b36f072a03a19faac8ee051fb32867`.

| Gate | Result |
|---|---|
| Technical verification | PASS. Original statistical and analytical CSVs and all six historical SVGs reproduce byte for byte. Phase 24 independent recomputation passes. The English build check passes for all 14 outputs. |
| Desktop rendering | PASS at 900 px. Zero baselines, separate revised markers, source locators and numeric labels checked. |
| Mobile rendering | PASS for seven dedicated 360 px layouts. Use these versions or the text alternatives on narrow screens. Shrunken desktop assets retain small type. |
| Claim verification | All C01–C20 checked. Evidence limitations remain explicit in the matrix. Holbæk's signed judgment and later disposition and the Solingen lower-court reasons are NOT REVERIFIED. |
| Editorial handoff | Ready for independent human editorial review. Human signoff, final dissemination-format review and explicit publication authorization remain pending. |

The initial build check failed because the SVG tag and numeric regular expressions were over-escaped. After repair, the six existing translations matched their committed SVG bytes exactly, including unchanged geometry and numeric labels relative to their originals. The lead chart now derives values and bar widths from the analytical dataset. Mobile rows use that same dataset and the committed institutional and judicial records. Column overlaps found in early mobile rendering were corrected. Historical Norwegian source artifacts remain versioned as audit evidence. The active editorial and figure package is in English.

The recalculation SHA-256 remains `fc351da07034e81754741f8fc3963855d62627747c84e366f634f9fcb5a6ab9f`. The analytical CSV SHA-256 remains `d88bbcae61083b791dc253f834d754767618f96e90c3d960ac41fa23ef02507d`.

## Unresolved issues

| Issue | Retained disposition |
|---|---|
| 2015 original 211 versus 193 in later charts | Both preserved. No revised value established. |
| 2016 379 overall versus 597 from three cases, with annex 374 jihadist casualties | Scope and measurement remain incompatible or unknown. |
| 2023 arrests 426 versus retrospective annex sum 431 | 426 remains baseline. 431 is a reconstruction. |
| 2025 jihadist arrests 347 versus age note 344 | Separate printed denominators, with no derived age share. |
| October 2023 Corsica 32 national facts versus 34 Europol attacks | Separate units and unknown event mapping. |
| A100, Essen, French candidate entries and historical cohort mapping | Candidate or unknown relationships retained. No exact linkage inferred. |
| Holbæk and Solingen documentary limits | Agency/court-summary provenance preserved. No inference of external operational command. |

[English report](../phase24/EDITORIAL_REPORT_DRAFT.md) · [Source guide](SOURCE_GUIDE.md) · [Direct-source verification](DIRECT_SOURCE_VERIFICATION.md) · [Figure validation and reproducible build](FIGURE_VALIDATION.md)

Publication, deployment, contact with investigated parties and merge remain outside this phase.
