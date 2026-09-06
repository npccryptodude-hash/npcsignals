# Corrections and Rejected Hypotheses

## AI Performance Narrative Audit 2026

This file records material revisions made during the investigation.

Corrections are preserved because the audit is designed to reduce confirmation bias, not to maximize suspicious-looking connections.

Each correction records:

1. the original hypothesis
2. why it was plausible
3. the evidence that changed the assessment
4. the revised conclusion

A correction is not treated as a failure to be hidden. It is part of the audit record.

---

## CORR-01 — HyperGrok attribution downgraded

### Original hypothesis

A HyperGrok token appeared to fit the same repeat-launch pattern as other AI/Grok-linked assets associated with the identified creator-wallet cluster.

### Why it was plausible

The token name, surrounding narrative and discovery context resembled other assets already linked to the same research thread.

### New evidence

A mint collision / token-identity conflict made the original attribution unreliable.

The available evidence did not support treating the initially identified HyperGrok asset as the same token or as a clean wallet-linked case.

### Revised conclusion

The HyperGrok connection was downgraded and excluded from the locked core findings.

No prevalence or repeat-launch conclusion relies on HyperGrok.

### What remains not established

- the correct HyperGrok mint for the originally observed narrative
- creator-wallet attribution
- common control
- coordination

---

## CORR-02 — Creator-fee capability separated from payout verification

### Original hypothesis

Public statements such as "fees redirected to GitHub" initially appeared too vague to represent a real technical fee-routing mechanism.

### Why it was plausible

GitHub is not itself a blockchain recipient address, and the wording can sound promotional rather than technical when read without protocol context.

### New evidence

Primary Pump.fun documentation showed that creator-fee and fee-sharing infrastructure exists, including social / identity-linked fee mechanics and configurable sharing.

This established that creator-fee routing language can correspond to real protocol capability.

However, the audit did not reconstruct a complete mint-specific path from fee configuration to recipient wallet for the SPIDER, REAPER or FACTORY cases.

### Revised conclusion

Creator-fee infrastructure is confirmed at the protocol level.

Specific payouts remain unverified unless an end-to-end path is reconstructed.

This produced the rule:

**Fee-routing claim ≠ verified payout.**

### What remains not established

- recipient wallet in each examined case
- amount received
- claim transaction in each case
- whether all routed fees were ultimately claimed

---

## CORR-03 — Creator coordination hypothesis weakened

### Original hypothesis

Repeated creator-linked token launches initially made pre-launch creator coordination a plausible explanation.

### Why it was plausible

Tokens referenced specific creators, repositories and public narratives.

Subsequent creator participation could superficially appear to be evidence that the creator had been involved from the beginning.

### New evidence

In SPIDER, Phosphen publicly stated that he did not deploy the token and learned about it from someone in his replies.

In REAPER, Kai publicly described the token as something someone else had launched in support of his work.

Subsequent public activity in both cases showed creator claim, adoption or onboarding after the token already existed.

### Revised conclusion

Pre-launch creator coordination is not required to explain the observed mechanism.

Post-launch creator onboarding is a better-supported interpretation for these cases.

This does not establish that no private pre-launch communication occurred.

This produced the rule:

**Creator adoption ≠ pre-launch coordination.**

### What remains not established

- absence of all private communication before launch
- identity of every token launcher
- whether coordination occurred in other cases
- common control across actors

---

## CORR-04 — GRASS Blockscout anomaly excluded as adverse evidence

### Original hypothesis

A conflicting Blockscout representation of the GRASS address appeared potentially useful as evidence against the token / contract record presented elsewhere.

### Why it was plausible

The explorer representation conflicted with other available indexing and therefore appeared, at first, to suggest a technical inconsistency.

### New evidence

The conflict was more consistent with explorer or indexing limitations than with a reliable contradiction in the underlying asset record.

Other sources did not support using the Blockscout result as clean adverse evidence.

### Revised conclusion

The Blockscout anomaly was excluded from the substantive GRASS findings.

The GRASS audit does not rely on this explorer conflict.

### What remains not established

- the exact cause of the indexing anomaly

---

## CORR-05 — "Touch grass" language rejected as prior-link evidence

### Original hypothesis

