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

## Critical provenance gap
The stopped Work checkpoint concludes that the creator's 70M tokens **reached the seller wallet immediately before the large sale**. However, the supplied text shows creator -> collector TOKEN ACCOUNT and separately identifies the seller wallet. It does **not** give the collector token-account owner, a collector -> seller transaction signature, or a demonstrated account-ownership link. **Thus creator -> sale-wallet attribution is NOT YET INDEPENDENTLY ESTABLISHED BY THE DATA PRESENTED HERE.** Resolve with exact account owners and full movement proof before making this claim publicly.

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
- UNRESOLVED: creator/collector/seller account-control chain; exact Kytro control; human ownership; beneficiaries; net profit; ranking of sellers; FEYN wallet set and 68.5% figure; X deletion status; ZYROX overlap.
- NOT ASSESSED: Legal fraud or coordination allegations.

## Next strictly scoped task
Re-fetch **only** the three signatures and their token account owner mappings from independent finalized Solana RPC. Document whether `2kCc...` token account belongs to `8hiMX...` or provide missing transfer path. Preserve raw JSON and reproducible balance deltas. Do not extrapolate ownership based on timing.
