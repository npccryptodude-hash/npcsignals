# Robinhood pooled funding/disposal completion at evidence boundaries

Continuation F0553–F0585. This research checkpoint adds account reconciliation, fresh onward-hop reproduction, a common funding-source observation and an exact Hyperliquid deposit link. It is not an article. Frozen v0.1 and all existing files and ledger objects are unchanged.

## Append-only correction: no new Mayan route

F0553 explicitly reconciles the preceding block with the full checkpoint. F0548 reproduces F0179; F0550 reproduces F0180 / F0477; F0551's block-local API lead was already globally CONFIRMED in F0477–F0479. The Mayan source hash 0xefa46658dead085751916c1368ed2590d72fa34dce36abf5c6b5a8cbcfc0d624 and order 0x8bf9dc549b8556ca011f2399a9a893eb53699af88bd2f8323bfdcc5fea2e6e5a belong to the existing 10.251 ETH → 26823.206875 USDC route. The three-route Mayan total remains 34.75 ETH → 92468.737932 USDC. Earlier wording describing these reproduction records as new economic edges or an unverified global Mayan route is superseded by this append-only clarification, not by rewriting old F IDs.

## Reconciled native routing account

Wallet: 0x427c4b37de0714821b09c4fc655a713abbcfba83, Ethereum. Scope: first observed funding at 2026-10-06 20:19:35 UTC through the last documented disposal at 2026-10-07 02:18:11 UTC.

| Accounting component | ETH |
|---|---:|
| Prior native balance | 0 |
| Reproduced inflows (35 ordinary, 27 internal credits) | 362.263931321884337807 |
| 15 outgoing principals, nonces 0–14 | 362.262907164350756807 |
| Sender-paid gas | 0.000910467051228 |
| Remaining balance | 0.000113690482353 |
| Unexplained residual | 0 |

Two ordinary-history pages and one internal-history page are exhausted. Fresh RPC transaction/receipt/block triples and call traces reproduce these observations. Historical pre/post balances independently check each outgoing block; code snapshots at captured native-event blocks are empty. The scoped accounting does not establish all lifetime activity, private identity, or clean affected-wallet funding. Small distinct-address credits are case-unassigned, not classified as attacker funding by resemblance or timing.

All seven contract-mediated Robinhood fills credit this wallet, as already established at F0539–F0545. The eight direct Robinhood fills and the separately verified Across Base route are retained distinctly. Other already-documented Ethereum protocol credits are reproduced without reopening their origin chains. Native upstream proceeds on Robinhood remain unresolved where historical state/tracing was unavailable.

## Allocation test: seven credits do not create seven separate disposal paths

The reconciled ledger tests two groups: the seven contract-mediated credits and all fifteen Robinhood credits. It uses conservative fungible balance intervals, not FIFO or a nearest-time rule. It adds exact credits, permits every prior principal and gas debit to consume the group, and caps possible remaining group balance at the actual account balance.

No individual outgoing principal is mathematically forced to include funds from the seven-credit group. Thus seven callback paths are complete to the pool; **0/7 individually allocated end-to-end disposal paths are complete, 7/7 remain incomplete at the pooling boundary**. This is not an assertion that the credited funds never left.

For the broader all-fifteen Robinhood group, two 18.501 ETH outgoing principals (F0115/F0116, freshly enriched here) each have a conservative minimum group contribution of 11.851225222747544873 ETH in this reconciled scope. These are partial group bounds only: they do not identify one of the seven deposits, a clean affected-wallet source, or ownership. Do not promote them to full 18.501 ETH allocation or propagate a full route allocation beyond retained gas/principal boundaries.

## Disposal inventory

All 15 routing-wallet outflows and 29 already-documented subsequent native transfers / protocol calls are freshly reproduced. `path_inventory.json` lists each root and its existing onward F IDs; `legacy_native_hop_reproductions.json` preserves full source, recipient, asset/value, gas, calldata, case code and pre-block balance observations.

The existing service routes remain distinct: six LI.FI/Relay routes, one LI.FI/Across route, three LI.FI/Mayan routes, two Chainflip routes and the NEAR Intents route. Separate tails stop at dated holding or pooled forwarding/collector boundaries. No service use proves an operator or owner. Prior protocol-specific linkages, amounts, destination transactions and fee limits remain in the unchanged Relay, Across/a3ca, Mayan, Chainflip and NEAR verification blocks. None is counted again as a new cross-chain edge or loss here.

