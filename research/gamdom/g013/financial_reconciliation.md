# Exact financial reconciliation

All USDT/DAI figures use 18 decimals. Machine-readable raw integers are in `financial_reconciliation.json`. Source principal is imported unchanged from G012, counted once. Locker deposit, mint, swap, burn and payout are route stages, not additional principal losses.

| Item | Route 1 | Route 2 |
| --- | ---: | ---: |
| Original BNB USDT principal | 3296.947360645719000000 | 3947.417222165521700000 |
| Settlement credit / actual HOT deposit, USDT | 3296.944723631957632111 | 3947.414585151760332111 |
| Source sell/buy difference, USDT | 0.002637013761367889 | 0.002637013761367889 |
| NEAR source-asset mint | 3296.944723631957632111 | 3947.414585151760332111 |
| NEAR DAI execution output / withdrawal | 3294.176314118353387030 | 3947.797560500152030405 |
| OMFT service-reported DAI withdrawal fee | 0.300000000000000000 | 0.300000000000000000 |
| Canonical Ethereum DAI payout | 3293.876314118353387030 | 3947.497560500152030405 |
| USDT principal − deposit − source difference | 0 | 0 |
| DAI withdrawal − reported fee − payout | 0 | 0 |

Totals remain **7244.364582811240700000 USDT principal**, **7244.359308783717964222 USDT actual locker deposits**, **0.005274027522735778 USDT source difference**, and **7241.373874618505417435 DAI Ethereum receipts**. No USDT/DAI unit-price parity or historical USD valuation is assumed.

The source locker deposit calls attach zero native value, so these calls add no msg.value locker fee. Each actual deposit receipt records 13298300000000 native BNB wei in transaction gas, paid by the respective deposit-address signer. This is separate from token principal and prior CoW solver gas. No fee is attributed to B's direct native balance solely because B initiated the original route.

The 0.3-DAI fees now appear in both the OMFT service's own withdrawal record and G012's 1Click status. Exact NEAR withdrawal minus exact Ethereum payout corroborates the arithmetic. The fee charge mechanism itself is not proven by a shared Ethereum withdrawal event; retain that distinction. Existing NEAR source-token and counterparty fees are preserved in G012 and are not added again.

The OMFT API also emits an `amount` JSON number in scientific notation that loses precision. It is preserved as raw response text and ignored for exact arithmetic. Exact on-chain NEAR strings and API `withdraw_amount`/`withdrawal_fee` strings are used instead. API `address` names the DAI asset contract, not B's withdrawal address; B is verified through the NEAR memo and Ethereum transfer recipient.

The new source deposit addresses have zero canonical USDT at the selected pre-settlement boundary and zero at their locker-deposit block end. These bounded states do not establish an exhaustive lifetime balance history or an exclusive identity of fungible tokens. G012 already documented substantial pre-existing DAI in B; later spending is not assigned exclusively to these receipts.

Unexplained same-asset arithmetic residuals: zero in the stated reconciliations. Complete cross-chain payout attribution remains SUPPORTED. Verified unauthorized loss and cross-asset loss residual: undetermined, represented as null rather than zero.
