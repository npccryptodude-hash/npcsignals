# NPCsignals — Gamdom evidence checkpoint G005

15 October 2026. Independent reconstruction. Research publication: evidence checkpoint only. Article decision: **HOLD**.

## Strongest new finding
Two Polygon receipts show the G004 candidate wallet sending 19,610.310097 USDT0 and 12,139.456905 USDC to the same full address, six seconds apart on October 13. The recipient appears in the Arkham entity linked directly by vxdb. Both exact token quantities subsequently enter separate Squid/Axelar operations, with destination Ethereum executions matched by payload hash and Axelarscan. Ethereum receipts show DAI delivered to that same address.

**Six movement transactions verified through explorers. Zero transactions independently established as unauthorized outflows from a confirmed compromised Gamdom wallet.** Ownership and authorization remain the evidence bottleneck. The transfer facts are CONFIRMED at explorer-evidence level; incident attribution is SUPPORTED; unauthorized status is UNRESOLVED. Direct RPC retrieval was blocked and is not claimed.

The two original token quantities sum numerically to 31,749.767002 stablecoin units across two different assets. This is not a verified USD loss. The downstream bridge and swap movements must not be counted again.

## Scope and files
- `transaction_ledger.csv`: six transactions, exact raw quantities, contracts, UTC timestamps, fees and split evidence classifications. It records one selected principal token flow per transaction, not every log.
- `evidence/bridge_matches.json`: two cross-chain pairs and matching payload hashes.
- `source_register.csv`, `incident_timeline.csv`, `wallet_registry.csv`: provenance and attribution limitations.
- `loss_reconciliation.md`, `cross_chain_routes.md`, `evidence_assessment.md`, `blocker_report.md`, `verification_report.md`.
- `prior-checkpoints/`: unchanged G001–G004 input ZIPs. No Gamdom directory was present in reviewed repository HEAD ac740cbac38273aef293ba4f88939c1ced1fc56e.
- `SHA256SUMS.json` and `verify.py`: local integrity and arithmetic validation. Run `python3 verify.py` inside this directory.

No ZYROX, GLITCH or Frogman files are changed. No human operator, beneficiary, recovery or customer insolvency is identified.
