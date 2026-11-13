> latest: [13 november independent 35-account audit](./audit_2026_11_13/README.md); older checkpoint sections below remain dated historical records.

# frogman — evidence trace tracker

**updated:** 2026-11-11  
**purpose:** keep source claims, independently reproduced evidence, and follow-up verification separate.

| trace id | stage | amount / observation | evidence class | verification state | next check |
|---|---|---|---|---|---|
| ft-001 | reported drain | approx. $4m | claimed | incident reporting | preserve victim statement and chain origin |
| ft-002 | privacy cash entry | 13,240.973780900 sol / 10 deposits | confirmed | npcsignals archive | no withdrawal attribution without linkage |
| ft-003 | evm bridge paths | relay, across, chainflip, mayan, near intents, li.fi | confirmed for selected routes | transaction-specific archive | audit each path separately |
| ft-004 | hyperliquid matched six | 561,850.214994 usdc credits | confirmed | account matching | compare with third-party inventory |
| ft-005 | hyperliquid fills | 205 fills; 561,824.8582 usdc spent | confirmed | first-party trade reconstruction | refresh fills and withdrawals |
| ft-006 | additional mayan-linked account | 26,823.206875 usdc | confirmed | matching credit | refresh account state |
| ft-007 | additional account trades | 28 fills; 47.146974 net xmr1 | confirmed | fills and fees reconciled | redemption / transfer audit |
| ft-008 | onchain files account set | 35 accounts; ~3,586.8 xmr1 | claimed / external | not independently reconciled | obtain full address list and timestamps |
| ft-009 | solsentry account set | 41 accounts; ~$2.2m xmr1 | claimed / external | not independently reconciled | compare sets, duplicates and time windows |
| ft-010 | native monero redemption | none verified in npcsignals archive | unresolved | no positive proof | inspect wagyu redemption evidence |
| ft-011 | november 2026 account state | unknown | unresolved | no fresh account-level audit | query first-party hyperliquid data |
| ft-012 | attacker identity / compromise | unknown | unresolved | no attribution | preserve evidence boundary |

## source reconciliation worksheet

| question | test | result |
|---|---|---|
| do 35 and 41 represent the same wallet set? | compare exact account addresses and observation times | pending |
| are all external accounts frogman-linked? | verify chain-origin tx and account credit individually | pending |
| were xmr1 balances redeemed after october? | account withdrawals, redemptions and first-party service evidence | pending |
| are reported 29 privacy withdrawals linked to deposits? | cryptographic/protocol-specific matching, not timing alone | pending |
| do routes overlap and double-count funds? | event-level input/output reconciliation | pending |

## update protocol

append new rows with utc observation time, chain, full address, transaction hash, amount, token decimals, first-party record url, evidence classification, and reviewer notes. never silently replace older snapshots. where data is pooled or private, mark the boundary and stop.

## source register

- npcsignals original: [readme](./README.md), [frozen v0.1](./frogman_research_v0_1/), [v0.2](./v0.2/)
- external: [onchain files scoreboard, 13 oct 2026 snapshot](https://www.onchainfiles.io/scoreboard/)
- external: [solsentry statement mirrored on nitter](https://nitter.gq/crashdiniz)

**no independent live blockchain recheck was completed for this 11 november editorial update.**

## superseding verification / 13 november 2026

| trace | observation | class | evidence / limits |
|---|---|---|---|
| ft-013 | 35 arbitrum deposits / 2,029,874.462280 usdc | confirmed | [receipts](./audit_2026_11_13/receipts.json); successful native-usdc events and block inclusion |
| ft-014 | 35 identical account credits | confirmed | [account audit](./audit_2026_11_13/ACCOUNT_AUDIT.md); exact transaction hashes and amounts |
| ft-015 | 537 xmr1 buy fills / 3,586.797483 net xmr1 | confirmed | [fills](./audit_2026_11_13/fills.json); fees and spot balances reconcile |
| ft-016 | november returned histories and current balances | confirmed within api scope | [timestamps](./audit_2026_11_13/summary.json); no returned external-transfer entries; no consensus/lifetime completeness claim |
| ft-017 | 70 separate post-13-october queries return empty | confirmed query result | [recent checks](./audit_2026_11_13/recent_window_check.json); not a proof about unqueried accounts or private records |
| ft-018 | one historical explorer-label checksum mismatch | confirmed integrity exception | [exception](./audit_2026_11_13/integrity_exception.json); original file retained |
| ft-019 | 25 additional mayan api refreshes and two chainflip status refreshes blocked | unresolved refresh | [limitations](./audit_2026_11_13/LIMITATIONS.md); individual access-error records preserved |

ft-008's 35-account count and rounded deposit/xmr1 totals are now reproduced for the published set. ft-011's unknown november account state is superseded by this dated snapshot. ft-009's 41-account set and ft-010's native monero receipt remain unresolved.

## additional verified findings

| trace | observation | class | evidence |
|---|---|---|---|
| ft-020 | additional account outside external 35 | confirmed deposit/credit/fill/balance | [new edges](./audit_2026_11_13/new_edges_summary.json); 55.569140 usdc / 0.089937 net xmr1 |
| ft-021 | 27 oct 4-eth branch outflow and mayan lock | confirmed ethereum facts | [additional findings](./audit_2026_11_13/ADDITIONAL_FINDINGS.md); solana order-state match supported, not fully confirmed |
| ft-022 | historical checksum discrepancy explained | confirmed newline transformation | [crlf reconstruction](./audit_2026_11_13/integrity_normalization_recheck.json); original bytes unchanged |
