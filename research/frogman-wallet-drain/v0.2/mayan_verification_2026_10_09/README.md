# Mayan verification block — 2026-10-09

Parent public checkpoint: `327971189980ac5e67cff758013d015a93b305e3`, main, through F0470. New ledger: F0471–F0480. This is an additive evidence block, not an article. Frozen v0.1 and all existing F0001–F0470 files and objects remain unchanged.

## CONFIRMED: three Ethereum → Arbitrum Swift V2 edges

| Existing origin | New records | Order hash | ETH in | USDC received on Arbitrum |
| --- | --- | --- | --- | --- |
| F0162 | F0471 origin enrichment; F0472 settlement; F0473 edge | `0x911a6366dbe71b41327c8da71a1707ed3d1785db78d6688dec9dd46a44319f13` | 22.5 | 60,416.783132 |
| F0178 | F0474 origin enrichment; F0475 settlement; F0476 edge | `0x42a2fd8e8464527d2d0d58fb05e721b50691b0c280cd0c1785d44322047a9f32` | 1.999 | 5,228.747925 |
| F0180 | F0477 origin enrichment; F0478 settlement; F0479 edge | `0x8bf9dc549b8556ca011f2399a9a893eb53699af88bd2f8323bfdcc5fea2e6e5a` | 10.251 | 26,823.206875 |

Total routing: **34.75 ETH → 92,468.737932 USDC**. These are subsequent routing observations, not additional losses. Origin, destination, cross-chain edge and driver reimbursement records must not be summed as separate loss events.

`cross_chain_edges.json` contains the complete transaction hashes, source/destination wallets, block numbers, UTC timestamps, protocol identifiers, contract roles, amount units, fee limitations and decoded event evidence. It extends the cross-chain reconstruction additively. `master_timeline_F0001_F0480.json` appends ten rows while preserving the prior 470 row objects exactly.

## Independent origin and destination reproduction

Fresh Ethereum RPC (dRPC) reproduces each outer transaction, successful receipt and containing block. The origin calls are to `0x1231deb6f5749ef6ce6943a275a1d3e7486f4eae`. Mayan's first-party explorer records identify LI.FI as the consumer; the preserved LI.FI source and receipt routing data provide additional protocol context. The outer router is distinct from Mayan's Forwarder and Swift source contract.

Each receipt independently shows:

1. Native ETH wrapped into WETH through the observed wrapping endpoint `0x529863940bf6065d8c122a550c2ff37c1cfefa16`.
2. Exact WETH transfers into Mayan Forwarder `0x337685fdab40d39bd02028545a4ffa7d287cc3e2`, then Swift source contract `0x40ffe85a28dc9993541449464d7529a922142960`.
3. `OrderCreated(bytes32)` with the exact case order hash.
4. Inner `createOrderWithToken` data in the Forwarder's emitted protocol data, decoded using the pinned first-party SDK ABI. Amount, trader, destination recipient, destination Wormhole chain ID 23, USDC address, minimum output, auction mode and fee parameters are preserved and checked.

Fresh Arbitrum RPC reproduces the three fulfillment transactions, successful receipts and containing blocks. Each emits `OrderFulfilled(bytes32,uint64,uint256)` from documented Swift destination contract `0xd78d199f8c402e7b5cc2abe278df0412400a3bae`, carrying exactly the same order hash as the corresponding Ethereum `OrderCreated`. Its net amount equals the independent USDC Transfer event to the exact destination recipient and the first-party explorer's `toAmount64`. All fulfilled amounts exceed the encoded minimums. The USDC contract's six decimals and symbol are freshly queried.

Mayan's current first-party SDK and documentation identify the explorer endpoint `/v3/swap/trx/{sourceTxHash}`. The three records report SWIFT_V2, COMPLETED and ORDER_UNLOCKED, and link those exact source, fulfillment and unlock transactions. Link classification is CONFIRMED because independently reproduced protocol events match exact order hashes, recipients and amount parameters on both chains. Timing and similar amounts are not the basis for matching.

| Origin UTC / Ethereum block | Fulfillment UTC / Arbitrum block |
| --- | --- |
| 2026-10-07T01:44:47Z / 26137303 | 2026-10-07T01:45:17Z / 512421055 |
| 2026-10-07T02:18:35Z / 26137471 | 2026-10-07T02:19:03Z / 512429025 |
| 2026-10-07T02:20:23Z / 26137480 | 2026-10-07T02:20:52Z / 512429436 |

## Underlying settlement: exact Wormhole batch correspondence

Swift is an intent fulfillment mechanism: destination liquidity is delivered first, and source locked funds are later released to the driver. This is distinct from claiming that the case ETH was minted or transported into Arbitrum USDC. The same assets are not literally carried across chains.

The shared Arbitrum message publication is independently reproduced:

- Transaction: `0x2a990ab0d2d82e77fed8b938494224550332f03564a30571b1d14eff47ce6d8d`.
- Block 512429549; UTC 2026-10-07T02:21:22Z.
- Message application emitter: Swift destination `0xd78d199f8c402e7b5cc2abe278df0412400a3bae`; Wormhole chain 23; sequence 8323.
- `LogMessagePublished` carries the compressed batch's exact payload hash. The contract emitting this core message event is `0xa5f208e072434bc67592e4c49c1b991ba79bca46`, matching Wormhole’s first-party SDK mainnet Arbitrum core address.

