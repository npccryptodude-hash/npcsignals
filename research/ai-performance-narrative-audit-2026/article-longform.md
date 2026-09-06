# Distribution Depth Is Not Evidence Depth

## Longform audit narrative

This document is the expanded narrative version of the NPCsignals **AI Performance Narrative Audit 2026**.

It is intentionally longer and more evidentiary than the public-facing Medium article. It explains the cases, analytical distinctions, rejected hypotheses and surviving structural findings in greater detail, while remaining subordinate to the frozen `evidence-ledger-v1.0.csv`.

The Evidence Ledger, not this narrative, is the authoritative adjudication layer.

If any wording below appears broader than a ledger verdict, the ledger controls.

---

## 1. The question that started the audit

The investigation began with a viral claim that an autonomous Grok-powered trading agent entered a fresh token with approximately `0.3 ETH` and exited with approximately `19.7 ETH`, presented as roughly a `66x` result.

The presentation looked unusually complete for a social-media trading claim:

- a terminal-style interface
- autonomous-agent framing
- safety checks
- a closed-position display
- a dramatic headline return
- a real underlying token that had experienced a large market move

At first glance, these layers can feel mutually reinforcing.

But they answer different questions.

A token chart can establish that the asset moved.

A repository can establish that software exists or is technically capable of performing certain functions.

A screenshot can establish that a claim was publicly presented.

None of those, by themselves, reconstruct a historical trade.

For a participant-level performance claim, the core evidentiary question is narrower:

**Where is the trade?**

That means the attributable wallet, the relevant entry transaction, the relevant exit transaction and enough surrounding context to independently reconstruct the reported result.

In the GRASS case, the underlying market movement was observable.

The claimed agent trade was not independently reconstructed.

That distinction became the first governing rule of the audit:

**Asset movement ≠ agent performance.**

The correct adjudication was therefore not that the claim was false.

It was that the claimed historical agent performance remained **UNVERIFIED**.

Failure to verify is not proof of non-occurrence.

But downstream popularity, repetition or token performance cannot be substituted for the missing transaction path either.

---

## 2. GRASS: observable market movement, unreconstructed actor performance

The exact primary X source was recovered during the source-hardening pass:

`https://x.com/0xzynex/status/2093658526820212996`

The captured post stated that a Grok bot bought `$GRASS` around a `$30K` market cap and sold around `$2M`, framed as a `66x` autonomous trade on an ETH-compatible chain.

The audit identified the GRASS contract as:

`0x16391C40e85FB2246A2C8c17bfA2594C5d3EF84b`

The underlying asset experienced a market move compatible with the scale described in the public narrative.

The arithmetic was also broadly compatible with the headline multiple. A move from approximately `$30,000` to approximately `$2,000,000` is about `66.7x`; applied mechanically to `0.3 ETH`, that yields about `20 ETH` before fees, slippage and execution effects.

That arithmetic is relevant because it shows that the headline return was not mathematically absurd.

It is not transaction evidence.

The captured video did not expose:

- an agent wallet
- a buy transaction hash
- a sell transaction hash
- a complete participant-level execution trail

A public or personal wallet associated with the claimant was examined:

`0x690d7552375Fcd23Bd2a5E1d74f7445FAdfc6c83`

The claimed GRASS trade was not reconstructed in that wallet.

That negative result was not treated as disproof because the public narrative distinguished personal and agent addresses.

The ledger therefore separates two propositions:

### GRASS-01

**CONFIRMED / E3** — underlying asset movement only.

### GRASS-02

**UNVERIFIED / E1** — claimed `0.3 ETH` to approximately `19.7 ETH` autonomous agent trade.

The audit also identified a technical-description mismatch.

The public GRASS presentation used the phrase `LP burned 95%` as part of the token-safety description. Primary Pons v2 material examined during the audit described a different launch architecture involving bonding-curve distribution followed by permanently locked full-range Uniswap v4 liquidity.

That was adjudicated as:

### GRASS-03

**MATERIAL MISMATCH / E3** — technical description only.

The mismatch does not establish fabrication, fraud or malicious intent.

This is important because an adversarial audit should not force every inconsistency into the same narrative.

