# NPCsignals — ZYROX / GLITCH Exchange Attribution Ledger v0.1

Date: 2026-10-14. Scope: public exchange/service attribution; evidence-led transfer anchors. Objective is to make future *authorized* provider compliance and law-enforcement examination possible, not to infer private customer records from the chain.

## Evidence classifications

- **CEX_OUTBOUND**: verified transfer **from** a published exchange-controlled wallet to a case counterparty. This is NOT a deposit of case proceeds into the exchange.
- **CEX_INBOUND**: verified transfer from case-linked wallet **to** an independently attributed exchange-controlled receiving address; strongest candidate for an internal customer-credit record. None yet documented.
- **INDIRECT_CEX**: case addresses have a transactional relationship to another wallet that interacts with a CEX, without proof the same funds traversed all edges.
- **PROVIDER_SERVICE**: hosted transaction/fee payer infrastructure. Not evidence of a customer account or wallet ownership.
- **UNRESOLVED**: customer, operator, beneficial owner, bank/KYC record and specific causation/flow of commingled funds.

## EA001 — MEXC published wallet → 8HCSEe, eight USDT transfers

**Class:** CEX_OUTBOUND at direct edge; INDIRECT_CEX with respect to ZYROX/GLITCH token launches.

MEXC-published Solana USDT wallet:
`ASTyfSima4LLAdDgoFGkgqoKowG1LZFDr9fAQrg7iaJZ`

Source USDT token account:
`5Q3tXXmEMxPiSDF3THqaxf4XkWac1B1JNXWGBiB8mYeP`

Recipient USDT token account:
`F98MY9Y7Lzn4cxn1SLXDNZNXyNRbqUSmFNWQkvu2CQ7Z`

Recipient historical token-account owner:
`8HCSEeC98fR2BcDs8mkyiRq3ahSc7GNEqNEsW5oWote2`

USDT mint: `Es9vMFrzaCERmJfrF4H2FYD4KCoNkY11McCe8BenwNYB`

All eight Work-preserved finalized successful receipts: SPL Token transferChecked, outer instruction index 0, signer, transfer authority and fee payer ASTyf. Each transaction fee 20,232 lamports. Amount reconciled to 477.442575 USDT.

| Evidence ID | UTC | Slot | USDT | Signature |
|---|---|---:|---:|---|
| H146 | 2025-08-28 09:32:05 | 363045296 | 21.500000 | `2b82H9M7U9tLZQWG41D5Qsfy1NubPsT1Ncs5X5NGXHg4mj49WRr7G7jxQCKg1XCALeLWcaJU1rE4Ciwdz2DDq7WQ` |
| H147 | 2025-08-29 19:22:11 | 363353812 | 26.500000 | `227YEv9ocf8uZ1FEsYMkTTPHQnRMGWNVWZBW2gbkMLyNnjBCX7FbYpJRSnCqqSyuvzbycCaRPHoTjc8CMozcRadr` |
| H148 | 2025-08-30 15:49:04 | 363540114 | 24.500000 | `3ydZPgYvezufdnnfbCUWWjKwFtZ7NGYz8dgDsixANpkDwcC4UuJ9pzLeAW3iSbXXUkw61fkWTPCsFdyEx6RKJwNa` |
| H149 | 2025-08-31 17:57:07 | 363778266 | 17.500000 | `4Y2wtVQ7Pydk5zjCuJPwRf2pG9WGybfatitNvJudZRaa26ME9p5eLgvwcs5Hq1wfbJyvmndFuEnzmdx1eN3PzEkv` |
| H151 | 2025-10-21 16:09:04 | 374867561 | 19.500000 | `5c5hQY21Ce7jEkBh6AhHBpYyJkMQ4KwVfadhnYsxn2bHrgiXmt24ens5VSBuR9fMpt1pqxqYXyjxGKxrL4LDx1M2` |
| H153 | 2025-10-23 17:03:11 | 375309766 | 29.500000 | `nQE1Kf9iarnsHJevofva62xPKuZatR3vSMmMYQ5k2kC1FbmXbWkB84uuNPA624VDZMX6Ji6f8hUSsMiuwY2mkd4` |
| H154 | 2025-10-25 13:22:07 | 375711428 | 36.500000 | `5caTYw7en7BvY8oRzjuQyLMoPDT3LQcU36fFTwu5j2vSz7EaWyB8GiktVWQmqzUq1utyEQoKGXPH24W5zhh62cvc` |
| H155 | 2025-10-30 17:13:04 | 376832239 | 301.942575 | `2bwfeRx2TP8RdFMU6NhBaAsLBxxKQ8zrRBTch8iyZFHc4FczthxNAGjXSnD447qq3RLHf6LmRcMeKsoSYKkBrtD1` |

