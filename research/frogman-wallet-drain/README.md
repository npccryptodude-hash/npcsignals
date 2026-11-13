# frogman wallet drain / public evidence record

## latest verified account checkpoint / 13 november 2026

**35 / 35 externally listed accounts reconciled.** successful arbitrum receipts and exact hyperliquid account credits total **2,029,874.462280 usdc**. **537 xmr1 buy fills**, minus **2.512517 xmr1** fees, reconcile to **3,586.797483 xmr1** in the queried november balances. no xmr1 sells or external-transfer/withdrawal ledger entries were returned; separate post-13-october queries also returned no activity. this is a timestamped rpc/api observation, not lifetime completeness, ownership or native monero proof.

- [updated technical main report](./audit_2026_11_13/TECHNICAL_REPORT.md)
- [35-account audit with primary links](./audit_2026_11_13/ACCOUNT_AUDIT.md)
- [downloadable account table](./audit_2026_11_13/accounts.csv)
- [visual timeline and money-flow map](./audit_2026_11_13/VISUAL_TIMELINE_AND_FLOW.md)
- [confirmed findings, limits and technical obstacles](./audit_2026_11_13/LIMITATIONS.md)
- [exact totals and observation times](./audit_2026_11_13/summary.json)

spot states were observed 13 november, 08:17:14–08:21:23 utc; each raw response records its exact retrieval time. the 35 accounts include all six earlier relay accounts, the separate mayan account and an additional across-linked credit already in the archive. the earlier seven-account coverage summary was incomplete as a description of all credit checks. these overlapping amounts must not be added together.

**publication status:** ready for a bounded account/money-flow reconstruction with stated limits. privacy cash withdrawal attribution, comprehensive victim-loss allocation, compromise method, human control, native monero settlement and recovery remain unresolved. one older upstream-label html byte mismatch is explained by lf/crlf conversion; original evidence remains unchanged. the medium draft is delivered separately and is not stored in github.

## additional findings / separate from the external 35

[one additional hyperliquid account and new october 27 movements](./audit_2026_11_13/ADDITIONAL_FINDINGS.md): 55.569140 usdc credited and 0.089937 net xmr1 on a distinct account outside the published list. total audited coverage is therefore 36 accounts, while the 35-account baseline stays separately reproducible. the old 4-eth holding was spent on 27 october; its new mayan order and subsequent supported solana association are documented with explicit boundaries.

## historical research checkpoints

older checkpoint text follows for continuity. statements that the live audit is blocked or the 35-account audit is pending are superseded by the linked november audit.


**status:** ongoing investigation  
**documentation language:** english  
**latest verified checkpoint:** `398fd4dd363cee636e4fe7a24fa4c243ff5becd2`  
**latest finding id:** `F0607`  
**checkpoint date:** 10 october 2026

npcsignals is independently reconstructing parts of the publicly reported frogman wallet-drain incident across solana and evm chains.

the current evidence reaches verified protocol deposits, bridge settlements, hyperliquid account credits and subsequent xmr1 purchases. it does **not** establish a withdrawal into native monero, the final beneficiary, the attacker's identity or the compromise method.

this readme is the reader-facing summary. technical records, transaction-level evidence, methodology and evidence classifications remain in the repository.

## educational visual evidence / 11 november 2026

the original verified research checkpoint remains **10 october 2026 / f0607**. the 11 november update adds an educational navigation layer and third-party source comparison, **not a new independently verified blockchain checkpoint**.

- [visual evidence map — follow the routes and evidence boundaries](./EDUCATIONAL_VISUAL_EVIDENCE.md)
- [evidence trace tracker — confirmed records vs external claims](./EVIDENCE_TRACE_TRACKER.md)
- [timeline — incident, checkpoints and dated source snapshots](./TIMELINE.md)

the visual map is designed for readers learning how to trace on-chain funds. it separates transaction-level confirmation from inferred connections, pooled/privacy boundaries, and unverified account-count claims. external reports describe 35 and 41 hyperliquid accounts respectively; their address sets and snapshot times have **not** been independently reconciled. no fresh november balance or redemption check has been completed.

---

### phase 2 / external transaction reconciliation — 12 november 2026

- [phase 2 external evidence comparison and verification checklist](./PHASE_2_EXTERNAL_RECONCILIATION.md)

this annex extracts the published 35-account / 2,029,874 usdc / 3,586.8 xmr1 external inventory as a **third-party claim** and identifies specific transactions and evidence boundaries for independent reproduction. it does not alter the frozen 10 october independently verified checkpoint. no new november account-state verification is claimed.

## publication readiness / 13 november 2026

- [publication readiness review and evidence limits](./PUBLICATION_READINESS_2026-11-13.md)
- [35 arbitrum transaction links and receipt spot checks](./PRIMARY_TRANSACTION_CHECKS_2026-11-12.md)
- [read-only arbitrum receipt verifier](./verify_arbitrum_receipts.py)
- [hyperliquid live-data access limitation](./HYPERLIQUID_FIRST_PARTY_CHECK_2026-11-12.md)

