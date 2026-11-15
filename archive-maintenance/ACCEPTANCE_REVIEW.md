# pull request 3 / final acceptance review

15 november 2026 · [quality report](REPORT.md) · [navigation tests](NAVIGATION_VALIDATION.md)

**owner acceptance recorded: ready for merging with the documented historical exceptions. no merge has been performed.** the earlier unspecified credential and mobile-width blockers have been resolved within the scope below. the three original checksum mismatches remain visible; explained provenance is not converted into a clean original-manifest result.

review started at `c1de3499671fe9dd3275cae49dbeb42a101d8b58`. two reader-entry link improvements were added in `585e9a6045887e12d5e22591edf9640a62f44ce4`. the review continues in the same branch and pull request, without a new reorganization.

## acceptance ledger

| area | review result | acceptance meaning |
| --- | --- | --- |
| provider identifiers | both exactly match provider-published shareable demonstration keys | no unresolved private-credential finding among the two flagged values; live validity not tested |
| zyrox main readme digest | manifest-matching version recovered from a pinned commit; three later readme revisions traced | historical reader-document drift, not changed frozen data; requires explicit acceptance of snapshot scope |
| control-attribution digest and coverage | original 63-file snapshot reproduces and its original verifier passes; later introduction and two visual files traced | old manifest describes its original snapshot, not the expanded current folder |
| frogman label response | exact expected digest reproduced by 7,158 lf→crlf substitutions in a disposable copy | byte-format discrepancy explained; no new claim of capture authenticity or original transport-byte recovery |
| mobile-width rendering | homepage, index and eight representative subjects pass at measured 340/454 css pixels | narrow-width reflow test, not physical iphone/safari certification |
| three reader perspectives | actual navigation walkthroughs completed and counted | agent-performed acceptance test, not a human-participant usability study |
| preservation | original evidence paths, hashes and frozen records retained | no original-material deletion, checksum replacement, merge or history rewrite |

## provider findings and owner decision

see [the redacted provider review](PROVIDER_IDENTIFIER_REVIEW.md) for the ten exact affected files and opaque identifiers. nodereal’s official public api overview explicitly publishes both values as shareable demonstration access; the first appears in its ethereum-mainnet row and the second in its bsc/opbnb rows. original code’s hostname usage is recorded separately from that public-document context.

no key was submitted to an rpc provider, tested for activity, revoked or rotated. public availability of an arbitrary string would not suffice; exact equality with the provider’s explicitly shareable table resolves these particular flags.

**owner decision recommended:** retain the public demo values as frozen acquisition provenance. if the owner has contradictory account-specific evidence, stop approval and authorize safe account-side treatment first. no current evidence from this review requires rotation of an owner’s private key.

## checksum exception 1 / zyrox main readme

manifest: `research/zyrox-investigation/SOURCE_INTEGRITY.json`.

| version | commit | bytes | relationship |
| --- | --- | ---: | --- |
| frozen reference | `049ca4889861fce989e2efe96e4c0d4538b4aa8c` | 2,273 | exact expected sha-256 |
| later status edit | `6f5e17d265ea45edffb78a89a80b844a69760a42` | 2,392 | ongoing-investigation status added |
| later investigation summary | `9ec50006c26411295fda65b710d4880cdec5cda3` | 3,500 | post-freeze findings summarized |
| current readme | `1ebc01f4dddd6350990750b8ca8b76408a449297` | 4,190 | summary updated to v0.121 |

