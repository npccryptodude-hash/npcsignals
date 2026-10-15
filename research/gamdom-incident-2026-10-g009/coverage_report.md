# Coverage report

## Bounded direct-RPC reconstruction

Canonical contract only: 0xc2132d05d31c914a87c6611c10748aeb04b58e8f. Two eth_getLogs requests cover blocks 93000000–95434113 inclusively, one with D in topic 1 and one with D in topic 2. Returned counts are 106 outgoing and 647 incoming, 753 unique (hash,logIndex) records. Original requests, responses, block hashes, transaction indices, log indices, raw amounts and provider timestamps are saved. Deduplication and ordering are deterministic. Zero-value and micro-value records are not silently discarded.

The first included block is August 31 19:37:07 UTC, covering all September and October 1 through the anchor. The last included block is October 13 01:54:20 UTC. No history after the anchor, earlier than this bound, or full lifetime export is claimed. Opening state is queried at block 92999999; no opening-balance assumption is required. Prior provenance of that opening balance remains unresolved. The April receipt is separately verified, outside the accounting interval.

Direct archive balanceOf results are saved for 92999999, 95399999, 95434112 and 95434113. The historical token display has six decimals. One provider returned successful state/log data. All three exact accounting windows reconcile with zero residual. This supports completeness of the bounded accounting but is not proof against offsetting omissions, provider errors or unlogged administrative changes. No independent consensus replay, Merkle inclusion proof or state-root verification was performed.

## Verification depth

753 RPC event records are not 753 fully investigated transactions. Thirteen selected transactions have raw receipts, transaction objects and matching block headers; twelve are new beyond G008, and one is the existing anchor extended to direct RPC/state verification. All ten newly selected incoming transactions include the actual transaction sender and success status. Remaining event-only rows deliberately do not invent transaction signers or classify route origins.

The anchor block query contains only one D canonical Transfer, the anchor at transaction index 19 and log 179. The separately accessed PolygonScan storage table shows the same transaction-local debit. Block-level and transaction-local boundaries agree for the observed token effects; no exact-time state was inferred from a current balance.

## Explorer observations

The D canonical-token holder page was inspected with 100 rows after initially showing 25. It exposed a longer history, with 138 pages at the 25-row setting; it was not exhaustively paginated. It guided receipt selection but does not determine accounting completeness. Current balance displayed there was not used. The anchor storage and April receipt were observed in the browser; compact transcriptions/notes distinguish them from saved raw RPC JSON. The browser binding was later lost after conversation continuation; no result from the failed unbound browser call is counted.

## Scope limits

No full native-token, other-token, permission or cross-chain history. No upstream expansion beyond the selected inputs that actually produced D's USDT0. No claim of independent infrastructure behind the explorer's matching state representation. Full sender/recipient labels were not used as ownership proof.
