# NPCsignals v0.19 — Attribution-oriented infrastructure checkpoint

Date: 2026-10-13. Scope: Public source check, no fresh Solana RPC or customer-level records.

## MEXC: primary-source exact address
MEXC's own public wallet address list identifies `ASTyfSima4LLAdDgoFGkgqoKowG1LZFDr9fAQrg7iaJZ` as a Solana address for USDT, USDC and ETH. Source: https://support.mexc.com/hc/ja/articles/13459541357209-MEXC%E3%82%A6%E3%82%A9%E3%83%AC%E3%83%83%E3%83%88%E3%82%A2%E3%83%89%E3%83%AC%E3%82%B9 . This primary-source address attribution is CONFIRMED for the published list, without proof of current custody status. Work reported 8 finalized USDT transfers totaling 477.442575 USDT from ASTyf to an 8HCSEe-owned token account in 2025; underlying raw receipts remain absent from this checkpoint. No specific MEXC customer attribution follows.

## Circle Gas Station: operation of sponsored transfers
Official Circle documentation describes a fee payer that signs the network-fee authorization separately from the user's transfer authorization; sponsored transfers may be sent using Circle programmable wallets and Gas Station. Circle wallets may be user-controlled or developer-controlled. Sources:
- https://www.circle.com/blog/how-circles-gas-station-uses-fee-payers-to-enable-gasless-transactions-on-solana
- https://www.circle.com/es/blog/how-programmable-wallets-enable-usdc-payments-for-payment-gateway-providers
- https://www.circle.com/wallets

Prior Work-reported Oct 3 transaction signature `56DhD8nNeLGxNzsTNQDQAEymkAgpfayANggNKxN8K4rqrG7rC41PB7JxoPWkevv7QpWPpoV2yw7ETJbrXQhz8to2`: 8HCSEe was USDC transfer authority and signer, AVUb owner of receiving token account, 6nvUky fee payer and second signer. Work reports 6nvUky appears in Circle's fee payer address list; the exact published address entry is not independently preserved here. Therefore Circle service interpretation SUPPORTED (exact address list claim Work-reported), but there is no identified app, Circle customer, wallet creation model, human controller or ultimate beneficiary.

## Conclusion and next evidentiary goal
The MEXC and Circle infrastructure touchpoints are different types of evidence. A MEXC-published sending wallet is not evidence that either ZYROX or GLITCH operators are MEXC employees/customers. A Circle fee sponsor is not evidence of common control with the asset sender. Both may provide potential organization-level audit records unavailable publicly.

Before larger attribution claims: preserve 8 full MEXC transfer signatures/receipts, original Circle list containing 6nvUky, and the complete 216-row 8HCSEe instruction ledger; test whether 8HCSEe historically used Circle Programmable Wallets and whether any publicly attributed application link exists. Do not infer or publish private individual identity from unnamed exchange customers.
