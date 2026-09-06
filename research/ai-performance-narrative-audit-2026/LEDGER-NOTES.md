# Evidence Ledger Notes

The verdict vocabulary in `evidence-ledger-v1.0.csv` must be read according to `methodology.md`.

A verdict applies only to the proposition and scope defined in its row.

In particular:

- `PROVENANCE FAILURE` does not mean fraud.
- `UNVERIFIED` does not mean false.
- `NON-REPRODUCIBLE` does not mean non-occurrence.
- `MATERIAL MISMATCH` does not establish intent.
- `INCONSISTENT` applies only to the conflicting elements identified in the row.
- `NOT ESTABLISHED` does not establish the opposite proposition.
- `SUPPORTED` and `STRONGLY SUPPORTED` remain subject to the limitations stated in the same row.

Evidence grades describe the support for a specific finding, not the seriousness of the finding.

## Row-level scope protection

Each substantive ledger row should be interpreted together with its:

- `claim`
- `observed_evidence`
- `evidence_grade`
- `supported_inference`
- `counterevidence`
- `verdict`
- `verdict_scope`
- `not_established`
- `limitation`
- `primary_source`
- `source_status`
- `raw_evidence`
- `synthesis_basis`, where applicable

No single verdict label should be quoted as if it represents a broader accusation than the row itself supports.

## Evidence grades

The audit uses one grade per finding:

- `E0` — claim only
- `E1` — public or archived support
- `E2` — independent corroboration
- `E3` — primary technical evidence
- `E4` — end-to-end reconstruction

Hybrid grades such as `E2/E3` are not used.

Cross-case synthesis findings receive the grade warranted by the evidence necessary to support the synthesis itself. Stronger grades held by individual contributing findings do not automatically transfer to the cross-case conclusion.

## Source status

Source status is recorded separately from evidence grade.

- `PRIMARY-LIVE` — original source remains directly accessible
- `PRIMARY-CAPTURED` — original source was captured directly but may not be reliably retrievable through external tooling
- `ARCHIVED-CORROBORATION` — archived copy of public material
- `SECONDARY-DISCOVERY` — third-party index or source used primarily for discovery or corroboration

A source status is not itself an evidence grade.

## Negative evidence

Failure to locate a wallet, transaction, payout or other record is not converted into proof that the event did not occur.

Where the audit cannot independently reconstruct a claim, appropriate verdicts include:

- `UNVERIFIED`
- `NON-REPRODUCIBLE`
- `NOT ESTABLISHED`

rather than `FALSE`.

## Structural findings versus actor attribution

The ledger separates structural findings from claims about common control, coordination or intent.

For example, evidence may support that:

- a narrative was amplified
- a token referenced that narrative
- creator-fee infrastructure existed
- creator onboarding occurred after launch

without establishing that all involved actors knowingly coordinated with one another.

Repeated structure does not automatically establish a single operator.

## Corrections

The ledger is versioned.

Once v1.0 is published, later evidence should not silently rewrite the historical record.

Material changes should be documented through:

- a revised finding status
- a new finding
- a correction entry in `corrections.md`
- or a later ledger version such as `evidence-ledger-v1.1.csv`

Corrections should explain:

1. the original hypothesis or classification
2. why it was plausible at the time
3. what new evidence changed the assessment
4. the revised conclusion

## Final reading rule

The ledger should be read as an adjudication record, not as a list of allegations.

The purpose is to preserve both supporting evidence and the limits of what that evidence can establish.
