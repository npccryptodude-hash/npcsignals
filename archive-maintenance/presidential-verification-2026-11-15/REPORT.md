# presidential claims: evidence verification

review date: 15 november 2026. base: `1abf5eb64d75d285f25cef8998ca3c7b86415d34`. research status remains **under verification**. document, not judge.

## answer

the deposited classifications and comparison statistics can be independently recalculated. the historical claim that these comparisons came from a completed, independent blind review cannot be established from the deposited material. the 50-item control dataset was not located in the searched repository material, so its reported distribution and the substantive high-salience/control comparison remain unverified.

new transcript annotations supply dated claim-family occurrences for 11 of the 18 rows with empty statement-url cells. three other rows have related passages that do not resolve the original claim. four still lack a matching original statement. none of these annotations fills a frozen cell, selects an undocumented historical scoring event, changes a classification or establishes the truth of a statement.

all 78 eligible records now have a machine-readable verification entry. the full accuracy distribution has **not** been independently re-adjudicated against primary evidence. one narrow existing finding, `L055` under the conventional percentage-reduction interpretation, is independently reproducible from a matching transcript and elementary arithmetic. that bounded result does not verify a whole drug-pricing programme or intent.

## deliverables and status meanings

- [claim-level matrix, json](verification-matrix.json): all 78 eligible records, original cell locations, recorded classifications, source roles, access results, comparison values, annotation pointers and limitations. `L053` is retained separately as the original exclusion.
- [claim-level matrix, csv](verification-matrix.csv): the same 78 records for filtering and reuse.
- [primary-source annotations](primary-sources.json): urls, event/publication dates where established, passage locators, short excerpts or paraphrases and limitations. existing references and newly located references are distinguished.
- [reproduced statistics](reproduced-metrics.json) and [read-only reproduction script](reproduce.py).
- [repository search and provenance](provenance-and-search.json) and [source-access checks](source-access.json).
- [issue register](issues.json): each finding or open question has one of the four requested verification labels.

**verified from existing evidence** means a fact about the deposited record is directly inspectable. **independently reproduced** means a stated calculation or bounded documentary result was reconstructed in this phase. **requires additional evidence** means the missing document, definition or record is identifiable. **unresolved** means the available evidence does not settle the historical explanation or attribution.

labels apply to their named dimension. a matrix row can have independently reproduced counting, an inspectable classification, and an unresolved review provenance at the same time. these labels do not replace research verdicts or change research status.

## complete archive read and search coverage

the existing subject contains four markdown documents and two workbooks. all were read, including the separately bounded 15-claim un speech supplement. every sheet in the seven-sheet main workbook and two-sheet blind workbook was extracted read-only. summaries, scoring definitions, input packets, claim records, comparisons and disagreement rows were examined. the complete phase 2 editorial review was also read. file hashes are recorded in the provenance file.

the core dataset ends on 3 september 2026. the 22 september speech supplement remains separate and does not enter any 78-family calculation. its existence is not a substitute for missing core evidence.

for the control search, all remote branches covered by the repository's normal fetch mapping were fetched. the clone is not shallow. the search covered 8,123 reachable named objects and 6,138 text-like, workbook or compressed blob versions, including 404 archive members. it inspected historical filenames, workbook xml, text references, nested zip members and gzip payloads. the two presidential workbook contents are the only presidential workbook blobs found; the rename did not create another scoring version.

matches outside this subject were inspected as search leads. none supplied a 50-item control ledger. the visible control material consists of aggregate descriptions and percentages in the overview, changelog and workbook summaries. no claim list, mechanical selection record, speech sampling frame, original row scores or control source register was located. the search does not cover private files, unpushed work, dangling objects or inaccessible history. it therefore does not establish that a control dataset never existed.

## reproduced classifications and statistics

`Public Ledger v1.0!W2:W80` is the current recorded accuracy field. column f preserves earlier assessments and must not be counted as the current harmonized classification. one row, `L053`, is excluded for its partly predictive/claim-definition problem.

| calculation | independently recalculated result | interpretation |
|---|---|---|
| raw / eligible rows | 79 / 78 | original exclusion preserved |
| supported | 9/78, 11.5% | recorded classifications, not new factual verdicts |
| mixed or misleading | 9/78, 11.5% | same limitation |
| unsupported | 9/78, 11.5% | not automatically false |
| false or severe | 51/78, 65.4% | same limitation |
| stored second-column classifications | 9 pass, 10 mixed, 4 unsupported, 55 false | provenance unresolved |
| accuracy exact agreement | 64/78, 82.1% | 14 disagreements |
| accuracy cohen's kappa | 0.64453125, rounds to 0.645 | conditional on the two stored columns |
| reconstructed amplification score at least 2 / at least 3 | 55/78 / 28/78 | 70.5% / 35.9% |
| amplification exact agreement | 46/78, 59.0% | scorer independence not established |
| amplification threshold agreement at 2 / at 3 | 64/78 / 60/78 | matches the recorded summary |
| amplification linear weighted kappa | 0.4778866842, rounds to 0.478 | matches the recorded summary |
| comparable persistence rows | 24 | 54 first-column scores are unassigned |
| persistence exact / threshold agreement | 12/24 / 21/24 | 50.0% / 87.5%; not global reliability |
| persistence kappa on comparable rows | 0.1627906977 | matches the rounded 0.163 |
| documented persistence / persistent-amplification floors | 24 / 21 | inspectable stored assignments, not an exhaustive repeat-search |

