# frogman — source-ledger audit / 12 november 2026

**npc / investigation / 001**  
**audit scope:** external published transaction ledger, not independent chain replay  
**status:** source references identified; reconciliation incomplete

## 01 / source verification

the onchain files #014 public record includes transaction links for ten privacy cash deposits, twenty-five mayan route entries, and thirty-five arbitrum hyperliquid deposits. its account counts and balances are reported observations, not npcsignals independently verified findings.

source: https://www.onchainfiles.io/files/014-frogman-token2049/

### example published hyperliquid deposit records

| external row | timestamp utc (7 oct 2026) | shortened account | reported usdc | explorer source |
|---|---|---|---:|---|
| hl-ext-01 | 01:45 | 0x9cb1…c01f | 60,417 | https://arbiscan.io/tx/0xc0e57329 |
| hl-ext-02 | 01:49 | 0xd7ef…e6b1 | 100,542 | https://arbiscan.io/tx/0xd0904491 |
| hl-ext-03 | 01:52 | 0x68d6…1ac4 | 93,738 | https://arbiscan.io/tx/0x953cb320 |
| hl-ext-04 | 02:21 | 0x3e2d…40a1 | 26,823 | https://arbiscan.io/tx/0x963c5625 |

**warning:** explorer links above are intentionally *not* treated as complete transaction hashes. shortened values are search identifiers only; use the original source's clickable explorer links to recover complete identifiers. no fabricated full hash is supplied.

## 02 / important reconciliation warning

the external ledger lists twenty-five mayan rows, including two displayed ~98k usdc deliveries among many ~49k deliveries. the reported mayan subtotal is 1,284,323 usdc. these values need exact-decimal reconciliation against each individual bridge receipt before we accept the subtotal or assume a one-to-one swap mapping.

the source also reports 29 inferred privacy cash withdrawals (12,693 sol), whereas npcsignals independently verifies ten deposits (13,240.973780900 sol). **do not link the two sets as confirmed flows.**

## 03 / evidence classifications

| proposition | status | why |
|---|---|---|
| external article publishes 35 hyperliquid deposit rows | confirmed as publication content | the published ledger can be inspected |
| all 35 deposits are valid on-chain | not yet independently checked | requires full hashes and receipt/event inspection |
| all 35 accounts belong to one actor | unresolved | routing similarity does not prove control |
| 3,586.8 xmr1 held on 13 oct | external dated claim | needs first-party account snapshot reproduction |
| xmr1 remained untouched in november | unresolved | october snapshot cannot establish november state |
| native monero redemption occurred | unresolved | no verified redemption evidence in this audit |

## 04 / next machine-verifiable audit

1. extract 35 complete destination addresses and 35 complete arbitrum tx hashes.
2. verify transaction success, usdc contract, decimals, recipient, value and utc block time.
3. compare exact addresses to npcsignals' six plus one independently documented accounts.
4. pull first-party hyperliquid user ledger, fills and account states for each account at an explicit observation time.
5. compute unique account set, sum deposits and xmr1 holdings without double counting.
6. check native redemption via first-party redemption records if obtainable; mark opaque service boundaries.
7. save raw records, checksums, scripts and a pass/fail matrix.

**no fresh november balance check or chain-level replay was performed in this audit.** the october 10 frozen checkpoint remains unchanged.
