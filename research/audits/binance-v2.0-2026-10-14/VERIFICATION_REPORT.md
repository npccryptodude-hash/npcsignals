# NPCsignals Binance Evidence Package v2.0 — final verification audit

Audit date: 2026-10-14 UTC. Independently obtained public evidence; no fresh blockchain queries, attribution searches or provider contact. This report and its supporting audit files are separate from the frozen evidence directory. No original receipt, manifest, script or historical verification result is replaced.

## Result

**CONFIRMED:** All **384** evidence files in public commit `46f5f3df4e4e20de712c48105533cd99e7f3fc28` were individually retrieved without authentication over HTTPS, returned HTTP 200, and matched their committed Git blob IDs. All 383 root-manifest entries matched their SHA-256 values. The root manifest is the 384th file and is deliberately excluded from its own entry list. Every one of the 384 evidence files is byte-identical to the corresponding member of the supplied 390-member export ZIP.

**INDEPENDENTLY REPRODUCED:** The unmodified committed `verify.py` completed with exit 0 on Linux/POSIX and produced five PASS outputs. Each of the four original packaged verification scripts was also independently extracted and run separately with exit 0. Historical outputs remain unchanged and are not used as substitutes for these new executions.

**CONFIRMED PORTABILITY DEFECT:** Windows-style relative-path strings cause the original coverage comparison to fail. The in-memory Windows-path emulation reproduced `AssertionError: Manifest coverage mismatch`. This is not caused by exclusion of the root manifest from its own manifest. A separately proposed one-expression normalization passes the modelled coverage comparison and the complete checks on Linux. **Native Windows execution of the full corrected checks remains NOT ASSESSED.**

## Commit reference discrepancy

The requested short reference `465ff3d` returned GitHub HTTP 422, “No commit found for SHA”. The actual public main-branch archive commit was `46f5f3df4e4e20de712c48105533cd99e7f3fc28` (short `46f5f3d`). This audit pins all requests and checks to that full immutable SHA, rather than silently treating the supplied spelling as resolved. The interpretation that this was the intended commit is based on its main-branch position, the specified evidence directory, the 384-file inventory and exact match to the supplied ZIP.

Public evidence directory:
https://github.com/npccryptodude-hash/npcsignals/tree/46f5f3df4e4e20de712c48105533cd99e7f3fc28/research/evidence/binance-v2.0-2026-10-14

## Public accessibility and byte integrity

The Git tree inventory contained 384 blob entries beneath `research/evidence/binance-v2.0-2026-10-14/`. Each was downloaded using an anonymous request to its commit-pinned `raw.githubusercontent.com` URL; no credentials or signed-in session were used. For every response the audit recomputed the Git blob SHA-1 over the exact bytes and compared it to the published tree. It independently computed SHA-256 and checked the root manifest.

| Check | Independently observed result |
|---|---|
| Committed evidence files | 384 |
| Anonymous complete HTTP 200 downloads | 384/384 |
| Computed Git blob ID matches | 384/384 |
| Root SHA-256 manifest entries | 383 |
| SHA-256 entry mismatches | 0 |
| Manifest-referenced files missing | 0 |
| Unlisted files excluding root manifest | 0 |
| Byte matches to export ZIP evidence members | 384/384 |
| Evidence bytes changed during audit/replay | 0 |

The supplied export ZIP has SHA-256 `409f9397411e35e6d53a26f56ef93f029492e91d0c68c717538a185fe5f1b963`. It contains 390 member files, of which 384 belong to the audited evidence directory. This finding does not claim that the other six outer export members are present under that directory.

[public-file-access.json](public-file-access.json) records every commit-pinned URL, HTTP result, Git blob ID, byte size and SHA-256. [audit-results.json](audit-results.json) preserves new execution outputs, integrity diagnostics, emulation findings and per-file hashes. Public availability is a capture-time observation, not a promise of future hosting.

## SHA256SUMS.json and verify.py review

Root manifest SHA-256:
`8b6764ea14e52f682f2fcfa4244f93414dcd411152a5afef33ef500e0a6b1f8a`

Original verifier SHA-256:
`56ef79204924242f185463551e9f1f9c7ef3b78f9b6208332652d80b6352b60c`

The root manifest has no entry for `SHA256SUMS.json` itself. That exclusion is intentional: an ordinary manifest cannot practically include the digest of its own final bytes. The commit and independent ZIP comparison pin the root manifest bytes externally. The three nested package manifests **are** included in the root manifest and match their hashes:

- `originals/NPCsignals_56HE_Binance/SHA256SUMS.json`
- `originals/NPCsignals_Additional_Exchange_Transfers/SHA256SUMS.json`
- `originals/NPCsignals_Binance_U300/SHA256SUMS.json`

The original coverage lines are:

```python
actual={str(p.relative_to(P)) for p in P.rglob('*')
        if p.is_file() and p != P/'SHA256SUMS.json'}
assert actual == set(manifest), 'Manifest coverage mismatch'
```

On this clean POSIX download, `actual` and the manifest key set both contain 383 entries and are identical. The original unmodified script therefore passes its coverage assertion. Excluding only the root manifest is correct. Excluding every file named `SHA256SUMS.json` would incorrectly omit the three nested manifests; the pinned script does not make that mistake.

### Reproduced Windows separator mismatch

