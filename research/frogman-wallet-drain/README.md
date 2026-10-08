# Frogman wallet-drain investigation

Status: Active research. Documentation language: English.

## Frozen v0.1 archive

The complete original package is preserved under [frogman_research_v0_1/](./frogman_research_v0_1/), with original filenames, directory structure and bytes. The 57-file ZIP was located in ChatGPT Library. All 56 SHA256SUMS entries verified; the checksum file itself is the 57th file. No separate original manifest was present.

| Evidence category | Files |
|---|---:|
| Finalized Solana transaction receipts | 28 |
| Address-history JSON responses | 2 |
| CSV records | 8 |
| Research/methodology/reproducibility Markdown | 4 |
| Python scripts | 2 |
| Calculated summary JSON | 1 |
| Access-error text records | 8 |
| Retrieved raw source responses | 3 |
| SHA256SUMS.txt | 1 |
| Total | 57 |

CSVs: transaction_ledger, asset_disposal, privacy_cash_deposits, timeline, token_account_authorities, wallet_entity_table, source_log and public_claim_tests. The ledger is F0001–F0102; ten verified Privacy Cash deposits total 13,240.973780900 SOL. The 28 receipts include failed and third-party transactions, not 28 unauthorized transfers.

[Complete file inventory](./evidence_inventory_v0.1.json). [Frozen source report](./frogman_research_v0_1/master_investigation_report.md). [Existing report](./master_investigation_report_v0.1.md).

The existing report is text-equivalent to the frozen source but lacks its final newline. It remains unchanged. The byte-exact source is preserved inside the archive directory. Original ZIP SHA256: `3fc70011e6e03ee4c6561981050ad9f1a77f1995f69dc2608aa94123694447d9`.

To verify after retrieving a repository checkout, run `sha256sum -c SHA256SUMS.txt` from `frogman_research_v0_1/`. Preserve these originals; run analysis scripts in a copy if regeneration changes serialization.

## Evidence boundaries

Wallet attribution remains SUPPORTED. The Solana transaction/deposit record is reproduced within its documented scope. Mixed balances are preserved. Privacy Cash withdrawal recipients are not established. EVM claims require independent receipt and bridge-fill verification. Neither fund flow nor a signer/fee payer identifies a human operator or compromise method. No Medium article has been written.
