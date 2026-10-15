# G006 verification report

## Completed online checks
- Read frozen G005 ledger, registry, bridge matches, assessment and blockers. No G001–G005 reconstruction restarted.
- Read Polygon A/B and Ethereum B token history pages, dates, full contracts/addresses and amount tooltips; observed pagination boundaries and active exclusion filters.
- Inspected 36 new successful transaction receipts beyond G005, including eight non-transfer authorization/order/delegation receipts, six native-funding/delivery receipts and three imitation-event transaction receipts. Counts are of distinct hashes, not unique victim losses. Full classification is in ledgers and collection_summary.json.
- Inspected decoded raw Transfer logs for all 20 new canonical Ethereum token rows, including the 0.0001 USDT dust transfer. Existing six G005 token movements are imported from frozen records; two were revisited only to recover nonces 0/1. Polygon dust and imitation rows have narrower field-level verification.
- Matched exact Polygon router allowance amounts and spender addresses in Approval logs.
- Inspected dated Ethereum type-4 self-transaction and delegation target; did not cryptographically recover its authorization signature.
- Read internal Polygon swap delivery to B and actual C sender; distinguished Multicall as transfer source from C as operation initiator.

## Offline checks
`python3 verify.py` checks hash coverage, every file digest, frozen G005 tracked content against starting commit, event uniqueness, raw/decimal conversion, distinct new transaction count excluding G005, exact DAI delta arithmetic, time ordering, lack of post-arrival DAI outflows within the saved sample, and exclusion of noncanonical events from balance calculations.

These tests validate captured records and calculations. They do not independently query the blockchain, validate an explorer index's completeness, recover an Ethereum signature or prove authorization/ownership. Receipt observations are transcribed primary explorer representations rather than original node JSON.

## Publication validation
Publish only this sibling G006 directory. No frozen G005 manifest or evidence is modified. Compare remote files against the validated tree and read back published checkpoint after branch update. A local commit or tool upload alone is insufficient to claim remote publication.
