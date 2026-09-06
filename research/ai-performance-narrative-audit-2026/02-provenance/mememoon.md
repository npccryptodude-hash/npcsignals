# MEMEMOON provenance case

## Purpose

This case examines content provenance, not whether the underlying trade occurred.

## Claim pattern

A first-person AI-performance narrative associated with Zynex described a Grok bot trading MEMEMOON with unusually specific details, including:

- 0.5 SOL buy
- entry around $0.0000012
- narrative score 0.94
- approximately +800% after about 11 seconds
- 42 new holders
- 3 whales
- 8 SOL liquidity
- approximately 60x

The same surrounding system narrative also reportedly stated that position size never exceeded 0.1 SOL.

A materially similar first-person narrative later appeared from `@0xBackwood`, preserving multiple unusual details while mutating some values.

## Observed

The duplicated narrative contains a concentration of unusual details that is unlikely to be explained by generic trading language alone.

The later version changes at least one parameter in a way that removes the internal position-size conflict present in the earlier version.

## Finding PROV-01

**Verdict:** PROVENANCE FAILURE  
**Evidence grade:** E2  
**Scope:** content provenance only

The available captures support the conclusion that a highly specific first-person performance narrative was recycled across accounts rather than independently originated in identical form.

### Not established

This does not establish:

- common account control
- coordinated fraud
- that the underlying trade was fabricated
- which account originated the narrative
- whether one account copied another directly or through an intermediary source

## Finding PROV-02

**Verdict:** INCONSISTENT  
**Evidence grade:** E1  
**Scope:** internal consistency of the Zynex-published narrative

The described 0.5 SOL entry conflicts with the separately stated 0.1 SOL maximum position-size rule.

This inconsistency weakens the published performance narrative but does not independently disprove the trade.

## Source status

Direct original screenshots should be treated as `PRIMARY-CAPTURED` once deposited in the repository.

Third-party archives may be retained only as `ARCHIVED-CORROBORATION` or `SECONDARY-DISCOVERY`.

## Final case conclusion

The strongest supported finding is about narrative provenance and internal consistency, not historical P&L.