[open the exact frozen readme](https://github.com/npccryptodude-hash/npcsignals/blob/049ca4889861fce989e2efe96e4c0d4538b4aa8c/research/zyrox-investigation/README.md).

the current-versus-frozen diff adds work status and a later launch-funding summary. the earlier report, mint, frozen v0.114/U453 basis and existing evidence discussion remain. the new summary is associated with later funding/fingerprint checkpoints, including [v0.121](../research/zyrox-investigation-post-freeze/ZYROX_BZ9m_Service_Boundary_v0_121.md); it is not part of the original frozen report. public-key structure and human attribution remain explicitly distinct.

**effect:** 22 of the 23 listed current files match. using the exact original readme in a disposable reconstruction yields 23/23 matches. the mismatch prevents certifying the present readme as the frozen version; it does not establish alteration of the other declared source files. the new `START_HERE.md` is a later navigation overlay, not an original manifest entry.

**recommended acceptance:** retain both versions through their existing git history and explicitly treat the original manifest as a dated snapshot. do not replace its digest with the current readme’s digest.

## checksum exception 2 / control-attribution readme

manifest: `research/zyrox-investigation-post-freeze/control-attribution-2026-10-14/SHA256SUMS.json`.

| version | commit | bytes | relationship |
| --- | --- | ---: | --- |
| original readme and manifest | `5259354b80c5c8f37cba4fb2b179bf44e6141a2e` | 10,326 | exact expected sha-256 |
| current readme | `470e8589bafde7f84a57d078e77f2294d76f0db8` | 11,230 | 904 bytes of visual/educational navigation added |

[open the exact original snapshot](https://github.com/npccryptodude-hash/npcsignals/tree/5259354b80c5c8f37cba4fb2b179bf44e6141a2e/research/zyrox-investigation-post-freeze/control-attribution-2026-10-14).

the diff adds the visual-story introduction, its existing html companion and the original medium link. the original executive findings and technical body are unchanged.

**additional scope finding:** the current folder has 65 files excluding the manifest, while the frozen manifest lists 63. the two extra files are `VISUAL_STORY.md` (added in `a8cf3f9b9b8a8ebd1e65604d3bcb050c897ae6f5`) and `story.html` (added in `18f769c0ce64ffe5ab33c1679be0f14ba39941fd`). neither extra file replaces an original receipt. therefore the original current-folder verifier also encounters a coverage difference, not merely a readme digest difference.

62 of the original 63 entries still match. reconstructing the original files directly from commit `5259354…` in a temporary directory produces an **unmodified-verifier exit code of 0**: manifest completeness, 11 receipts, fee conservation, ledger rows, token reconciliation, history scope and bounded key comparison pass.

**recommended acceptance:** preserve the original 63-file snapshot as the reproducible technical reference, and treat the readme introduction plus two later visual files as dated presentation additions. do not present the expanded current folder as the unchanged original snapshot or edit its manifest to imply that it was.

## checksum exception 3 / frogman explorer-label response

file: `research/frogman-wallet-drain/v0.2/inbound_sender_attribution_2026_10_10/access/explorer_label.response.txt`.

only one content version was found in the reachable history of this path: commit `554963adad68fffab14595885584a7d772542c24`, 841,345 bytes. no exact expected-digest original was recovered from that git path’s content history.

the committed file has 7,158 lf bytes and zero crlf pairs. replacing only those lf endings with crlf in memory produces 848,503 bytes and **exactly** the manifest’s expected digest. the content lines are otherwise unchanged. the already preserved november normalization derivative has the same expected digest.

the original upstream verifier was run in an isolated copy with that one line-ending reconstruction and the required earlier timeline input. it exits 0. the public source, original manifest and existing derivative were not changed.

**effect:** this explains the byte mismatch; it does not recover or authenticate the original http transport, prove when conversion occurred or independently authenticate the explorer label. current findings do not newly rely on this label. the [existing integrity exception](../research/frogman-wallet-drain/audit_2026_11_13/integrity_exception.json) remains applicable.

**recommended acceptance:** retain the original committed lf file, historical manifest and separately labelled reconstruction, with the precise normalization limitation. never call the reconstructed file a newly recovered original capture.

## mobile and reader results

[the test log](NAVIGATION_VALIDATION.md) records 25 live-page observations, including retests. sampled entrances had no tables and no horizontal article overflow at either width. homepage identity and the research index remained readable. all 16 entrances remain in the registry and their local targets are checked.

successful practical routes:

- nontechnical reader: gamdom scope and uncertainty in 2 content-link activations; detailed loss explanation in 3 after the added direct link.
- school reader: norway findings in 3; original ministry chapter reached in the combined findings-and-sources session after 6 content-link activations, 1 browser-back action and 1 cookie choice.
- journalist: preserved original glitch transaction response in 3 after a direct link was added. the slot and signature-bearing response is accessible in github’s read-only source view; its minified format remains a technical-source limitation.

## owner decisions and merge boundary

**no unclassified technical blocker remains within this review’s scope.** the owner has now explicitly accepted the three historical checksum exceptions and the responsive-width test, and conditionally accepted retention of the two public nodereal demo keys. see [owner acceptance](OWNER_ACCEPTANCE.md).

1. accepted by the owner: the three fully described historical exceptions, including the control package’s expanded presentation layer, without requiring original manifests to certify later reader material.
2. conditionally accepted by the owner: preservation of the provider-published public demonstration values, provided no private-account information contradicts the public-demo classification. contradictory private-account information would reopen a security blocker and require separate authorization before any key action.
3. accepted by the owner: the documented narrow-width test scope; physical-device/safari and recruited-human tests were not performed and are not claimed.

actual merging into main remains separately unauthorized. marking this pull request ready is not permission to merge or enable auto-merge.

the strict original hash audit still reports its three mismatches by design. an explained historical exception is not a green original checksum test. no evidence was deleted, original checksum updated, git history rewritten, website changed or pull request merged.

[full version metadata and isolated reproduction results](HASH_EXCEPTION_REVIEW.json) preserve exact hashes, commit ids and test outcomes without copying source captures.
