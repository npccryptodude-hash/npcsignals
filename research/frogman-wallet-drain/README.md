# Frogman wallet-drain investigation

**Status:** Active research. **Latest research cutoff:** 2026-10-08. **Evidence version:** v0.1.

[Read the frozen v0.1 investigation report](./master_investigation_report_v0.1.md).

The report covers a 46-minute Solana incident window backed by 28 finalized transaction receipts and a 102-row instruction/fee ledger (F0001–F0102). The EVM branch and cross-chain exits have **not** yet been independently reproduced. The compromise method, operator and ultimate beneficiary remain unresolved.

## Evidence archive

The original `NPCsignals_Frogman_Research_Package_v0_1.zip` (57 files, including raw JSON-RPC receipts, CSVs, scripts, SHA256SUMS.txt and the report) is preserved in the user's ChatGPT Library as of 2026-10-08. **Only the report is committed to GitHub so far**; this GitHub directory is not yet a self-contained reproducibility archive. Upload the untouched evidence package contents in a subsequent Work session, preserving exact bytes and checksums.

## Methodological boundaries

- Wallet attribution to Frogman: SUPPORTED, not independently established by underlying attribution receipts.
- Solana transaction paths and ten Privacy Cash deposits: reproduced from finalized receipts within documented scope.
- Privacy Cash withdrawal recipients: UNRESOLVED; deterministic provenance stops at deposits.
- EVM 362.26 ETH, Relay and other exits: public CLAIMS requiring independent reproduction.
- Do not infer attack vector, beneficial ownership or criminal identity from transaction paths.
- Never describe unobserved transactions as confirmed.

No Medium article has been prepared from this evidence version.