Historical use of "touch grass" wording by accounts later associated with the GRASS discussion initially appeared potentially relevant to prior knowledge or narrative linkage.

### Why it was plausible

The wording overlapped directly with the token name and appeared repeatedly in account history.

### New evidence

Historical searches showed that "touch grass" had been used generically as common internet slang long before the 2026 GRASS token case.

Examples appeared in unrelated contexts and were not specific to the token.

### Revised conclusion

Historical "touch grass" wording is not evidence of prior knowledge of, or coordination around, the 2026 GRASS token.

The wording was retained only as counterevidence against that hypothesis.

---

## CORR-06 — Older Grass crypto reference determined to be unrelated

### Original hypothesis

A 2025 crypto-related reference to "the next Grass" initially appeared potentially relevant to the later GRASS token case.

### Why it was plausible

Unlike generic slang, this was an explicitly crypto-related use of the word Grass.

### New evidence

The post referred to the pre-existing Grass Network / airdrop ecosystem rather than the later Robinhood Chain GRASS token examined in this audit.

### Revised conclusion

The 2025 reference is unrelated to the 2026 GRASS token case and is not used as evidence of prior knowledge or coordination.

---

## CORR-07 — Uniform sub-minute launch hypothesis rejected

### Original hypothesis

Very short intervals observed between some public posts and token creation raised the possibility of a repeated sub-minute launch process.

### Why it was plausible

At least one identified case, HIVEMIND, showed an indexed token creation time less than one minute after a relevant Orbital post.

Earlier working notes also contained another possible sub-minute case.

### New evidence

Other identified launches showed materially longer intervals.

GBC, for example, showed an interval of approximately 16 minutes between the referenced public post and indexed token creation.

The second sub-minute candidate was not sufficiently source-verified for inclusion in the locked finding set at the time of v1.0 preparation.

### Revised conclusion

The hypothesis that relevant launches consistently occur within seconds was rejected.

Timing remains useful as a structural indicator, but not as standalone evidence of automation or coordination.

This produced the rule:

**Temporal proximity ≠ causal provenance.**

### What remains not established

- automation
- manual launch process
- pre-coordination
- common control
- causal direction between post and token creation

---

## CORR-08 — Repeat-launch wallet prevalence claim withheld

### Original hypothesis

Search results and third-party indexes suggested that a large share of launches from the identified creator wallet might follow the AI/Grok narrative-tokenization pattern.

### Why it was plausible

Multiple identified launches from the same wallet referenced AI/Grok builders, repositories or performance narratives.

A third-party index also reported a larger total launch count for the wallet.

### New evidence

The audit did not reconstruct a complete and independently validated historical launch census for the wallet.

Search-driven discovery disproportionately surfaces assets matching the investigation's existing terms, creating selection bias.

### Revised conclusion

The audit records repeated AI/Grok narrative tokenization among identified launches, but makes no percentage or prevalence estimate across the wallet's full launch history.

The full-population prevalence claim is classified as `NOT ESTABLISHED`.

### What remains not established

- complete number of launches
- percentage matching any narrative class
- whether most launches follow the observed pattern
- whether selection is automated

---

## CORR-09 — Wallet identity attribution kept unresolved

### Original hypothesis

The Pump.fun profile name `ridarkdev`, together with a RIDARK token launched by the same wallet, made attribution of the wallet to `@ridark_eth` appear plausible.

### Why it was plausible

The naming overlap and token metadata created a strong public association.

### New evidence

The broader investigation independently demonstrated that third parties can create tokens around other creators and projects without proven pre-launch creator control.

Using token naming or metadata as identity proof would therefore apply a weaker attribution standard than the audit uses elsewhere.

### Revised conclusion

The public association is retained as a lead, but control of the wallet by `@ridark_eth` is `NOT ESTABLISHED`.

### What remains not established

- legal or personal identity of the wallet controller
- common control with Orbitalx0
- common control with referenced creators

---

## Correction standard

Future corrections should preserve the same four-part structure:

**Original hypothesis**  
**Why it was plausible**  
**New evidence**  
**Revised conclusion**

When a correction changes a locked ledger finding, the change should be recorded in a later ledger version rather than silently rewriting the published v1.0 record.
