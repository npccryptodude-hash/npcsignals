# editorial validation — 15 november 2026

## scope and preservation

base commit: `45682ee3879d20d703e04fe3e1d5a4fd96e939e8`.

- 6,504 base files are byte-identical to the merged base; exactly three existing files changed, all reader entrances.
- no base file was removed or moved. the registered 16 subjects, research statuses, homepage and research index are unchanged.
- the changed entrances are `research/democratic-representation-stress-test-2026/START_HERE.md`, `research/presidential-claim-stress-test-2025-2026/START_HERE.md` and `research/traore-narrative-audit-2026/START_HERE.md`.
- three new maintenance files contain the review, document/hash record and this validation. no original evidence, manifest, frozen report, historical correction or workbook changed.
- the [review record](EDITORIAL_REVIEW_RECORD.json) contains 89 central-document records across all 16 subjects, with sha-256 hashes. long documents were reviewed with emphasis on conclusions, methods, limitations and source references; this is not an assertion that every underlying evidence item was re-adjudicated.

## local navigation and integrity

`archive-maintenance/tools/audit_archive.py` was rerun against the worktree. all 16 registered entrances remain present and linked from the research index. its whole-archive results retain the known exceptions rather than making the test artificially green:

- 4,706 manifest comparisons: 4,703 matches and the same three accepted historical mismatches; no missing manifest targets;
- 763 local link targets checked; 40 unresolved local links, all in the same two frozen copied zyrox ledgers; no new unresolved local target;
- no removed baseline files and no unexpected changes to the original 6,469-file historical baseline.

the nonzero audit exit code is expected for those preserved exceptions. explanations and owner acceptance remain in [the historical exception review](HASH_EXCEPTION_REVIEW.json), [source-link alternatives](SOURCE_LINKS.md) and [the owner's acceptance record](OWNER_ACCEPTANCE.md). none was rewritten for this review.

## selected data checks

both presidential workbooks were opened read-only and never saved. the main ledger has 79 claim rows, one excluded, and 78 eligible classifications: 9 supported, 9 mixed, 9 unsupported and 51 false/severe. `Inter-Rater Analysis` contains 78 claim comparisons and 64 accuracy agreements. the unfilled blind scoring sheets and pending status notes were retained, not reconciled by editing. 18 statement-url cells are blank. the traoré ledger has 23 claim rows; its sample summary reports 28 + 50 + 50 observations. these are different units, and the missing observation/coding map remains explicitly unresolved.

## original-source link sample

five external links surfaced in the edited entrances were opened and their content checked on 15 november 2026:

| source | observed result | bounded role |
|---|---|---|
| swedish election authority, 19 september 2026 | readable official notice; date and certification passage present | explains why the later checkpoint closes the earlier pending condition |
| american presidency project, 4 march 2025 address | readable transcript with date and speech text | original statement for `L001`, not independent verification of accuracy |
| burkina faso government, agricultural equipment announcement | readable official article dated 6 may 2024 | government's account of equipment and inputs, not measured self-sufficiency |
| imf, 26 june 2026 review | readable assessment and financing review | economic context, not sole-leader causal attribution |
| dfrlab, 30 august 2024 research | readable original research article | third-party synthetic-content research, not control of all sampled narratives |

these are availability/content checks, not perpetual availability guarantees or exhaustive verification of every central citation in all 16 archives. no provider keys were tested, copied or rotated. existing provider-bearing source files remain unchanged.

## presentation and public branch

the edited entrances use short paragraphs, lists, descriptive links and no tables. the recorded click paths are reviewer walkthroughs, not recruited-user tests. no new physical iphone/safari test is claimed. the prior accepted mobile-width result remains historical and unchanged.

the public-branch check returned http 200 for all 31 tested github urls: the six changed/added files and their linked repository targets on the draft branch. the published git tree matched the locally validated tree exactly. main is not changed by this pull request. unresolved research provenance is detailed in [the editorial review](EDITORIAL_REVIEW_2026-11-15.md); link success and byte preservation do not resolve it.
