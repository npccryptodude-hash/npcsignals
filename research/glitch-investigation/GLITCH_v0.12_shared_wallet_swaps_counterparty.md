# GLITCH v0.12 — Shared 6hR7 swap activity and ZYROX counterparty

Source: User-provided Work checkpoint, 2026-10-13. Work reports finalized Solana getTransaction and getSignatureStatuses, with ten reviewed receipts, including version 1. Raw RPC JSON not independently re-fetched in this GitHub edit.

## Starting point
Shared wallet: `6hR7GwHpdHbJgNJAagm64KMsMYu8mR6ExzmbE5N8wv1N`
Opening SOL before GLITCH-related B receipt: **316.491815962 SOL**. GLITCH-linked B sent **435.460959353 SOL**; all later balance was commingled.

## Verified within Work's receipt reconstruction
- 2026-10-12 17:55:00 UTC: 6hR7 wrapped/swapped **400 SOL** through route including USDC intermediary, receiving **42,746.888737 USDT** net. Signature `5MTqpwkqCo4UwjfM1inoNi8b9anHB5c8URcey6suT6kWsi7SNGfV5B6aDopzQ6EeK9ryjpy7AZPMtp6EK68UdqwV`.
- 17:55:44 UTC: 6hR7 swapped **5,000 USDT** to **45.984865115 WSOL**, unwrapped to native SOL; signature `5P8ncSAeC7Z1sAvmVf567pb7ZqQNHsPyzB7zghiteZLQW5vXShg5BKzqSBBAUpm3UEtFA6jrPRGUd55aCVzPzGsq`.
- 18:10:36 UTC: **250.323698 USDT** sent from 6hR7-owned token account `8uKAGuxowd2eM4vfzgorTq9dCBZoeSNTpsmLhziziWfK` to token account `8VTK2SCpGegu4igKdcj1mtc7CagTaKsFHhJqjVeSjv68`; signature `5fmbHLLNu5E17uSwrodxe2ZtwENYtGy53nXjJa1GgUqbt1X4TF6GAJ1HNzYhyBme6zSkU1FjLACGCXAFFpiUkvbR`.
- 18:11:24 UTC: **801.034319 USDT** to same token account, signature `3EQGKm3gwLdcD6LkgEgSdhiTkVzwKx8VJn1rKhCdfNNc9Rm3R7H6v6ZDXSd7a8X8zWDTY5wwcdsm7cQTjYYeWUrm`.
- Total external USDT transfer: **1,051.358017 USDT**. Work reports destination token account historical owner `EnVAvXwCpDCmaSFYpgs5N9BiKhhyV83zWQ6APBKjv92z`, exactly previously documented in ZYROX primary ledger v0.44 as a USDT/USDC counterparty of 6hR7. The source's own USDT and USDC accounts also match ZYROX U326/U327. Exact new cross-case counterparty reuse is **reported confirmed**, while human ownership remains unresolved.
- Distinct address `EnVAe5xn8rWHnrhJtBncKGSx6tZiTPtCTZYxUZBJ492z` was a small inbound signer; **not** the recipient owner EnVAvXw... .

## Balance reconciliation
SOL: `316.491815962 + 435.460959353 + 81.344118961 - 400 + 45.984865115 - 0.000051167 - 0.001664394 = 479.280043830`.

USDT: `64502.988313 + 42746.888737 - 5000 - 250.323698 - 801.034319 + 0.000100 = 101198.519133`.

USDC: **69.071398** before and after (net neutral intermediary).
Work reports a finalized snapshot at slot 456510500 for 6hR7 SOL 479.280043830, USDT 101198.519133, USDC 69.071398, temporary WSOL account closed.

## Limits
This is a **cross-case reused wallet and recipient-owner relationship**, not proof that GLITCH sale proceeds funded any particular later swap or transfer. Prior 6hR7 SOL and USDT existed before the GLITCH-linked receipt. The recipient's service role, human ownership, Kytro control and ultimate beneficiary remain **UNRESOLVED**. Work did not trace more hops.

Next focused question: assess historical relationship of 6hR7 with recipient owner EnVAvXw..., using only exact transaction signatures and dates; do not infer common control from repeated transfers.
