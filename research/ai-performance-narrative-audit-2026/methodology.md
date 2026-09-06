# Methodology

## AI Performance Narrative Audit 2026

Version: 1.0  
Status: Locked methodology for Evidence Ledger v1.0

---

## 1. Purpose

This methodology defines how evidence is collected, classified and adjudicated in the NPCsignals AI Performance Narrative Audit 2026.

The investigation examines public claims involving AI or autonomous-agent performance, their provenance, amplification, downstream tokenization, creator-fee infrastructure and post-launch creator participation.

The purpose is not to determine whether an account, creator or project is "good" or "bad."

The purpose is to answer narrower questions:

1. What was claimed?
2. What can be directly observed?
3. What can be independently verified?
4. What reasonable inference follows from the evidence?
5. What stronger conclusion is not established?
6. What evidence weakens the working hypothesis?

Claims are not upgraded because they are popular, detailed, repeated or financially successful.

---

## 2. Unit of analysis

The audit distinguishes between several types of observational unit.

### 2.1 Performance claim

A specific claim about historical AI or agent performance.

Examples:

- a trading agent entered and exited a token
- an agent generated a specific profit
- an autonomous system performed a measurable amount of work

### 2.2 Public content item

An identifiable public post, video, repository, metadata record or statement.

Different reposts of the same underlying claim are not automatically treated as independent performance observations.

### 2.3 Asset

A specific token, contract, mint or trading pair.

Asset performance is analyzed separately from claims about who captured that performance.

### 2.4 Actor

An account, creator, developer, amplifier, wallet or tokenization participant.

Shared behavior or overlapping content does not establish shared control.

### 2.5 Case

A bounded group of evidence relating to one claim, asset, provenance cluster or onboarding sequence.

### 2.6 Cross-case synthesis

A structural finding derived from multiple individually adjudicated cases.

Cross-case synthesis does not inherit the strongest evidence grade present in the contributing cases.

Its grade reflects the weakest evidence necessary to support the synthesis.

---

## 3. Evidence hierarchy

The audit uses five evidence grades.

The grade describes the strength of the evidence supporting a specific finding.

It does not describe the seriousness of the finding.

### E0 — Claim only

A public or reported assertion exists, but no independent supporting evidence has been identified.

Examples:

- a claimed profit with no identifiable wallet or transaction
- a statement repeated without additional evidence
- a fee claim without identifiable routing or recipient evidence

E0 does not mean false.

It means unsupported beyond the claim itself.

### E1 — Public or archived support

The finding is supported by identifiable public material such as:

- original social posts
- archived posts
- screenshots
- videos
- creator statements
- public descriptions

but has not been independently corroborated through a separate technical or metadata source.

E1 may establish that a statement was made.

It does not necessarily establish that the underlying event occurred.

### E2 — Independent corroboration

The finding is supported by more than one non-identical evidentiary source or by independent metadata/provenance evidence.

Examples:

- a public post plus independently retrievable token metadata
- the same provenance relationship visible through separate public systems
- a creator statement plus independently established launch chronology
- multiple directly observed cases supporting the same structural mechanism

Sources must add independent information.

Ten copies of the same post do not create E2 evidence.

### E3 — Primary technical evidence

The finding is supported by primary technical material such as:

- blockchain transactions
- contract state
- wallet history
- token mint data
- primary protocol documentation
- primary platform metadata
- directly inspectable repository data

E3 can strongly establish a technical fact.

It does not automatically establish actor intent, motive or off-chain coordination.

### E4 — End-to-end reconstruction

The complete material chain has been independently reconstructed.

For a claimed trade, this may include:

wallet  
→ entry transaction  
→ asset  
→ exit transaction  
→ resulting proceeds

For a creator-fee payout, this may include:

token mint  
→ fee configuration  
→ recipient mapping  
→ claim transaction  
→ recipient wallet

E4 is reserved for complete reconstruction of the relevant event.

Partial reconstruction remains E3 or below.

---

## 4. Evidence-grade constraints

### 4.1 Grades apply to findings, not cases

A single case may contain findings at several evidence levels.

Example:

The existence of a token may be E3.

The claim that a specific AI agent traded that token may remain E0 or E1.

These findings must not be merged into one grade.

### 4.2 Strong evidence for one fact does not transfer to another fact

Evidence of asset movement does not establish participant performance.

Evidence of code capability does not establish historical execution.

Evidence of creator-fee capability does not establish a specific payout.

Evidence of later creator adoption does not establish pre-launch coordination.

### 4.3 Repetition does not raise the grade

Repeated claims are not independent corroboration unless the new source provides genuinely new evidence.

This applies especially to:

- reposts
- copied first-person narratives
- aggregator pages
- token descriptions quoting upstream posts

### 4.4 Cross-case findings receive one grade

Combined grades such as `E2/E3` are not used in the Evidence Ledger.

