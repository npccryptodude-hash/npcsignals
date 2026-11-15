# Historical balance and provenance

## Fixed anchor

`0x5e1fd78c9b4f5881d28eb2f14f0c59b32bda206a942a6956316c07965b570591` was already explorer-verified in G008. G009 adds raw RPC receipt, transaction, block header, event-query and historical-state verification; it is not counted as a new transaction. Chain ID is 137. Block 95434113, timestamp 2026-10-13T01:54:20Z, transaction index 19, log index 179. Sender and fee payer D; direct interaction with canonical USDT0; Transfer raw value 674470970 from D to C; receipt status 1. All fields match the frozen G008 record.

## Actual state, not an event-sum assumption

Archive balanceOf(D) at block 95434112 returns raw 1579018972. At 95434113 it returns raw 904548002. The explorer's expanded USDT0 storage table independently displays the same debit, while C's displayed state rises from 440.393671 to 1,114.864641. This separately accessed representation corroborates transaction-local state; infrastructure independence is not established. The sole D Transfer in the anchor block and exact state delta support equivalence of block-end and transaction-local boundaries here. No intervening D event was omitted from the saved returned query set. A cryptographic state proof or full replay was not performed.

The successful transfer proves at least the transferred quantity was spendable in this transaction. The recorded balance is not a broader audit of token restrictions, all spending permissions or legal ownership.

## Immediate funding window

At block 95399999 D already held 936.499001 USDT0. Six later canonical inflows before the anchor total 642.519971:

| UTC October 12 | USDT0 credited | Initiator / input | Classification |
|---|---:|---|---|
| 14:57:30 | 600.000000 | 0x9f273c1fd76b09cb09278019a50991a5f6265b0d | Direct token transfer |
| 18:43:48 | 2.760531 | 0x532857ca20ee151295d7d4085a6dde7132758904; 27 POL native value | Same-chain native/wrapped-native swap through router |
| 18:47:57 | 2.145856 | 0x938711f3c125f165cbcdcbc0711eec4512316118; 21 POL | Same-chain swap |
| 18:51:24 | 17.231063 | Same initiator; 169 POL | Same-chain swap |
| 18:59:42 | 20.382515 | Same initiator; 200 POL | Same-chain swap |
| 20:35:41 | 0.000006 | 0xfe17e720f36c3d1ffde5bfbedeac2c17f19ef2b0; contract creation | Micro-transfer; no owner-control inference |

Full hashes and raw units are in funding_transaction_ledger.csv. The four routed credits total 42.519965 USDT0. Receipts show reciprocal wrapped-native transfers to the pool and USDT0 output through Multicall to D. A router name alone was not used to infer a bridge. No cross-chain source was established.

No D outflow appears in the returned recent pre-anchor window. Therefore 936.499001 + 642.519971 = 1,579.018972, then −674.470970 = 904.548002. Pre-existing holdings alone exceeded the transfer by 262.028031 USDT0. This rejects the necessity of a recent deposit, not the possibility that mixed funds were economically used.

## Larger documented funding sources

The bounded token-sender aggregates rank 0x37c29b046d2253ac7291bcf131282e0441cc9282 first at 24,815.820000 USDT0. That address additionally initiated the largest individually selected swap on September 10: 13,083.760000 USDC was contributed, and 13,086.833938 USDT0 reached D. Its direct 5,796.660000 September 8 and 3,603.140000 September 23 payments are receipt-verified. The swap is not double-counted as another direct USDT0 deposit from its initiator: its USDT0 event sender is Multicall. Multicall is an infrastructure-level event sender, not an attributed owner.

Other sender totals and event counts are preserved in inbound_counterparty_totals.csv. Most were verified as RPC events, not individually classified transaction paths. Do not treat an aggregate event sender as the initiating signer.

## April candidate

The candidate `0x06f5eeef95dcabfcb68f7241990594977f23d4a19e1c89d01a2bf4321313ead5` is CONFIRMED: block 85959863, April 24 14:09:30 UTC, status 1. Initiator 0xca25eb4d9bde0a86d1176f367830c66813d6ffa7 contributed 300 DAI (raw 300000000000000000000, contract 0x8f3cf7ad23cd3cadbd9735aff958023239c6a063), and raw 299826616 canonical USDT0 reached D at log 2784. This is a same-chain swap path. It is outside the reconciliation interval and is not added to its opening balance. Retention of those funds until October is NOT ESTABLISHED.