The manifest's nested keys use `/`. Python's native Windows path string representation uses `\`. A concrete example is:

```text
Expected: original_archives/NPCsignals_56HE_Binance_USDT_Disposition_Checkpoint_v1_0.zip
Windows:  original_archives\NPCsignals_56HE_Binance_USDT_Disposition_Checkpoint_v1_0.zip
```

Using `PureWindowsPath` to model the original expression gives **373 missing keys and 373 extra keys**, without changing any file or hash. Replacing only the coverage expression with Windows-path string semantics in memory triggers exactly `AssertionError: Manifest coverage mismatch`, before downstream checks run. Converting relative paths with `.as_posix()` makes the modelled sets equal.

This establishes a deterministic Windows portability defect and an explanation consistent with the reported error. The actual failing local PC tree, exact command, interpreter version and traceback were not inspected in this audit. Extra local files, missing files or a changed script can also trigger a coverage assertion. Their involvement in the originally reported failure remains **UNRESOLVED**. The public committed bytes do not show missing evidence or corruption.

## Historical results versus fresh independent replay

Historical `offline-verification-results.txt` and `original-verification-results.json` are preserved unchanged. Their PASS statements describe prior executions. New audit executions and their stdout/stderr are stored separately.

| Script/check | Historical record | This audit |
|---|---|---|
| NPCsignals_Binance_U300/verify.py in `NPCsignals_Binance_U300_Evidence_Package_v1_0.zip` | Historical PASS preserved | **PASS**, exit 0, independently run from anonymously downloaded ZIP |
| NPCsignals_Additional_Exchange_Transfers/verify.py in `NPCsignals_Additional_Binance_Transfers_2026-09-30_v1_0.zip` | Historical PASS preserved | **PASS**, exit 0, independently run from anonymously downloaded ZIP |
| NPCsignals_56HE_Binance/verify.py in `NPCsignals_56HE_Binance_USDT_Disposition_Checkpoint_v1_0.zip` | Historical PASS preserved | **PASS**, exit 0, independently run from anonymously downloaded ZIP |
| NPCsignals_U300/verify.py in `NPCsignals_U300_Binance_inbound_checkpoint_2026-10-14.zip` | Historical PASS preserved | **PASS**, exit 0, independently run from anonymously downloaded ZIP |
| Committed evidence-root `verify.py` | Historical five PASS lines preserved | **PASS**, exit 0; original source, Linux/POSIX |

The root verifier extracts and invokes the four packaged scripts and then completes its consolidated checks. Counting its five printed PASS lines is not five independent data sources. This audit additionally ran all four child scripts directly, separately from the root invocation, to distinguish the checks and isolate failures.

The replays check preserved response/status consistency, full signature fields, successful finalized status objects, receipt UTC and slots, zero-based instruction indices, amounts, relevant historical token-account owners, authority, signer/fee-payer fields and applicable native/token balance reconciliations. They reproduce **472.929423997 SOL** across four transfer rows and **995.831502 USDT** in the fifth, including the USDT flow/rent/fee treatment and supporting linkage checks. They verify the saved evidence, not the chain's present state.

## Separate proposed correction

Do not edit the frozen `verify.py`. The minimal proposed portability change is:

```diff
-actual={str(p.relative_to(P)) for p in P.rglob('*') if p.is_file() and p!=P/'SHA256SUMS.json'}
+actual={p.relative_to(P).as_posix() for p in P.rglob('*') if p.is_file() and p!=P/'SHA256SUMS.json'}
```

[verify_portable_proposed.py](verify_portable_proposed.py) is a separate wrapper. It requires the exact original verifier SHA-256, refuses Python `-O`, and executes the original source with precisely that one expression changed **in memory**. `__file__` still points to the original evidence-root verifier, so all original files, manifests, receipt checks and assertions remain part of the run. It does not replace or write any evidence file. Its output is labelled a proposed portable run, not an original-verifier result.

The proposed wrapper independently completed with exit 0 and five PASS outputs on Linux/POSIX. Its path-normalization logic passes the Windows-path coverage model. No full native Windows execution was performed. Do not upgrade this result into a claim that the complete Windows run has passed.

Run from a checkout, with the existing evidence left untouched:

```sh
python3 research/evidence/binance-v2.0-2026-10-14/verify.py
python3 research/audits/binance-v2.0-2026-10-14/verify_portable_proposed.py research/evidence/binance-v2.0-2026-10-14
```

On Windows use the installed Python launcher as appropriate. Keep audit files outside the evidence directory: adding unmanifested local files inside it correctly makes strict coverage fail. Do not disable assertions, remove the coverage test, add a self-hash entry, delete unexpected files without inspection, or rewrite a historical PASS record to obtain a passing result.

## Limitations and remaining uncertainties

- The two supplementary B→6hR7 and U326 original transport response/request objects remain unavailable. Preserved parsed objects and separately labelled replacement response/finality records are present and consistent; this audit did not reconstruct originals.
- Original full attribution HTML/notarized captures were not recovered in the prior package. Available targeted excerpts, titles, URLs and source records remain preserved.
- Fresh blockchain finality, raw wire transaction signature validation and cryptographic remote-provider authenticity were not assessed. A preserved finalized-status object is not a fresh query to a Solana node.
- Binance affiliation remains the package's **SUPPORTED** independent-label attribution. Historical custody confirmation, internal customer credit, customer identity and common human control remain **UNRESOLVED** and were not newly investigated.
- The original local failure's exact cause is not proven without its local path-set diagnostics. The Windows separator defect is independently reproduced; full native Windows execution remains **NOT ASSESSED**.
- Only the 384-file evidence directory at the audited commit was reviewed for this integrity finding. No unrelated research or frozen baseline was changed.

## Preservation and publication boundary

Every downloaded evidence file was hashed before and after all executions and remained unchanged. All 384 files also match the supplied ZIP evidence members. The original root verifier, nested scripts, manifests and historical results are not replaced. Publication adds only this separate report, audit JSON, public-access register and separately proposed wrapper under `research/audits/binance-v2.0-2026-10-14/`. Its resulting commit SHA is reported in the handoff after remote verification; the archived evidence subtree must remain identical to the audited commit.
