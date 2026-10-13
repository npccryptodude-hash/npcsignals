# GLITCH Launch Investigation — v0.1 stopped checkpoint

Status: SOURCE-REPORTED / INDEPENDENT RECEIPT REVALIDATION PENDING
Checkpoint supplied by user from ChatGPT Work session on 2026-10-13. This file preserves that session's reported finalized RPC findings; this commit does not independently re-fetch or authenticate the Solana receipts.

## Scope
Solana mint: `9XxtEBjxj2Z7DZ775foA1iq2zeZdYMKXD6fq8qCNpump`

All clock times CEST (UTC+2) unless specified. This is distinct from research/zyrox-investigation and research/zyrox-investigation-post-freeze. Personal test trades excluded.

## G001 — Reported large sale
- Seller wallet: `8hiMXA1UHYUAeW6gd6q1XQLWzZkQL48znqgdgY1388B7`
- Signature: `5nRVLSVpSVDsmJ22zLL1ywrThq7y4VpybrdJnetbSi2KwTaAao5o7fy9aRPdkjF8tuvLvW21Zn99pBuEqboTjMkE`
- Work-reported finalized receipt: `meta.err=null`, slot `456135129`, timestamp `2026-10-12T17:51:19Z` (19:51:19 CEST)
- Reported sale: `594,968,303.379290 GLITCH`
- Reported WSOL transferChecked: pool quote `96XzgQ9i8fBrRscUUwfNmWzuTqfhJFMGreHDXADMUAZL` -> account `E7JyKtcHWFDKx81SsFpSNrKcNPNhhesbUbL3gGjvUNXh`
- Raw amount: `132890991957`, decimals `9` => `132.890991957 WSOL`
- Work reports closure of WSOL token account to seller wallet, excluding separate pool-fee transfers.
- Gross proceeds, **NOT** net profit.
- Explorer: https://solscan.io/tx/5nRVLSVpSVDsmJ22zLL1ywrThq7y4VpybrdJnetbSi2KwTaAao5o7fy9aRPdkjF8tuvLvW21Zn99pBuEqboTjMkE

## G002 — Creator initial 70M acquisition (reported)
- Creator: `Ft2XtprBymZsGwYUMjsLN6z8WZzguTVa5rFYSuN41S8i`
- Signature: `5xrGXTXnf7ZDe731C7EB5cNVnERshsZhT3E66udWiXmCtzaBGSVbmFygDovhJmzSrvUpG6m1PBRWQcq6S8UT18FV`
- Timestamp: `2026-10-12 18:32:33 CEST`
- Transfer: 70,000,000 GLITCH from curve token account to creator-owned token account `3G8nF6vv8PXMxs5YkygH7eTUPA4A85QZvJXJj58Yh965`
- Explorer: https://solscan.io/tx/5xrGXTXnf7ZDe731C7EB5cNVnERshsZhT3E66udWiXmCtzaBGSVbmFygDovhJmzSrvUpG6m1PBRWQcq6S8UT18FV

## G003 — Creator-to-collector transfer (reported)
- Signature: `3ttmcRNck85nUEcnaTZ3nmMWpq9sAdCwjq8EF56Zz4wzsi3dz2AB1G18FibKKmqNzShVexFVanogoAUSJeJXojy1`
- Timestamp: `2026-10-12 19:51:18 CEST`
- Work reports co-signed 70,000,000 GLITCH transfer from creator account above to collector-owned token account `2kCcBigGMmdbqRUGfzprxiwMX9EQvKdPUQWRrjf8qpwx`
- Explorer: https://solscan.io/tx/3ttmcRNck85nUEcnaTZ3nmMWpq9sAdCwjq8EF56Zz4wzsi3dz2AB1G18FibKKmqNzShVexFVanogoAUSJeJXojy1

## G004 — Historical token account owner verification (Work follow-up, 2026-10-13)
The user supplied a separate follow-up from Work stating it **independently inspected its previously collected finalized Solana JSON-RPC getTransaction receipt** for signature `3ttmcRNck85nUEcnaTZ3nmMWpq9sAdCwjq8EF56Zz4wzsi3dz2AB1G18FibKKmqNzShVexFVanogoAUSJeJXojy1`.

- Slot: `456135125`; timestamp: `2026-10-12T17:51:18Z`; `meta.err=null`.
- `transaction.message.accountKeys[8].pubkey` = destination `2kCcBigGMmdbqRUGfzprxiwMX9EQvKdPUQWRrjf8qpwx`.
- `meta.preTokenBalances` at `accountIndex:8` identifies token-account `owner: 8hiMXA1UHYUAeW6gd6q1XQLWzZkQL48znqgdgY1388B7`.
- `meta.postTokenBalances` at `accountIndex:8` independently reports the same owner.
- Outer instruction 1 `Associated Token Account createIdempotent` names the destination and wallet owner consistently. Because a pre-balance exists, **this is not proof of first initialization**. `innerInstructions` empty.
- **Finding (receipt-verified as reported by Work):** the creator's 70M token transfer went directly into an SPL token account belonging to the identified large seller wallet, one second before its reported large sale. There is no necessary intermediate collector-to-seller transfer; the "collector" is the seller's owned token account.
- **Scope limitation:** historical token-account ownership is technical account ownership, NOT evidence of human identity, Kytro control, common ultimate beneficiary, net profit, or a fully traced token-level sale allocation.
- **Audit limitation:** This GitHub update records Work's exact reported parsed-receipt fields; the raw receipt was not independently re-fetched or attached during this edit.

## Resolved provenance gap
Previous checkpoint left destination token-account ownership unidentified. G004 supplies explicit historical pre/post token-balance owner fields establishing the wallet mapping (as independently inspected within Work). The ownership-mapping question is **resolved on Work's receipt evidence**, with raw JSON export/reproduction still outstanding.

## Additional user screenshot observations (not chain verified here)
- Around 19:29 CEST, X screenshot shows @KytroCrypto advertising GLITCH as “THE NEXT 1000x RUNNER”.
- FEYN screenshot displays "SCAM DETECTED", claims 90 insider wallets / 68.5% bought, and mentions bundled curve completion, relay-funded buyer network and majority launch-block supply.
- 19:35 screenshot: approx $215,550 market cap / 823 holders.
- ~20:05 screenshot: approx $12,380 market cap / 876 holders.
- Telegram later displayed an edited post attributing decline to sellers.
- Promotional X post no longer visible in observed profile; URL/post ID not recovered and deletion NOT confirmed.

## Evidence status
- OBSERVED: User-provided images and textual Work stopped checkpoint.
- CLAIMED BY WORK AS RECEIPT-VERIFIED: G001, G002, G003 (signature-linked; re-fetch pending).
- UNRESOLVED: raw receipt export and independent second-client reproducibility; exact Kytro control; human ownership; beneficiaries; net profit; ranking of sellers; FEYN wallet set and 68.5% figure; X deletion status; ZYROX overlap.
- NOT ASSESSED: Legal fraud or coordination allegations.

## Next strictly scoped task
Preserve raw finalized RPC JSON receipts for G001–G004 with reproducible token/WSOL balance deltas, then independently confirm the creator-to-seller token-account ownership mapping. Do not infer human control, token-level sale allocation or net profit solely from wallet ownership.
