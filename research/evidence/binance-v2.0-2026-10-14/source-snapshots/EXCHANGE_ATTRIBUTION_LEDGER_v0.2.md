# NPCsignals — Exchange Attribution Ledger v0.2: R → Collector → H2fv / 99Gc

Date: 2026-10-14. Source: user-provided Work checkpoint reporting 195 unique successful finalized Solana receipts (112 newly retrieved + 60 preserved across 6hR7, plus R and collector). **Raw 195 receipts, the instruction ledger and replay script were offered via Work but not uploaded into this GitHub commit**. No fresh independent RPC replay in this commit.

## Outcome
**NO CONFIRMED CASE-FUNDS DEPOSIT TO INDEPENDENTLY ATTRIBUTED CEX** in examined scope. Existing MEXC→8HCSEe eight transfers are CEX_OUTBOUND, not an inbound deposit. Bitget→ZYROX program deployer is another CEX-outgoing lead; Circle fee sponsor is service infrastructure.

## New finalized anchors

- R: `DYxqyuLyttmd1XbTXeeZCKKEQN1MCGws3aSYLakYeb6f`
- Collector: `7aTpxyyaVhgKY8irjffP2uFkD5379aepfPfJtjYLqZAk`
- H2fv: `H2fvqz3zjr3GgwENZXoWZoafBV3jC48KRShZYfJAuvtv`
- 99Gc: `99GcqafMcohBvKDw9pR1TXQuAXzB4ZEU3JWLWz7eNtTm` (already documented in ZYROX)

| ID | UTC | Slot | Outer instruction | SOL | Source → destination | Signature |
|---|---|---:|---:|---:|---|---|
| EXD002 | 2026-10-13 19:02:50 | 456549995 | 0 | 7.894545597 | R → Collector | `4oAiLXHcNk6sVYZJuQHPiKY3dWeoNstuKKABC2UZ1JmJKFQCfhdjCD84QNxRUvLuzhSLo57bYFCrieuw8uBnmeQp` |
| EXD003 | 2026-10-13 19:12:13 | 456552587 | 0 | 19.313574183 | Collector → H2fv | `3VFwG45pKTaYCHMfqMQD426UkjWGMwooyMzWSwGjrFAqCHU4FReF8ZVSiUxeDsUiifV3zsUbh39AMHdf8DAJ9jtg` |
| EXD004 | 2026-10-13 19:12:13 | 456552587 | 1 | 3.408277796 | Collector → 99Gc | Same `3VFwG45pKTaYCHMfqMQD426UkjWGMwooyMzWSwGjrFAqCHU4FReF8ZVSiUxeDsUiifV3zsUbh39AMHdf8DAJ9jtg` |

All three System Program transfers, successful finalized; each sending wallet sole signer / fee payer, 5,000 lamports fee *per transaction*. SPL token historical owner fields not applicable to native SOL.

## Balances and commingling

R initial inputs: 1.250000000 SOL earlier seller payment + 6.644549597 later seller payment + 0.000001000 dust = 7.894550597; minus 7.894545597 to Collector and fee 0.000005000 = zero. Work reports full 4-transaction R account history.

Collector incoming total 22.721856979 SOL (of which R contributed 7.894545597, others 14.827311382); out 19.313574183 SOL to H2fv + 3.408277796 SOL to 99Gc + fee 0.000005000 = zero. Work reports 20 transactions and exact account balance reconciliation.

Non-R contributions 14.827311382 SOL cannot alone cover 19.313574183 SOL payment to H2fv. A **conservative mathematical lower bound 4.486262801 SOL of the H2fv payment was supported by R contribution**. This is accounting provenance for this transfer, NOT exclusively GLITCH sale proceeds: seller and R had pre-existing commingled SOL. Collector's 99Gc payment is exact address overlap with ZYROX, not common controller.

H2fv held 62.988899871 SOL before receipt; mixed funds rule also applies downstream.

## Negative and open items
- All 172 6hR7 wallet history references from 2026-09-30 to 2026-10-14 capture were reportedly decoded; 22 archived CEX address adapters did not yield exact deposit destination match.
- **BOUNDED NEGATIVE** only: no exhaustive deposit address inventory / token history, and no verified exchange label on H2fv, Collector, 99Gc.
- Exchange customer and ultimate beneficiary UNRESOLVED.

## Next focused trace
Trace **H2fv's outgoing transaction history from the receipt onward**, capturing exact signatures, amounts, slots, UTC, recipients, signers, fee payers, pre/post balances and independently sourced CEX destination labels. Preserve its pre-existing 62.988899871 SOL and any other inflows for commingling. Do not turn a generic intermediary address or exchange withdrawal into a case-proceeds deposit. Stop with either one confirmed CEX_INBOUND or a bounded negative checkpoint.
