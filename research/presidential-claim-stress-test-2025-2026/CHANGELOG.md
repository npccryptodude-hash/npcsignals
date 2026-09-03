# Changelog

All material changes to the NPCsignals **Presidential Claim Stress Test 2025–2026** are recorded here.

## v1.0-audit — 2026-09-03

### Source and denominator cleanup

- Reconstructed a claim-level public ledger from the working analysis.
- Source-checked and benchmark-checked the high-salience claim families.
- Reduced the high-salience factual-accuracy denominator from approximately **79** to **78** scoreable claim families.
- Excluded one partly predictive / claim-definition-failure row rather than forcing it into the factual-accuracy denominator.
- Corrected a year assignment for one documented drug-overdose claim.
- Identified and repaired a temporary speaker mismatch during source audit before final inclusion.

### Accuracy result

The audit-cleaned high-salience distribution is:

- **Supported:** 9 / 78 — 11.5%
- **Mixed / Misleading:** 9 / 78 — 11.5%
- **Unsupported:** 9 / 78 — 11.5%
- **False / Severe:** 51 / 78 — 65.4%

The previously published False / Severe figure was **65.8%**.

The core result remained materially unchanged:

- **Control sample False / Severe:** 30.0%
- **High-salience False / Severe:** 65.4%
- **Ratio:** approximately 2.18×

### Sensitivity table

Updated high-salience failure rates after denominator cleanup:

- **False / Severe only:** 65.4%
- **False + Unsupported:** 76.9%
- **Everything below Supported:** 88.5%

### Claim Amplification Index

The original row-level CAI assignments had not been preserved in a fully auditable form.

A new explicit CAI rubric was therefore applied from the claim-level evidence rather than tuning scores to reproduce the original aggregate.

Current reconstruction:

- **CAI ≥2:** 55 / 78 — 70.5%
- **CAI ≥3:** 28 / 78 — 35.9%

Previously published figures were:

- **CAI ≥2:** 68.4%
- **CAI ≥3:** 40.5%

The structural amplification finding remains, but the exact CAI distribution changed under the explicit audit rubric.

### Persistence Index and Persistent Amplification Rate

The original published persistence counts were found to be incomplete during repeat-search reconstruction.

The article was updated so that exact final **PI** and **PAR** percentages are no longer presented as settled results.

Current status:

- additional persistent claim families have been documented beyond the original count;
- exhaustive repeat-search across all eligible claim families is still incomplete;
- final PI and PAR rates remain **under audit**.

### Independent second-pass

A blind second-pass was completed on the 78 eligible claim families without access to NPCsignals' original scores.

Results:

- **Accuracy exact agreement:** 64 / 78 — 82.1%
- **Accuracy Cohen's kappa:** 0.645
- **CAI exact agreement:** 46 / 78 — 59.0%
- **CAI ≥2 threshold agreement:** 64 / 78 — 82.1%
- **CAI ≥3 threshold agreement:** 60 / 78 — 76.9%
- **CAI weighted kappa (linear):** 0.478

The second scorer produced:

- **PASS / Mostly Supported:** 11.5%
- **Mixed / Misleading:** 12.8%
- **Unsupported:** 5.1%
- **False / Severe:** 70.5%

The main inter-rater disagreement is concentrated in the boundaries between `MIXED`, `UNSUPPORTED`, and `FALSE`, and in the severity levels of CAI.

### Interpretation

The core high-salience accuracy gap survived source cleanup and independent scoring.

CAI remains structurally informative but materially scorer-sensitive.

PI is the least mature layer and remains under active audit.

---

Future changes should be appended as new dated versions rather than modifying this entry.
