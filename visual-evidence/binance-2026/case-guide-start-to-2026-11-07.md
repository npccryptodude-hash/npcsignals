# binance incident / from the first breach to 7 november 2026

**npcsignals | educational evidence guide | case snapshot: 7 november 2026**

this guide explains the reported binance incident in chronological order for readers who may be new to blockchains or cybersecurity. it is a gateway to the original evidence, not a replacement for the raw records.

## the case in brief

on 29 october 2026, binance reported a major multi-chain security incident. external reports estimated the affected assets at approximately **usd 6.3–6.4 billion**. npcsignals has **not independently reconstructed that entire total**. instead, our archive focuses on a reproducible subset of ethereum transfers, including **700 million authentic ethereum usdt**. subsequent movements of the same money are not added to the theft amount.

the fbi publicly attributed the wider incident to **north korea / tradertraitor** on 31 october. this is official attribution, not proof of who operated each wallet shown in our graph. a company reconstruction published on 3 november described a multi-stage intrusion into developer environments, credential access and malicious deployment; this account is **source-reported**, not independently reproduced endpoint forensics. the first week's reported freezing, laundering and recovery measures appear in [b017](./b017-weekly-developments-2026-11-01-to-07.md).

## a beginner's glossary

- **wallet:** signing technology that can authorize blockchain asset transfers; an address alone does not identify its operator.
- **transaction hash:** a unique identifier that lets readers inspect a blockchain transaction.
- **ethereum:** the network studied in our retained b002–b015 receipts; the reported incident affected additional networks.
- **usdt:** a token intended to track the us dollar. its name can be imitated; the authentic ethereum contract address is `0xdAC17F958D2ee523a2206206994597C13D831ec7`.
- **token transfer event:** an on-chain log of a token movement. it is not proof of who ultimately owns an address.
- **rpc receipt:** an interface for fetching raw blockchain transaction and log information. b013–b015 retain comparisons from two public endpoints for specified transfers.
- **eip-7702:** an ethereum mechanism permitting account-authorized delegated execution. binance associates delegated execution with the incident's reported mechanism.
- **freeze:** tokens are blocked from movement. this is not equivalent to returning them to the victim.
- **replenishment:** a company restores its reserves using its own resources. that is not recovery from the attacker.

## chronology and the underlying record

| period / event (utc when available) | what is established or reported | evidence level | follow the source |
|---|---|---|---|
| june–september 2026 | binance later reported compromised developer tooling and a fraudulent recruitment assignment | binance reconstruction, not independently replicated | [3 nov technical report](https://www.binance.com/en-AU/blog/community/3229153443759566763) |
| 20 oct | binance later reported further access to wallet-team environments | binance reconstruction | [report](https://www.binance.com/en-AU/blog/community/3229153443759566763) |
| 29 oct 20:20:59 | a transaction involving eip-7702 authorization in the reported account compromise | original ethereum transaction, interpretation partly source-reported | [b002 tx](https://etherscan.io/tx/0xad99264d5532ae0dd04b2004eebda05f25657e70dacb764f7ac8d4ccd051298b) |
| 29 oct 20:24:23 | explorer data recorded a 167,464.247856558836135296 eth internal transfer and 63 token transfer events | blockscout observations, not complete incident accounting | [b004 ledger](./b004-token-ledger.json) |
| 29 oct 20:30–20:33 | 500m + 200m genuine usdt left the collection wallet for two receivers | selected raw logs matched through two public rpc endpoints | [b006](./b006-receiver-outgoing-summary.json), [b013](./b013-independent-rpc-usdt.json) |
| 29–30 oct | the same 700m passed to additional receivers; 365m selected third-hop transfers and an 80m/30m route were checked in later checkpoints | mixed: b014–b015 receipt matched; remainder explorer observed | [interactive flow](./flow.html), [b007](./b007-second-hop-usdt-ledger.json), [b014](./b014-independent-rpc-third-hop.json), [b015](./b015-independent-rpc-80m.json) |
| 30 oct 00:10:35 | a later authorization transaction was described as clearing the delegation | original transaction exists; historical authorization-state effect requires specific verification | [b005 transaction](https://etherscan.io/tx/0xafbf94c92a8d749988411669fa14d4f8866d9b4420b4ebd299f28e958dac7209) |
| 31 oct | the fbi publicly attributed the attack to north korea / tradertraitor | official agency attribution | [fbi advisory](https://www.fbi.gov/investigate/cyber/alerts/2026/north-korea-responsible-for-6-billion-binance-attack), [b016](./b016-fbi-attribution-20261101.md) |
| 1–7 nov | company reports described the intrusion, asset freezing, replenishment and staged reopening; analysts reported continuing laundering | dated company/analyst claims, not independently replayed cross-chain transactions | [weekly annex b017](./b017-weekly-developments-2026-11-01-to-07.md) |

## what happened to the 700 million usdt?

first, the original collection address sent **500 million** and **200 million** authentic usdt to two receiving addresses. in the next hop, the full 700 million was distributed through 19 positive transfer events to 15 destination addresses in an explorer snapshot. b014 identifies a subset of **365 million** at later destinations, including a **175-million** branch. b015 follows an **80-million** sub-branch that split between reported liquidity infrastructure and a **30-million** onward transfer.

these are selected routes, not a complete recovery ledger. **do not sum 700 + 365 + 175 + 80 + 30 million.** this would count the same tokens multiple times. a transfer to a contract does not prove a trade completed; a balance does not prove ownership or the absence of a freeze.

## what changed during the next week?

- binance's 3 november reconstruction described the intrusion as a chain of technical and organizational compromises, not just one transaction.
- chainalysis reported around **usd 325m in stablecoins exchanged for about usd 285m in eth** and suspected mixing with funds from an earlier bitget incident. those transactions are not independently replayed in this archive.
- sources gave dated estimates of **usd 2.8–2.85b frozen/intercepted** around 3 november; the figures are overlapping estimates, not additive.
- binance said it had **replenished about 98% of impacted token assets** using its funds by 4 november. replenishment is not the same as seizure or recovery from the attackers.
- service withdrawal restoration was reported as **phased**, not a single full reopening.

full source links, dates and limits: [b017 weekly annex](./b017-weekly-developments-2026-11-01-to-07.md).

## how can a reader verify a claim?

1. identify the **claim and evidence class**. an official statement that an agency attributed an attack is not the same as independent proof of a person's identity.
2. open the original transaction hash and check block number, status, contract, log index, sender, receiver and raw value. distinguish an erc-20 log recipient from the transaction's outer `to` field.
3. compare b013–b015 retained receipts for the selected usdt events; do not assume every downstream observation received the same cross-provider check.
4. inspect later routes with [flow.html](./flow.html) and the underlying b006–b015 json ledgers. verify that no value is counted twice.
5. distinguish source publication time from the observed blockchain event time.
6. read the [documentation standard](./documentation-standard.md) to understand classification, limitations and correction rules.

## questions for further research

what can a public blockchain prove without revealing who owns an address? why is a freeze not the same as recovered assets? why can a token ticker be misleading? what parts of a cyber incident can an affected company describe without outsiders being able to reproduce them? when does a source report become a verified finding?

**status:** the incident is not fully resolved. this guide is a dated snapshot and later changes belong in separately dated annexes. *observe first. verify before concluding.*
