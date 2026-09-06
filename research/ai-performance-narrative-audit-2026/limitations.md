# Limitations

## Purpose

This file records the main limitations of the AI Performance Narrative Audit 2026.

The purpose is to make the boundaries of the investigation explicit and to prevent the evidence from being read as stronger than it is.

The audit is designed to separate what was observed from what was inferred, and to preserve unresolved uncertainty where the available public evidence does not support a stronger conclusion.

---

## 1. Public evidence is incomplete

The audit relies primarily on public posts, public repositories, public platform metadata, protocol documentation, token and wallet data, archived material and user-captured source material.

Private communications, unpublished wallet mappings, internal platform records, deleted material and non-public agreements are outside the available evidence set unless independently surfaced.

This means that some events may have occurred without leaving enough public evidence for independent reconstruction.

Failure to verify is therefore not proof of non-occurrence.

---

## 2. Missing wallet attribution limits performance verification

Several AI-performance claims examined during the audit did not expose the full transaction path needed for independent reconstruction.

A market move may be visible while the claimed agent performance remains unverifiable.

Without a sufficiently attributable wallet and the relevant entry and exit transactions, the audit cannot independently establish that a specific agent captured the reported profit.

This is the central limitation in the GRASS and KITSUNE performance cases.

---

## 3. Asset movement and actor performance are different questions

The existence of a large price move does not establish who captured it.

A token may have traded from one valuation to another exactly as described while the associated first-person performance claim remains unverified.

The audit therefore does not treat market charts as substitutes for participant-level transaction evidence.

---

## 4. Technical capability does not establish historical execution

Public repositories can demonstrate that software exists, that code is capable of performing certain actions, or that an agent architecture is technically plausible.

They do not independently establish that a reported historical trade, profit or decision sequence occurred.

The audit therefore separates code capability from historical P&L.

---

## 5. Archived material has lower evidentiary value than primary live sources

Some findings rely partly on archived captures or third-party mirrors because original posts can be difficult to retrieve or may later become unavailable.

Archived material is useful for documenting that content existed, but may not preserve all metadata or context.

Where possible, the audit distinguishes:

- `PRIMARY-LIVE`
- `PRIMARY-CAPTURED`
- `ARCHIVED-CORROBORATION`
- `SECONDARY-DISCOVERY`

Third-party copies are not treated as equivalent to primary evidence.

---

## 6. Third-party indexes can be incomplete or inconsistent

Token and blockchain indexes are useful for discovery, chronology and cross-checking, but they may lag, omit records, normalize timestamps differently or index the same object inconsistently.

For this reason, third-party index values are not automatically promoted to E3 technical evidence.

The GRASS Blockscout anomaly was excluded from the main findings because conflicting indexing reduced confidence in the observation.

---

## 7. Timing evidence does not establish causality

Short intervals between public content and token creation can be structurally interesting.

They do not, by themselves, establish:

- automation
- prior knowledge
- common control
- coordination
- causal dependence

The audit therefore treats timing as an indicator requiring additional evidence.

The initial idea of a uniform sub-minute launch pattern was rejected after cases with materially different intervals were identified.

---

## 8. Creator chronology may not capture private pre-launch contact

SPIDER and REAPER provide public evidence consistent with post-launch creator onboarding.

That weakens the hypothesis that pre-launch creator participation is necessary for the observed tokenization mechanism.

However, public chronology cannot exclude undisclosed private communication before launch.

The correct conclusion is therefore that pre-launch participation was not established, not that it was impossible.

---

## 9. Creator-fee capability is not the same as a verified payout

Pump.fun documentation can establish that creator-fee and fee-sharing mechanisms exist.

A public statement or metadata field may indicate that fees were intended to be routed to a creator.

Neither establishes a completed payout to a specific wallet unless the path is reconstructed.

The audit therefore separates:

1. capability
2. token-specific configuration
3. verified payout

Only an end-to-end reconstruction can establish the third level with high confidence.

---

## 10. Repetition does not create independent corroboration

Repeated posts, screenshots, amplifications and token metadata may all descend from one original narrative.

The number of appearances is therefore not equal to the number of independent sources.

Distribution depth and evidence depth are treated as separate variables throughout the audit.

---

## 11. Similar wording does not prove common control

