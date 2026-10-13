# GLITCH v0.13 — Repeated payments to EnVAvXw and USDC correction

**Evidence source:** User-supplied Work checkpoint, 2026-10-13, reporting freshly inspected finalized Solana mainnet parsed receipts and getSignatureStatuses. This file preserves Work's verification; raw RPC JSON is not independently archived here.

Sender S: `6hR7GwHpdHbJgNJAagm64KMsMYu8mR6ExzmbE5N8wv1N`
Recipient owner E: `EnVAvXwCpDCmaSFYpgs5N9BiKhhyV83zWQ6APBKjv92z`

## Four confirmed direct payments to E

| UTC | Asset and amount | Signature | Outer instruction |
|---|---|---|---|
| 2026-10-02 19:26:42 | 100.022387 USDT | `2vj3WSdQ4LRhTzE5EGjutkAfXrtmhLMqaCRxYdAVeJqByPn5GmGsM7YYCASWhFP9uovjydBL91NZFJmtBcu1o51E` | 2 |
| 2026-10-04 18:28:26 | 0.823595201 SOL | `4Dboji6RX29mptKPaSRnpC6a9iipirLGnTw9idLZHiTuDicqSaavefmAKeS73E6yKyg18qUCo5arbqRfKqGMX5d5` | 2 |
| 2026-10-12 18:10:36 | 250.323698 USDT | `5fmbHLLNu5E17uSwrodxe2ZtwENYtGy53nXjJa1GgUqbt1X4TF6GAJ1HNzYhyBme6zSkU1FjLACGCXAFFpiUkvbR` | 2 |
| 2026-10-12 18:11:24 | 801.034319 USDT | `3EQGKm3gwLdcD6LkgEgSdhiTkVzwKx8VJn1rKhCdfNNc9Rm3R7H6v6ZDXSd7a8X8zWDTY5wwcdsm7cQTjYYeWUrm` | 2 |

Work reports S as sole signer and fee payer for all, finalized, meta.err=null. Total payments to E: **1,151.380404 USDT plus 0.823595201 SOL**.

USDT token accounts:
- Source: `8uKAGuxowd2eM4vfzgorTq9dCBZoeSNTpsmLhziziWfK` (historical owner S).
- Destination: `8VTK2SCpGegu4igKdcj1mtc7CagTaKsFHhJqjVeSjv68` (historical owner E).
- Work reports before/after owner fields in historical receipts establish the two owners.

USDT recipient pre → post balance values (raw units, 6 decimals):
- Oct 2: 50,049,037 → 150,071,424.
- Oct 12 18:10:36: 30,000,000 → 280,323,698.
- Oct 12 18:11:24: 280,323,958 → 1,081,358,277.

## CORRECTION — earlier ZYROX v0.44 USDC attribution is unsupported

The 2026-10-03 19:24:08 transaction `2aZLpZFofU3mudj9BqUt6bvT4SY7Hua1JFdGJfFwzuHNY5bRVMLhhUFSBGNeUfM7qj9paAQvQape5oohixdsEXc2` transferred **150.005059 USDC** from S, but its destination token account `j1wVJA3CU9jAHNk1nJ95sU1nk2zLYzmv9xZEYz2YvTC` was owned by **`8HCSEeC98fR2BcDs8mkyiRq3ahSc7GNEqNEsW5oWote2`**, not E, according to pre/post token-balance historical owner fields. This payment **must not be counted as S→E**.

This is an addendum to the existing ZYROX research, NOT a silent alteration of its frozen v0.44 record. The old statement should be cross-referenced to this corrective notice before any public use.

## Limits
- **CONFIRMED WITHIN WORK RPC REVIEW:** repeated direct payments in both research periods; one incorrectly attributed USDC recipient.
- **NO EVIDENCE:** reverse E→S transfer in the five examined receipts. Not an exhaustive wallet history.
- **UNRESOLVED:** purpose of payments; service role, human owners, shared controller, Kytro involvement or exclusive provenance of commingled GLITCH proceeds.

**Next step:** synchronize correction addendum with ZYROX documentation using a non-destructive errata reference, and archive raw finalized receipts before external publication.
