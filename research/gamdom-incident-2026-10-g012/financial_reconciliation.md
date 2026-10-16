# Financial accounting

All canonical BNB USDT and Ethereum DAI amounts use 18 decimals. Arithmetic uses integer raw units; no floating-point sums or USD-loss assumption is used.

| Item | Route 1 raw | Route 2 raw | Asset / meaning |
| --- | ---: | ---: | --- |
| B source debit | 3296947360645719000000 | 3947417222165521700000 | BNB USDT principal |
| Unique deposit credit | 3296944723631957632111 | 3947414585151760332111 | BNB USDT, source-chain buy consideration |
| Debit minus deposit | 2637013761367889 | 2637013761367889 | USDT; API executedFee, on-chain sell/buy difference |
| Trade event feeAmount | 0 | 0 | Distinct from API executedFee |
| NEAR DAI withdrawal | 3294176314118353387030 | 3947797560500152030405 | Wrapped Ethereum DAI |
| Reported withdrawal fee | 300000000000000000 | 300000000000000000 | DAI; protocol status service |
| Ethereum DAI to B | 3293876314118353387030 | 3947497560500152030405 | Observed canonical DAI receipt |
| DAI withdrawal less fee less receipt | 0 | 0 | Exact arithmetic, mapping remains SUPPORTED |

Source total: **7244.364582811240700000 USDT** = **7244.359308783717964222 USDT deposits** + **0.005274027522735778 USDT difference**. Residual: zero, within source-chain token transfers. Ordered Transfer events inside settlements are not additional principal.

Ethereum receipts total **7241.373874618505417435 DAI**. The two wrapped-DAI withdrawals total 7241.973874618505417435 DAI, less protocol-reported 0.6 DAI withdrawal fees. These are different assets from source USDT. A numerical USDT-minus-DAI difference is neither a verified fee nor a verified loss. No historical market-price source is used; archived API USD estimates are unvalidated service valuations, not NPCsignals valuations.

NEAR intent events independently expose source-token fees of 3296944723631958 and 3947414585151761 raw units. The respective source-token net counterparty receipts are 3296941426687234000153 and 3947410637737175180350; each sum reconciles exactly to its deposit. Counterparty DAI/USDT fees in the same atomic batch are recorded in `near_execution_register.json`; they are not counted as additional B outflows. Quote output, minimum output and API refundFee are not substituted for executed output. API reports zero refunds; no exhaustive independent lifetime refund search is claimed.

Settlement gas was paid by each solver, not B: 7420545000000 and 7497325000000 native wei. Ethereum payout initiator paid 24709124638560 and 23352324919006 wei. These receipt-derived fees are separate from token principal. B's presignature gas belongs to the previously recorded G011 transaction, not an additional settlement principal loss.

## Prior balances and mixing

New historical DAI balanceOf calls and all canonical DAI Transfer logs involving B within each receipt block reconcile opening plus incoming minus outgoing to closing with zero residual. Immediately before the first receipt B already held 397182.046690514776816479 DAI; before the second it held 476525.166133649988746401 DAI. There is exactly one B-involving DAI transfer in each selected block. Those ordered logs establish transaction-local pre-receipt amounts rather than substituting current balances.

No onward spending is assigned exclusively to either receipt. Other balances/inflows exist and fungible tokens do not preserve identities after mixing. Source BNB balances and S1 funding were already reconstructed in G011 and are not repeated here.

Verified unauthorized loss: **undetermined**, not zero. Unknown consideration and cross-asset loss residuals remain null in the machine-readable totals; zero is used only for demonstrated same-asset arithmetic residuals. Destination route confidence remains SUPPORTED even though the destination receipt amounts themselves are CONFIRMED.
