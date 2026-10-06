# Repository preparation QA — 6 October 2026

**File/data integrity: PASS. Figure publication readiness: NEEDS CORRECTION.**
Evidence basis remains v0.114 / U453; no ledger changes and no research.

## Verified

- Original 24 recorded SHA-256 values and byte counts match the uploaded files.
- Locked main report and technical report match the previous exact frozen copies.
- 35 unique sales, 17 sellers, 1,527,248,306.725914 gross FACv sold and 606.331808740 SOL/WSOL received; row-by-row amounts/signatures/accounts match the previous export after column-name mapping.
- Cumulative dataset reconciles at every row; +57s = 251.752785673 and +2422s = 606.331808740. SVG Figure 3 step coordinates reproduce all 35 rows, including same-second events, without interpolation.
- Nine signature-derived Solscan links; ten figure assets (five PNG/SVG pairs); original claims images present.
- Figure 1 retains slot/index ordering. Figure 2 names the correct frozen six-wallet matrix. Figure 4 uses distinct FDV observations, not a fabricated price series. Figure 5 numbers reconcile exactly.

## Publication blockers in preserved figures

| Figure | Finding | Required correction before Medium |
| --- | --- | --- |
| 1 | Long event text extends beyond its boxes; fine text is difficult at mobile width. | Reflow labels and test mobile presentation, retaining same-second/slot ordering. |
| 2 | Text overruns boxes and overlaps the matrix/status area. The claim that all 63 other sources transferred across 10 additional transactions is unsupported: D12 itself includes HZrAo **and five other sources**. | Reflow layout. Retain 64 sources / 11 transactions total and 481,307,162.351855 FACv from the other 63, but remove the separate 10-transaction attribution. Source: v0.100 D12 and v0.110 consolidation manifest. |
| 3 | Axis says “Seconds since launch” while ticks use minutes:seconds; there is no specified first-minute inset. | Use “Elapsed time since launch (mm:ss)” and add a readable first-minute view. The step series itself passes exact verification. |
| 4 | Panel text spills across adjacent boxes. | Reflow the three comparison panels. Preserve logarithmic-scale notice, candle/proxy limitations and non-lifetime-ATH wording. |
| 5 | Joint-only remainder appears as a connected sixth branch. Category percentage labels suggest allocation/composition. Boundary is beside the flow rather than terminating category endpoints; text overruns boxes. | Show the 3.398211330 joint-only remainder as a disconnected dashed accounting note, not a receiving branch. Clearly label category numbers as lower bounds; avoid composition percentages. Stop categories at the attribution boundary and keep final-beneficiary box disconnected. Preserve all amounts and distinctions. |

No figure has been regenerated or substituted. The assets remain the received originals for transparent review. These issues do not alter the frozen report or claim classifications.

## Packaging changes

README now supplies working relative navigation and the FACv mint. Stale “figures not rendered” packaging language has been corrected. SOURCE_INTEGRITY.json is refreshed only for packaging changes/additions; original hashes remain in SOURCE_INTEGRITY_UPLOADED.json. Public-link Medium copy changes link markup only, once the GitHub evidence path is available.

## Before Medium publication

Correct figure presentation/semantics above; check the resulting PNG and SVG exports together. Review images/captions/tables on mobile in Medium. Decide whether the internal verification appendix should be linked as evidence only. Explorer links are preserved signatures, not newly archived explorer captures. Do not publish until separately instructed.
