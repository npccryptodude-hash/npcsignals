# Financial reconciliation

## E1 gross principal received once

| Asset | Successful original candidate inputs | Decimals |
| --- | --- | --- |
| USDT | 426040.814198 | 6 |
| USDC | 503001.390869 | 6 |
| USD1 | 20077.942698961878000000 | 18 |
| DAI | 738.148858772417648963 | 18 |
| ETH | 86.956356111770671236 | 18 |

These are exact asset quantities, not verified USD loss amounts. E1 principal is 20 incoming token transactions and six successful native transfers from A/S1/S2. Seven swaps transform existing principal and are not additional losses. A self-authorization transaction is not a principal outflow. Two failed native attempts contribute no transferred principal.

At the collection boundary E1 holds 949428.481297752991539942 DAI and 86.946079420134397606 ETH. Native accounting is: zero opening + 86.956356111770671236 incoming − 0.010000000000000000 returned to A − 0.000276691636273630 E1-paid fees = 86.946079420134397606 ETH. Other initiators pay their own fees; do not charge solver gas again to E1. Failed senders pay fees but no ETH principal moves to E1.

For every tracked E1 token and four B tokens, `balance_reconciliation.json` gives opening raw units + inflows − outflows = historical closing raw units with residual zero. Swapped stablecoin quantities versus DAI output differences combine pricing/execution effects; they are not automatically protocol fees or recovered funds.

## B/E2

BNB-chain USDT bridge inputs total 706943.421822265793499428. Count each B debit once, not the successive intermediary debit again. They are already downstream bridge inputs; their originating incident principal remains unresolved. The first Ethereum USDT output is later converted into DAI in frozen G006. The second Ethereum DAI output is not added to the BNB input as another loss.

B's Ethereum DAI is 816635.912748421658923307 at block 26185250. G006 later observed a net delta of 869368.076253071235248671 DAI after additional arrivals. This is consistent in scale with the ~$870000 lead, but does not independently identify every originating chain or prove that most of the full amount arrived through Relay. A 10k BUSD conversion, Polygon bridge arrivals and C-directed swaps are separate transformations of existing funds, not automatically additional stolen value.

## Testing reported dollar estimates

At a hypothetical $1 per tracked stablecoin, E1 incoming stablecoin units sum to 949858.296624734295648963 dollars, before assigning any ETH price. This is a clearly labeled unit-peg scenario, not a dated market valuation. An ETH/USD price series, consistent valuation cutoff and non-Ethereum originating ledgers have not been obtained. We do not substitute the explorer's current dollar prices or rounded media totals.

The ~$1.2m E1 description could include native ETH and rounding; the token-only sum does not establish a contradiction. Neither the >$2.3m first-hour figure, just-over-$3m company claim nor $4.208m cross-chain estimate is reproduced by this bounded ledger. Definitions, wallet coverage, price times, recovery and original authorization remain unresolved. Do not calculate an exact unexplained dollar deficit against these estimates from partial asset coverage.

Verified unauthorized losses: **UNRESOLVED, not zero**. Verified financial movements: the asset quantities above. Verified recovery/customer reimbursement: not established. Fungible balances and pooled services do not preserve exclusive inbound-unit identity.
