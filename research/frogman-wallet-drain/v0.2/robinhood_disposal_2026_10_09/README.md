# Robinhood callback credits and bounded Ethereum disposal

Continuation F0539–F0552. This is a research block, not the final article. Prior F0001–F0538 are copied as unchanged objects; frozen v0.1 and all prior files are untouched.

## Confirmed observations

All 15 already-confirmed Robinhood destination transaction/receipt/block triples were freshly reproduced on Ethereum. Seven Gateway/Across fills have independently reproduced successful call traces: WETH native unwrap into callback 0x4216e5ae6021c523aae05b6ac6824f3c096cf905, then exact full fill amount sent to 0x427c4b37de0714821b09c4fc655a713abbcfba83 in the same transaction. These complete the callback/native-credit boundary of existing routes, not new bridge routes or losses.

0x07ae8551be970cb1cca11dd7a11f47ae82e70e67 is the transaction sender for those Ethereum fills and the seven Robinhood zero-value submissions. 0x427c funded the latter through per-witness native prefunds. These are distinct account roles. No common owner, operator, custody arrangement, or beneficiary is inferred.

Historical Ethereum state shows the routing wallet already had native liquidity before the first Robinhood fill. The existing F0127 disposal of 10.251907164350756807 ETH to 0xec96957de4ececf24abd382090026e9b5c647405 was freshly reproduced. That EOA had zero prior balance, then sent 10.251 ETH at nonce zero to 0x3e2d81f7a5659e4760ba929ef88eed40ef6640a1. This is a confirmed local forwarding edge; it does not allocate the upstream routing-wallet pool to a particular Robinhood deposit.

The second EOA had zero balance before that transfer, received an additional 0.0063514945831509 ETH from 0xae06669dfd3e932476f00ea49fce82e5e63f83bf, and sent 10.251 ETH into verified LI.FI Diamond 0x1231deb6f5749ef6ce6943a275a1d3e7486f4eae. Its pre-router balance equals both inflows. The small inflow supports a gas-funding interpretation, but does not identify a common fee funder, account controller, or operator. The extra inflow creates a two-source balance boundary; exclusive previous-inflow allocation is not assumed.

The later tiny transfer from 0x3e2df1a63dd295891663bb1697375e3df46d40a1 into the first EOA is distinct from the actual second EOA. Similar address text is not a linkage.

## Supported downstream lead and stop boundary

LI.FI's own API identifies source transaction 0xefa46658dead085751916c1368ed2590d72fa34dce36abf5c6b5a8cbcfc0d624, transaction ID 0x76b9be437acfe060e06a1cc7c43177615c14406153ec2221664862d08c380630, and a Mayan route to Arbitrum. The ID is reproduced in the source receipt. Its reported receiving hash is 0x6e0e5363e1d9665fd9d6360655c1ffd7a66f397fab0731fe65d06e8d630bfb6f, with 26823.206875 USDC to the same second EOA address. This transaction-specific API correspondence is SUPPORTED, not a newly confirmed cross-chain edge: destination receipt and Mayan order correspondence were not independently reproduced in this block. This exact destination/order is the next bounded disposal target. `Cow` is an integrator string, not an operator identity. Empty API feeCosts does not establish zero fees.

## Funding conclusions

Eight direct Robinhood bridge entries retain UNRESOLVED upstream native provenance. Seven contract-mediated entries now have PARTIAL / RE-ESTABLISHED last-hop funding from 0x427c. Affected-wallet V4 and wrapped-token disposal observations are separately reproduced in the direct-funding block; complete native payout tracing remains unavailable on Robinhood RPC. No CLEAN affected-wallet-to-all-bridges claim is made. Post-bridge Ethereum disposal proceeds enter an already-funded pooled account; individual Robinhood allocations remain UNRESOLVED. Prior Relay totals remain unchanged; Privacy Cash remains separate; no new losses, private custody attribution or beneficiary identification.

## Reproduction

Run the four collect scripts for read-only RPC/explorer/protocol requests (existing captured responses are retained). Run `python build.py`, then `python verify.py` from this directory against the committed SHA256SUMS.json. Block/hash/receipt status, 15 destination triples, seven native callbacks, local balances, nonce-zero forwarding, LI.FI source/API ID correspondence and all prior ledger objects are checked offline. Ethereum callTracer availability does not cure the separately documented Robinhood historical-state/tracing limitation.
