# Verification report

Offline checks hash historical factory WASM bytes to the captured on-chain code hash; confirm the same factory code hash at both snapshots; parse actual WASM export sections rather than search text alone; demonstrate current-source registry methods absent from historical exports; verify both historical MethodNotFound results; decode on-chain token source metadata and match its exact JSON inside historical token WASM; reconstruct both complete EIP-1559 envelopes, transaction hashes and recovered signing keys; exhaustively decode each 68-byte transfer input and its canonical DAI event; check package tarball SHA-512/SHA-256 integrity; and enforce full-route SUPPORTED classifications.

`verification_results.json` records the observed result. `verify.py` compares all 244 frozen G005–G013 files byte-for-byte to the starting commit, validates every canonical source hash and enforces manifest coverage. No previously completed source bridge proof is rerun. The new Ethereum signature work is counted as verification of existing transactions, not discovery of new transactions.

Limitations: no authenticated source-referenced OMFT payout signature, no historically authorized treasury signer set, no independent backend provenance, no deployed-source rebuild, no exhaustive alternative-withdrawal census, and no consensus/Merkle replay. Financial figures remain unchanged in frozen G013.

After publication the remote commit is fetched, every new file is byte-compared with the local package and offline verification is rerun in a separate checkout. Post-commit results are returned to the user, avoiding self-referential commit assertions in this report.
