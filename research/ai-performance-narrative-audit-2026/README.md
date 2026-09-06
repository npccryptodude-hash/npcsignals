# AI Performance Narrative Audit 2026

## Evidence repository

This repository contains the evidence, methodology, source material, corrections and adjudication record supporting the NPCsignals investigation:

# Distribution Depth Is Not Evidence Depth

The investigation began with a viral claim that an autonomous Grok trading agent turned 0.3 ETH into approximately 19.7 ETH.

The underlying asset movement was observable.

The claimed trade itself could not be independently reconstructed from the public evidence identified during the audit.

Following the provenance of related AI-performance claims exposed a broader structure involving:

- recycled first-person performance narratives
- amplification without additional transaction-level verification
- downstream tokenization
- creator-fee infrastructure
- post-launch creator onboarding
- creator adoption becoming new social proof

This repository documents the evidence behind those findings.

---

## Scope

This is an evidence audit.

It is not an allegation that the creators, amplifiers, token launchers and onboarding accounts documented here form one coordinated operation.

We did not establish that:

- every AI-performance claim examined was false
- every creator knew about a token before launch
- every creator-fee routing statement resulted in a verified payout
- every account discussed shared common control
- RoundtableSpace created, approved or financially benefited from the tokens examined
- GRASS belonged to the later Pump.fun creator-tokenization pattern
- the surrounding tokenization ecosystem explains the motive behind the original GRASS claim

Where the evidence did not support a stronger conclusion, the finding was downgraded, rejected or left unresolved.

Failure to verify is not proof of non-occurrence.

Absence of verification also cannot be replaced by downstream popularity, token performance or repetition.

---

## Core methodological rules

### Asset movement ≠ agent performance
A token price movement does not establish that a specific trading agent captured that move.

### Code capability ≠ historical P&L
A working repository, trading bot or agent architecture can establish technical capability. It does not establish that a claimed historical trade or profit occurred.

### Fee-routing claim ≠ verified payout
Protocol support for creator fees, or a public statement that fees were routed, does not by itself establish the final recipient or amount paid.

### Creator adoption ≠ pre-launch coordination
A creator who later claims, acknowledges or promotes a token cannot automatically be treated as having participated in its original launch.

### Distribution depth ≠ evidence depth
More reposts, larger amplifiers, downstream references or token metadata do not constitute independent corroboration unless they introduce new evidence.

### Temporal proximity ≠ causal provenance
Very short intervals between a public post and token creation may justify further scrutiny, but timing alone does not establish automation, common control, prior knowledge or causality.

---

## Evidence grades

- **E0 — Claim only:** assertion without independent support.
- **E1 — Public or archived support:** identifiable public material, but no independent technical reconstruction.
- **E2 — Independent corroboration:** multiple non-identical sources or independent metadata/provenance support.
- **E3 — Primary technical evidence:** primary protocol, contract, wallet, transaction, platform metadata or repository evidence.
- **E4 — End-to-end reconstruction:** complete relevant path independently reconstructed.

Cross-case synthesis findings receive one evidence grade. Hybrid grades such as `E2/E3` are not used.

---

## Audit principles

- Separate claims from evidence.
- Preserve counterevidence.
- Downgrade findings when new evidence weakens them.
- Do not infer common control from repeated structure.
- Do not convert missing evidence into a negative claim.

The appropriate verdict is often `UNVERIFIED`, `NON-REPRODUCIBLE` or `NOT ESTABLISHED`, rather than `FALSE`.

---

## Findings that survived the audit

1. A real asset move can be attached to an unverified agent-performance claim.
2. Highly specific first-person AI-performance narratives can be recycled across accounts.
3. Amplification can increase reach without increasing independent verification.
4. Amplified narratives can later become part of the provenance of tradable assets.
5. Third parties can tokenize technical or AI narratives without proven pre-launch creator participation.
6. Creator-fee infrastructure can support post-launch creator onboarding.
7. Later creator adoption can generate additional social proof.
8. Financialization can occur faster than independent verification.

The audit did not establish that these findings require one coordinated operator.

---

## Corrections and rejected hypotheses

This repository preserves corrections made during the investigation, including rejected or downgraded hypotheses.

Examples include:

- a HyperGrok relationship downgraded after a mint collision
- creator-fee infrastructure confirmed without assuming specific payouts
- SPIDER and REAPER weakening the hypothesis of necessary pre-launch creator coordination
- a GRASS Blockscout anomaly excluded because of conflicting indexing
- generic "touch grass" language rejected as evidence of prior GRASS-token knowledge
- an older Grass crypto reference determined to concern an unrelated project
- a uniform sub-minute launch-latency hypothesis rejected after materially different observed intervals

See `corrections.md`.

---

## Repository structure

```text
research/
└── ai-performance-narrative-audit-2026/
    ├── README.md
    ├── methodology.md
    ├── evidence-ledger-v1.0.csv
    ├── LEDGER-NOTES.md
    ├── source-index.md
    ├── timeline.csv
    ├── limitations.md
    ├── corrections.md
    ├── SOURCE-HARDENING-STATUS.md
    ├── FREEZE-READINESS.md
    ├── 01-entry-case/
    ├── 02-provenance/
    ├── 03-validation/
    ├── 04-amplification/
    ├── 05-tokenization/
    ├── 06-creator-onboarding/
    ├── 07-economics/
    ├── 08-timing/
    └── evidence/
        ├── CAPTURE-MANIFEST.md
        ├── raw/
        └── figures/
```

---

## Source policy

Where possible, the repository prioritizes primary on-chain evidence, primary protocol documentation, original public posts, original repositories and primary token metadata before archives or third-party indexes.

Source status may be recorded as:

- `PRIMARY-LIVE`
- `PRIMARY-CAPTURED`
- `ARCHIVED-CORROBORATION`
- `SECONDARY-DISCOVERY`
- `DERIVED`

`DERIVED` is reserved for analysis generated from other evidence, such as arithmetic, timing calculations or cross-case synthesis. It is not a substitute for a primary source.

---

## Raw-evidence preservation

Direct screenshots and videos are catalogued in `evidence/CAPTURE-MANIFEST.md` with intended repository paths and SHA-256 hashes.

Where the current GitHub connector cannot deposit binary files directly, that operational limitation is declared rather than treating a planned raw-evidence path as though the binary were already present.

See `SOURCE-HARDENING-STATUS.md` and `FREEZE-READINESS.md` for the current archival status.

---

## Relationship to the Medium article

The accompanying article presents the investigation as a readable narrative. This repository contains the underlying audit trail.

The article should not make a stronger claim than the Evidence Ledger supports.

---

## Final principle

The purpose of this repository is not to maximize the number of suspicious connections.

It is to determine which connections survive adversarial review.

A hypothesis survives only what we failed to falsify.
