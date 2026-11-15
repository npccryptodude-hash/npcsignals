# Coverage report

## Requested and achieved scope
Requested: October 6–15 UTC, preferably extending to September 1. October 15 is an incomplete day; no future period is claimed. Historical indexes were inspected on October 15. All dated records used are October 12–14. The absence claims below refer to displayed, filtered explorer indexes only.

| Address/network | History retrieval and pagination boundary | Temporal coverage supported by display | Missing coverage |
|---|---|---|---|
| A / Polygon | Page 1 of 11; source reports 519 total rows. First five rows cover Oct12–14; next row is Sep2 **2025**, block 75974257. Fifty rows displayed, remainder older than requested interval. No additional pagination is required to cross the Sep1 2026 lower boundary in this displayed order. | Displayed index spans the requested interval and the Sep1 extension without earlier in-window entries. Two genuine stablecoin outflows on Oct13; one dust event Oct12; two noncanonical events Oct14. | Poor-reputation and zero-value filters enabled; no full raw-log scan. The other ten pages are older than the lower boundary, not independently downloaded. History-index omissions cannot be ruled out. |
| B / Polygon | One page; five displayed token rows, all Oct13–14. Four canonical stablecoin movements already in G005 and one noncanonical POL-named event. | No earlier visible token event back to Sep1 in the returned index. | Same token/zero filters. Native/internal records retrieved separately; no complete archive export. |
| B / Ethereum | Page 1 of 1; 24 displayed token rows; all Oct13–14. Earliest row Oct13 16:34:35 UTC, block 26184796; latest Oct14 17:15:23 UTC, block 26192172. | All returned rows captured: 20 new rows plus two G005 arrivals and two noncanonical imitation rows. Canonical DAI entries include both before and after G005 arrivals. | Poor-reputation and zero-value filters enabled. No independent all-contract log enumeration. Latest dated row is not an independently verified chain-head cutoff. |

Native/ordinary Ethereum B history separately displays 16 normal transactions, all October 13, plus a displayed internal ETH swap return. Four native funding receipts, five approval/order actions and a type-4 delegation self-transaction were additionally inspected. Not every internal trace was exported. The internal swap return (about 0.007145187 ETH) was observed in the index but not preserved as a fully verified exact-amount record.

A / Ethereum was examined only for the additional BUSD transfer found in B's history. No historical baseline for A on Ethereum is claimed. C was examined only for three operations directed to B; C's broader history remains outside completed coverage.

## Filters and precision
No browser preferences were changed. Site settings confirmed that reputation and zero-value hiding were enabled. Consequently this package does **not** claim exhaustive ERC-20 event histories. No whole-calendar-day completeness is certified by independent RPC. Every negative finding is scoped to the returned filtered history; unreturned events can exist on any date in the window.

Canonical token selection uses full contract addresses, not names or tickers. Unknown imitation-token decimals/raw units are intentionally blank. Exact decimals for DAI/BUSD (18) and USDC/USDT/USDT0 (6) are consistent with decoded raw values and explorer amount display. Most new canonical Ethereum token amounts were cross-checked in decoded Transfer logs; native values come from receipt/internal-transfer views. Polygon dust was inspected at receipt/index level, without a completed raw-log capture, and is SUPPORTED. Third-party imitation rows are indexed observations with verified actual transaction sender, not authenticated spending by the named event sender.

Fees are per transaction, repeated on event rows for convenience; aggregate only unique `(chain, tx_hash)` values. Selected ledger records do not contain every internal pool transfer. Approvals, order invalidations and delegation are stored separately and are not transfer volume.

## Alternative access attempts
- PolygonScan token-history page initially showed a Cloudflare check; one reload succeeded. No bypass or repeated challenge attempts.
- Public Blockscout APIs for Polygon A and Ethereum B returned HTTP 403.
- Routescan Etherscan-compatible API returned JSON `status=0`, `message=chain not supported` for chain 137.
- Search-service explorer-history opens were unavailable; browser history and pagination were usable as explicitly requested.
- G005 documented direct RPC access failures. They were not treated as proof of missing chain data, and direct RPC success is not claimed here.

## Statistical limits
There is no comparable prior active outgoing-operation period in the displayed September–October baseline. Incoming unsolicited tokens do not constitute routine operational behavior. Nonces 0/1 establish first ordinary sender use on Polygon; Ethereum B's first displayed self-transaction has nonce 0 and type 4. Authorization processing and contract/delegated activity must be considered separately. No anomaly score, typical-outgoing median, habitual-counterparty classification or generalized expected holding-time model is computed from this one-day activation sample.
