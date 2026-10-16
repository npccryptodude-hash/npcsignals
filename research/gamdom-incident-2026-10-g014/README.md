# G014 — OMFT payout authorization boundary

16 October 2026. Starting checkpoint: `543c6435dbd0bf18e3049cf0cefcb868e7d37092`. All G005–G013 evidence remains unchanged. Medium and X: **HOLD**.

**Result: both complete routes remain SUPPORTED.** No authenticated OMFT instruction binding either NEAR withdrawal to its exact Ethereum payout was obtained. G013's confirmed BNB→NEAR deposit proofs are retained without rerunning that investigation.

Substantive new findings:

1. Historical OMFT token source metadata points to `near/intents` but supplies **no build commit**. Current source cannot be substituted for the historical deployment.
2. The repository's current PoA factory includes `record_withdrawal`, `update_withdrawal` and `get_withdrawal`. The actual historical `omft.near` factory WASM has **none of these exported methods**. Historical calls at both incident snapshots return MethodNotFound. The same factory code hash is observed at both snapshots. This closes a specific apparent on-chain-registry lead for the historical factory, not all possible archives or later records.
3. Both Ethereum transaction signatures are now independently reconstructed and verified. They authorize ordinary DAI transfers to B. Their fully decoded calldata has no separate NEAR withdrawal identifier or bridge instruction. Signer recovery proves the Ethereum signing key, not its historical OMFT payout authority or human consent.
4. Historical SDK-pinned public package artifacts were retrieved and SHA-512 integrity checked. The examined `withdrawal_status` client schema returns database-style source/destination mappings without a signature/attestation field. This is a bounded interface finding; backend independence and unpublished records remain unproved.

Second withdrawal action receipt, recovered from frozen G013: `96ktG3EwUqmz24aeen7ptcQLJfKrFdox8rsUF1kqHEwq`. It is not the second NEAR transaction hash or intent hash.

No new transaction identities or financial movements are added. Two existing Ethereum signatures receive new cryptographic verification. The historically absent factory registry and client-interface checks justify this bounded negative checkpoint. They do not justify extending the search indefinitely or promoting the routes.

## Reproduction

Install `requirements.txt`, then run `python analyse.py` and `python verify.py`. Both run offline against the new acquisition archive and adjacent frozen G012/G013 evidence. `historical_architecture_verification.json` contains exact WASM export tables and metadata; `payout_signature_verification.json` contains signing digests, r/s/parity, recovered keys and complete reconstructed signed envelopes; `payout_instruction_register.json` preserves null instructions and SUPPORTED classifications; `public_interface_audit.json` records pinned package schemas and integrity checks.

`acquisition_archive.json.gz` preserves new requests, exact HTTP bodies, binary artifacts and failures as deterministic normalized JSON. Binary artifacts remain lossless base64. `source_register.json` hashes each canonical record. `SHA256SUMS.json` hashes every published file except itself. `python replay.py /new/output/path` repeats read-only acquisitions without changing the original evidence. The complete 244-file frozen evidence set is compared against the starting commit.

Recommendation: close this bounded payout-proof search at the present evidence boundary and change investigative direction. Reopen it if a source-referenced signed payout instruction, historical registry or independently authenticated relayer archive becomes publicly available.

NPCsignals documents. It does not judge. Evidence, not velocity.
