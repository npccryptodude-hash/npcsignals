# GLITCH v0.6 — Common V-layer funder checkpoint

Source: user-supplied Work findings on 2026-10-13. Work reports finalized Solana mainnet parsed receipts. Underlying JSON receipts not independently re-fetched in this checkpoint.

## C001 — Shared direct funder for ten V-wallets

Common sending wallet: `8CRkgUBFwKTMVD9GoG4uMhE357S1jmZhstkNJxcQNYW4`

Funding transaction: `2LbAoFBq1qDCH2dqrouEsz4GCZqvTRD7mt6ACYNm6CP8AuWwg98ZhXXr72vbRhCQG4UZKC5nEWitXiMyKvSzV39R`

Timestamp `2026-10-12T16:22:10Z`. Work reports finalized, `meta.err=null`, sender sole signer and fee payer, 5,000 lamport fee.

| V ID | Recipient | Outer instruction index | Lamports |
|---|---|---:|---:|
| V01 | `CEhWwatzVBaPMGMpJCLzoeHNEunggaSMFFkZxEUFUh4g` | 1 | 11448924 |
| V02 | `7N8Gu4Cjqsjpkw5k3btHJFUj6E2cdq6ftYGDULtd5BNE` | 2 | 11448924 |
| V03 | `6RDEuQ56YmqRuJfS997xDxDQzquoZNfNwXy5YYNHU5JJ` | 3 | 11448924 |
| V04 | `6FBpQFcEkqb1i76qSpi3Rh1nYTno5WxJvRiufpuN2vA2` | 4 | 11448924 |
| V05 | `BmLqCgzVNrsJ1ozrsih6G2vJtqQ2sBp5V7YP4Dcn1V8i` | 5 | 11448924 |
| V06 | `5n2YNaBQGML8SZz1JrPpvAnaNk4HfocvvCwcCW7XFgCj` | 6 | 11448924 |
| V07 | `6zQR4bDFHG8KeFaQ48qxmNEzdCgrdcz8rw3f5YS3UjjS` | 7 | 11448924 |
| V08 | `84jq4ideiq24E8C1R3f8GA11g2P5Ran9TVUWfNDkGKKs` | 9 | 11448924 |
| V09 | `ChEnvEEZxiKnCJdPB9SVU4brqTavfXv6aaXrAuagHjnH` | 8 | 11448924 |
| V10 | `2rC6iSHXRKzThKPrTBVjQUExupR3GFTP28pR1ePk19US` | 10 | 11448924 |

Reported balance reconciliation:
- 10 × 11,448,924 = 114,489,240 lamports sent by common funder.
- Funding source opening balance 114,494,240 less these transfers and 5,000 fee = 0.
- Each V wallet received 11,448,924 lamports from initial zero balance; then allegedly sent 4 × 2,860,981 lamports and paid 5,000 fee, ending with zero.

## Critical evidence boundary

The supplied Work summary includes the shared funder → V01–V10 transaction reference and numeric V outflow reconciliation, but **not the signatures, destinations or individual instruction indices for V → U01–U10**. Therefore the full uninterrupted `common funder → V → U → A → F → seller` route remains **pending instruction-level documentation of V → U** in the archived evidence, even though Work reports convergence.

The common funding transaction demonstrates shared *transaction-level funding* for V addresses; it does NOT establish common human control, a Kytro relationship, or proceeds beneficiaries.

Work reported no exact address-string hits for the V wallets or shared funder in two existing ZYROX research directories at commit `44c3a4501ad37caee2821fe1a430e8e144fa279b`. This is a bounded negative file search, not an exhaustive on-chain comparison.

## Next bounded checks

1. Retrieve V → U instruction-level signatures, addresses, instruction indices and finalized results; confirm whether V outflows actually land at U01–U10.
2. Preserve the raw JSON receipts.
3. Only then consider tracing the single common funder's prior funding, without implying who operated the addresses.

No ZYROX material changed. No fraud or personal control attribution assessed.
