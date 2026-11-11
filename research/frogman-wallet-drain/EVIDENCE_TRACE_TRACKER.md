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
