# Frogman Investigation — Public Evidence Summary

**Status:** Ongoing investigation  
**Documentation language:** English  
**Latest verified checkpoint:** `398fd4dd363cee636e4fe7a24fa4c243ff5becd2`  
**Latest finding ID:** `F0607`  
**Checkpoint date:** 10 October 2026

NPCsignals is independently reconstructing parts of the publicly reported Frogman wallet-drain incident across Solana and EVM chains.

The current evidence reaches verified protocol deposits, bridge settlements, Hyperliquid account credits and subsequent XMR1 purchases. It does **not** establish a withdrawal into native Monero, the final beneficiary, the attacker's identity or the compromise method.

This README is the reader-facing summary. Technical records, transaction-level evidence, methodology and evidence classifications remain in the repository.

## Current evidence boundary

The strongest current finding is narrow:

> Bridge deposits linked to the examined Frogman routes were followed by XMR1 purchases on matched Hyperliquid accounts.

That statement is supported by transaction-specific bridge records, exact transaction-hash and amount correspondence, first-party Hyperliquid account data and reproduced trading activity.

It is **not** evidence that native Monero was withdrawn or received.

No verified external XMR1 redemption into native Monero has been established. No final recipient has been identified.

## Solana / Privacy Cash

NPCsignals independently reproduced **10 successful Privacy Cash deposits totaling 13,240.973780900 SOL**.

The approximate amount, publicly reported as 13,241 SOL, was already known. The contribution here is independent reproduction of the deposits from transaction records, including program calls and transfers into the pool.

No withdrawal has been defensibly linked to those deposits.

A verified Privacy Cash deposit shows that funds entered the protocol. It does not identify who later withdrew them. Mixed source balances are preserved in the evidence model and the total should not be described as exclusively victim-funded without qualification.

## EVM bridge reconstruction

Multiple EVM-side routes have been independently reconstructed using transaction-specific evidence and protocol identifiers.

Verified protocol boundaries in the investigation include routes involving Relay, Across, Chainflip, Mayan, NEAR Intents and LI.FI. These records improve the precision of the route reconstruction, but protocol use by itself does not identify a human operator or beneficiary.

Bridge inputs, settlement outputs, account credits and subsequent trades are successive representations of value. They must not be added together as separate losses.

## Hyperliquid account activity

The earlier verified block contains **six matched Hyperliquid accounts** whose examined deposit credits total **561,850.214994 USDC**.

Those same accounts subsequently recorded **205 reproduced XMR1 spot fills**, spending **561,824.8582 USDC**.

A later account reached through a separately reproduced Mayan route received a matched **26,823.206875 USDC** Hyperliquid deposit. The account then recorded **28 XMR1 buy fills** across three orders:

- 26,817.3668 USDC spent
- 47.18 XMR1 bought gross
- 0.033026 XMR1 in recorded fees
- 47.146974 XMR1 net

The recorded balances reconcile at the documented checkpoint.

No external withdrawal, bridge-out or native Monero receipt was verified for the examined XMR1 account activity.

## What is confirmed

Within the documented scope, the repository contains independently reproduced evidence for:

- Solana transaction activity and the ten Privacy Cash deposits
- selected EVM bridge origins and destination settlements
- exact Hyperliquid deposit credits matched by transaction hash and amount
- XMR1 spot purchases on matched Hyperliquid accounts
- selected downstream routing and funding relationships
- protocol-specific execution boundaries for the reconstructed routes

Each finding remains limited to the evidence attached to its finding ID and source record.

## What remains unresolved

The investigation does **not** currently establish:

- attacker identity
- relevant human wallet-controller identity
- compromise method
- final beneficiary
- a verified native Monero withdrawal or receipt
- a complete end-to-end allocation of every mixed or pooled balance
- a complete final destination for all examined value
- recovery status

Common funding does not establish common control. A bridge, router, relayer, transaction submitter or protocol account is not automatically the beneficiary.

## Evidence classifications

The investigation keeps evidence classes separate:

- **CONFIRMED** — independently reproduced transaction, protocol or account fact at the stated scope
- **SUPPORTED** — concrete evidence supports the interpretation, but the point is not independently conclusive
- **CLAIMED** — externally reported and preserved as a claim
- **UNRESOLVED** — the available evidence does not settle the question

The latest finding, **F0607**, is explicitly UNRESOLVED for upstream case provenance.

## Where the trail currently stops

The public evidence currently reaches account-level XMR1 activity on Hyperliquid and several verified protocol/funding boundaries.

It does not reach an identified final beneficiary.

**The money trail is better documented. The person behind it is not.**

## Repository structure

### Frozen v0.1 archive

The original v0.1 evidence package remains preserved and unchanged under [frogman_research_v0_1/](./frogman_research_v0_1/).

The frozen archive contains the original transaction records, ledgers, methodology, source records and checksums. The original reports remain unchanged.

- [Complete v0.1 file inventory](./evidence_inventory_v0.1.json)
- [Frozen source report](./frogman_research_v0_1/master_investigation_report.md)
- [Preserved v0.1 report](./master_investigation_report_v0.1.md)

Original ZIP SHA256:

`3fc70011e6e03ee4c6561981050ad9f1a77f1995f69dc2608aa94123694447d9`

### Ongoing v0.2 research

New investigation work is stored under [v0.2/](./v0.2/).

The v0.2 material contains the expanding findings ledger, raw protocol records, transaction reconstructions, account-level evidence, routing analysis, reproducibility records and unresolved-question boundaries.

The repository is designed so that reader-facing claims can be checked against the underlying technical evidence rather than relying on narrative alone.

## Publication status

No final long-form Frogman article is published from this research checkpoint.

This repository remains the public evidence record while the investigation is ongoing.
