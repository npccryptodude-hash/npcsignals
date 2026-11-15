# NPCsignals — Gamdom G010

Independent Incident-Origin Reconstruction. Research date: 15 October 2026. Starting commit: `00bb8846e65ce0ac44446e02185c5d859bc9bca3`.

## New evidence

The E1 candidate recipient is **0x4b304741599c125a244e498d14562487d7109ab8**. Its earliest verified candidate inflow in this bounded reconstruction is A's **738.148858772417648963 DAI**, at **16:00:23 UTC**, Ethereum block **26184626**, transaction **0xb2cca150592b3ba9344ff17a6f39888a40a855fc1619e8946b8b87e17217578f**. This identifies a movement, not an unauthorized loss. Larger USDT arrivals from two other sources occur at 16:16:47.

Three source addresses delivered exactly 426040.814198 USDT, 503001.390869 USDC, 20077.942698961878 USD1, 738.148858772417648963 DAI and 86.956356111770671236 ETH to E1. Seven stablecoin conversion executions are separately recorded. Nine token/native balance reconciliations have zero residual against historical RPC state. Two failed ETH attempts are excluded from transferred principal.

Two new BNB Chain deposit transactions are matched to existing Ethereum B receipts by distinct 32-byte identifiers in source deposit events and destination calldata, corroborating Relay's public index. B deposited 370000 and 336943.421822265793499428 BNB-chain USDT. These are bridge inputs, not independently identified original victim outflows.

**39 new transactions verified: 37 successful and 2 failed.** Two existing Ethereum transactions gain upstream matching evidence and are not recounted. New raw RPC evidence is distinct from earlier explorer transcriptions. No originating wallet is independently proven to belong to Gamdom, and no unauthorized-loss total is established.

## Package

- `incident_origin_ledger.json`: exact integer event/native ledger, classifications, receipts, initiators, fees and URLs.
- `transaction_register.json`: one record per chain/hash, including failures.
- `principal_by_source.json`, `balance_reconciliation.json`, `baseline_comparison.json`, `results.json`: deterministic accounting and bounded comparison.
- `ethereum_routes.md`, `wallet_attribution_register.md`, `earliest_outflow_timeline.md`, `financial_reconciliation.md`, `hypothesis_test.md`: interpretation and limits.
- `source_register.json`, `rpc_archive.json.gz`: 230 preserved acquisition records, including failed requests. The gzip file contains a JSON object keyed by record name, not a tar archive.
- `coverage_report.md`, `blocker_report.md`, `verification_report.md`, `verification_results.json`, `SHA256SUMS.json`: verification and boundaries.

Run `python3 verify.py` offline from this directory in the repository. Python standard library only. Raw integer amounts are JSON strings to prevent floating-point truncation. JSON rather than a formatted workbook is intentional for machine reproducibility. Raw acquisition cache files may remain locally under evidence/; the published compressed archive preserves their parsed contents without deleting the originals.

Evidence checkpoint: **PUBLISH**. Article: **HOLD**. G005, G006, G008 and G009 remain unchanged. NPCsignals documents. It does not judge.
