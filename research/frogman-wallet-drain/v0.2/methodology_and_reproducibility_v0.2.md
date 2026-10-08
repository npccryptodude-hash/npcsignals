# Methodology and reproduction

## Evidence labels

CONFIRMED: directly reproduced from reliable primary evidence. SUPPORTED: credible evidence but not fully reproduced. CLAIMED: public assertion not independently established. UNRESOLVED: insufficient evidence. NOT ESTABLISHED: a specific proposition has not been demonstrated in the examined evidence.

Labels apply to narrow propositions, not to all statements about a wallet. Token movement, transaction sender, affected-person linkage, protocol identity, destination fill, ownership, beneficiary and compromise vector are separate propositions.

## Reproduction

Clone the repository and change to research/frogman-wallet-drain/v0.2. Use Python 3, OpenSSL, and pycryptodome for Keccak-256 (`python -m pip install pycryptodome`). Do not replace Keccak with standardized SHA3-256.

1. `python decode_and_verify_conversion.py`: decode preserved Solana binary signers and verify Ed25519 signatures.
2. `python reconcile_accounting.py`: recompute Solana accounting from sibling frozen CSVs without changing them.
3. `python build_eth_ledger.py`: reproduce F0113–F0127 from preserved Ethereum transactions, receipts and blocks.
4. `python verify_relay_pairs.py`: reproduce six exact source deposit/fill matches, including the batched mint fill, event-derived token origin and transaction executor.
5. `python build_expanded_record.py`: reproduce F0128–F0186 and corresponding graph/wallet records.
6. `python verify_chain_extensions.py`: reproduce F0187–F0206, exact Robinhood source transfers and Arbitrum consolidation; exclude zero-value events from monetary totals.

Collection scripts perform read-only public RPC/API requests. They can yield different latest-state snapshots or access errors on rerun. `resume_evm.py` appends attempt suffixes rather than overwriting previously preserved request/response records. Some older collection scripts predate append-only naming: do not rerun those over frozen records. `build_update.py` regenerates only F0103–F0112; do not treat it as a complete ledger builder.

## Exact scope

Robinhood first-window Transfer search: first block at or after 2026-10-06T20:10:00Z (81901837) through the block before 2026-10-06T21:10:00Z (81936936), sender topics for the affected and receiving addresses; split into provider-accepted ranges. Does not search earlier native transactions or approvals. Historical nonce queries failed because state was unavailable. Current nonces are not incident chronology.

Arbitrum USDC onward search: contract 0xaf88d065e77c8cc2239327c5edb3a432268e5831, sender topics for the six matched Relay recipients, blocks 512422000–512820654 inclusive, split into four ranges. It covers that token and those senders only, not all assets or all addresses. Zero-value events are retained, not counted as funds and not treated as authorization by Transfer.from.

Ethereum ordinary-address pagination and internal index results are preserved. Positive native movements in new ledgers were cross-checked using RPC transaction/receipt/block records or successful execution traces. Index completeness, unrelated dust and affected-person attribution are not inferred solely from pagination ending.

## Precision and accounting

Amounts derive from integer token units/wei/lamports and Decimal arithmetic. No binary floating-point accounting. Metadata decimals were queried and the snapshot records retained. Historical mutable metadata is not assumed proven merely by a current query. Prices/slippage are absent unless backed by contemporaneous evidence; USDC quantities are not substituted for USD valuations.

Ledger rows at successive hops describe the same routing funds; summing the entire ledger would double-count. Evidence enrichments are not additional transfers. Several event rows can share one transaction/network fee: deduplicate fees by chain and transaction hash. A batched transaction fee is not automatically attributable solely to the case order.

## Provenance and control

Relay order association is independently reproduced by matching order IDs in source deposit call/log and destination calldata plus the actual matching token event. This establishes a deterministic exchange association through mixed liquidity, not identical-coin continuity. The affected Robinhood token sender is reproduced, but the Robinhood-to-Ethereum bridge source/fill mapping remains unresolved.

The Arbitrum consolidation recipient may contain other funds. Until its complete relevant inflows/outflows are examined, do not extend exclusive case provenance beyond it. Privacy Cash pool withdrawal linkage remains broken. A fee payer, gas funder, common recipient, matched timing or transaction signer does not on its own establish beneficial ownership or attack methodology.

## Integrity and limitations

evidence_index_v0.2.json records paths, sizes and SHA256 hashes for the checkpoint's files, excluding itself. SHA256SUMS_v0.2.txt provides a separate integrity list, excluding itself and the index to avoid circularity. Prior intermediate commits retain older snapshots. Git content verification is distinct from cryptographically signed-commit verification.

The two initial Relay wallet lookup response files survived a duplicate failed lookup whose request metadata overwrote the successful request record. This limitation is explicitly recorded in those request files; their exact successful retrieval time is NOT ESTABLISHED. Source-specific order records used for confirmed bridge matches have preserved matching request metadata. An access failure is not an empty history. No new post-cutoff public recovery/attack-vector review was completed in this resumed EVM-focused run.