A mismatch is a mismatch.

An unreconstructed trade is an unreconstructed trade.

A real market move is a real market move.

The findings remain separate.

---

## 3. Provenance became more important than the original claim

GRASS alone did not justify a broader market-level conclusion.

The investigation widened when highly specific AI-performance narratives began appearing across multiple accounts.

The strongest provenance case involved MEMEMOON.

Across separate first-person narratives, the audit observed an unusually specific cluster of repeated details, including:

- `0.5 SOL` entry
- narrative score `0.94`
- approximately `+800%`
- `42` new holders
- `3` whales
- `8 SOL` liquidity
- approximately `60x`

These are not generic similarities such as "AI bot traded a meme coin".

They are a dense cluster of numerical and descriptive overlaps.

That materially weakens the assumption that each public appearance represents an independent observation.

One version also contained an internal inconsistency: the same published system description that reported a `0.5 SOL` MEMEMOON entry also stated that position size never exceeded `0.1 SOL`.

A related version under another account used a `0.5 SOL` maximum position size, removing that contradiction.

The audit deliberately did not leap from this to common account control or fraud.

The correct evidentiary conclusion was about provenance.

### PROV-01

**PROVENANCE FAILURE / E2** — content provenance only.

The apparent independence of the narratives is materially weakened.

### PROV-02

**INCONSISTENT / E1** — published Zynex execution description only.

The `0.5 SOL` entry conflicts with the stated `0.1 SOL` maximum-position rule.

The audit did **not** establish:

- common account ownership
- coordinated fraud
- fabrication of the underlying trade
- shared wallet control
- one operator

Similarity can arise from copying, template reuse, reposting, common source material or coordination.

The evidence did not allow the audit to select among those explanations.

This produced the second core rule:

**Repetition does not create independent corroboration.**

A narrative appearing in several places may still represent one underlying evidentiary unit.

This is the distinction behind the title of the investigation:

**Distribution depth is not evidence depth.**

---

## 4. KITSUNE: claim precision exceeded evidence precision

A separate Enko-linked KITSUNE performance claim contained unusually precise historical performance parameters:

- approximately `0.8 ETH` entry
- approximately `$1.5M` entry market cap
- approximately `$120M` exit market cap
- approximately `+62 ETH`
- approximately `5,820` holders
- autonomous-execution framing
- safety-language and position-cap language

The public material therefore looked highly specific.

But precision in presentation is not the same as precision in auditability.

The audit did not identify a unique token contract, attributable agent wallet, buy transaction hash and sell transaction hash sufficient to reconstruct the reported historical P&L.

The resulting verdict was:

### VAL-01

**NON-REPRODUCIBLE / E1** — publicly reconstructible historical performance only.

This means the claim could not be independently reconstructed from the available public evidence.

It does **not** mean the trade was proven not to have occurred.

The case reinforced another core rule:

**Code capability ≠ historical P&L.**

Technical plausibility, code availability and historical execution must remain separate questions.

---

## 5. Amplification can increase distribution without increasing verification

The investigation then moved from performance claims to amplification.

A captured RoundtableSpace post amplified a narrative that a Grok bot had been taught to autonomously launch memecoins on Pump.fun, kill failed launches and collect creator fees from successful ones.

This was analytically important because distribution expanded dramatically without adding participant-level transaction evidence for the underlying claims.

The audit therefore treated RoundtableSpace as an **amplification layer**, not as independent verification.

### AMP-01

**SUPPORTED / E2** — public amplification and downstream provenance only.

The audit did **not** establish that RoundtableSpace:

- created downstream tokens
- approved them
- received payment from them
- knew any underlying claim was false
- participated in a coordinated operation

What mattered was what happened downstream.

Material associated with a token called FACTORY later incorporated upstream creator and amplifier references into the public provenance of the tradable asset.

This created an observable sequence:

**technical or performance narrative**

→ **amplification**

→ **downstream token provenance**

The exact primary Pump.fun asset URL and full mint were not sufficiently preserved for an E3 upgrade, so the FACTORY finding remained deliberately conservative:

### FACTORY-01

