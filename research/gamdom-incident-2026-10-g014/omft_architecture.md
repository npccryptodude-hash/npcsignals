# Historical architecture and version boundaries

The observed route is NEAR intents execution→DAI OMFT token's ft_transfer-to-self with WITHDRAW_TO:B memo→token burn→Ethereum treasury EOA DAI payment. G013 already verified the exact receipt actions, burn events, account owner and empty Ethereum sender code. This is not a demonstrated Ethereum bridge-verification contract withdrawal.

The token account is `eth-0x6b175474e89094c44da98b954eedeac495271d0f.omft.near`; its historical owner_get is `omft.near`. The two historical code snapshots in G013 have the same token code hash. New historical contract_source_metadata at NEAR block 219842443 reports version 0.1.0, source link https://github.com/near/intents and null build_info. The exact metadata JSON is also present in the captured historical WASM. This supplies source-family provenance, not a source-to-WASM build proof.

The pinned repository token source, including an older pre-reorganization version, describes a special ft_transfer-to-self branch that burns tokens and emits an FtBurn event carrying the supplied memo. It has no source-defined Ethereum payout transaction field in that branch. This is consistent with the actual recorded burn, but no local Rust rebuild is claimed. Exact deployed behavior is bounded by observed execution, exported methods, historical code hashes and metadata.

## The apparent factory registry lead

Current factory source under contracts/poa/factory has a withdrawal registry with caller-supplied 20-byte IdDigest keys and 32-byte payload hashes. It exposes record/update/remove/read operations governed by protocol roles. These current source records would not automatically be immutable state, although their on-chain event history could authenticate writes. The derivation of an actual target withdrawal's 20-byte key is not supplied by the examined code. No arbitrary truncation/hash guess is made from a 32-byte NEAR ID.

The historical omft.near factory account code hash is `Ar8QnDvvksbFZCk5J5F4m46ZwoWxynF2aXN2xvJ1gAr2` at blocks 219842443 and 219842723. Its actual WASM export table lacks get_withdrawal, record_withdrawal and update_withdrawal. Direct historical get_withdrawal probes using the real action receipt IDs fail at method resolution, before argument decoding; they are not claimed to be valid current-schema queries or proof of an absent record. This proves that the examined current registry interface was unavailable in that historical factory at the selected snapshots.

It does not rule out a different contract, later record, off-chain signed archive or another public record. The historical factory binary does not contain a byte-identical copy of the selected deployed token WASM; no embedded-build equivalence is claimed.

## Operational components and authority

The Ethereum sender is `0x2cff890f0378a11913b6129b2e97417a2c302680`. Current first-party treasury documentation names it as NEAR Intents treasury; that operational label was preserved in G013. Historical EOA code and valid transaction signatures establish account execution, not its private-key custodian or an authorized bridge signer set. Token owner/factory roles do not independently establish who controls this Ethereum key.

The exact off-chain payout-instruction formation, persistence, threshold signing and relayer key authorization are UNRESOLVED. The observed architecture is consistent with treasury/liquidity-mediated redemption, but discretionary operator policy, pooling and netting are not established as facts for these two payments.
