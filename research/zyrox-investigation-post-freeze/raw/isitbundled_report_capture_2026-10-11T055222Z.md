# IsItBundled rendered-report capture — ZYROX

- Capture UTC: `2026-10-11T05:52:22Z`
- Report URL: <https://isitbundled.com/FACvJMFBWQ1GYm9dgZ7XHvs85V1EcK2SqHf534kspump>
- API documentation: <https://isitbundled.com/api>
- Mint: `FACvJMFBWQ1GYm9dgZ7XHvs85V1EcK2SqHf534kspump`
- Evidence class: `THIRD-PARTY REPORT`; not a primary-chain substitute.

## Rendered fields captured

| Field | Rendered value |
|---|---:|
| Risk | HIGH |
| Made with Proxima | yes |
| Known bundlers | 2 |
| Bundled at launch | 82% |
| Bought in first second | 82% |
| Creator bought | 10% |
| SOL spent | 97.71 |
| Launch-block buys | 3 |
| Creator-linked wallets | 88 |
| Proxima-labelled wallets | 87 |
| All listed wallets | 104 |
| Hand-offs | 66 |
| Bundle already sold | 88% |
| Insiders hold now | 0% |
| Caught-wallet buys | 806.3 SOL |
| Caught-wallet sales | 848.5 SOL |
| Peak shown in first-seven-minute chart | $466.7K |

The report separately states that 100% of what insiders gathered was “sold or moved”. This is not the same metric as the 88% “bundle already sold” field or the 0% current-holdings field.

## Launch transactions exposed by the report

| Role | FACv share / site SOL | Transaction |
|---|---:|---|
| Creator create + buy | 10% / site summary 3.1 SOL | `5ubvNRPDbdXtHaiexB4zroZxUDFS9mwDmDwJ3HnvdGrxuiqxDDGsZnkjdAGVHysDZgiCFqVASoinDu1bADPAbowo` |
| Creator-side bundled buy | 69.31% / 81.922 SOL | `52ZjUbg4bzdQoAsFeJuLgqM5b5kmeQpgp79ndnAi13D7W795N8A7BLon9t7LhENRi5wUGcqMb5RWzNDs2AB9nKkw` |
| Creator-side bundled buy | 2.69% / 12.704 SOL | `4JrhsmKT44mQpZh5kTYFMcFWXi2Hu8Lg3U5BkUS4WEw66pWeR7GkiR299KY2WFD5XZQTH5pvBMW957WrdjjRh5Xf` |

The report's “proof” link for its Proxima statement targets program account `8gxk64hYgGAEnHVhRMvBGVvBXZM5WhkGkaQ6DVgVV2kn`.

## Site methodology statement captured

The rendered footer says the scan read 4,000 transactions in the first seven minutes and then followed 88 “insider” wallets for six hours. It reports a 24.6-second check and warns that links may be missed and coincidences are possible. The API documentation defines `bundledPct`, `creatorBundlePct`, `otherBundlesPct`, `firstSecondPct`, `devBoughtPct`, `bundleWallets`, `fundedTogether`, `throwawayFunded`, `insidersHoldPct`, and `flaggedHoldPct`, and documents wallet-role labels such as `creator`, `bundle`, `proxima`, `handoff`, `got_tokens`, `linked`, `first_second`, and `sniper`.

## Red-flag assertions requiring independent evidence

- 87 wallets were described by the site as using Proxima under one operator, with 170 trades including the creator.
- Three bundle wallets were described as funded within the same minute through separate temporary relays.
- The site asserts 66 matched sell/buy events involving fresh wallets.
- The site asserts two rounds of temporary-wallet token hops.

These statements are preserved as third-party assertions. The capture does not itself provide the 66 source/destination signature pairs or a complete machine-readable methodology for the matching heuristic.

## Address export

The rendered “Copy 104 wallets” list was expanded and every first-column Solscan account URL was read in displayed order. The exact export is stored in `isitbundled_zyrox_104_wallets_2026-10-11T055222Z.csv`. The list contains launch-slot wallets, later Proxima/handoff-labelled wallets, snipers, and six `Linked` wallets; inclusion must not be treated as common beneficial ownership.