**SUPPORTED / E2 / PROVISIONAL** — token metadata and provenance relationship only.

The audit did not establish that Enko or RoundtableSpace created, approved or financially benefited from FACTORY.

The narrower finding is enough:

**Amplification can become part of a tradable asset's provenance without adding independent verification to the original claim.**

---

## 6. The narrative can become a financial object before the evidence is complete

At this stage the audit's central question changed.

It was no longer only:

**Is the original AI-performance claim true?**

It became:

**What can the market do with the narrative before that question is resolved?**

Permissionless tokenization allows technical narratives, AI-agent demonstrations, repositories and public creator identities to become part of the provenance layer of tradable assets.

Once that happens, the narrative can acquire a financial layer containing:

- trading volume
- token price
- community formation
- fee-routing incentives
- creator-recognition incentives
- promotional incentives
- later creator adoption
- additional social proof

The market does not have to wait for independent reconstruction of the original claim.

That is the structural issue documented by the audit.

The research does not require every originating claim to be false.

It does not require a single operator.

It does not require fraud.

It only requires a market structure capable of financializing a narrative before its evidence reaches the same depth as its distribution.

---

## 7. Creator-fee infrastructure: capability, configuration and payout are different propositions

Primary Pump.fun documentation confirms the existence of creator-fee and fee-sharing infrastructure.

The documentation supports protocol-level mechanisms including configurable fee shares and multiple recipients.

That establishes:

### ECON-01

**CONFIRMED / E3** — protocol capability only.

The audit separated three evidentiary levels:

### 1. Capability

Can the protocol technically support creator-fee routing or sharing?

Yes.

### 2. Configuration

Was a specific token configured to route fees to a specific recipient?

This requires token-specific evidence.

### 3. Payout

Did the specific recipient actually receive or claim the fees?

This requires end-to-end reconstruction of the relevant mint, configuration, recipient mapping, claim transaction and recipient wallet.

These levels cannot be collapsed.

A public statement saying fees were routed to a creator is not equivalent to a verified payout.

This became another audit rule:

**Fee-routing claim ≠ verified payout.**

That distinction became particularly important in the SPIDER and REAPER cases.

---

## 8. SPIDER: counterevidence against necessary pre-launch creator coordination

Before SPIDER, repeated creator-linked tokenization made pre-launch creator involvement look like a plausible working hypothesis.

SPIDER weakened that hypothesis.

The creator account `@phosphenq` publicly stated, in substance, that someone had turned the spider-bot concept into a coin overnight, that the creator did not deploy it and that the creator discovered it through someone in replies.

The token mint recorded in the audit was:

`6m6hkSNrZ1FxuLLdbcf9UAraPvUZMgfcCSsx3hh4pump`

Later Orbital material referenced the same mint and public claim/onboarding language.

The public chronology was therefore consistent with:

**third-party tokenization**

→ **creator discovery**

→ **claim / onboarding**

→ **later public association**

The audit explicitly preserved the limitation that private pre-launch communication could not be excluded.

The correct conclusion was therefore not "there was definitely no prior contact."

It was:

### SPIDER-01

**NOT ESTABLISHED / E1** — pre-launch creator participation.

### SPIDER-02

**SUPPORTED / E2** — public post-launch onboarding chronology.

### SPIDER-03

**UNVERIFIED / E1** — specific creator-fee payout.

SPIDER mattered because it functioned as counterevidence against the audit's own earlier assumption.

The investigation did not strengthen the coordination theory to absorb the counterexample.

It weakened the theory.

That is the point of a stress test.

The governing rule became:

**Creator adoption ≠ pre-launch coordination.**

---

## 9. REAPER: a second post-launch creator-onboarding case

REAPER provided a second directly captured case consistent with the same public mechanism.

The creator account `@0xkkai` publicly stated that someone else had launched REAPER as a sign of support.

In another captured post, Kai stated that a token had launched using his agent's name and that nobody had told him; he said he discovered it because the agent flagged it.

The REAPER mint recorded in the audit was:

`FRPV7Df98MRYLQus6LvJHkjWukUai9wonumScVcypump`

Later Orbital material used the phrase:

`He tapped in and claimed`

