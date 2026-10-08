# Frogman v0.2 checkpoint

English-language research checkpoint, 8 October 2026. Frozen v0.1 remains unchanged.

## Saved state before resumption

Inspected GitHub main at 29732dcb330bf04d30aede1b781756f0750865b4. This commit contains the frozen v0.1 package, English README and evidence inventory. No v0.2 files had been committed. The following recovered local work is now preserved as a checkpoint, rather than repeating the completed reconstruction.

## Completed evidence enrichments

Ledger F0103–F0112 adds evidence enrichments, not additional fund transfers. The binary finalized USDC conversion transaction contains two verifiable Ed25519 signatures: Grr9WnZdcetQywtFXog81UhqmnJyvFhb4AT3ipw44mZP and 69FnU8vszZSZF6DZCT6VHdsvm3DvvojDgbwqzHJ4cCFS. This CONFIRMED observation supersedes the v0.1 non-signer assertion; the frozen source remains untouched. Cosigning this RFQ does not establish common beneficial ownership. First-party Jupiter source identifies 61DFfeTKM7trxYcPQCM78bJ794ddZprZpAwAnLiwTpYH as the order engine.

The current Just a Backpack Token-2022 mint has 100 basis point transfer fees in both fee configurations (CONFIRMED current snapshot). Its explanation of the historical exact 1% debit-credit difference remains SUPPORTED, because historical extension state was not obtained.

The preserved receiving-wallet accounting reconciles native inflows of 13240.996153263 SOL to 13240.973780900 SOL deposited, 0.002050000 network fees, 0.013919200 new-account allocations and 0.006403163 remaining at the final incident receipt. Residual is exactly 0.000000000 SOL. This includes third-party dust and does not establish exclusive incident provenance. Privacy Cash withdrawal linkage remains broken.

## EVM investigation state

BSC JSON-RPC responds, with affected-address nonce 4 and candidate receiving-address nonce 34. Nonces and snapshots do not establish incident transfers. The eight-hour Transfer-log requests returned limit exceeded. Ethereum and Robinhood RPC attempts have access errors preserved. No EVM incident transaction, Relay deposit or corresponding fill has yet been independently reproduced. All reported EVM route amounts remain CLAIMED; the corresponding trace tests remain UNRESOLVED.

## Reproduction and limitations

New request/response records are in raw_sources. Run decode_and_verify_conversion.py with OpenSSL to verify the binary signatures. Run reconcile_accounting.py against the sibling frozen archive directory to reproduce accounting. build_update.py regenerates only this checkpoint ledger; do not run after appending later IDs. Source snapshots establish observed state at retrieval, not historical deployed bytecode equivalence. Some collection scripts retain investigative queries and are not comprehensive address-history scanners.

Next priority: acquire independent EVM transaction history and verify Relay request identifiers against both source deposits and destination fills. A protocol API label alone is insufficient for provenance continuity. No identity, compromise method, exchange freeze, recovery or ultimate beneficiary has been established.