## Mayan output reaches a Hyperliquid account

Fresh source/destination order events reproduce the already-confirmed LI.FI → Mayan Swift V2 route, including destination hash 0x6e0e5363e1d9665fd9d6360655c1ffd7a66f397fab0731fe65d06e8d630bfb6f. Arbitrum recipient 0x3e2d81f7a5659e4760ba929ef88eed40ef6640a1 is an EOA at settlement. Its USDC balance was zero before fulfillment and 26823.206875 immediately after.

Its subsequent transfer 0x963c56253dedcfd5ff9f944c91eb9cb9e94d12701d9165f66a40b9aa0b4cfc1f sends 26823.206875 USDC to the documented Hyperliquid Bridge2 endpoint 0x2df1c51e09aecf9cacb7bc98cb1742757f163df7. Hyperliquid's own API confirms a deposit credit for the queried source account by identical transaction hash and amount. This account-level transfer/credit linkage is CONFIRMED and is the additional endpoint linkage, not a new Mayan route.

A bounded 10000-block log window contains this one positive USDC outflow, the fulfillment inflow, and a later zero-value lookalike-address Transfer log. The latter is not a second debit or control finding. Some later Arbitrum state queries failed; their errors and rejected explorer requests are retained. Do not claim complete lifetime exclusive token provenance or a present balance from those failures. Classification is PARTIAL / RE-ESTABLISHED at the reproduced token boundary, while the upstream Ethereum pool remains MIXED.

The API also reports 26823.2 USDC internally moved to spot. This is not external withdrawal or XMR1 redemption. No new fills, XMR1 balances, Monero redemption or beneficiary are asserted. The six Relay route totals and existing XMR1 accounting remain unchanged.

## Special small ETH funding test

Source: 0xae06669dfd3e932476f00ea49fce82e5e63f83bf, a case-block EOA. Transaction: 0x48ccd6181b3c6357ba9f29ffd238c20fc129f09b5a5cc1330dbb07ea23c864a6. At 2026-10-07 02:20:11 UTC it sent 0.0063514945831509 ETH to the second EOA. The latter already held exactly 10.251 ETH and then attached exactly that amount to the router. Gas was 0.001157294241859464 ETH; remaining native balance by this arithmetic was 0.005194200341291436 ETH. Additional gas liquidity was necessary; no additional trade principal was necessary. A fee-funding purpose is SUPPORTED, not a proven intention or a specific fungible-wei allocation.

A bounded source-account history (Ethereum blocks 26136700–26137480) returned 33 transactions. Ten exact outgoing transfers into ten documented downstream source EOAs were independently reproduced, including the special transfer. This establishes a common funding-source account relationship. It does not establish common ownership, a fee-service name, common operator, signer control or beneficiary. No direct transfer with the affected wallet, 0x427c or 0x07ae appears in that bounded source history; this is not a lifetime absence claim. Other source history and public metadata do not independently name an operator.

The small transfer creates a two-inflow native boundary and prevents an exclusive single-inflow provenance claim at that EOA. It does not change the exact Mayan order/settlement or exact USDC/Hyperliquid credit. It advances funding-account observations, not beneficiary attribution.

## Remaining gaps and reproduction

The Robinhood branch is resolved to current evidentiary boundaries, not to complete affected-wallet provenance. Next highest-priority target remains native token-sale payout tracing / historical Robinhood state; it must independently connect the affected-wallet asset flow to bridge principal. Individual seven-fill disposal allocation, earlier fee funding/control, source-service/operator identity and final beneficiary remain unresolved. No new bridge branch is opened. Privacy Cash remains separate.

Run the collect scripts for read-only manifests, `python build.py` to reproduce append-only records, and `python verify.py` against committed SHA256SUMS.json. Offline checks preserve all 552 prior objects, reproduce scoped balances and interval bounds, check 15 nonce-sequenced outflows, 29 onward native hops, ten source funding edges, exact prior Mayan order/settlement, and the Hyperliquid hash/amount match. No article was written.