while referencing the same token context.

Again, the public record was consistent with post-launch creator adoption.

Again, it did not establish the full private communication history.

And again, the specific creator-fee payout was not reconstructed transaction-by-transaction.

The resulting ledger findings were:

### REAPER-01

**NOT ESTABLISHED / E1** — pre-launch creator participation.

### REAPER-02

**SUPPORTED / E2** — public post-launch creator-onboarding chronology.

### REAPER-03

**UNVERIFIED / E1** — specific creator-fee payout.

Across SPIDER and REAPER, the audit supported a cross-case synthesis:

### ONBOARD-01

**STRONGLY SUPPORTED / E2** — recurring post-launch creator-onboarding mechanism in the observed cases.

The synthesis does not establish universal prevalence, one operator, common control, fraudulent intent or verified payouts.

Its importance is structural:

**A third party can tokenize someone else's technical or AI narrative, and the referenced creator can become publicly associated with the token later.**

That later association can generate new social proof for subsequent observers.

---

## 10. Repeat launch-wallet evidence: recurrence without population claims

The audit identified repeated narrative-linked launches associated with the Pump.fun creator address:

`HAh7q881D5qUiXuHCZQXx7PcQQWiyHWE3fVXF5j8khpV`

The wallet-level finding was separated from identity attribution.

The audit did not claim that any named X account necessarily controlled the wallet.

It also did not estimate what percentage of the wallet's total launch history matched the AI/Grok narrative pattern, because the discovery process was not a random sample and a complete independently verified launch census was not reconstructed.

The relevant distinctions were:

### WALLET-01

**CONFIRMED / E3** — repeat creator-wallet attribution across individually verified tokens only.

### WALLET-02

**SUPPORTED / E2** — repeated AI/Grok narrative tokenization is present among the identified source-hardened subset.

### WALLET-03

**NOT ESTABLISHED / E0** — population prevalence.

### ATTRIB-01

**NOT ESTABLISHED / E1** — wallet-to-person identity attribution.

This preserved an important anti-selection-bias rule:

A discovered cluster cannot be converted into a population statistic without a defensible denominator.

---

## 11. Timing: a suspicious-looking observation that failed to generalize

Timing initially appeared capable of supporting a stronger mechanistic hypothesis.

For HIVEMIND, the captured Orbital post was timestamped approximately `53.468 seconds` before the token's third-party indexed creation time.

That is a short interval.

It is structurally interesting.

But a short interval is compatible with several different mechanisms, including:

- automation
- rapid manual response
- prior preparation
- prior knowledge
- coincidence within an active launch workflow

Timing alone cannot distinguish among them.

The audit therefore treated the interval narrowly:

### TIMING-01

**CONFIRMED / E2** — observed post-to-indexed-creation interval only.

The evidence did not establish automation, common control, coordination or causality.

A second case, GBC, provided counterevidence to a stronger pattern claim.

The comparable interval was approximately `16 minutes 1.938 seconds`.

That materially weakened the idea that narrative-linked launches followed a consistent sub-minute latency.

The audit therefore rejected its own stronger hypothesis:

### TIMING-02

**REJECTED / E2** — uniform sub-minute launch-latency hypothesis.

This is one of the most important parts of the audit because it demonstrates the difference between noticing an anomaly and converting it into a rule.

The first case looked unusually suggestive.

The second case forced the inference to become weaker.

The governing rule became:

**Temporal proximity ≠ causal provenance.**

---

## 12. What the audit did not establish

The audit deliberately preserved several negative boundaries.

It did **not** establish that:

- every AI-performance claim examined was false
- the GRASS trade did not occur
- KITSUNE did not occur
- every repeated narrative came from one operator
- every creator knew about a token before launch
- SPIDER or REAPER had no private pre-launch contact
- every creator-fee routing statement resulted in a payout
- RoundtableSpace created, approved or financially benefited from downstream tokens
- Enko created or approved FACTORY
- the HAh7q wallet was controlled by a specific named person
- all observed accounts formed one coordinated operation
- most Pump.fun launches follow the identified pattern
- a population-level fraud rate can be estimated from this evidence set

