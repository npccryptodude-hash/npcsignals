# Reproduction and scope

Run from any directory:

```bash
python research/glitch-investigation/scripts/analyze.py
python research/glitch-investigation/scripts/compare.py
python research/glitch-investigation/scripts/collect.py --output /tmp/glitch-recheck
```

`analyze.py` rebuilds CSV tables using raw integer amounts. It separates pool-to-seller WSOL receipts from pool fee destinations. A newly initialized or subsequently closed WSOL account is mapped to its owner using parsed initialize instructions; wallet SOL balance change is not substituted for sale receipts. Every selected receipt must have `meta.err == null`. Failed transactions, dust-only third-party account fan-outs and unrelated wallet activity are excluded.

`compare.py` compares complete addresses, not abbreviations, against `.md`, `.csv`, `.json` and `.jsonl` records under both read-only ZYROX paths. It reports corpus equality, not ownership. The 71 sampled actors include transaction signers and creator direct funders; the mint-account signer is not a human wallet. Common programs/pools/tip accounts must be interpreted separately. The reference commit is pinned in `data/comparison_scope.json`.

`collect.py` re-fetches only the already selected signatures, using finalized `getTransaction`, JSON-parsed encoding and maximum supported transaction version 1. Rate limits are retried with bounded backoff. It cannot reconstruct the 90-wallet historical FEYN classifier without an archived report.

Acquisition used finalized mint-address history pagination: 10 full pages of 1,000 signatures plus a final page of 873; the earliest record was then verified as an actual create instruction. A finalized creation block was fetched, with 1,492 transactions; only eight relevant successful economic receipts were selected. Whole-market histories and unrelated block transactions are not included in the research dataset. This acquisition is discovery coverage, not an exhaustive sell analysis. The initial version-0 block request failed because the block contained version-1 transactions; version 1 succeeded. Several creator-history receipt requests returned HTTP 429; missing unrelated/dust records were not silently treated as zero activity. Selected reported findings have successful receipts.

## Provenance

`raw/receipt_manifest.json` records receipt hashes and local save times; these save times are not transaction times. `raw/acquisition.json` identifies acquisition scope. Blockchain timestamps come from finalized `blockTime`, with slot/block order used where available. UTC to CEST is +2 hours for October 12. No millisecond precision is inferred.

The Jito per-transaction historical API returned the same bundle identifier for all five launch signatures; its bundle record has identical ordering, slot and timestamp. Bundle membership shows common ordered submission, not common signing-key ownership. Jito reports a 3,000,000-lamport tip and 671,721 CU. The selected receipts reconcile those metrics; no separate historical validator/leader identity verification was performed.

Original user screenshots were retrieved, inspected and hashed. Seven relevant public-claim screenshots are included. Market images containing position or trade overlays remain source-only; financial activity of the observer is excluded. Original social-message/post IDs were not recovered. OCR and pixels establish displayed content, not independently authenticated server records.

## Methodology availability

The standalone NPCsignals Methodology v2.0 document was not recovered: repository filename/content searches did not locate it, exact-title and alternate Library queries did not resolve it, and `npcsignals.com` retrieval was blocked. Do not interpret this checkpoint as a certified review against that unavailable complete document. The explicit standards in the research instruction and the latest ZYROX evidence guide/checkpoint were applied: distinguish observed data from scanner claims, record limitations, require exact signatures and calculations, avoid funding/control and receipts/profit conflation, and preserve negative findings.

## Numerical checks

- Creation supply: 1,000,000,000,000,000 raw units / 1,000,000 = 1,000,000,000 GLITCH.
- Creator funding: 10 × 240,469,594 lamports = 2,404,695,940 lamports = 2.404695940 SOL.
- First bundle: 789,999,999,999,972 raw token units / creation supply × 100 = 78.9999999999972%.
- Creation-block buys: 798,740,588,272,887 raw units = 79.8740588272887%.
- Collector sale: 594,968,303,379,290 raw units; receipt 132,890,991,957 lamports. Quote fee transfers are excluded.
- Pool reserve-ratio decrease: `100 * (1 - (8444240582 / 708656294139178) / (142680283066 / 113687990759888))` = 99.0505423933477%. The common decimal scaling cancels. This is not a USD-price series.

A complete market seller ranking, a historical FEYN reproduction, full initial buyer funding graph and final beneficiary accounting require a reviewed continuation.