all first-column comparison accuracy, amplification and persistence values match the current main ledger after the documented accuracy-label normalization. agreement labels and deltas were recalculated rather than accepted as formulas. the workbook contains no formula cells: the numbers and summaries are stored values. the supplied standard-library script reconstructs them from the original xml and cross-checks matrix fields without saving a workbook.

older 77-row amplification summaries, original 79-row publication percentages and later 78-row reconstructions coexist. their presence is a version-layering limitation, not permission to choose whichever result is convenient. the changelog explicitly states that the original per-row amplification assignments were not retained and that the later rubric is a reconstruction. this phase reproduces the later stored reconstruction, not the missing original scoring process.

the reported 2.18 ratio is arithmetically reproducible **only conditional on** accepting the reported 30% control rate: `(51/78)/0.30 = 2.179487...`. no missing control rows or scores were reconstructed from aggregate percentages. neither the control distribution nor a sampling-based comparison has been independently reproduced.

## comparison provenance and blind-review discrepancy

the first main workbook upload is commit `91295bc938e93c94da61b8e7d24d2fd4a6ed1aa7`, recorded at 16:10:51 +02:00 on 3 september 2026. its original filename was `NPCsignals_Trump_Claim_Ledger_v1_0_INTER_RATER_AUDIT (1).xlsx`. commit `50490d6` renamed it. the current workbook is byte-identical to that first upload, with sha-256 `2ff8be2c756ddc73f0c7ce24ab9afdf59f2e2b5158404347c5766db949671222`.

therefore, the populated comparison table, empty embedded blind scores and pending review note already coexisted at deposit. this discrepancy was not introduced by the archive restructuring. the overview's completed-review assertion was already present in the earlier `9eb38da` upload at 16:05:23 +02:00. chronology locates the assertions and file deposit; it does not authenticate the review they describe.

specific records:

- `Inter-Rater Analysis` contains 78 comparisons and 64 accuracy agreements.
- `Blind Second Pass` contains 79 claim rows, including the later-excluded row, with no completed second-scoring output cells.
- the separate `Blind Claims` packet contains the 78 eligible rows, also with no completed output scores.
- `Publication Audit!C11:D11` says no independent scorer has run it and marks the step pending.
- `Audit Summary!B9` describes a future independent scorer.
- the overview and changelog instead say a separate scorer completed a blind pass.

one packet-version difference can now be specified: the embedded blind row for `L042` has older normalized wording and lacks its later date, quote, statement url, benchmark and benchmark url. the separate 78-row packet matches the current main ledger's eight claim/evidence input fields for every eligible row. this establishes a version difference; it does not establish which packet, if either, was actually scored.

there is no deposited completed independent response packet, named scorer, review attestation, session record or evidence establishing what the scorer could see. the upload author is not evidence of reviewer identity. the packages contain no core-properties author record or reviewer comments, and their internal zip timestamps have unspecified timezones. no reviewer identity or scoring chronology is inferred from those timestamps.

possible explanations include a stale status note after a genuine review or a comparison table whose historical review process is undocumented. the repository does not choose between them. provenance of the deposited **file** is verified; provenance and independence of the **scoring activity** remain unresolved.

## review of all 18 missing statement urls

the table records annotations, not replacement values. source identifiers resolve to the separate primary-source register. “dated family occurrence” confirms that a materially matching formulation can be located; where the original date was blank, it does not identify the occurrence originally selected by the researcher.

| claim | outcome | source / date | remaining distinction |
|---|---|---|---|
| `L012` | dated family occurrence located | `P001`, 4 march 2025; already referenced elsewhere in the workbook | crossing/apprehension measure and original selected event remain unspecified |
| `L014` | dated family occurrence located | `P003`, 17 december 2025 | states versus individual places and state averages require care |
| `L015` | dated family occurrence located | `P003`, 17 december 2025 | conflict definition and claimed contribution remain unaudited |
| `L016` | dated family occurrence located | `P004`, 21 june 2025 | assertion is not independent physical-damage evidence |
| `L018` | dated family occurrence located | `P003`, 17 december 2025; `P002` is an already cited 2026 repeat | commitments versus realized investment; original event not identified |
| `L019` | dated family occurrence located | `P003`, 17 december 2025 | basket, reference period and price level versus inflation unresolved |
| `L022` | related passage only | `P003`, 17 december 2025 | predicts electricity-price declines rather than establishing a past-tense claim |
| `L023` | dated family occurrence located | `P005`, 2 december 2025 | a commercial transcript reproduction; production series and policy cause separate |
| `L027` | dated family occurrence located | `P006`, 21 january 2026 | inflation measure and original selected occurrence not fixed |
| `L041` | existing date and core wording matched | `P007`, 4 august 2026, 00:06:03–00:06:26 | transcript reproduction, not a fox-hosted recording; revenue not audited |
| `L061` | no matching original statement located | none accepted | historical percentage, geography and reference period still missing |
| `L068` | dated family occurrence located | `P008`, 4 may 2026 | confidence series and comparison window remain unspecified |
| `L070` | dated family occurrence located | `P009`, 8 july 2026 | appears to overlap the assertion already represented by `L069` |
| `L071` | no matching original statement located | none accepted | later treasury commentary is not the frozen presidential occurrence |
| `L072` | no matching original statement located | none accepted | september 4 and october releases fall after the core freeze |
| `L073` | no matching original statement located | none accepted | policy orders or admissions statistics do not supply the missing utterance |
| `L075` | related institutional statement only | `P010`, published 3 june 2026 | white house statement does not establish the original presidential speaker/event |
| `L076` | related passage only | `P009`, 8 july 2026 | housing/rent costs are not a defined home-sale-price measure |

