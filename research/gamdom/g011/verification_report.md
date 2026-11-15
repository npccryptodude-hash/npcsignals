# Verification report

Run `python3 verify.py` after installing the pinned requirements. verification_results.json records the saved result. No network is required for offline verification.

The verifier deterministically derives seven JSON ledgers/reports from the parsed evidence archive, validates acquisition-record checksums, matches each selected receipt to transaction/header/hash position, checks success and event identity, decodes direct token transfers and approvals, reconstructs raw integer accounting, and compares eight reconciliation windows against archive state. It checks that each bridge block has only one returned canonical B event.

Fourteen new successful BNB transactions are verified: five direct funding transactions to B, two settlement transactions, two selected S1 source-history transactions, four permission transactions and one type-4 delegation transaction. Two existing bridge transactions are imported without being recounted. The new source receipts and complete raw metadata are accessible in the compressed archive by their named source-register entries.

Fourteen new envelopes plus two existing Ethereum envelopes used for the new A/S1 key comparison are reconstructed and keccak-matched. secp256k1 signatures recover the claimed senders; low-s checks are enforced. The one BNB authorization tuple is independently verified: chain 56, nonce 4, recovered B authority; outer nonce 3 and recovered B sender. Adjacent historical states confirm empty code then the corresponding EIP-7702 designator at the located block. No Ethereum G008 authorization is recreated or modified.

Two key funding receipts agree with another provider's block/status/index/log representation. Both successful archive URL forms are from NodeReal and are explicitly not counted as independent providers. RPC representations and signed bytes do not constitute a separately replayed consensus/state-root proof.

All 168 frozen tracked files in G005/G006/G008/G009/G010 are compared with the starting commit. The manifest covers only G011 published top-level files, excluding itself, evidence cache directories and __pycache__. The compressed archive preserves all 136 parsed acquisition records, including exact failed attempts. Local cache files remain intact.

Publication is complete only after the remote branch points to the actual new commit, all new files are byte-compared with that fetched commit, the diff adds only G011, and pinned GitHub files are independently read back. Final publication readback is reported separately after it occurs.