A synthesis finding receives one grade based on the evidence required to support that specific proposition.

The contributing findings are listed separately in `synthesis_basis`.

---

## 5. Source hierarchy

Sources are prioritized in the following order where applicable:

1. primary on-chain evidence
2. primary protocol or platform documentation
3. original public post
4. original repository
5. primary token metadata
6. creator or developer statement
7. archived public material
8. third-party index or aggregator
9. secondary commentary

This hierarchy does not mean that every higher-ranked source is automatically correct.

It defines preferred evidence provenance.

---

## 6. Source-status labels

Each material source should be classified where practical.

### PRIMARY-LIVE

Original source currently retrievable from its primary platform.

### PRIMARY-CAPTURED

Original source captured directly from its primary platform and preserved locally, even if later retrieval is restricted or unavailable.

### ARCHIVED-CORROBORATION

A preserved public copy used to corroborate or recover material not reliably retrievable from the primary platform.

### SECONDARY-DISCOVERY

A third-party index, aggregator or secondary source used primarily to discover candidate evidence.

Secondary-discovery sources should not be promoted to primary evidence merely because they are convenient.

---

## 7. Adjudication fields

Every substantive row in `evidence-ledger-v1.0.csv` should contain the following:

### finding_id

Permanent identifier for the finding.

Example: `PROV-01`

### case

The relevant case or evidence cluster.

### claim

The proposition being tested.

### observed_evidence

What was directly observed.

This field should avoid interpretation where possible.

### source_type

The type of source supporting the observation.

### evidence_grade

One of:

`E0`  
`E1`  
`E2`  
`E3`  
`E4`

### supported_inference

The strongest reasonable interpretation supported by the evidence.

### counterevidence

Evidence that weakens, complicates or contradicts the working interpretation.

This field should not be omitted merely because it is inconvenient.

### verdict

The adjudicated result.

### verdict_scope

The precise domain to which the verdict applies.

Example: `Content provenance only`

### not_established

Stronger interpretations that the evidence does not justify.

### limitation

Important evidentiary limitations.

### primary_source

Direct source URL, transaction identifier, contract, mint, repository or internal source reference.

### source_status

One of the source-status labels defined above.

### raw_evidence

Repository path to preserved raw evidence where available.

### synthesis_basis

Used only for cross-case findings.

Lists the contributing finding IDs.

### status

Examples:

`LOCKED`  
`PROVISIONAL`  
`REVISED`  
`REJECTED`

---

## 8. Verdict vocabulary

Verdicts should use controlled terminology.

### CONFIRMED

The proposition is supported by sufficient evidence.

### STRONGLY SUPPORTED

The proposition is supported across multiple relevant observations, but full end-to-end reconstruction is not available or not applicable.

### SUPPORTED

Evidence reasonably supports the proposition, with meaningful limitations.

### UNVERIFIED

The claim exists but could not be independently verified to the required standard.

This does not mean false.

### NON-REPRODUCIBLE

The audit could not reconstruct or reproduce the claimed event from the evidence available.

This does not mean the event did not occur.

### INCONSISTENT

Two or more elements of the available evidence materially conflict.

The scope of the inconsistency must be stated.

### MATERIAL MISMATCH

The published description does not cleanly match independently established technical or factual properties.

A mismatch does not by itself establish fabrication or intent.

### PROVENANCE FAILURE

The apparent independence or origin of content is materially undermined.

This verdict applies to content provenance only unless additional evidence supports a wider interpretation.

### NOT ESTABLISHED

The available evidence is insufficient to support the proposition.

### REJECTED

The audit identified evidence that makes the working hypothesis no longer supportable in its previous form.

---

## 9. Required scope protection

Verdicts that could be misunderstood if isolated must include `verdict_scope` and `not_established`.

Example:

Finding: `PROV-01`  
Verdict: `PROVENANCE FAILURE`  
Verdict scope: `Content provenance only`

Not established:

- common account control
- coordinated fraud
- fabrication of the underlying trade
- financial coordination

This protects the meaning of the finding if ledger rows are quoted or machine-extracted outside the repository.

---

## 10. Claim versus event separation

The audit treats the following as separate questions:

### Did the underlying event occur?

Example: did the token move from approximately one market capitalization to another?

### Did the claimed actor participate?

Example: did the identified AI agent execute the entry and exit?

### Did the actor realize the claimed result?

Example: did the wallet actually receive the claimed profit?

A positive answer to the first question cannot substitute for evidence answering the second or third.

This produces the rule:

**Asset movement ≠ agent performance.**

---

## 11. Capability versus historical execution

Technical systems may be evaluated independently from claims about historical performance.

Evidence that software can scan tokens, execute trades, hold keys, trigger exits or launch assets does not establish that a particular historical event occurred.

This produces the rule:

**Code capability ≠ historical P&L.**

