# KITSUNE validation case

## Purpose

KITSUNE was used as a validation case to test whether another highly specific AI trading-performance claim could be independently reconstructed.

## Claim examined

A public narrative associated with Enko described an autonomous agent trading KITSUNE with approximately:

- 0.8 ETH entry
- around $1.5M market cap at entry
- around $120M market cap at exit
- approximately +62 ETH
- about 5,820 holders
- no honeypot / verified / renounced / LP burned safety language
- a stated position-size hard cap of 0.8 ETH

The text of this claim was independently recoverable during source hardening from current public archive/profile mirrors for `@enkoxbt`.

Archived corroboration located during the audit includes:

- `https://www.sotwe.com/enkoxbt`
- `https://m.twstalker.com/enkoxbt`

These are corroborating mirrors, not substitutes for an original X capture.

## Arithmetic check

A market-cap move from $1.5M to $120M is approximately 80x.

A mechanical 80x multiple applied to 0.8 ETH produces approximately 64 ETH before execution effects.

The stated +62 ETH is therefore arithmetically plausible at headline level.

Arithmetic compatibility is not evidence that the trade occurred.

## Reconstruction attempt

The audit did not identify a unique combination of:

- token contract
- agent wallet
- buy transaction
- sell transaction

sufficient to independently reconstruct the claimed historical P&L.

The public claim contains high numerical precision, but the public audit trail identified during this investigation does not provide the transaction identifiers required to reproduce that precision.

## Finding

**Verdict:** NON-REPRODUCIBLE  
**Evidence grade:** E1  
**Scope:** publicly reconstructible historical performance

The public material identified during the audit was insufficient to reproduce the claimed trade end to end.

### Not established

This does not establish that:

- the trade was false
- the agent did not exist
- the published code or capability was non-functional
- the claimant intentionally misrepresented performance

## Source status

The claim text is currently supported by `ARCHIVED-CORROBORATION` from public profile mirrors.

A direct original X post capture or exact original status URL would strengthen source preservation, but would not by itself raise the historical P&L finding above E1 unless transaction-level evidence were also supplied.

## Final case conclusion

KITSUNE reinforces the audit rule that technical capability, arithmetic plausibility and public presentation remain separate from independently reconstructed historical P&L.