Highly similar first-person narratives can support a provenance finding and may justify examination of copying, mutation or narrative reuse.

They do not, on their own, establish:

- shared account control
- one operator
- coordinated fraud
- fabricated performance

The MEMEMOON material is therefore adjudicated as a content-provenance issue rather than as proof of actor identity.

---

## 12. Search selection creates sampling bias

The tokenization portion of the audit was built by following known AI, Grok and creator-linked narratives.

This is not a random sample of all launches from the identified wallet or of all Pump.fun activity.

As a result, the audit does not estimate the prevalence of AI-linked launches across the full wallet history.

Any denominator-based claim would require a complete, independently reconstructed population.

---

## 13. Wallet identity attribution is limited

A wallet may repeatedly launch tokens associated with a profile name, project name, repository or public account.

That does not automatically establish the real-world identity or X-account controller of the wallet.

The repeat-launch wallet `HAh7q881D5qUiXuHCZQXx7PcQQWiyHWE3fVXF5j8khpV` is therefore treated as a wallet-level observation.

The audit does not claim that `ridarkdev`, `@ridark_eth` or any other named person necessarily controlled the wallet unless separate evidence establishes that attribution.

---

## 14. The audit is not a fraud-rate study

The cases were selected because they were relevant to the provenance and financialization question.

They do not form a representative sample of AI-performance claims, meme tokens, X accounts or Pump.fun launches.

The audit therefore cannot estimate:

- the percentage of AI-performance claims that are false
- the percentage of tokens launched without creator consent
- the percentage of creator-fee claims that result in actual payouts
- the prevalence of coordinated operations

No population-level fraud rate is inferred.

---

## 15. Structural recurrence does not establish one operation

The audit identifies a recurring mechanism across observed cases:

viral AI or technical narrative
→ amplification
→ tokenization
→ fee-bearing trading
→ possible creator onboarding
→ possible creator adoption
→ new social proof

Not every case contains every step.

The recurrence of this structure does not establish that all observed cases were organized by one actor or group.

Structural findings and actor attribution are kept separate.

---

## 16. Intent is usually not observable

Public actions can establish that a post was made, a token was launched, metadata was attached, a creator later engaged, or a fee mechanism existed.

They usually cannot establish motive or intent without additional evidence.

The audit therefore avoids inferring deceptive intent from technical mismatch, timing, repetition or tokenization alone.

---

## 17. Arithmetic consistency is only an indicator

Some performance narratives contain arithmetic that is approximately consistent with the reported market-cap move.

Others contain internal constraints that appear inconsistent with the stated position size.

These checks are useful for identifying questions and contradictions, but arithmetic alone does not establish whether a trade occurred or whether a narrative was fabricated.

---

## 18. Deleted or changing platform content can alter future reproducibility

X posts, token pages, profile metadata and platform interfaces can change or disappear.

A future researcher may therefore be unable to retrieve the exact live material available during the audit.

For this reason, captured source material and hashes are preferred where practical.

---

## 19. Derived figures are not raw evidence

Annotated composites, diagrams and editorial graphics may be used to explain chronology or relationships.

They must not be treated as source evidence.

Where a derived figure is included, the underlying unedited source material should be preserved separately whenever available.

---

## 20. No claim should be read beyond its verdict scope

Each Evidence Ledger row is intended to answer one defined proposition.

A finding such as `PROVENANCE FAILURE` applies to provenance.

It does not automatically establish fraud, common control or false performance.

A finding such as `NON-REPRODUCIBLE` applies to the ability to reconstruct the event from the available public evidence.

It does not establish non-occurrence.

The fields `verdict_scope`, `not_established` and `limitation` are therefore part of the finding, not optional commentary.

---

## 21. The evidence set may improve after publication

Additional primary evidence may later become available, including:

- wallet addresses
- transaction hashes
- fee-recipient mappings
- claim transactions
- original posts
- archived metadata
- platform records
- creator statements

New evidence may strengthen, weaken or overturn individual findings.

Any material change should be recorded through versioned updates and the correction log rather than silently modifying the historical record.

---

## Final limitation

The investigation can establish what the available evidence supports.

It cannot make missing evidence disappear.

Where the evidence stops, the conclusion must stop with it.
