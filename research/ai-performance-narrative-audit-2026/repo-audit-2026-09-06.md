# Repository Consistency Audit

Date: 2026-09-06  
Scope: AI Performance Narrative Audit 2026  
Status: PRE-PUBLIC SOURCE-HARDENING REVIEW

## Purpose

This review compares the repository README, methodology, Evidence Ledger v1.0, source index, timeline and case files for internal consistency.

The purpose is not to strengthen the narrative. It is to identify places where the repository currently claims more source finality than the deposited evidence can independently support.

No finding should be promoted because it is narratively useful.

---

## Audit result

The methodological framework is internally coherent, but the repository is **not yet ready to be described as a fully source-hardened public evidence package**.

The main issue is not the analytical model. The main issue is source deposition and status consistency.

Several ledger rows refer to raw-evidence paths that are not yet present in the repository, and several case files explicitly state that source hardening remains pending.

The correct response is to preserve the current limitations rather than silently treat planned evidence paths as deposited evidence.

---

## A-01 — Raw-evidence paths are referenced before deposit

### Observation

Evidence Ledger v1.0 contains paths such as:

- `evidence/raw/video/grass-original.mp4`
- `evidence/raw/x/mememoon-zynex.png`
- `evidence/raw/x/mememoon-backwood.png`
- `evidence/raw/x/kitsune-enko.png`
- `evidence/raw/x/roundtablespace-2093824765785976942.png`
- `evidence/raw/metadata/factory-pumpfun-01.png`
- SPIDER and REAPER raw screenshot paths

The repository currently does not contain the corresponding deposited raw-evidence tree.

### Methodological conflict

`methodology.md` defines `raw_evidence` as a repository path to preserved raw evidence **where available**.

A planned path is not the same thing as a deposited file.

### Audit disposition

**SOURCE-HARDENING REQUIRED**

Until files are uploaded, these references should be read as intended destinations, not as proof that the evidence is publicly deposited.

No substantive verdict is upgraded by a planned path.

---

## A-02 — GRASS original X-source mapping is inconsistent across files

### Observation

Evidence Ledger v1.0 records an exact X URL for `GRASS-02`.

By contrast:

- `01-entry-case/grass.md` says the exact original X-source mapping should remain `PENDING` until the raw capture and final source URL are placed in the repository.
- `timeline.csv` states that the exact original X status remains unresolved.
- `source-index.md` lists the exact original X URL as source-hardening work still to be completed.

### Audit disposition

The more conservative treatment controls.

**Exact original GRASS X status: PENDING / unresolved in the public audit package.**

The captured GRASS video remains valid presentation evidence and its recorded SHA-256 is retained, but an unresolved source mapping must not be presented as finalized provenance.

### Effect on finding

`GRASS-02` remains `UNVERIFIED`, E1.

No change to the substantive verdict is required.

---

## A-03 — REAPER source status is stronger in the ledger than in the case file

### Observation

Evidence Ledger v1.0 records `REAPER-01` and `REAPER-02` using `PRIMARY-CAPTURED` status, with `REAPER-02` adjudicated as E2 / `SUPPORTED` and `LOCKED`.

However, `06-creator-onboarding/reaper.md` states:

- REAPER relies more heavily than SPIDER on archived and secondary-discovery material.
- exact status IDs, original captures and same-mint chronology should remain `PENDING` until deposited and independently checked.
- `REAPER-02` is supported **subject to final primary-source capture**.

`timeline.csv` likewise marks the REAPER origin event as `ARCHIVED-CORROBORATION` and `PENDING`.

### Audit disposition

The case-file limitation controls until source hardening is complete.

**REAPER-02 must not be treated as source-final merely because the ledger row says LOCKED.**

### Effect on synthesis

`ONBOARD-01` depends in part on `REAPER-02`.

The structural interpretation may remain a useful working synthesis, but its public source-final status depends on hardening REAPER or replacing it with another independently deposited onboarding case.

---

## A-04 — FACTORY E3 requires primary metadata deposit

### Observation

`FACTORY-01` is recorded as E3 / `CONFIRMED` for token-metadata provenance.

The case file states that the exact primary Pump.fun token page and mint still need to be preserved.

The source index also lists the exact primary Pump.fun page / mint as pending source-hardening work.

### Audit disposition

The finding can remain technically plausible at E3 if the primary metadata was directly observed during the audit, but the **public repository cannot independently demonstrate the E3 basis until that primary metadata or an auditable capture is deposited**.

