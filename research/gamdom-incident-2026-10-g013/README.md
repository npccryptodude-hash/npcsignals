# G013 — HOT deposit proof and OMFT payout attribution

16 October 2026. Starting checkpoint: `cc8262b6891648934a2114495c1542816cb51b53`. G005–G012 remain frozen. Medium and X: **HOLD**.

## New result

Both BNB settlement receivers subsequently called the actual HOT locker, `0x233c5370ccfb3cd7409d9a3fb98ab94de94cb4cd`. Two newly verified BNB transactions expose NewTransfer deposit nonces, canonical USDT amounts and receiver hashes. Each nonce, token, amount and receiver commitment matches its already documented NEAR deposit call exactly. The source contract's historical stored message hashes match independently reconstructed SHA-256/RLP messages, and both NEAR deposit attestations verify under the chain-56 public key returned by the historical HOT contract.

This establishes the selected **BNB→NEAR deposit linkage as CONFIRMED**, within the stated RPC/cryptographic evidence standard. It does not audit the MPC quorum, globally prove replay protection or identify an operator.

| Route | New BNB locker deposit | UTC, 13 October | Deposit nonce |
| --- | --- | --- | --- |
| 1 | `0x241cc0f33d586d99c2cf1d1382b09fc71129efef29069c5bbb92eb2f26a46123` | 16:45:06 | 1791909906000001324516 |
| 2 | `0xd64d7ef1322cbfa531f71e9dafa937682a0a060ec0de57980840fd4f4b0d4cdc` | 16:48:04 | 1791910084000001324521 |

The four existing NEAR execution trees are expanded with **24 new receipt-detail records**, including predecessors, signers, child relationships and the exact OMFT ft_transfer withdrawal actions. The OMFT service's own withdrawal_status endpoint, queried by the NEAR execution transaction hashes, independently returns the two exact Ethereum payout hashes and exact string-valued payout/fee amounts. Its responses corroborate G012's 1Click mappings. The services' backend independence is not established.

The Ethereum sender had empty code at both payout blocks and made ordinary DAI transfers. No signed payout instruction or shared on-chain withdrawal identifier was obtained. Consequently **both complete routes remain SUPPORTED**. The weakest edge is NEAR OMFT withdrawal→Ethereum treasury payment.

No new Gamdom ownership, compromised-key, common human operator or legitimate-consent finding is established. H1/H2/H3 remain UNRESOLVED. A completed financial route does not prove theft.

## Reproduction and integrity

Install `requirements.txt` in an isolated Python environment. Run `python analyse.py` and `python verify.py` from this directory or using their absolute paths. Frozen adjacent G012 data are required; no new API access is required for offline verification. `verification_results.json` records the observed verification result.

`acquisition_archive.json.gz` contains every attempted new request, success, failure and collection timestamp. It is deterministic gzip of normalized JSON. Later OMFT API responses also preserve exact raw response text; earlier parsed JSON records are not claimed to preserve HTTP whitespace. Binary WASM and source message/signature bytes are preserved losslessly through base64/hex. `source_register.json` names and SHA-256 hashes each canonical archive record; `SHA256SUMS.json` covers every published file except itself. `python replay.py /new/output/path` optionally repeats the read-only acquisitions into a separate directory. Mutable service responses and provider limits may differ.

See `cross_chain_proof_graph.md`, `attestation_verification.json`, `financial_reconciliation.md`, `coverage_report.md` and `blocker_report.md` for the exact limits. All **220 frozen files** are checked against the supplied starting commit.

NPCsignals documents. It does not judge. Evidence, not velocity.
