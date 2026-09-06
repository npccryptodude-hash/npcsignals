# GRASS entry case

## Purpose

GRASS is the entry case for the audit.

The case is used to separate observable token price movement from a separate claim that an autonomous Grok trading agent captured that move.

## Claim examined

A public performance narrative stated that a Grok bot entered GRASS with approximately 0.3 ETH and exited with approximately 19.7 ETH, presented as roughly a 66x result.

## Identified asset

GRASS contract:

`0x16391C40e85FB2246A2C8c17bfA2594C5d3EF84b`

Network context used during the audit: Robinhood Chain, chain ID 4663.

## Observed

- GRASS experienced a large market-cap expansion consistent with the scale described in the public narrative.
- The captured presentation showed an entry of 0.3 ETH and a final result of approximately +19.7 ETH.
- The presentation also included safety-language such as no honeypot, verified, renounced and LP burned.
- The captured video did not expose an agent wallet, buy transaction hash or sell transaction hash.

## Published wallet checked

A public/personal wallet associated with the claimant was identified during the audit:

`0x690d7552375Fcd23Bd2a5E1d74f7445FAdfc6c83`

The audit did not identify the claimed GRASS trade in that wallet.

This does not establish that the trade did not occur, because the claimant also described agents as using separate addresses.

## Arithmetic check

A move from approximately $30,000 market cap to approximately $2,000,000 is about 66.7x.

Applied mechanically to 0.3 ETH, that produces about 20 ETH before fees, slippage and execution effects.

The arithmetic is broadly compatible with the headline multiple, but arithmetic compatibility is not transaction evidence.

## Technical-description mismatch

The presentation included the phrase `LP burned 95%` as part of its safety description.

Primary Pons v2 material examined during the audit described a different launch architecture involving bonding-curve distribution followed by permanently locked full-range Uniswap v4 liquidity.

This was adjudicated as a **MATERIAL MISMATCH** in technical description, not as proof that the trade was fabricated.

## Findings

### GRASS-01

**Verdict:** CONFIRMED  
**Evidence grade:** E3  
**Scope:** underlying asset movement only

The asset experienced the relevant market movement.

This finding does not establish that a particular agent captured the move.

### GRASS-02

**Verdict:** UNVERIFIED  
**Evidence grade:** E1  
**Scope:** claimed 0.3 ETH to approximately 19.7 ETH agent trade

The audit did not identify the agent wallet or reconstruct the entry and exit transactions.

The correct conclusion is unverified, not false.

### GRASS-03

**Verdict:** MATERIAL MISMATCH  
**Evidence grade:** E3  
**Scope:** public safety/launch-architecture description

The `LP burned 95%` language did not cleanly match the launch architecture described in the primary protocol material examined.

This finding does not establish intent, fraud or falsification of the trade itself.

## Counterevidence retained

The audit rejected several weak linkage ideas:

- generic earlier uses of the phrase `touch grass` were treated as ordinary slang, not prior knowledge of the token
- an older crypto reference to Grass was determined to concern an unrelated project
- a Blockscout anomaly was excluded because indexing conflict made it unreliable as adverse evidence

## Raw evidence status

A captured GRASS video was preserved during the investigation and hashed locally:

`a935e1e4d3722c073bd58693e8721d135c2f31e152f8b3fffff4be780c3ab330`

Repository upload of the raw file is pending.

Exact original X-source mapping should remain `PENDING` until the raw capture and final source URL are placed in the repository.

## Final case conclusion

The strongest defensible conclusion is narrow:

A real asset move was observable, while the specific claimed agent P&L remained independently unreconstructed.

Asset movement and agent performance therefore remain separate findings.
