NPCsignals — Presidential Claim Stress Test 2025–2026

This directory contains the public audit materials for the NPCsignals Presidential Claim Stress Test 2025–2026.

The project tests how closely falsifiable presidential claims remain attached to the strongest relevant evidence, with particular attention to political salience, amplification, and persistence.

Dataset

Control sample: 50 mechanically selected falsifiable claims from complete presidential speeches.

High-salience layer: 78 scoreable claim families after source validation and claim-definition cleanup.

Dataset window: January 2025 – September 3, 2026.

Unit of analysis: one claim family counts once toward factual accuracy. Repetitions are tracked separately.

The high-salience layer is not intended to estimate the accuracy of all presidential speech. It is a structured test of politically prominent, repeated, numerically specific, or publicly disputed claims.

Accuracy framework

Claims are classified as:

PASS / MOSTLY SUPPORTED

MIXED / MISLEADING

UNSUPPORTED

FALSE / SEVERE FALSEHOOD

HOLD / EXCLUDED where a claim cannot be scored cleanly

The audit-cleaned high-salience layer currently contains:

Supported: 9 / 78 — 11.5%

Mixed / Misleading: 9 / 78 — 11.5%

Unsupported: 9 / 78 — 11.5%

False / Severe: 51 / 78 — 65.4%

The control sample remains:

Supported: 50%

Mixed / Misleading: 16%

Unsupported: 4%

False / Severe: 30%

The False / Severe rate in the high-salience layer is therefore approximately 2.18× the control-sample rate.

Claim Amplification Index (CAI)

CAI measures transformation of an identifiable empirical core. A claim does not receive a high CAI score simply because it is false.

CAI 0: no material amplification, or no identifiable empirical kernel to amplify

CAI 1: mild strengthening

CAI 2: material transformation

CAI 3: severe transformation

CAI 4: extreme distortion, mathematical failure, categorical reversal, or comparable structural mismatch

Current audit reconstruction:

CAI ≥2: 55 / 78 — 70.5%

CAI ≥3: 28 / 78 — 35.9%

CAI is more scorer-sensitive than the core accuracy classification and should be interpreted accordingly.

Persistence Index (PI)

PI tracks repetition separately from factual accuracy.

P0: single occurrence after reasonable repeat search

P1: repeated

P2: repeated after relevant contradictory or corrective evidence became publicly available

P3: systematically repeated or amplified over time after corrective evidence

The full repeat-search is still in progress. Exact final PI and Persistent Amplification Rate (PAR) percentages should therefore be treated as under audit.

Independent second-pass

A separate scorer reviewed the 78 eligible claim families without access to NPCsignals' original classifications.

Current inter-rater results:

Accuracy exact agreement: 64 / 78 — 82.1%

Accuracy Cohen's kappa: 0.645

CAI exact agreement: 46 / 78 — 59.0%

CAI ≥2 threshold agreement: 64 / 78 — 82.1%

CAI ≥3 threshold agreement: 60 / 78 — 76.9%

CAI weighted kappa (linear): 0.478

PI agreement is not yet suitable for a global reliability estimate because the NPCsignals repeat-audit is incomplete.

Files

NPCsignals_Presidential_Claim_Stress_Test_Ledger_v1.0.xlsx
Main source ledger, audit classifications, CAI reconstruction, persistence evidence, publication audit, and inter-rater comparison.

NPCsignals_Presidential_Claim_Stress_Test_Blind_Second_Pass.xlsx
Blind scoring packet containing claims, sources, and benchmark evidence without NPCsignals' original scores.

CHANGELOG.md
Version history and material audit corrections.

Evidence and intent rules

The evidence hierarchy prioritizes the strongest relevant evidence available for the claim and period assessed.

A factual discrepancy does not establish deliberate deception. The stress test evaluates factual stability, not intent or motive.

Versioning

Material changes are versioned rather than silently overwritten.

Where an audit changes a previously published figure, the change should be documented in CHANGELOG.md and reflected in the public article.

Publication

The narrative analysis is published by NPCsignals on Medium:

Presidential Claim Stress Test 2025–2026
What happens to factual information when political claims become larger, more useful, and more repetitive?

Repository files are the audit layer; the Medium article is the public explanation layer.

NPCsignals
Observe → Filter → Validate → Stress → Archive → Review
