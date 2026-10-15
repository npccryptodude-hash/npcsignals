# Upstream provenance

C: `0xaCc0c1f672B03B9a5fED4535f840f09B85f40E98`. Immediate observed token source D: `0xE757683a51CfD002De479385c2F4C9DB10A5E8D2`. Token: `0xc2132d05d31c914a87c6611c10748aeb04b58e8f`, six decimals.

CONFIRMED primary explorer receipts: D sent 674.470970 USDT0 to C at 01:54:20 UTC and 40.000000 USDT0 at 10:04:47 UTC on October 13. Actual transaction sender is D in both receipts, interacting directly with the token. Full hashes, blocks, fees, raw units and event indices are in funding_transaction_ledger.csv.

Between these deposits and the 17:54:18 anchor, C sent 49.975000, 189.950412 and 299.850030 USDT0 to three different full recipient addresses. Total verified deposits 714.470970 minus these outflows 539.775442 gives a +174.695528 observed net delta. This is not an independently proven historical balance. Under the displayed event coverage it establishes that prior same-day D inflows exceed the anchor's 14.950094 input even after intervening spending. An unknown opening balance and missing raw-log completeness prevent exclusive assignment of fungible units. Do not call the latest 40-unit deposit the sole source: a 299.850030 outflow followed it.

The G006 anchor establishes C initiating a Squid swap delivering native POL to B. The token-holder index additionally displays a 0.044716 USDT0 return to C in that transaction. This return is an indexed observation, not a newly decoded receipt log in G008; do not use it to claim a fully verified net swap cost.

## Backward stopping point
D-to-C is verified. D's own upstream funding, opening balance and signed operations were not reconstructed. No bridge-origin claim is made for these two direct token transfers. Other tokens, older swaps and router use are visible as leads but are not attributed as the source of these units.

## Native funding
The normal-history sample contains a pre-anchor 0.00011315 POL incoming row at block 95453742. Its full receipt was not inspected; its short sender differs from D. The initial native-funding link led to a browser transport timeout and web retrieval was unavailable. Neither is a verified funding edge in this ledger. Native gas provenance and historical native balances remain unresolved. Current balances are not substituted for historical state.

## Comparison with A and B
Frozen G005/G006 establish C→router→B operations, B→A native funding, and A→B token movements. These are preserved rather than repeated. Searching those saved records for the full D address did not establish D funding A or B. That is a negative finding within the stored sample, not a full-chain absence claim. Shared Squid infrastructure cannot establish shared ownership. No shared signing key between C, A and B is established.

Reproduce: inspect each listed PolygonScan overview and Transfer log; match full contract, full from/to, raw uint256 and event index; order by block; sum signed raw units with verify.py. To strengthen provenance, obtain complete canonical-token logs and balanceOf(C) at block 95434112, then reconcile through the anchor.
