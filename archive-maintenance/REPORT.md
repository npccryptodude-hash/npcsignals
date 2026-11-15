# archive quality audit / 15 november 2026

[project home](../README.md) · [research archive](../research/INDEX.md)

**result: navigation and preservation improvements prepared; full acceptance remains blocked by declared pre-existing integrity exceptions and credential-ownership review.** this report does not claim a completely clean archive.

baseline: `75fcb4966e4c21590cce363fcff2d94641d41257`. work is on a separate branch. no research conclusions, raw evidence, original manifests or git history were rewritten.

## what changed

- replaced the conceptual homepage with the project identity, archive entrance and research principle.
- provided 16 subject entrances with purpose, documented scope, uncertainty, research status and evidence links. short lists avoid wide navigation tables on phones.
- grouped all gamdom checkpoints behind one case entrance and a readable checkpoint guide.
- connected zyrox’s later technical records to its main reader entrance. separated the binance incident from the exchange-attribution case.
- replaced opaque reader labels for the demographic study and early gen z framework while retaining original ids and filenames.
- corrected the norwegian welfare overview’s link to a nonexistent translated review file; it now opens the available english review.
- replaced one obsolete frogman work checklist with a dated research-status explanation and the later account audit.
- repaired the binance consistency checker’s requirement for removed editorial drafts. its financial assertions are unchanged; all 323 checks pass.
- added a separate gamdom compatibility runner and explicit row-order proposal without changing frozen scripts.

## complete mapping and preservation

all 6,469 baseline files were inventoried by path, size and sha-256 before larger changes. [baseline inventory](BASELINE_INVENTORY.csv) and [duplicate groups](DUPLICATE_GROUPS.csv) make the mapping inspectable. 262 groups share identical bytes; these include deliberate source copies, repeated observations and small common responses, not 262 proven redundant research documents. no duplicate evidence was deleted.

all baseline files remain at their paths. the only five edited baseline files are the homepage, research index, norwegian welfare navigation, frogman’s obsolete checklist and binance’s current consistency checker. every other baseline file is byte-identical. additions are reader guidance and maintenance material.

one reader entrance per subject does not require moving immutable technical bundles into a new folder. the existing `research/evidence/`, `research/audits/`, `research/authority-handover/`, zyrox post-freeze and `visual-evidence/` locations remain technical/source layers reached through the relevant subject. their names are no longer the main navigation vocabulary.

## research coverage and status

[the registry](research-registry.json) lists all 16 entrances. no subject was newly labelled completed. ongoing reconstruction, exploratory research, unfinished verification and dated archived reference states are distinguished.

the separate telenor–myanmar branch is linked explicitly without being merged or certified. older restructuring, glitch and visual-evidence branches were identified as separate working histories; their existence is not treated as additional current findings. projects mentioned outside this repository, including work not deposited here, have not been invented as archive folders.

## integrity checks

32 local `SHA256SUMS.json` manifests and the zyrox `SOURCE_INTEGRITY.json` were checked: **4,706 hash comparisons; 4,703 match and three pre-existing mismatches remain.** none is repaired by replacing a reference digest.

| location | observation | treatment |
| --- | --- | --- |
| zyrox main `README.md` | differs from the reader-document bytes in `SOURCE_INTEGRITY.json` | unchanged; separate current entrance provided |
| zyrox/glitch control-attribution `README.md` | differs from its frozen manifest entry | unchanged; disclosed to readers |
| frogman upstream explorer-label response | differs from the stored digest | unchanged; the existing november audit documents lf/crlf normalization, not a new authentic source capture |

all other declared entries match; this is not a claim that every original capture has a manifest or that a matching hash proves source authenticity. [frogman’s existing integrity explanation](../research/frogman-wallet-drain/audit_2026_11_13/integrity_exception.json) remains part of its evidence package.

## gamdom relocation and reproducibility

all ten checkpoint manifests match. the old scripts contain historical sibling paths and repository-depth assumptions. the new [verification guide](../research/gamdom/VERIFICATION.md) and compatibility runner reconstruct that layout only in temporary copies.

- nine of ten unmodified verifiers pass in that layout.
- G009’s original regeneration comparison is sensitive to filesystem iteration order for `upstream_routes.csv`.
- a separately labelled proposal compares that table’s complete records independently of row sequence, while keeping all other output bytes, original hashes and subsequent assertions checked. all ten pass in that mode.
- each verifier gets a fresh copy because historical verifiers can regenerate files. no collector, network replay or transaction is run.
- the preserved exchange-attribution package’s independent offline verifier also passes.

this validates saved data within the scripts’ scope, not consensus replay, human ownership, consent or a refreshed investigation.

## links and reader navigation

the baseline markdown scan found 41 missing local targets. one editable welfare link was fixed. forty links inside two manifest-covered source copies remain exactly as captured; the [source-link resolution guide](SOURCE_LINKS.md) supplies their existing canonical destinations. these exceptions are not hidden as passes.

all new subject entrances and their document targets are checked. workbook links retain exact filenames. [external availability results](EXTERNAL_LINKS.md) distinguish accessible pages, blocked sources, unavailable endpoints and dated 404 observations. rpc roots may require post requests; access denial is not proof that a source is false or deleted.

actual github desktop rendering and sampled case navigation were inspected. mobile-width rendering could not be executed in this environment and remains an acceptance item. details are recorded in [navigation validation](NAVIGATION_VALIDATION.md).

## internal material and historical provenance

current reader pages contain no ai continuation prompts, task assignments or next-session plans. the obsolete current frogman checklist was replaced with research status. a wider heading/text scan distinguished genuine work instructions from source documentation, legal referral records, methodological falsification requirements and version history.

some original dated glitch checkpoints contain research instructions from their creation. they remain historical source/checkpoint content, with their role explained by the new reader guides. changing those originals merely to remove old wording would obscure provenance; they no longer serve as the current entry points. documented limitations, rejected hypotheses, corrections and uncertain findings were not removed.

## sensitive-material review

pattern checks found provider access identifiers in historical acquisition material. whether they are intentionally public examples or account-bound credentials requires owner review. values have not been reproduced in this report, moved to a new public file or tested against a provider account. no private signing-key block or github-token pattern was found by the bounded scans, which included 381 zip members and five gzip bundles; that is not a guarantee that the complete git history contains no sensitive information.

if an identifier belongs to an account, revoke or rotate it first. an agreed redacted derivative must remain separate from the immutable original and its provenance. ordinary deletion would leave git history intact. any history rewrite requires separate approval.

## acceptance and review decisions

safe navigation and documentation changes are reviewable in the pull request. the branch should remain unmerged while full acceptance is requested: three pre-existing digest exceptions, provider-identifier ownership and mobile rendering acceptance are unresolved. selecting an authoritative reader-document revision, accepting a documented exception, rotating credentials or approving history treatment must be explicit decisions; this maintenance pass does not silently decide them.

no medium publication, website update, contact with subjects, fund transfer or history rewrite was performed.

## reproduce

```sh
python archive-maintenance/tools/audit_archive.py
python archive-maintenance/tools/verify_gamdom.py
python archive-maintenance/tools/verify_gamdom.py --row-order-proposal
python research/evidence/binance-v2.0-2026-10-14/verify.py
python visual-evidence/binance-2026/audit_archive.py
```

the general auditor deliberately exits nonzero for the preserved known exceptions. the unmodified gamdom mode also reports its G009 failure. the proposed mode is explicitly labelled. run without python optimization; do not repair a check by regenerating original manifests.
