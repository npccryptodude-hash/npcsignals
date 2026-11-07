# documentation standard / evidence and educational use

**npcsignals | archive protocol | version 1.0 | 7 november 2026**

## purpose

every npcsignals research archive should serve two audiences at once: readers with no specialist background (including a school class) and independent reviewers who wish to reproduce, question or cite a finding. clarity is necessary but cannot replace verifiability. a clean presentation must never turn reported claims into proven facts.

## required structure for each case

1. **case identity and scope:** case id, descriptive title, time period, networks and assets covered, document version and last review date. mark whether complete or a continuing investigation.
2. **plain-language overview:** what happened, why it matters, what was established, and what remains unresolved, without requiring knowledge of technical jargon.
3. **chronology:** each event dated and identified as event time, publication time or observation time. use utc for blockchain events and spell out other time zones.
4. **evidence register:** each material assertion receives an evidence id and exact source reference, with publication and access date, retrieval method, transaction hash/log index where applicable, and immutable source-file digest where preserved.
5. **findings and reasoning:** show calculations, token decimals, wallet roles, exclusions, counterexamples and why each conclusion follows—or does not follow—from the records.
6. **limitations:** distinguish missing evidence, contradictory sources, reporting delays, measurement uncertainty and snapshots that may change.
7. **updates and corrections:** new dated annexes preserve the earlier state; corrections specify what changed and which earlier statement is superseded.
8. **reader's guide:** definitions, clearly described visuals and a reproducible path from summary to primary evidence.

## claim classifications

| label | permitted use | must never imply |
|---|---|---|
| **directly verified** | explicitly named raw receipt/log or original record inspected, with method and evidence artifact | authorship, ownership, intent or the truth of unrelated statements |
| **officially attributed** | a named agency has publicly assigned responsibility, with the original advisory cited | independent forensic proof by npcsignals or personal identification |
| **source-reported** | a company, government, analyst or news outlet made the stated claim at a stated date | independent replication or final certainty |
| **supported inference** | traceable reasoning supported by multiple specified pieces of evidence, with alternative explanations considered | legal proof, identity or a unique causal explanation |
| **unresolved** | presently insufficient, missing or contradictory evidence | negative proof that a connection does not exist |
| **rejected** | a stated hypothesis is contradicted by identified evidence and methodology | rejection of every adjacent hypothesis |

**source confidence and claim confidence are different things.** an authentic press release proves the issuer made a claim, not that every factual detail is proven. a blockchain receipt proves a logged event, not the person controlling the address.

## evidence register template

| evidence id | exact claim | source id / original link | source type | event time (utc) | observed / retrieved (utc) | method | retained digest or transaction id | classification | limitation |
|---|---|---|---|---|---|---|---|---|---|
| example only | canonical token transfer recorded | ethereum tx link | chain receipt | yyyy-mm-dd hh:mm | yyyy-mm-dd hh:mm | eth_getTransactionReceipt from named endpoints | tx hash / log index / sha256 | directly verified | ownership not established |

do not fabricate timestamps or digests to fill empty fields. write `not captured`, `not applicable` or `pending` as appropriate. snapshot values must never be presented as continuously live figures.

## money movement and accounting rules

- canonical token contract and decimals before symbol. report integer raw amount and human-readable units.
- use **from**, **to**, transaction hash, block number, block hash and log index whenever available.
- track funds through hops without adding later movements to the original theft amount.
- keep distinct columns for **stolen**, **frozen/intercepted**, **returned/recovered**, **replenished/replaced**, and **remaining under reported actor control**; each may have different dates and overlapping funds.
- do not infer successful swaps or ultimate cash-out merely because a transfer reached a smart contract.
- official wallet labels are annotations, not conclusive proof of beneficial ownership.
- when observations come from two public rpc endpoints, report them as matching endpoints, not necessarily fully independent infrastructure operators.

## source preservation and transparency

prefer the official primary record, underlying chain data and contemporaneous snapshots. retain original URLs and access timestamps; preserve raw response or export when permitted, then record a sha256 digest. avoid quoting a screenshot without recording the underlying original if available. distinguish quoted text, paraphrase, our calculation and our judgment.

a publication-ready archive requires a readable summary, full source register, working links, reproducible calculations, and a dated limitations section. a passed software test is not a substitute for factual editorial review, and a source list alone is not a reproducible investigation.

## corrections and release control

no silent rewriting of evidence history. retain superseded versions through git and add a correction note stating why the interpretation changed. publication to the main branch, website, medium or x requires separate approval; editorial drafts for medium/x remain outside the research archive.

**observe first. verify before concluding.**