**editorial conclusion:** a source-linked historical reconstruction is feasible. a claim that all 35 hyperliquid accounts were independently reconciled, or that xmr1 has not moved since october, is **not** supported by the present audit. the last independently reproduced npcsignals checkpoint remains 10 october; the external monitoring page reports its last check as 13 october. no medium publication has been made.

---

## current evidence boundary

the strongest current finding is narrow:

> bridge deposits linked to the examined frogman routes were followed by xmr1 purchases on matched hyperliquid accounts.

that statement is supported by transaction-specific bridge records, exact transaction-hash and amount correspondence, first-party hyperliquid account data and reproduced trading activity.

it is **not** evidence that native monero was withdrawn or received.

no verified external xmr1 redemption into native monero has been established. no final recipient has been identified.

## solana / privacy cash

npcsignals independently reproduced **10 successful privacy cash deposits totaling 13,240.973780900 sol**.

the approximate amount, publicly reported as 13,241 sol, was already known. the contribution here is independent reproduction of the deposits from transaction records, including program calls and transfers into the pool.

no withdrawal has been defensibly linked to those deposits.

a verified privacy cash deposit shows that funds entered the protocol. it does not identify who later withdrew them. mixed source balances are preserved in the evidence model and the total should not be described as exclusively victim-funded without qualification.

## evm bridge reconstruction

multiple evm-side routes have been independently reconstructed using transaction-specific evidence and protocol identifiers.

verified protocol boundaries in the investigation include routes involving relay, across, chainflip, mayan, near intents and li.fi. these records improve the precision of the route reconstruction, but protocol use by itself does not identify a human operator or beneficiary.

bridge inputs, settlement outputs, account credits and subsequent trades are successive representations of value. they must not be added together as separate losses.

## hyperliquid account activity

the earlier verified block contains **six matched hyperliquid accounts** whose examined deposit credits total **561,850.214994 usdc**.

those same accounts subsequently recorded **205 reproduced xmr1 spot fills**, spending **561,824.8582 usdc**.

a later account reached through a separately reproduced mayan route received a matched **26,823.206875 usdc** hyperliquid deposit. the account then recorded **28 xmr1 buy fills** across three orders:

- 26,817.3668 usdc spent
- 47.18 xmr1 bought gross
- 0.033026 xmr1 in recorded fees
- 47.146974 xmr1 net

the recorded balances reconcile at the documented checkpoint.

no external withdrawal, bridge-out or native monero receipt was verified for the examined xmr1 account activity.

## what is confirmed

within the documented scope, the repository contains independently reproduced evidence for:

- solana transaction activity and the ten privacy cash deposits
- selected evm bridge origins and destination settlements
- exact hyperliquid deposit credits matched by transaction hash and amount
- xmr1 spot purchases on matched hyperliquid accounts
- selected downstream routing and funding relationships
- protocol-specific execution boundaries for the reconstructed routes

each finding remains limited to the evidence attached to its finding id and source record.

## what remains unresolved

the investigation does **not** currently establish:

- attacker identity
- relevant human wallet-controller identity
- compromise method
- final beneficiary
- a verified native monero withdrawal or receipt
- a complete end-to-end allocation of every mixed or pooled balance
- a complete final destination for all examined value
- recovery status

common funding does not establish common control. a bridge, router, relayer, transaction submitter or protocol account is not automatically the beneficiary.

## evidence classifications

the investigation keeps evidence classes separate:

- **confirmed** — independently reproduced transaction, protocol or account fact at the stated scope
- **supported** — concrete evidence supports the interpretation, but the point is not independently conclusive
- **claimed** — externally reported and preserved as a claim
- **unresolved** — the available evidence does not settle the question

the latest finding, **f0607**, is explicitly unresolved for upstream case provenance.

## where the trail currently stops

the public evidence currently reaches account-level xmr1 activity on hyperliquid and several verified protocol/funding boundaries.

it does not reach an identified final beneficiary.

**the money trail is better documented. the person behind it is not.**

## repository structure

### frozen v0.1 archive

the original v0.1 evidence package remains preserved and unchanged under [frogman_research_v0_1/](./frogman_research_v0_1/).

the frozen archive contains the original transaction records, ledgers, methodology, source records and checksums. the original reports remain unchanged.

- [complete v0.1 file inventory](./evidence_inventory_v0.1.json)
- [frozen source report](./frogman_research_v0_1/master_investigation_report.md)
- [preserved v0.1 report](./master_investigation_report_v0.1.md)

original zip sha256:

`3fc70011e6e03ee4c6561981050ad9f1a77f1995f69dc2608aa94123694447d9`

### ongoing v0.2 research

new investigation work is stored under [v0.2/](./v0.2/).

the v0.2 material contains the expanding findings ledger, raw protocol records, transaction reconstructions, account-level evidence, routing analysis, reproducibility records and unresolved-question boundaries.

the repository is designed so that reader-facing claims can be checked against the underlying technical evidence rather than relying on narrative alone.

## publication status

no final long-form frogman article is published from this research checkpoint.

this repository remains the public evidence record while the investigation is ongoing.