The successful Ethereum unlock transaction is `0xf788968ccc5365380bdd27dc6b8e26151f910af0118a90e9090f3d0154188afd`, block 26137567, UTC 2026-10-07T02:37:47Z. Its `unlockCompressedBatch(bytes,bytes,uint16[])` calldata includes the encoded VAA and batch payload.

The VAA bytes independently match Wormholescan's exact emitter/sequence response. The decoded emitter, timestamp and sequence match the independently reproduced Arbitrum publication. Its payload commits to Keccak-256 of the exact eight-record compressed batch. Case order indices are 0, 2 and 1 respectively; all three exact hashes occur at their API-reported indices. Batch records also reproduce the source chain, unlock receiver, zero fee basis points and corresponding fulfillment timestamps. The executed index array covers 0–7. The VAA has guardian set 7 and 13 signatures; its double-Keccak body digest matches the indexed digest.

`wormhole_batch_correspondence.json` preserves these decoded fields and bytes. No standalone guardian ECDSA validation or deployed-bytecode audit was performed. The evidence demonstrates exact publication/VAA/batch/successful unlock correspondence, not an independently reconstructed guardian consensus audit.

## Driver and reimbursement role; F0480

All three fulfillment transactions, the message publication and source unlock are sent by `0x754dcfb2861547015b221e963b4133a71dbdc024`, which matches the API's driverAddress. The Arbitrum outer fulfillment router `0x3e07be15370d8b12d80a159a7ef14b9e51869497` is distinct from the Swift destination transfer/event contract.

In the shared unlock receipt, each case `OrderUnlocked` is immediately preceded by a WETH transfer from Swift source to that driver for its exact input amount: 22.5, 10.251 and 1.999 WETH. F0480 records those three reimbursements, totaling 34.75 WETH. The receipt contains eight orders; the other five are not assigned to this case and their transfers are not included in case totals.

CONFIRMED: case-specific fulfiller, publication sender, unlock submitter and reimbursement recipient roles. This reimbursement is compensation in the reproduced protocol flow; receiving it does not identify the case funds' final beneficiary. No named driver operator, owner or custody company is established.

The API supplies Solana auction/state addresses and auction mode 2. Independent Solana competition, winning-bid events and winner identity were not decoded. API driver metadata and independent fulfillment/reimbursement roles are preserved without equating them to an independently audited auction winner. The API's relayerAddress is null; no separately identified relayer is invented. Auction account metadata is API-only and must not be collapsed into driver or wallet ownership.

## Fees and accounting limits

Protocol/referrer fee basis points are zero in the API and relevant reproduced source/batch parameters. The source releases the full per-order WETH input to the driver; the exact recipient USDC transfer supplies the net settlement amount. The API reports zero bridge fee and protocolFeeUsd. Cancellation and refund fee parameters and API redeemRelayerFee/refundRelayerFee fields are retained in the edge records, but they are not labeled as independently proved fees charged on these successful settlements.

Origin and fulfillment execution gas is calculated separately from receipt gasUsed × effectiveGasPrice. Shared publication/unlock transaction gas is not allocated to individual orders; Arbitrum's receipt-level gas accounting is preserved without inventing a separate fee allocation. No ETH-minus-USDC subtraction or independent market spread is asserted. API quote/market estimates are not proof of a realized fee or loss. API `redeemTxHash` here denotes the source unlock transaction, not a new recipient payout or XMR redemption.

## Attribution boundary and remaining gaps

CONFIRMED protocol/service endpoints: Mayan Forwarder, Swift source/destination contracts and exact Wormhole messaging mechanics. LI.FI outer routing is supported by the first-party case record and preserved origin routing evidence. These roles are distinct from the destination wallets and the driver.

The destinations have the same literal EVM addresses as the respective origin senders. This is an encoded routing fact, not independent proof of common control, human ownership or beneficiary identity. No new private custody relationship or common operator is established. Complete upstream provenance from the affected wallet remains unresolved. Earlier SUPPORTED, CLAIMED and UNRESOLVED classifications elsewhere are unchanged.

All three reported Mayan candidates are resolved transaction-specifically through settlement and source reimbursement. Remaining limits concern independent auction reconstruction, standalone VAA signature verification, ownership and upstream provenance. Next branch: NEAR Intents. No NEAR, unlabeled-destination, Robinhood-gap or XMR1 research was undertaken in this block. Privacy Cash remains separate and was not reopened. No article was written.

## Reproduction and integrity

Run `python verify_mayan.py` offline. The verifier checks chain identities, successful receipts and block inclusion, exact event signatures/order hashes, wrapped input routing, decoded recipient/amount parameters, USDC metadata and transfers, message publication, VAA bytes/digest, batch hash/indices and case reimbursements. It preserves the prior 470 timeline objects and reproduces the three aggregate edge amounts.

`access/*.json` contains read-only request records: URL, UTC retrieval time, request payload, HTTP result or error. `*.response.txt` contains exact response bytes. Pinned SDK/documentation files provide ABI and endpoint/address provenance; current documentation does not replace transaction-specific evidence. A guessed public contract-source repository returned 404; that is a retrieval failure, not evidence of missing contracts. `SHA256SUMS.json` indexes source and derived files. No swap was requested, auction entered, channel created or funds moved.
