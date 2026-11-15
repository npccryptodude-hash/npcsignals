# editorial quality review — 15 november 2026

base: `45682ee3879d20d703e04fe3e1d5a4fd96e939e8` (merged pull request #3). scope: the 16 registered research subjects. principle: document, not judge.

## what this review establishes

this is an editorial and documentary-consistency review, not a new investigation or an independent re-adjudication of every claim. all 16 entrances were read alongside their main findings, methods, limitations and central source references. workbook classifications and selected denominators were reproduced read-only. source access was sampled, not exhaustively certified. the accompanying [review record](EDITORIAL_REVIEW_RECORD.json) identifies the central files and their hashes.

research status and editorial quality are separate. `archived` does not mean independently verified; `requires verification` below does not mean a claim is false. no evidence grade, original conclusion or historical report was changed.

## assessment of all 16 subjects

questions: q1 understandable without specialist knowledge; q2 what was documented; q3 findings versus allegations and unknowns; q4 accessible original sources; q5 agreement with latest deposited research status.

q1–q5 record the baseline assessment; before/after columns show the overall package rating. for compactness, **g = good**, **n = needs improvement**, **v = requires verification**. the overall rating is the most serious of the five. “after” evaluates the deposited package after the three entrance edits; it does not certify unresolved underlying research.

| subject | q1 | q2 | q3 | q4 | q5 | before | after |
|---|---|---|---|---|---|---|---|---|
| frogman wallet drain | n | n | g | g | g | needs improvement | needs improvement |
| zyrox token launch | n | n | g | g | g | needs improvement | needs improvement |
| gamdom incident | n | n | g | g | g | needs improvement | needs improvement |
| glitch token launch | g | g | g | g | g | good | good |
| binance incident reconstruction | n | n | g | g | g | needs improvement | needs improvement |
| exchange-attributed wallet transfers | g | g | g | g | g | good | good |
| gen z movements and institutional change | n | n | g | v | g | requires verification | requires verification |
| democratic representation and governing power | n | n | g | v | v | requires verification | requires verification |
| demographic change and electoral competition | n | n | g | g | g | needs improvement | needs improvement |
| norway: welfare buildings and public capacity | g | g | g | g | g | good | good |
| presidential claims and supporting evidence | n | v | v | v | v | requires verification | requires verification |
| netanyahu: un speech claim audit | g | g | g | v | g | requires verification | requires verification |
| tennessee execution protocol | n | n | g | g | g | needs improvement | needs improvement |
| ibrahim traoré: documented record and online claims | n | v | n | v | g | requires verification | requires verification |
| ai trading-performance narratives | g | g | g | g | g | good | good |
| gen z political participation: early framework | g | g | g | v | g | requires verification | requires verification |

post-edit totals: 4 good, 6 needs improvement, 6 requires verification. the three edited entrances are clearer; missing research provenance remains visible rather than being reclassified as solved. q5 for democratic representation and presidential claims is now good **at the entrance level**; historical inconsistencies remain in the package and are explicitly explained.

## concrete findings and recommended remedies

all paths below are relative to the repository root. recommendations are maintained here, outside the research folders. only the three entrance changes described later are implemented in this phase.

1. **frogman** — `research/frogman-wallet-drain/START_HERE.md` does not give a plain-language account of the latest scale or observation cutoff. `audit_2026_11_13/TECHNICAL_REPORT.md`, `ADDITIONAL_FINDINGS.md` and `LIMITATIONS.md` distinguish the original 35 accounts from one additional account and separate xmr1 exposure from native monero. add dated headline amounts and define wallet, bridge and xmr1 in the entrance. keep the extra account separate and the no-native-monero limitation. source receipts are reachable through the dated account audit; no numerical conflict identified in this review.

2. **zyrox** — `research/zyrox-investigation/START_HERE.md` gives little of the actual transaction finding. `report/ZYROX_Main_Report_v1_1_Verified.md` documents 17 sellers and 35 sales in its bounded window; gross traded tokens are not unique supply. the newer funding trail is separate from the 6 october baseline. add a dated two-stage summary and plain-language source links; do not convert a connected transaction structure into identified human control or proven liquidity removal.

3. **gamdom** — `research/gamdom/README.md` and `g015/loss_reconciliation.md` correctly separate a 34-movement selection from a proven loss total. the entrance still relies on terms such as payout attestation and wallet attribution. explain the incident and these terms, and foreground the source-assessment record. company and third-party dollar estimates are not an independently reconciled loss; ownership and authorization remain unresolved.

4. **glitch** — `research/glitch-investigation/README.md` provides a visual explanation, audit and direct original transaction anchor. the underlying control-attribution report bounds six source transfers, seven signers and one transaction, while rejecting an inference of identified human ownership. good against this editorial rubric; exact transaction identifiers remain technical by necessity. no finding was upgraded.

5. **binance** — `research/binance-incident/README.md` describes the guide rather than stating the bounded result. `visual-evidence/binance-2026/case-guide-start-to-2026-11-07.md` distinguishes independently checked selected transfers from reported incident-wide loss and official attribution. add the incident date, the checked-transfer scope and the 7 november cutoff to the entrance. the old branch-state sentence in `b017-weekly-developments-2026-11-01-to-07.md` is historical editorial context, not current research status; preserve it and explain its date if surfaced.

6. **exchange attribution** — `research/exchange-attribution/README.md` leads directly to the reconstruction and original bundles. `research/evidence/binance-v2.0-2026-10-14/README.md` distinguishes confirmed transfers from a supported exchange label. the documented four sol transfers total 472.929423997, with a separate 995.831502 usdt transfer; neither establishes a human owner or exchange account holder. `documentation-reconciliation.md` preserves the 0.000100 usdt distinction. good; do not silently promote an explorer label to official exchange confirmation.

7. **gen z movements** — `research/gen-z-movements-evidence-archive/START_HERE.md` should name the four country cases and latest dated outcomes. a deeper source-access gap is recorded by `DOCUMENT_LINK_MANIFEST.md`: some election outcomes rely on republished journalism, and the direct serbian election-commission result is not deposited. `CASE_FRANCE_2026.md` marks several broad findings confirmed while the accessible source trail does not supply item-level links for every such finding. restore claim-to-source mappings and verify source fit in a later research pass; do not infer that these outcomes are false. preserve the existing narrower euronews qualification and the unresolved accountability claims.

8. **democratic representation** — `research/democratic-representation-stress-test-2026/START_HERE.md` previously selected `PRE_SCORE_FREEZE_v1.0.md` and left certification apparently open. `PRE_SCORE_FREEZE_v1.1.md`, `AUDIT_LEDGER_v1.2.md` and `FINAL_TEMPORAL_SOURCE_AUDIT_v1.0.md` close the case design on 20 september, including swedish certification. the ledger explicitly says source-pack labels are not a final source register and leaves numerical fields blank. entrance corrected; the missing final source register and scored results remain a verification limitation. do not describe 90 eligible cases as 90 fully verified findings.

9. **demographic change** — `research/ddr-01/README.md` links the archived summary and cross-country ledger but does not state the main answer. `research/democratic-representation-stress-test-2026/DDR01_ARCHIVE_SUMMARY_v1.0.md` and `DDR01_CROSS_COUNTRY_LEDGER_v1.0.md` distinguish the country-specific mechanism from an unsupported universal left/right direction. add that result and the archive date to the entrance. preserve null, mixed and non-comparable cases and do not convert a descriptive contribution into a universal causal coefficient.

10. **norway welfare** — `research/norway-welfare-infrastructure-2001-2036/START_HERE.md` makes the evidence and model distinction accessible. `findings.md`, `methodology.md`, `deep-research-en.md` and the 4 november verification records separate a gross scope from a modelled incremental programme. nok 250 billion is a policy envelope; a provisional net sensitivity range is a different quantity. incomplete baseline subtraction and staffing constraints remain explicit. good; continue to distinguish modelled affordability from established need and infrastructure condition from educational causation.

11. **presidential claims** — `research/presidential-claim-stress-test-2025-2026/START_HERE.md` previously said that a 50-claim control and blind second pass were preserved without qualifying their reproducibility. the main `.xlsx` has 79 rows, 78 eligible, and 9/9/9/51 classifications: arithmetic agrees with the overview. however, `Inter-Rater Analysis` contains 78 comparisons and 64 accuracy agreements while `Publication Audit!C11:D11` says no independent scorer has run it / pending. `Blind Second Pass` and the separate blind template contain no completed second-pass scores. `Audit Summary!B9` still describes a future scorer; old 77-row and revised 78-row summaries coexist. 18 statement-url cells in column k are empty; benchmark urls are present but not all are primary documents. a 50-item control ledger was not located. obtain review provenance, the relationship between comparison results and blank templates, and the control-item dataset before independently certifying those analyses. no allegation about how results were produced follows from these gaps. entrance corrected without touching either workbook.

12. **netanyahu speech** — `research/netanyahu-unga-2026-claim-stress-test/findings.md` and `methodology.md` clearly retain 30 families, seven held and 23 adjudicable. however, `final-evidence-ledger.csv` has no direct urls and `source-notes.md` is a descriptive bibliography. some links are only in `article/medium-draft.md`; it is not a complete 30-row source map. add a separate claim-to-document register with dates, excerpts and scope, and verify its fit before treating every classification as independently reproducible. preserve held legal/counterfactual claims and distinctions between self-report, cause and measurement.

13. **tennessee** — `research/tennessee-execution-protocol-stress-test-2026/START_HERE.md` is abstract; it should state the narrow finding and 7 october cutoff. `protocol-analysis.md`, `sources.md` and `unresolved.md` preserve the difference between protocol wording, a party's request for admission, an unlocated written response and later medical hypotheses. an older question about who would lead the review is answered in a later dated update; explain chronology rather than delete it. primary court documents and state sources have direct links. no new medical or legal conclusion is made here.

14. **traoré** — `research/traore-narrative-audit-2026/START_HERE.md` previously omitted the deposited sample's reproducibility gap. `sample-summary.md` reports 28 + 50 + 50 observations and 32 main-sample clusters; `evidence-ledger.csv` instead contains 23 claim rows, without urls. these are different units, not a proven count contradiction. no item-level 128-observation list, coding sheet or cluster map was located in this subject's deposited files. references in `article/medium-draft.md` do not supply that mapping. entrance now separates reported assessments from what readers can inspect and links original policy and economic sources directly. preserving or recovering a sample-level source/coding register and checking verdict-to-source fit requires a later research pass. no new internet-wide prevalence or common-controller conclusion is justified.

15. **ai performance narratives** — `research/ai-performance-narrative-audit-2026/START_HERE.md` leads to frozen findings, methodology, source index, captures and limitations. `source-index.md` distinguishes primary captures from discovery indexes; `corrections.md` preserves narrowed wallet attribution. asset movement is not proof of the claimed autonomous trade or payout. missing exact primary asset data for provisional cases remains explicit. good against the rubric; archived does not close those limitations.

16. **early gen z framework** — `research/gcr-01/README.md` correctly labels this as an early archived framework and points to the fuller movement archive. `GCR01_RESEARCH_FRAME_v0.1.md` contains numerical ipu/oecd baselines and case assertions but no direct document urls or claim-source register. named organizations alone are insufficient to reproduce the specific baselines. attach dated primary citations in a future annotation, preserving the framework and its age-versus-generation uncertainty. do not present it as a completed cross-country test.

## why these three entrances were edited first

the democratic study directed readers to an obsolete checkpoint; the presidential entrance implied review/control documentation was preserved in a form that the deposited files do not substantiate; the traoré entrance did not disclose a central sample-provenance gap. these directly affect a reader's understanding of research completion and reproducibility. the other verification flags remain important but were not silently repaired through new research or edits to frozen records.

| entrance | before | after |
|---|---|---|
| democratic representation | version 1.0 checkpoint; “scoring and certification conditions ... remain applicable” | version 1.1 and ledger 1.2 first; later certification closure explained; blank scores and missing final source register explicit |
| presidential claims | “a separate 50-claim control and blind second pass are preserved” | reproduced 78-family counts; explicit 64/78 comparison versus blank-template/pending-status discrepancy; control-ledger gap and precise workbook navigation |
| traoré | generic frozen-findings and sample-summary links | distinguishes 23 claim rows from 128 reported sample observations; discloses missing item/cluster mapping; direct original-source links with self-report limits |

## practical reader navigation

these are reviewer walkthroughs, not tests with recruited participants. starting point is the repository homepage. the unchanged research-index link is one click; each subject entrance is the second. the edited entrances add no technical table and use short sections and descriptive links.

- non-specialist: two clicks to any edited entrance, then read the question, findings and limits without opening technical files. no download is needed for the summary.
- pupil: three clicks to democratic methods or traoré findings; three clicks to the presidential workbook, followed by a sheet selection. downloading/using a spreadsheet remains a real obstacle, now stated and explained rather than hidden.
- journalist: three clicks to the swedish official notice, the example presidential speech transcript or the original agriculture/imf sources. these are examples, not a claim that every underlying case now has an original-source link. the 90-case register, presidential control/review provenance and traoré sample mapping remain obstacles to full reproduction.

## preservation, status and validation

only the three `START_HERE.md` files above and new files under `archive-maintenance/` belong to this change. no move, deletion, registry/status edit, research conclusion change, workbook save or source acquisition was performed. historical overviews, all evidence, manifests, frozen reports, prior maintenance reports and correction logs remain byte-identical to the merged base.

see [technical validation](EDITORIAL_VALIDATION_2026-11-15.md) for exact scope, link counts, hashes, historical exceptions and public-branch checks. unresolved research provenance is not cured by passing navigation checks. the new pull request remains a draft and is not merged.
