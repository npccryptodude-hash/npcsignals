# b017 / one week after the binance incident

**npcsignals | documentary annex | reporting window: 1–7 november 2026 | checked: 7 november 2026**

this annex records publicly documented developments after the 29 october binance incident. it is an addendum to the original b002–b016 records, **not** a restatement or reclassification of their ethereum transaction receipts. where sources report different estimates or snapshots, each number retains its source and observation date.

## 01 / chronological developments

| date (utc unless stated) | development | evidence class | supporting source |
|---|---|---|---|
| 1 nov | binance recovery update #4: phased reopening of withdrawals; company resources replenished approximately 95% of the impacted amount, versus around 90% in the previous update. | official company report | [binance recovery #4](https://www.binance.com/en-GB/support/announcement/security-incident-recovery-update-4-withdrawals-resume-in-phases-2026-11-01-73911fb819b240f88b88256bdd318eda) |
| 2 nov | binance recovery update #5 reported that the 31 october proof-of-reserves snapshot had become user-verifiable after the zk proof was generated. this is a reserve verification update, not on-chain recovery of the stolen assets. | official company report | [binance recovery #5](https://www.binance.com/en/support/announcement/detail/185bd9a4717f44088b3be70287b8237f) |
| 3 nov | binance released a preliminary technical incident reconstruction: estimated impacted assets of about **usd 6.34b**; around **usd 2.85b frozen or intercepted** at its reporting snapshot; staged compromise involving developer tooling, a fraudulent job interview, internal ai tooling, credentials and a container. | official company report, preliminary / subject to independent review | [binance incident report](https://www.binance.com/en-AU/blog/community/3229153443759566763) |
| 3 nov | chainalysis updated its analysis: approximately **usd 2.8b frozen as of 11:30 et on 3 nov**; **usd 325m stablecoins exchanged for about usd 285m in eth** over nearly 20 minutes; funds linked to this case commingled with funds from an earlier bitget theft. | third-party blockchain-analysis assessment; underlying transaction list not replayed here | [chainalysis](https://www.chainalysis.com/blog/binance-exploit-latest-findings-and-response/) |
| 4 nov | binance recovery update #7 reported approximately **98% of the impacted amount replenished using binance funds**. a 4 november 00:00 utc proof-of-reserves snapshot expanded coverage from 10 to **44 tokens**; binance said generating the new snapshot's complete zk proof would require approximately 50–60 hours. | official company report; replenishment is not returned stolen assets | [binance recovery #7](https://www.binance.com/en-GB/support/announcement/security-incident-recovery-update-7-98-of-stolen-assets-replenished-and-new-por-snapshot-with-expanded-coverage-2026-11-04-c6ba9aa726974fc6b9332a2c8f63b405) |
| 5 nov | binance published recovery update #8 describing further phased withdrawal resumption. no separate new recovered-funds total is established in this annex. | official company announcement | [binance recovery #8](https://www.binance.com/en-GB/support/announcement/security-incident-recovery-update-8-withdrawals-for-more-assets-to-reopen-2026-11-05-a225a3b6084c41dc8c8dfb33f4de5872) |
| 6 nov | binance recovery update #9 provided a network/asset list scheduled for staged withdrawal resumption beginning 04:00 utc. not all listed services were guaranteed to reopen simultaneously. | official company announcement | [binance recovery #9](https://www.binance.com/en/support/announcement/detail/a2dd10b860a14c35a856fe9d66d6032c) |
| 7 nov | npcsignals documentary checkpoint: sources above checked; no fresh transaction-level ethereum or tron rpc replication was performed for the new cross-chain claims. | research status, not an incident event | this file |

### important prior context (not a new event during this week)

the **31 october fbi advisory** attributed the attack to north korea and called the operation **tradertraitor**. this is the government's published assessment and is already documented separately in [b016](./b016-fbi-attribution-20261101.md). this annex does not investigate or identify individual suspects. [fbi primary advisory](https://www.fbi.gov/investigate/cyber/alerts/2026/north-korea-responsible-for-6-billion-binance-attack).

elliptic's **31 october** reporting described automated-looking tron distribution: approximately usd 196m sent out from a main distribution wallet to about 200 wallets at its 22:41 utc update. it also cited about usd 2.85b verified frozen **at that snapshot**. these are prior-context figures, not independent 1–7 november transfers verified by npcsignals. [elliptic analysis](https://www.elliptic.co/insights/the-binance-hack-is-laundering-on-autopilot/).

## 02 / technical incident reconstruction — binance's account

binance's 3 november preliminary report describes a **multi-stage intrusion**, rather than a simple one-transaction wallet compromise:

1. **june:** a wallet devops engineer reportedly downloaded a modified homebrew installer while setting up an ai coding tool. binance says this incident was detected, the device replaced and credentials rotated, but organizational information was exposed.
2. **september:** a software engineer reportedly downloaded a malicious coding assignment after a fraudulent recruitment process. binance says the payload replaced a legitimate developer-tool component, allowing further access.
3. **20 october:** according to binance, the actor used the compromised device and an internal ai tool to reach additional wallet engineering workstations and discover a container-deployment credential.
4. **29 october:** binance says stolen access enabled deployment of a container and execution of a malicious script affecting wallet signing operations.
5. **during containment:** binance reports malicious **eip-7702 authorizations** continued to permit on-chain activity even after ordinary withdrawals were suspended. it says revocation was complicated by the multiparty computation wallet architecture.
6. **23:56 utc, 29 october:** binance reports that a previously pending final unauthorized transfer of **2,961.9 eth** finalized.
7. **00:10 utc, 30 october:** binance reports issuing a new zero-address authorization to clear the eip-7702 delegation.

**classification:** source-reported technical reconstruction by the affected company; not independently replayed from endpoint telemetry or authorization-state proof in this annex. points 5–7 may be compared to existing b002/b004/b005 observations, but this annex does not claim an independent confirmation of every step.

source: [binance technical incident report, 3 november](https://www.binance.com/en-AU/blog/community/3229153443759566763).

## 03 / laundering developments and what the evidence does not show

chainalysis reports: (a) commingling between funds from this incident and an earlier bitget theft; (b) about **usd 325m in stablecoins** swapped for approximately **usd 285m in eth** in a roughly 20-minute period; and (c) automated-looking transfers, including many recipient addresses pre-funded with exactly 1 trx.

these are **reported analytics findings**. this annex does not provide the complete hash-by-hash receipts for these cross-chain flows, does not determine final beneficiaries and does not claim they are the same transactions as the original **700m canonical-usdt ethereum** b006–b015 path. do not combine 325m, 700m, 175m or 80m as separate thefts unless provenance and non-overlap have been demonstrated.

source: [chainalysis technical analysis and 3 november freeze snapshot](https://www.chainalysis.com/blog/binance-exploit-latest-findings-and-response/).

## 04 / accounting: four different measures

| metric | reported value | source / observed date | interpretation |
|---|---:|---|---|
| incident-wide affected assets | approximately **usd 6.34b** | binance, 3 nov | preliminary valuation of affected assets, not this archive's independently reconciled total |
| frozen / intercepted assets | approximately **usd 2.85b** | binance, 3 nov | blocked or intercepted; **not equivalent to recovered and returned assets** |
| frozen assets (analysis estimate) | approximately **usd 2.8b** | chainalysis, as of 3 nov 11:30 et | separately dated estimate, not a second amount to add to binance's 2.85b |
| asset replenishment | approximately **98%** of impacted token assets | binance, 4 nov | replacement / reserve replenishment using company funds; **not 98% of funds recovered from the attacker** |

**accounting rule:** frozen, returned, recovered, replenished, replaced and proof-of-reserves-backed are different concepts. percentage of token assets replenished is not necessarily the percentage of theft proceeds recovered. estimates reflect the reporting date and possible market-price changes. avoid adding chainalysis's 2.8b to binance's 2.85b or treating them as two independent freezes.

## 05 / impact and service restoration

binance reported staged withdrawal resumption rather than a single reopening of all networks and assets. its 6 november recovery update #9 lists specific network/asset combinations scheduled to reopen **beginning at 04:00 utc**; it explicitly warns that rollout is progressive, conditional on security checks, and subject to delays. the post does not establish that every listed market was available at the same instant.

sources: [recovery #4](https://www.binance.com/en-GB/support/announcement/security-incident-recovery-update-4-withdrawals-resume-in-phases-2026-11-01-73911fb819b240f88b88256bdd318eda), [recovery #7](https://www.binance.com/en-GB/support/announcement/security-incident-recovery-update-7-98-of-stolen-assets-replenished-and-new-por-snapshot-with-expanded-coverage-2026-11-04-c6ba9aa726974fc6b9332a2c8f63b405), [recovery #9](https://www.binance.com/en/support/announcement/detail/a2dd10b860a14c35a856fe9d66d6032c).

## 06 / evidence status and boundaries

- **publication verified:** existence and text of source statements; their underlying technical/financial assertions remain source-attributed. source statements of binance's 3 nov incident report, its 1/4/6 nov service/replenishment updates, the chainalysis report and fbi attribution advisory.
- **source attributed, not independently replicated:** incident entry method, cross-chain laundering routes, commingling with bitget, frozen totals, reserve replenishment and operational recovery claims.
- **retained independently matched token logs:** b013–b015 cover selected ethereum canonical-usdt transfer events; their prior verification level is **unchanged** by this annex.
- **not assessed:** direct address overlap between chainalysis, elliptic or fbi lists and b006–b015; cross-chain net asset conservation; total frozen-to-returned reconciliations.
- **not claimed:** a named perpetrator, an arrest, ownership derived from graph proximity, full recovery of stolen assets, or proof of every point in binance's attack narrative.

this annex is **documentary**, not a new blockchain monitoring result. no live node queries, publication, wallet interaction or on-chain transactions were performed to create it.

## 07 / source register

- **s01** / [binance preliminary incident report, 3 nov](https://www.binance.com/en-AU/blog/community/3229153443759566763) — affected assets, incident sequence, mitigations, frozen/intercepted estimate.
- **s02** / [chainalysis analysis, published 30 oct and updated through 3 nov](https://www.chainalysis.com/blog/binance-exploit-latest-findings-and-response/) — reported swap sequence, bitget commingling, freezing snapshot, and automated-looking behavior.
- **s03** / [binance recovery update #4, 1 nov](https://www.binance.com/en-GB/support/announcement/security-incident-recovery-update-4-withdrawals-resume-in-phases-2026-11-01-73911fb819b240f88b88256bdd318eda) — 95% replenished and phased services.
- **s04** / [binance recovery update #7, 4 nov](https://www.binance.com/en-GB/support/announcement/security-incident-recovery-update-7-98-of-stolen-assets-replenished-and-new-por-snapshot-with-expanded-coverage-2026-11-04-c6ba9aa726974fc6b9332a2c8f63b405) — 98% replenished, proof-of-reserves snapshot for 44 assets.
- **s05** / [binance recovery update #9, 6 nov](https://www.binance.com/en/support/announcement/detail/a2dd10b860a14c35a856fe9d66d6032c) — asset- and network-specific staged withdrawal restoration.
- **s06** / [binance recovery #5](https://www.binance.com/en/support/announcement/detail/185bd9a4717f44088b3be70287b8237f) — 31 october zk proof completion and reserve verification; [binance recovery #8](https://www.binance.com/en-GB/support/announcement/security-incident-recovery-update-8-withdrawals-for-more-assets-to-reopen-2026-11-05-a225a3b6084c41dc8c8dfb33f4de5872) — 5 november staged withdrawal schedule.
- **s07** / [fbi advisory, 31 oct](https://www.fbi.gov/investigate/cyber/alerts/2026/north-korea-responsible-for-6-billion-binance-attack) — prior official attribution; see b016.
- **s08** / [elliptic tron-laundering bulletin, 31 oct](https://www.elliptic.co/insights/the-binance-hack-is-laundering-on-autopilot/) — prior-context distribution estimates; not counted as new november events.

**editorial state: addendum on draft branch only; no changes to main and no public publication.**
