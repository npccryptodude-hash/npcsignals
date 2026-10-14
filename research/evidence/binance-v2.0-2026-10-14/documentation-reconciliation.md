# Documentation reconciliation — 2026-10-14

Baseline read at commit `6348371f21b8dbb6693297ef775092db9fed6ff1`.

| Existing document | Earlier statement | Current correction |
|---|---|---|
| EXCHANGE_ATTRIBUTION_ARCHIVE_STATUS_2026-10-14.md | Original raw archives not present | Status updated with recovered archives, paths, passing offline replay and remaining gaps. |
| BINANCE_U300_EVIDENCE_PACKAGE_v1.0_CHECKPOINT.md | Seven-receipt export not attached; no extra match in 786 cached receipts | Preserved as historical baseline. Original seven-receipt ZIP now archived. Three older SOL transfers and distinct 56HEQ route now independently replayed; bounded cache result remains accurate for that prior scope. |
| EXCHANGE_ATTRIBUTION_LEDGER_v0.1.md | CEX_INBOUND none yet; no exclusive case-proceeds deposit | Five on-chain receipts into independently labelled infrastructure now documented. Exclusive token-sale provenance and customer deposit credit still unresolved. Baseline unchanged. |
| EXCHANGE_ATTRIBUTION_LEDGER_v0.2.md | No deposit in examined earlier window; raw195 receipt archive absent | Bounded negative not rewritten. Current package recovers relevant linkage receipts only; it does not claim all195 receipts are archived here. |
| Previous Library secondary v2.0 report | Starting payment signatures not supplied; originals pending | Previous report preserved unchanged in secondary ZIP. Complete two initiating signatures and original five 56HEQ flow receipts are now in this evidence package. |

Terminology: CONFIRMED applies to chain events and historical token ownership. Binance affiliation remains SUPPORTED. A transfer into Binance-attributed infrastructure is not automatically an internally credited customer deposit. September transfers cannot be the proceeds of October launches. Direct transactional linkage is not common human control.

Missing original transport envelopes for the two supplemental linkage receipts are retained as NOT RECOVERED; their separately identified replacement responses and finality were captured during this archival pass. No synthetic envelope was wrapped around old parsed data. Public source records are targeted excerpts/titles, not full web captures. These limitations remain visible in README and the updated archive status.