These are not omissions from the conclusion.

They are part of the conclusion.

The fields `verdict_scope`, `not_established` and `limitation` in the Evidence Ledger are part of each finding and should be read as such.

---

## 13. What survived the stress test

After counterevidence, downgrades and rejected hypotheses, the surviving structural findings were narrower than the strongest initial suspicions.

They were also more defensible.

The audit supports the following observed mechanism:

1. A real market move can coexist with an unreconstructed actor-level performance claim.
2. Highly specific first-person AI-performance narratives can be repeated or mutated across accounts.
3. Repetition can expand distribution without adding independent evidence.
4. Large-account amplification can expand the narrative further without independently reconstructing the underlying claim.
5. Amplified technical or AI narratives can become part of the public provenance of tradable tokens.
6. Protocol-level creator-fee infrastructure can support economic incentives around those tokens.
7. Third parties can tokenize a creator's technical narrative without proven pre-launch creator participation.
8. The creator can later discover, claim, adopt or publicly associate with the token.
9. That later association can create additional social proof.
10. Financialization can therefore occur before independent verification reaches the same depth as distribution.

The cross-case ledger synthesis records:

### NETWORK-01

**NOT ESTABLISHED / E2** — one coordinated operation.

### NETWORK-02

**STRONGLY SUPPORTED / E2** — recurring structural mechanism across the observed cases.

This distinction is central.

The audit does not need one operator to explain the market structure.

The mechanism can exist even when actors are independent.

---

## 14. The larger market implication

The strongest conclusion from this audit is not that AI-performance claims are generally false.

The evidence set cannot support that statement.

The stronger structural concern is that social and financial systems can act on a narrative before the underlying evidence has matured.

A technically sophisticated post can contain:

- autonomous-agent language
- a repository
- terminal output
- precise numerical returns
- safety checks
- multiple agents
- charts
- creator references
- downstream amplification

Each additional layer can increase perceived credibility.

But these layers do not all verify the same proposition.

A repository can establish technical capability.

A chart can establish asset movement.

A screenshot can establish public presentation.

A token can establish financialization.

Creator adoption can establish later public association.

A creator-fee mechanism can establish protocol capability.

None of those, by themselves, reconstruct a historical performance claim.

The market may nevertheless price, trade and promote the narrative.

That leads to the central structural conclusion:

**Verification can lag financialization.**

Or, stated in the language of the project:

**Distribution depth is not evidence depth.**

---

## 15. The question remains simple

When a post claims that an autonomous agent turned a small bankroll into a spectacular return, the first question should not be how many views it received, how many accounts repeated it, whether someone launched a token around it, whether the creator later acknowledged that token, or whether the token itself increased in price.

The question is still:

**Where is the trade?**

If the transaction path is unavailable, everything downstream may still be economically real.

The attention can be real.

The token can be real.

The fees can be real.

The creator onboarding can be real.

The market move can be real.

But none of those things retroactively reconstruct the original performance claim.

That is the central finding of this audit.

---

## 16. Relationship to the evidence repository

This longform narrative is an interpretive layer over the frozen Evidence Ledger v1.0.

The repository also contains:

- `methodology.md`
- `evidence-ledger-v1.0.csv`
- `LEDGER-NOTES.md`
- `source-index.md`
- `timeline.csv`
- `limitations.md`
- `corrections.md`
- `SOURCE-HARDENING-STATUS.md`
- `FREEZE-READINESS.md`
- `FREEZE-v1.0.md`
- case files under `01-entry-case/` through `08-timing/`
- raw screenshots and video captures under `evidence/raw/`
- `evidence/CAPTURE-MANIFEST.md`

The raw-evidence package was deposited and byte-identity checked during the 2026-09-06 source-hardening pass.

The v1.0 freeze retains unresolved items rather than silently strengthening findings to compensate for missing evidence.

Material later changes to verdicts, evidence grades, scope or evidentiary basis should be recorded in later versions rather than silently rewriting the frozen record.

---

## Final principle

The purpose of this investigation is not to maximize the number of suspicious connections.

It is to determine which connections survive adversarial review.

**A hypothesis survives only what we failed to falsify.**
