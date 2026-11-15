# Original-principal reconciliation

The ledger selects only G010 `candidate_original_principal`, G011 `B_funding`, G005 T01/T02 and G006 E009. It is a bounded lower coverage of verified movements, not a minimum theft calculation. All quantities are exact integers by chain and contract in principal_totals.json. Thirty-four records are unique; downstream executions are excluded. No token is assumed worth one dollar.

| Chain | Asset | Gross selected source movement |
|---|---|---:|
| Ethereum | USDT | 426040.814198 |
| Ethereum | USDC | 503001.390869 |
| Ethereum | USD1 | 20077.942698961878000000 |
| Ethereum | DAI | 738.148858772417648963 |
| Ethereum | ETH | 86.956356111770671236 |
| Ethereum | BUSD | 10456.137361559383267328 |
| BNB | USDT | 714187.786405077034199428 |
| Polygon | USDT0 | 19610.310097 |
| Polygon | USDC | 12139.456905 |

BNB original source funding 714187.786405077034199428 USDT equals two later Relay deposits 706943.421822265793499428 plus two later settlement debits 7244.364582811240700000. Adding either component to original funding would count the same principal twice. Later Ethereum DAI receipts are consideration/subsequent movement, not additional source loss. G014's last OMFT edge remains SUPPORTED.

G010 separately records E1 returning 0.01 ETH to A. Keep this as a returned movement, not proof of recovery by a company. Source gas and downstream fees are separate from principal. Failed native attempts are excluded. BUSD swaps and Polygon bridge outputs are excluded from new principal. Fungible balances cannot exclusively identify later spending.

The founder's statement claims just over $3m without a public wallet-by-wallet accounting. The external estimate is approximately $4.208m: $2.2m EVM + $965k Solana + $668k Bitcoin + $375k TRON. That arithmetic is reproducible; the valuation and authorization are not independently audited. The estimates may have different chain coverage, gross/net definitions, protective movements, pricing or recoveries. None is resolved by these records. No exact difference from an imprecise 'over $3m' can be calculated.

No timestamped market price series is acquired in G015; no USD conversion or consolidated token-unit total is presented. Solana, Bitcoin, TRON, XRP, Arbitrum and Optimism original-principal coverage is not completed here. Ownership and instruction consent are also unresolved. Consequently independently verified unauthorized loss is **not established**, rather than $0. Customer custodial liabilities and insolvency are not assessed by these asset movements.