**Public primary attribution:** MEXC's own 2022-12-13 wallet address publication lists the exact Solana-USDT address:
https://support.mexc.com/hc/ja/articles/13459541357209-MEXC%E3%82%A6%E3%82%A9%E3%83%AC%E3%83%83%E3%83%88%E3%82%A2%E3%83%89%E3%83%AC%E3%82%B9

**Reproducibility:** eight complete signatures and balance deltas in `research/glitch-investigation/GLITCH_v0.20_MEXC_recovered_eight_receipts.md`. Work offered cached parsed receipt files, finality records and an offline checker, but the actual archive has not been copied into this repository.

**Critical limitation:** No MEXC customer ID, account, deposit tag, customer withdrawal request, bank identity or linked GLITCH/ZYROX sale proceeds has been verified. MEXC outgoing transaction ≠ proof of 8HCSEe's MEXC account ownership.

## EA002 — Circle Gas Station sponsored transaction

**Class:** PROVIDER_SERVICE, **not** CEX.

Circle-listed fee payer reported by Work: `6nvUkyJG5j6rH3Hfm15mJNgPMJ1cxHQapfm5K3k647iv`. Oct 3 USDC sender and transfer authority was `8HCSEeC98fR2BcDs8mkyiRq3ahSc7GNEqNEsW5oWote2`; the fee payer was 6nvUky; recipient owner `AVUbPESe87nx9DqhJp2Xi5x8omd4bT9TRod9dk2P31yD`. Signature `56DhD8nNeLGxNzsTNQDQAEymkAgpfayANggNKxN8K4rqrG7rC41PB7JxoPWkevv7QpWPpoV2yw7ETJbrXQhz8to2`. Token transfer 159.006259 USDC. This does not establish a common operator or CEX account.

## EA003 — GLITCH/ZYROX proceeds trace, exchange destination NOT YET CONFIRMED

GLITCH seller `8hiMXA1UHYUAeW6gd6q1XQLWzZkQL48znqgdgY1388B7` sold ~594.97m GLITCH for 132.890991957 WSOL; unwrapped, commingled with existing SOL; sent 150.173828355 SOL to B `F2khA1QZooUzidyycMzpJ6x38eQBxuDq4UrvdUUiSwuo`, which later paid 435.460959353 SOL to cross-case wallet `6hR7GwHpdHbJgNJAagm64KMsMYu8mR6ExzmbE5N8wv1N` using a mixed balance. This is a confirmed address-level route, NOT an exact 132.89 SOL exclusive trace. No verified **case-proceeds → CEX deposit** has been established in this ledger.

## Next test priority

1. Trace outflows from 6hR7 and separately ZYROX sale-proceeds recipients for **direct CEX_INBOUND** routes, preserving signatures, service-address attribution and amounts. Treat wrapped SOL, swaps, fees and mixed balances carefully.
2. Prefer verified original exchange deposit endpoints; verify whether exchange is actual receiver, not merely a previously labeled intermediary.
3. For any CEX_INBOUND, prepare a provider-ready public evidence pack: exact chain, mint, source wallet, receiving address, tx signature, slot, UTC, token amount, token-account historic owner and chain of custody / limitations.
4. If only exchange outgoing payments exist, label them accurately as CEX_OUTBOUND; seek lawfully authorized cooperation for nonpublic customer records.

**No user-facing allegation of a named private person or entity.** Customer identity and beneficial-owner mapping remain UNRESOLVED.
