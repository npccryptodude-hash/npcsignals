# MEMEMOON provenance case

## Purpose

This case examines whether highly specific first-person AI trading-performance narratives appearing across multiple accounts represent independent observations or reused narrative material.

The audit treats content provenance separately from the truth of the underlying trade.

## Zynex narrative

A captured Zynex MEMEMOON post described a Grok-based trading system and included unusually specific details:

- starting bankroll framed as 1 SOL
- MEMEMOON as the selected token
- a 0.5 SOL buy
- entry around `$0.0000012`
- narrative score `0.94`
- approximately `+800%`
- `42` new holders
- `3` whales
- `8 SOL` liquidity
- approximately `60x`

The same published system description also stated that position size never exceeded `0.1 SOL`.

That creates an internal conflict with the stated `0.5 SOL` MEMEMOON entry.

## Backwood duplicate narrative

A direct capture from `@0xBackwood` on Aug 30 showed a highly similar first-person narrative:

- 1 SOL assigned to the bot
- MEMEMOON selected
- narrative score `0.94`
- 0.5 SOL buy
- entry around `$0.0000012`
- `+800%`
- `42` new holders
- `3` whales
- `8 SOL` liquidity
- approximately `60x`

The Backwood version also used a maximum position size of `0.5 SOL`, which removes the contradiction present in the Zynex version.

A later Aug 31 Backwood post again framed the result as 1 SOL becoming approximately 60 SOL within about 60 seconds.

## Observed

The overlap is not limited to a generic theme such as "AI trading bot" or "meme coin profit."

The two narratives share a cluster of unusual numerical and descriptive details.

The later version contains small mutations rather than a wholly independent presentation.

## Finding PROV-01

**Verdict:** PROVENANCE FAILURE  
**Evidence grade:** E2  
**Scope:** content provenance only

The apparent independence of the public narratives is materially weakened by the unusually specific overlap.

This finding does not establish:

- common account control
- coordinated fraud
- fabrication of the underlying trade
- shared wallet control
- shared operator identity

## Finding PROV-02

**Verdict:** INCONSISTENT  
**Evidence grade:** E1  
**Scope:** published Zynex execution description only

The claimed `0.5 SOL` entry conflicts with the published `0.1 SOL` maximum-position rule.

An undocumented configuration change, exception or narrative error could theoretically explain the conflict.

No transaction-level reconstruction was available to resolve it.

## Counterevidence and limitations

Similarity alone does not identify who originated the narrative or why it was reused.

Public reposting, copying, template reuse, shared source material or coordinated publication are all possible explanations.

The audit does not select among those explanations without additional evidence.

## Raw evidence status

Direct screenshots of the Backwood Aug 30 and Aug 31 posts were captured during source hardening on 2026-09-06.

They should be deposited under `evidence/raw/x/` and referenced from the ledger once uploaded.

## Final case conclusion

The strongest defensible conclusion is about provenance, not fraud.

The MEMEMOON narrative cannot be treated as multiple independent performance observations simply because it appeared under multiple first-person accounts.

Distribution depth is not evidence depth.
