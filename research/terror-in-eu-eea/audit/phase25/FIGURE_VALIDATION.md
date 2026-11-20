# phase 25 — validated English figures

All seven desktop SVGs were rendered at 900 px. The same desktop files were also rendered at 360 px and found too small for reliable mobile reading. The dedicated 360 px layouts below were then rendered and inspected. They use the same values and qualifications in a compact tabular layout with visible units and source notes. The six desktop translations preserve the original graphic geometry and numerical labels.

| figure | desktop | mobile |
|---|---|---|
| 2019–2020 geography | [SVG](figures/01_2019_2020_geography.svg) | [360 px SVG](figures/mobile/01_2019_2020_geography.svg) |
| EU28 and fixed EU27 | [SVG](figures/01_geography_en.svg) | [360 px SVG](figures/mobile/01_geography_en.svg) |
| fixed EU27 series | [SVG](figures/02_eu27_series_en.svg) | [360 px SVG](figures/mobile/02_eu27_series_en.svg) |
| revisions and sensitivity | [SVG](figures/03_revisions_en.svg) | [360 px SVG](figures/mobile/03_revisions_en.svg) |
| identification coverage | [SVG](figures/04_coverage_en.svg) | [360 px SVG](figures/mobile/04_coverage_en.svg) |
| institutional observations | [SVG](figures/05_institutions_en.svg) | [360 px SVG](figures/mobile/05_institutions_en.svg) |
| judicial evidence | [SVG](figures/06_judicial_en.svg) | [360 px SVG](figures/mobile/06_judicial_en.svg) |

[Lead text alternative](figures/01_2019_2020_geography_ALT.md) · [Captions and data locators](../phase23/FIGURES.md) · [Text alternatives](../phase24/TEXT_ALTERNATIVES.md)

Run the [baseline script block](../phase23/BUILD.md) and then, from the repository root:

```sh
set -eu
root=research/terror-in-eu-eea
python3 -B "$root/audit/phase24/verify_independent.py"
python3 -B "$root/audit/build_english_figures.py" --check
python3 -B "$root/audit/phase25/verify_layouts.py"
```

The last check requires Inkscape. It measures text bounds, validates title/description metadata and tests minimum mobile text size and left-column clearance. For a raster review, export each desktop SVG with `inkscape INPUT.svg -w 900 -o OUTPUT.png` and each dedicated mobile SVG with width 360. The builder without `--check` regenerates the 14 tracked SVGs. The original six Phase 23 SVGs are preserved.