---

## 12. Creator-fee verification

Creator-fee analysis is separated into three levels.

### Capability

Does the protocol support the relevant fee mechanism?

### Configuration

Was the specific asset configured to use that mechanism?

### Payout

Can the actual payment path to a recipient be reconstructed?

A confirmed capability does not automatically confirm configuration.

A confirmed configuration does not automatically confirm payout.

This produces the rule:

**Fee-routing claim ≠ verified payout.**

---

## 13. Creator chronology

Creator association must be evaluated chronologically.

The following events are distinct:

1. technical work or narrative exists
2. token is created
3. creator becomes aware
4. creator is offered fee participation
5. creator claims or accepts
6. creator publicly acknowledges token
7. downstream accounts use creator participation as social proof

Later participation must not be projected backward without evidence.

This produces the rule:

**Creator adoption ≠ pre-launch coordination.**

---

## 14. Content provenance

The audit distinguishes between:

### Independent observation

A source provides independent evidence of an event.

### Independent publication

A different account publishes the same information.

These are not the same.

When highly specific narratives recur across accounts, the audit asks whether the accounts are independently observing the event or reproducing common source material.

This produces the rule:

**Distribution depth ≠ evidence depth.**

---

## 15. Arithmetic checks

Arithmetic comparison may be used as an indicator.

Examples include comparing entry market cap, exit market cap, stated position size and claimed profit.

Arithmetic similarity does not prove fabrication.

It may identify a claim that warrants stronger provenance or execution checks.

Arithmetic-only findings must not be assigned intent.

---

## 16. Timing analysis

Timestamp analysis may support chronology.

Timing alone does not establish:

- coordination
- automation
- common control
- prior knowledge
- causal direction

Very short intervals may be consistent with several explanations, including automated discovery, manual rapid response, prior preparation or shared workflow.

Where timing is used, alternative explanations must be retained unless independently excluded.

This produces the rule:

**Temporal proximity ≠ causal provenance.**

---

## 17. Negative evidence

Failure to locate evidence is treated cautiously.

The audit does not infer:

`not found → did not happen`

Instead, searches may support verdicts such as:

- `UNVERIFIED`
- `NON-REPRODUCIBLE`
- `NOT ESTABLISHED`

Search limitations should be documented where relevant.

---

## 18. Counterevidence protocol

Counterevidence is mandatory when discovered.

For each working hypothesis, the audit should actively seek evidence that could weaken it.

Examples include:

- unrelated historical use of similar terminology
- creator statements indicating no pre-launch knowledge
- alternative token mints
- indexing conflicts
- evidence that an amplification account has a much broader content scope
- examples inconsistent with an apparent timing pattern

Counterevidence must not be removed because it weakens the article narrative.

---

## 19. Correction protocol

When a finding changes, the original reasoning should remain visible.

Each correction should document:

### Original hypothesis

What was initially suspected or classified.

### Why it was plausible

What evidence made the hypothesis reasonable at the time.

### New evidence

What later information changed the assessment.

### Revised conclusion

What the evidence now supports.

Corrections are recorded in `corrections.md`.

A correction is evidence that the audit process is functioning.

It is not treated as a failure to be hidden.

---

## 20. Version control

Evidence Ledger v1.0 is frozen once published.

New evidence should not silently modify historical adjudications.

Material updates should create a new finding, a revised finding status or a new ledger version.

Example: `evidence-ledger-v1.1.csv`

The correction record should identify what changed and why.

---

## 21. Raw evidence handling

Original evidence captures should remain unedited where available.

Examples include screenshots, videos, exported metadata, protocol documentation and transaction records.

Derived figures may be cropped, annotated, combined or resized for readability.

Derived figures must not replace the raw evidence record.

Where practical, raw evidence files should be accompanied by SHA-256 hashes.

---

## 22. Reporting standard

The public article may simplify technical detail for readability.

It may not make a stronger claim than the Evidence Ledger.

If the article and ledger appear to conflict, the ledger and underlying evidence control the audit conclusion.

---

## 23. Structural findings versus actor attribution

The audit makes an explicit distinction between:

### Structural finding

A recurring economic or information mechanism exists.

and:

### Actor attribution

Specific actors knowingly coordinated or operated the mechanism together.

Evidence supporting the first does not automatically support the second.

Repeated structure may arise from:

- imitation
- shared incentives
- automation
- opportunistic behavior
- common tools
- independent actors responding to the same market conditions
- coordination

The audit does not select among these explanations without evidence.

---

## 24. Final methodological principle

The audit is designed to reduce the risk that the investigation itself becomes an example of the problem it is examining.

A compelling narrative is not enough.

A repeated pattern is not enough.

A plausible connection is not enough.

The standard is:

**What survives after the strongest reasonable alternative explanations and counterevidence have been considered?**

A hypothesis survives only what we failed to falsify.
