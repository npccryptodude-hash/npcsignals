# external source-link availability

[quality report](REPORT.md)

checked 15 november 2026 using bounded unauthenticated http get requests. this tests transport availability, not source content, authenticity or agreement with a claim. source fragments and social-media bot restrictions are not validated by a status code. api roots may require post requests; a failed get is not evidence that the api or research is invalid.

| observed result | urls |
| --- | --- |
| 200 | 346 |
| 202 | 1 |
| 400 | 2 |
| 401 | 7 |
| 403 | 9 |
| 404 | 14 |
| 405 | 1 |
| 500 | 1 |
| 503 | 2 |

## sources requiring manual or authenticated review

403 and 401 responses are access restrictions, not proven broken links. 404 responses are dated availability observations, not proof of deletion, wrongdoing or false claims. historical source records remain unchanged; no speculative replacement has been inserted.

- `403` — [https://academic.oup.com/afraf/article/125/499/323/8499740](https://academic.oup.com/afraf/article/125/499/323/8499740)
- `405` — [https://api.hyperliquid.xyz/info](https://api.hyperliquid.xyz/info)
- `400` — [https://arb1.arbitrum.io/rpc](https://arb1.arbitrum.io/rpc)
- `404` — [https://arbitrum.gateway.tenderly.co](https://arbitrum.gateway.tenderly.co)
- `404` — [https://boldnet.twstalker.com/Zyrox0x/status/2104673752521003441](https://boldnet.twstalker.com/Zyrox0x/status/2104673752521003441)
- `404` — [https://bsc-dataseed.binance.org](https://bsc-dataseed.binance.org)
- `403` — [https://bscscan.com/address/0xe5686AaE44d392aa6A0637FD38393859502F8667#tokentxns](https://bscscan.com/address/0xe5686AaE44d392aa6A0637FD38393859502F8667#tokentxns)
- `400` — [https://bundles.jito.wtf/api/v1/bundles/transaction/{signature}](https://bundles.jito.wtf/api/v1/bundles/transaction/{signature})
- `404` — [https://isitbundled.com/FACvJMFBWQ1GYm9dgZ7XHvs85V1EcK2SqHf534kspump](https://isitbundled.com/FACvJMFBWQ1GYm9dgZ7XHvs85V1EcK2SqHf534kspump)
- `404` — [https://isitbundled.com/api](https://isitbundled.com/api)
- `404` — [https://isitbundled.com/api/v1/token/FACvJMFBWQ1GYm9dgZ7XHvs85V1EcK2SqHf534kspump](https://isitbundled.com/api/v1/token/FACvJMFBWQ1GYm9dgZ7XHvs85V1EcK2SqHf534kspump)
- `404` — [https://mainnet.gateway.tenderly.co](https://mainnet.gateway.tenderly.co)
- `403` — [https://medium.com/@npcsignals/can-gen-z-turn-protest-into-power-527f688367c8](https://medium.com/@npcsignals/can-gen-z-turn-protest-into-power-527f688367c8)
- `403` — [https://medium.com/@npcsignals/distribution-depth-is-not-evidence-depth-f449cdde3796](https://medium.com/@npcsignals/distribution-depth-is-not-evidence-depth-f449cdde3796)
- `403` — [https://medium.com/@npcsignals/six-wallets-seven-signers-one-transaction-4c95601a555a](https://medium.com/@npcsignals/six-wallets-seven-signers-one-transaction-4c95601a555a)
- `403` — [https://medium.com/@npcsignals/who-is-gen-z-part-4-d3dcfee0f7c8](https://medium.com/@npcsignals/who-is-gen-z-part-4-d3dcfee0f7c8)
- `403` — [https://medium.com/@npcsignals/who-is-gen-z-part-5-94dc2565a637](https://medium.com/@npcsignals/who-is-gen-z-part-5-94dc2565a637)
- `404` — [https://solscan.io/tx/](https://solscan.io/tx/)
- `404` — [https://twstalker.com/ExploitedSOL/status/2009642067983761454](https://twstalker.com/ExploitedSOL/status/2009642067983761454)
- `404` — [https://web.archive.org/web/20261002114902/https://t.me/SolanaInsiderTerminal/1009](https://web.archive.org/web/20261002114902/https://t.me/SolanaInsiderTerminal/1009)
- `503` — [https://www-qa.servel.cl/2025/07/22/padron-electoral-provisorio-2025/](https://www-qa.servel.cl/2025/07/22/padron-electoral-provisorio-2025/)
- `403` — [https://www.ed.gov/about/news/press-release/us-department-of-education-releases-latest-foreign-funding-disclosures-federally-funded-american-universities](https://www.ed.gov/about/news/press-release/us-department-of-education-releases-latest-foreign-funding-disclosures-federally-funded-american-universities)
- `500` — [https://www.energie-mines.gov.bf/accueil/details?cHash=7640c11bbc0535fd7286d630bf593eab&tx_news_pi1%5Baction%5D=detail&tx_news_pi1%5Bcontroller%5D=News&tx_news_pi1%5Bnews%5D=369](https://www.energie-mines.gov.bf/accueil/details?cHash=7640c11bbc0535fd7286d630bf593eab&tx_news_pi1%5Baction%5D=detail&tx_news_pi1%5Bcontroller%5D=News&tx_news_pi1%5Bnews%5D=369)
- `401` — [https://www.reuters.com/legal/government/un-sees-no-budget-cuts-2027-after-us-welcomes-cash-saving-steps-2026-07-07/](https://www.reuters.com/legal/government/un-sees-no-budget-cuts-2027-after-us-welcomes-cash-saving-steps-2026-07-07/)
- `401` — [https://www.reuters.com/world/africa/forget-democracy-burkina-faso-military-leader-traore-says-2026-04-03/](https://www.reuters.com/world/africa/forget-democracy-burkina-faso-military-leader-traore-says-2026-04-03/)
- `401` — [https://www.reuters.com/world/berlins-acute-housing-shortage-soaring-rents-dominate-city-election-2026-09-18/](https://www.reuters.com/world/berlins-acute-housing-shortage-soaring-rents-dominate-city-election-2026-09-18/)
- `401` — [https://www.reuters.com/world/europe/merz-under-pressure-two-more-german-states-go-polls-2026-09-20/](https://www.reuters.com/world/europe/merz-under-pressure-two-more-german-states-go-polls-2026-09-20/)
- `401` — [https://www.reuters.com/world/far-left-party-wins-berlin-election-pledging-nationalise-housing-2026-09-20/](https://www.reuters.com/world/far-left-party-wins-berlin-election-pledging-nationalise-housing-2026-09-20/)
- `401` — [https://www.reuters.com/world/germanys-far-right-afd-seeks-landmark-state-victory-saxony-anhalt-votes-2026-09-06/](https://www.reuters.com/world/germanys-far-right-afd-seeks-landmark-state-victory-saxony-anhalt-votes-2026-09-06/)
- `401` — [https://www.reuters.com/world/middle-east/usaid-analysis-found-no-evidence-massive-hamas-theft-gaza-aid-2025-07-25/](https://www.reuters.com/world/middle-east/usaid-analysis-found-no-evidence-massive-hamas-theft-gaza-aid-2025-07-25/)
- `403` — [https://www.tn.gov/correction/news/2026/9/30/media-advisory--christa-pike--261368.html](https://www.tn.gov/correction/news/2026/9/30/media-advisory--christa-pike--261368.html)
- `503` — [https://www.tn.gov/governor/news/2026/5/21/gov--lee-grants-temporary-reprieve-for-tony-von-carruthers.html](https://www.tn.gov/governor/news/2026/5/21/gov--lee-grants-temporary-reprieve-for-tony-von-carruthers.html)
- `202` — [https://www.un.org/sg/en/content/sg/statements/2025-10-17/secretary-generals-remarks-the-fifth-committee-of-the-general-assembly-the-proposed-programme-budget-for-2026](https://www.un.org/sg/en/content/sg/statements/2025-10-17/secretary-generals-remarks-the-fifth-committee-of-the-general-assembly-the-proposed-programme-budget-for-2026)
- `404` — [https://x.com/KytroCrypto](https://x.com/KytroCrypto)
- `404` — [https://x.com/Zyrox0x/status/2104673752521003441](https://x.com/Zyrox0x/status/2104673752521003441)
- `404` — [https://x.com/zyrox0x/status/2105354234820497855](https://x.com/zyrox0x/status/2105354234820497855)
- `404` — [https://x.com/zyrox0x/status/2105354234820497855?s=46](https://x.com/zyrox0x/status/2105354234820497855?s=46)