This is an auditability gap, not evidence that the finding is false.

---

## A-05 — Source status and repository availability must remain separate

### Observation

`PRIMARY-CAPTURED` is defined as material captured directly from the primary platform, even if it has not yet been archived in the repository.

That definition is valid, but a reader can easily interpret a populated `raw_evidence` path as meaning that the file is already available.

### Audit disposition

For the public package, distinguish explicitly between:

- captured during investigation
- deposited in repository
- independently retrievable live

A source can be `PRIMARY-CAPTURED` while its repository deposit remains `PENDING`.

---

## A-06 — Timing findings are appropriately limited

### Observation

HIVEMIND and GBC timing comparisons rely on third-party indexed token-creation timestamps rather than fully reconstructed primary on-chain creation events.

The timeline, source index and timing case preserve this limitation.

### Audit disposition

**NO MATERIAL CORRECTION REQUIRED.**

`TIMING-01` is defensible only as confirmation of the interval between the observed public timestamp and the **indexed** creation timestamp.

It does not establish causality, automation, prior knowledge or common control.

`TIMING-02` appropriately rejects a uniform sub-minute latency hypothesis.

---

## A-07 — Wallet prevalence restraint is internally consistent

### Observation

The repeat-launch-wallet case identifies multiple AI/Grok-linked launches but explicitly rejects using the discovered set to estimate population prevalence.

`WALLET-03` records the prevalence claim as `NOT ESTABLISHED` because the full launch population was not reconstructed and discovery is selection-biased.

### Audit disposition

**NO MATERIAL CORRECTION REQUIRED.**

Do not introduce a numerator/denominator or percentage unless a complete, independently reproducible launch census is later built.

---

## A-08 — Actor attribution restraint is internally consistent

### Observation

The repository repeatedly distinguishes structural mechanisms from common-control allegations.

`ATTRIB-01` does not identify `@ridark_eth` as the controller of the HAh7q wallet, and `NETWORK-01` does not establish one coordinated operation.

SPIDER and REAPER are used as counterevidence against projecting later creator adoption backward into pre-launch coordination.

### Audit disposition

**NO MATERIAL CORRECTION REQUIRED.**

This distinction should remain unchanged in the Medium article.

---

## A-09 — Payout language is appropriately separated from protocol capability

### Observation

The methodology distinguishes:

1. capability
2. configuration
3. payout

`ECON-01` establishes platform capability only. SPIDER and REAPER payout claims remain unverified without end-to-end reconstruction.

### Audit disposition

**NO MATERIAL CORRECTION REQUIRED.**

Do not convert creator statements, fee-routing metadata or claim language into verified recipient payouts without transaction-level evidence.

---

# Public-lock decision

## What can be considered stable now

The following methodological conclusions are stable:

- asset movement is separate from agent performance
- code capability is separate from historical P&L
- protocol fee capability is separate from verified payout
- creator adoption is separate from pre-launch coordination
- distribution depth is separate from evidence depth
- temporal proximity is separate from causal provenance
- repeated structure is separate from common-control attribution

The conservative verdict vocabulary and evidence-grade framework are also internally coherent.

## What should remain pre-public / source-hardening status

The following should not be represented as fully source-final until the evidence is deposited or independently re-established:

1. exact original GRASS X-source mapping
2. original MEMEMOON duplicate-pair captures
3. KITSUNE original source capture
4. RoundtableSpace original capture if not yet deposited
5. FACTORY primary Pump.fun mint/page and metadata capture
6. SPIDER original screenshots and exact post URLs/timestamps
7. REAPER original or sufficiently strong archived evidence, including same-mint chronology
8. primary Pump.fun fee-documentation snapshot or immutable reference
9. primary on-chain creation timestamps for HIVEMIND/GBC/OPENCODEX if timing is to be upgraded beyond indexed chronology
10. SHA-256 hashes for deposited raw files

---

# Audit conclusion

The investigation does not currently fail because the structural thesis is too weak.

Its principal pre-public weakness is that several evidentiary references are **described more completely than they are currently deposited in the repository**.

That is fixable without strengthening any verdict.

The correct next step is source hardening, not narrative expansion.

Until that is complete, Evidence Ledger v1.0 should be treated as a frozen adjudication pass with known source-deposition limitations, not as a fully self-contained final evidence package.