`L028` is a separate date gap: its statement url was already present, but its date cell was blank. the cited transcript supplies 24 february 2026 as a date candidate, recorded separately. no original date field was changed.

`L055` has a dated statement already recorded in the workbook. the newly located `P003` transcript corroborates the formulation, and a reduction of a positive price by more than 100% would imply a negative price under the conventional formula `new = old × (1 − reduction/100)`. this independently reproduces the existing narrow mathematical assessment. it does not measure actual discounts, resolve every alternative rhetorical percentage base or authorize a new classification.

## primary records, secondary reporting and unsupported references

among the 78 eligible statement fields, 23 point to reproduced primary speech/interview transcripts, one points to a primary white house release containing an attributed quote, 36 point to secondary reporting, and 18 are empty. a publisher name is not an evidence grade: a speech transcript is primary for what was said, not for whether it was accurate.

all original benchmark-url fields point to secondary reporting. their articles may cite primary data, but those pointers are not themselves deposited agency datasets, historical table snapshots, legal texts or calculations. the workbook's `Source-verified` label is retained as an original label, not adopted as a new verification result.

45 distinct original statement/benchmark urls were probed. 44 returned http 200 with relevant page titles. the reuters benchmark for `L079` returned http 401. these are access checks, not a full reading or truth validation of all linked articles; a successful response does not prove an article supports the full normalized claim. the 401 is an access limitation, not evidence of falsity. no access control was bypassed.

new source `P011` adds an official energy-statistics publication for record annual production. it narrows the benchmark-source gap for `L023` and `L078`, but does not reproduce the underlying historical series or demonstrate a president's causal effect. sources found after the core freeze, including later manufacturing releases, are not used to backfill original statement occurrences.

## additional definition and chronology issues

- `L029`, `L038` and `L044` have a recorded year of 2026 but explicit dates in 2025. these fields are preserved; year-based subgroup results require clarification.
- `L020` uses a future tax-cut pledge dated 29 april 2025 to represent an enacted-law claim. `L056` also references a pre-enactment bill discussion. bill version, tense and comparison date matter.
- `L069` and `L070` appear to represent the same rental-cost assertion. `L012`/`L061` and `L023`/`L078` also warrant a documented family-boundary explanation. this is a deduplication question, not a newly calculated denominator. 78 remains the deposited denominator.
- `L074` normalizes an economic superlative into a specific comparison with the previous administration. the exact metric and interpretation need supporting documentation.
- for undated `L068` and `L076`, the period of the supplied benchmark is not automatically the period of the statement. subsequent lows or a two-year price increase cannot alone decide an unspecified short-term assertion.
- the 24 persistence and 21 persistent-amplification counts are floors of stored assignments. the underlying recurrence search and date of publicly available corrective evidence were not exhaustively reproduced.

these issues are documented in individual matrix limitations and the issue register. no row was deleted, reclassified or silently corrected.

## reproducibility conclusion

**reproducible now:** stored 78-family classification totals, comparison-column distributions, agreement counts and rounded kappas, later amplification-score aggregates, partial persistence arithmetic and the narrow percentage-reduction example. a reader can run the supplied script without network access to verify the stored calculations.

**partly resolved:** primary-source access for 11 previously unlinked claim families, one additional date candidate, a concrete blind-packet version difference, and the file-level history of the comparison results.

**not established:** original 50-item control selection and scoring, historical reviewer identity/independence/blindness, every original selected occurrence for undated rows, full claim-to-primary-benchmark reproduction, final persistence rates, causal interpretations and a justified deduplicated family denominator. the full published research conclusions cannot be certified as independently reproducible from the deposited evidence. this is a limit of the accessible documentation, not a finding that all conclusions are wrong.

## preservation and technical validation

the branch adds only this phase's files under `archive-maintenance/presidential-verification-2026-11-15/`. no existing file, workbook, source, conclusion, historical correction, research status or integrity manifest is modified. input hashes and current-field cross-checks are supplied with the reproduction results. all 6,510 existing base files remain byte-identical. the archive check covers 771 local link targets and 4,706 manifest comparisons, retaining the three previously accepted checksum mismatches and 40 frozen copied-ledger link exceptions. no new local link or manifest exception was found. no history rewrite, website change, article publication, contact or merge is part of this work.
