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

## v0.2 investigation updates

The archive and v0.1 reports above remain frozen. New English-language research is in [v0.2](./v0.2/), with [master report](./v0.2/master_investigation_report_v0.2.md), [evidence index](./v0.2/evidence_index_v0.2.json), [Relay matched pairs](./v0.2/relay_verified_pairs_v0.2.csv), and [reproducibility methodology](./v0.2/methodology_and_reproducibility_v0.2.md).

New unique ledger range F0103–F0206 spans four CSVs: transaction_ledger_v0.2 (evidence enrichments), evm_transaction_ledger_v0.2 (15 Ethereum outgoing transactions), evm_extended_ledger_v0.2 (funding, internal credits, onward routing and Relay fills), and chain_extension_ledger_v0.2 (Robinhood transfers and Arbitrum consolidation). Do not add amounts across successive hops or count repeated per-transaction fees per event.

Narrow CONFIRMED findings include 362.262907164350756807 ETH sent from the Ethereum routing address; six Relay deposits totaling 212.499 ETH matched to 561850.214994 USDC on Arbitrum; and six subsequent USDC transfers to one consolidation recipient. Three Robinhood token transfers from the affected address to the receiving address are reproduced at 2026-10-06T20:14:00Z within the examined window. The Robinhood-to-Ethereum bridge origin match, downstream recipient ownership and compromise method remain UNRESOLVED.

Supporting files include raw request/response records, execution traces, token-state snapshots, zero-value event exclusions, wallet/entity tables, graph data, scoped EVM timelines and verification scripts. See the index for a complete path/size/checksum inventory and unresolved_questions_v0.2.md for next nodes. No article has been written or published.
