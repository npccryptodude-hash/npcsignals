# Cross-chain execution matching

## Route 1

BNB settlement: `0xe4eea89ea32d675baa724d2e3926ffd3d4fbbe8d4f73ce381799bf9550a92347`, block 127436960, 13 October 16:45:01 UTC.

Actual 56-byte UID:
`0xa6e7012a35800d9ae6c9262d49c2f055303b7f9014219a64e5a92e0f6edb5cf8e5686aae44d392aa6a0637fd38393859502f86676ace6701`.

The UID is digest (32 bytes), owner B (20 bytes), validTo (4 bytes). The first 32 bytes are the EIP-712 order digest, not the settlement transaction hash. Full order metadata hashes to `0xf498b4b510e8bb40a722ab3b76374a3616aa26a3778e8d03c71af28553062091`. It specifies provider `cow-sdk://bridging/providers/near-intents`, destination chain 1, DAI, recipient B, and source receiver `0x16ee1ef93df4657a52f8ea6eebe950b54bc91265`.

The status query by that exact receiver returns the source settlement hash and destination `0x6b282435dc06107a499c8b8ef0ed83632a51d32738d81c143dc7e2d53542fd40`. Ethereum receipt: block 26184851, 16:45:35 UTC, 3293.876314118353387030 DAI to B. Initiator/token sender: `0x2cff890f0378a11913b6129b2e97417a2c302680`. Its standard ERC-20 transfer input is 68 bytes with no appended UID.

NEAR deposit `7ANgmgCrZnot8uA2NRuLQxCmrtpR5n2E6aURrimmDbvF` credits 3296944723631957632111 raw source units to internal account `5cda9ad0f0feb2020d8b722ba07641f96fe70e34bafc9bb6f7919e9a83ef9520`. NEAR execution `3CucqT6YmivRFpNMtgsiuR43d2JXJcBuMLUYU9vHzjV6` contains intent `75XrduXEdVBYFwCDXakMPLM7xn68p4xs8db6U3enR16t`, debits that source asset and withdraws 3294.176314118353387030 wrapped DAI with `WITHDRAW_TO:B`. The status service reports a 0.3 DAI withdrawal fee, accounting exactly for the Ethereum receipt. That fee subtraction is corroborated accounting, not a cryptographic link embedded in the Ethereum transfer.

## Route 2

BNB settlement: `0xcda9343de4eb5ad1e96d210d3e215bdf55cb33fba1c5f3fe3a6456afbe6781d2`, block 127437353, 16:47:58 UTC.

Actual UID:
`0xf122a39685746aa58924b1afbd9183500e83ec45d6553bc6a4245d6a107777bfe5686aae44d392aa6a0637fd38393859502f86676ace67ad`.

Full metadata hashes to `0x3776ed11421cd2ad5b04773d64b98aef0e9b975753fe49d6304d73a4a45a5474`. Source receiver: `0x66e6a2a0a9d871011b60b2e39902f10a33da4a2c`. The protocol status index maps it and the source transaction to Ethereum `0x3afe0536e5a7bc6f33da46ecef12c11a0591c9b13df90cb58f73c6839c99efaf`, block 26184865, 16:48:23 UTC. Receipt: 3947.497560500152030405 DAI to B from the same service transaction initiator as route 1. Again, the 68-byte ERC-20 transfer contains no cross-chain identifier.

NEAR deposit `HFrVzrvRmLUF4FNd1UyiaMRD9JwCWSS5jnpgsCBNLQkA` credits 3947414585151760332111 source units to internal account `387e8a75773d5489e648756f04faba9d1ca8d01787e8e6e274faa570f8aebea6`. NEAR execution `7dbo8A2xAkge8A6q139CsjcKd7rTHrK5U8aSyMxRMNiT` contains intent `8KMQAbV7JGDtQ1qxtXztYT1MTYjv64SpAnexcG4LvnHT`. Its atomic batch includes source-asset/USDT and USDT/DAI counterparty legs, then a 3947.797560500152030405 wrapped-DAI withdrawal addressed to B. Subtracting the status-reported 0.3 DAI withdrawal fee matches the Ethereum receipt exactly. Counterparties' fees and their internal token movements are not additional B principal.

## Identifier and trust boundaries

Both routes: **SUPPORTED**. Unique deposit addresses, exact source hashes and destination hashes provide a protocol-specific execution mapping. Independent NEAR RPC executions corroborate the intent hashes, internal accounts, source debits, asset transformations and withdrawal recipients. A consensus-verifiable bridge proof joining BNB deposit, NEAR mint and Ethereum payout was not obtained. Service API mapping remains necessary at those boundaries. No common amount/timestamp alone is used to assign a route.

Metadata `quoteId` values are preserved verbatim as protocol metadata identifiers. They are neither actual CoW UIDs nor proven on-chain message hashes, and the verifier does not claim they equal keccak(quoteBody). Quote attestation and ed25519 signatures are preserved but their issuer authenticity is NOT ASSESSED. B's executed order commits cryptographically to the metadata contents; that does not authenticate every statement or third-party signature within those contents.

The chain-56 settlement ABI has no universal destination-chain correlation event. Ethereum payouts do not execute the CoW settlement contract or carry its UID. Mainnet orderbook lookups for both BNB UIDs returned 404; this narrow negative result does not disprove the bridge routes. No other destination candidates were searched: the two candidates are confined to the existing G006 window and uniquely identified by the protocol index.
