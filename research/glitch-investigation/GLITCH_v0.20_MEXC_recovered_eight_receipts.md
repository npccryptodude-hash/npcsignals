# NPCsignals — GLITCH / ZYROX v0.20 MEXC eight-transfer recovered evidence

**Date:** 2026-10-14. **Source:** User-supplied ChatGPT Work recovered checkpoint, reporting eight cached finalized Solana RPC result objects and status records. Underlying receipt export / offline verification script was linked in Work but is not copied into this repository by this commit. Full original HTTP/JSON-RPC envelopes were not preserved.

## Exact address attribution

Official MEXC wallet-address announcement dated 2022-12-13 lists `USDT | SOL | ASTyfSima4LLAdDgoFGkgqoKowG1LZFDr9fAQrg7iaJZ`. Work retrieved indexed original announcement row but did not capture complete live HTML table. Public listed-address attribution **CONFIRMED as reported**, exchange-related withdrawal interpretation **SUPPORTED**. No customer identity follows from the wallet listing.

Source wallet and USDT transfer authority / sole signer / fee payer for every transfer:
`ASTyfSima4LLAdDgoFGkgqoKowG1LZFDr9fAQrg7iaJZ`

Source token account: `5Q3tXXmEMxPiSDF3THqaxf4XkWac1B1JNXWGBiB8mYeP`
Destination token account: `F98MY9Y7Lzn4cxn1SLXDNZNXyNRbqUSmFNWQkvu2CQ7Z`
Destination historical owner: `8HCSEeC98fR2BcDs8mkyiRq3ahSc7GNEqNEsW5oWote2`
USDT mint: `Es9vMFrzaCERmJfrF4H2FYD4KCoNkY11McCe8BenwNYB`

All eight: SPL Token `transferChecked`, outer instruction index 0, `meta.err=null`, archived signature status finalized, fee 20,232 lamports (paid by ASTyf).

## Complete eight-signature instruction ledger

| ID | UTC | Slot | USDT | Signature |
|---|---|---:|---:|---|
| H146 | 2025-08-28 09:32:05 | 363045296 | 21.500000 | `2b82H9M7U9tLZQWG41D5Qsfy1NubPsT1Ncs5X5NGXHg4mj49WRr7G7jxQCKg1XCALeLWcaJU1rE4Ciwdz2DDq7WQ` |
| H147 | 2025-08-29 19:22:11 | 363353812 | 26.500000 | `227YEv9ocf8uZ1FEsYMkTTPHQnRMGWNVWZBW2gbkMLyNnjBCX7FbYpJRSnCqqSyuvzbycCaRPHoTjc8CMozcRadr` |
| H148 | 2025-08-30 15:49:04 | 363540114 | 24.500000 | `3ydZPgYvezufdnnfbCUWWjKwFtZ7NGYz8dgDsixANpkDwcC4UuJ9pzLeAW3iSbXXUkw61fkWTPCsFdyEx6RKJwNa` |
| H149 | 2025-08-31 17:57:07 | 363778266 | 17.500000 | `4Y2wtVQ7Pydk5zjCuJPwRf2pG9WGybfatitNvJudZRaa26ME9p5eLgvwcs5Hq1wfbJyvmndFuEnzmdx1eN3PzEkv` |
| H151 | 2025-10-21 16:09:04 | 374867561 | 19.500000 | `5c5hQY21Ce7jEkBh6AhHBpYyJkMQ4KwVfadhnYsxn2bHrgiXmt24ens5VSBuR9fMpt1pqxqYXyjxGKxrL4LDx1M2` |
| H153 | 2025-10-23 17:03:11 | 375309766 | 29.500000 | `nQE1Kf9iarnsHJevofva62xPKuZatR3vSMmMYQ5k2kC1FbmXbWkB84uuNPA624VDZMX6Ji6f8hUSsMiuwY2mkd4` |
| H154 | 2025-10-25 13:22:07 | 375711428 | 36.500000 | `5caTYw7en7BvY8oRzjuQyLMoPDT3LQcU36fFTwu5j2vSz7EaWyB8GiktVWQmqzUq1utyEQoKGXPH24W5zhh62cvc` |
| H155 | 2025-10-30 17:13:04 | 376832239 | 301.942575 | `2bwfeRx2TP8RdFMU6NhBaAsLBxxKQ8zrRBTch8iyZFHc4FczthxNAGjXSnD447qq3RLHf6LmRcMeKsoSYKkBrtD1` |

## Historical six-decimal USDT balance deltas

| ID | Source before | Source after | Recipient before | Recipient after |
|---|---:|---:|---:|---:|
| H146 | 3957662.042445 | 3957640.542445 | 0.000000 | 21.500000 |
| H147 | 4529159.921206 | 4529133.421206 | 21.500000 | 48.000000 |
| H148 | 4201155.826580 | 4201131.326580 | 48.000000 | 72.500000 |
| H149 | 3162522.983290 | 3162505.483290 | 72.500000 | 90.000000 |
| H151 | 4988346.854611 | 4988327.354611 | 0.000000 | 19.500000 |
| H153 | 4634685.673723 | 4634656.173723 | 0.000000 | 29.500000 |
| H154 | 4279815.378543 | 4279778.878543 | 29.500000 | 66.000000 |
| H155 | 3315266.427655 | 3314964.485080 | 66.000000 | 367.942575 |

Sum token transfers **477,442,575 raw units = 477.442575 USDT**; source deltas -477.442575, destination +477.442575, fee 8 × 20,232 = **161,856 lamports**, paid by MEXC-listed sender. Historical pre/post owner fields were reviewed for source and destination. Balances between these eight receipts are **not continuous**; intervening destination account activity existed.

## Evidence classification and scope

- **CONFIRMED in Work's preserved finalized receipts:** eight exact direct transfers and balanced amounts / owner mappings; total 477.442575 USDT.
- **CONFIRMED from indexed official publication (Work-reported, full live HTML not preserved):** ASTyf published in MEXC wallet list.
- **SUPPORTED:** exchange infrastructure transfers compatible with withdrawals.
- **UNRESOLVED:** which MEXC customer or account instructed payments; whether the recipient 8HCSEe is a MEXC customer; any relationship of a MEXC customer to 6hR7, ZYROX or GLITCH operators.
- **NOT ASSESSED:** MEXC internal logs / KYC / bank or customer information.

The recovered data is an **important infrastructure and reproducibility finding**, not a real-world operator identification. The original user said Work offered a downloadable evidence export and offline script, but the bytes of that archive are not present in this repository; obtain them separately for complete third-party replay.
