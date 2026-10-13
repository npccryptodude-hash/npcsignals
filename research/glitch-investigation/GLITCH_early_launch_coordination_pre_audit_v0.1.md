# NPCsignals GLITCH — Early launch coordination pre-audit v0.1

Date: 2026-10-13. Source: existing GitHub GLITCH v0.1, v0.2, v0.3, v0.5, v0.6, and user-supplied Work finalized-receipt checkpoints. **No new RPC transactions decoded in this file.**

## Key timing (UTC; CEST +2)
- `2026-10-12T16:22:10Z`: common wallet `8CRkgUBFwKTMVD9GoG4uMhE357S1jmZhstkNJxcQNYW4` funded ten V wallets with 11,448,924 lamports each, signature `2LbAoFBq1qDCH2dqrouEsz4GCZqvTRD7mt6ACYNm6CP8AuWwg98ZhXXr72vbRhCQG4UZKC5nEWitXiMyKvSzV39R`.
- 16:22:10–16:22:27Z: reported V→U→A–J→F funding cascade, ten wallets in each layer, each intermediate sends four transfers and spends 5,000 lamports fee, balances end at zero.
- `16:22:25–16:22:27Z`: F001–F010 send ten equal `0.011428924 SOL` transfers to **the eventual major seller** `8hiMXA1UHYUAeW6gd6q1XQLWzZkQL48znqgdgY1388B7`. Total 0.114289240 SOL.
- `16:32:33Z`: first documented creator acquisition, 70,000,000 GLITCH by `Ft2XtprBymZsGwYUMjsLN6z8WZzguTVa5rFYSuN41S8i`, signature `5xrGXTXnf7ZDe731C7EB5cNVnERshsZhT3E66udWiXmCtzaBGSVbmFygDovhJmzSrvUpG6m1PBRWQcq6S8UT18FV`.
- `17:51:18Z`: creator → seller-owned GLITCH token account 70m transfer, signature `3ttmcRNck85nUEcnaTZ3nmMWpq9sAdCwjq8EF56Zz4wzsi3dz2AB1G18FibKKmqNzShVexFVanogoAUSJeJXojy1`.
- `17:51:19Z`: seller sale 594,968,303.379290 GLITCH for gross 132.890991957 WSOL, signature `5nRVLSVpSVDsmJ22zLL1ywrThq7y4VpybrdJnetbSi2KwTaAao5o7fy9aRPdkjF8tuvLvW21Zn99pBuEqboTjMkE`.

## Interpretation and major gap

The repeated exact-sized transfers among many temporary wallets and deterministic fee-adjusted balances strongly support an **automated or carefully structured funding process**, before the known creator acquisition. Crucially **F wallets are funded intermediaries that sent SOL to the seller; no report yet demonstrates that V/U/A/F wallets were themselves GLITCH token buyers.** The patterned source-to-seller graph cannot be called a 40-buyer or 90-insider cluster. The 68.5% / 90-wallet FEYN screenshot is a scanner claim, not an independently reproduced attribution.

Creator's 70m transfer directly to a seller-owned token account is a distinct stronger observable operational linkage, but source of the 594.97m sold inventory has not been fully identified.

## Exact follow-up questions that can be tested on finalized receipts
1. Anchor exact launch mint/curve initialization slot and earliest public GLITCH purchase transaction order, then enumerate purchases during first minute and first five minutes.
2. Resolve every **buyer**, token owner, purchase quantity, timestamp, slot, signature and signer; do not count token accounts as separate humans.
3. Intersect buyers' full **owner pubkeys** with all documented funding-layer wallets and seller/creator accounts.
4. Quantify initial unique token supply acquired by those overlapping buyers, but do not divide gross resales by initial supply.
5. Test direct funder and common-authority links among early buyers separately from common Jito/tip/payment-program overlaps.
6. If none of V/U/A/F were buyers, record that null and separately assess their exact role in seller funding.
7. Preserve any original full-frame fair-launch promises and exact post timestamps; do not manufacture a pledge from recollection.

## Status
**SUPPORTED:** systematically organized seller pre-funding. **CONFIRMED AS REPORTED BY WORK:** timestamped flows, creator transfer into seller-owned token account, major sale. **UNRESOLVED:** buyer count and coordinated early accumulation, beneficial owner, Kytro control, fairness claims. **NOT ASSESSED:** criminal fraud.
