# G012 — Cross-chain settlement and order-identifier audit

Independent evidence checkpoint, 16 October 2026. Starting checkpoint: `1d057aa9456d2d40401683438cf0468a5cb969cf`. All 196 files in G005/G006/G008/G009/G010/G011 remain unchanged. Medium and X: **HOLD**.

Two actual CoW order UIDs are independently reconstructed from BNB settlement calldata, the chain-56 EIP-712 domain and successful Trade events. Their signed appData hashes match the exact full metadata returned by the BNB orderbook. That metadata specifies NEAR Intents, Ethereum DAI and B as the ultimate destination. The source-chain buy token is BNB USDT, delivered to two distinct deposit addresses; it is not DAI.

The public NEAR Intents status service explicitly maps each of those deposit addresses and source settlement hashes to one Ethereum payout. Four newly obtained NEAR transactions independently confirm deposit credits, intent execution and DAI withdrawals addressed to B. The two Ethereum payouts were already documented in G006 and are not counted again.

**Evidence boundary:** each observed blockchain execution, recomputed UID and authorization result is CONFIRMED within the stated RPC evidence standard. The complete cross-chain mapping is **SUPPORTED**, because its unique deposit-address-to-execution index is supplied by the protocol service. Neither Ethereum ERC-20 transfer contains the BNB order UID or a NEAR withdrawal identifier. This is an execution-specific primary-source mapping corroborated on three chains, not an amount/timing inference, but it is not a trustless cross-chain proof.

| Route | BNB principal, USDT | BNB deposit, USDT | Ethereum receipt to B, DAI | Route level |
| --- | ---: | ---: | ---: | --- |
| 1 | 3296.947360645719000000 | 3296.944723631957632111 | 3293.876314118353387030 | SUPPORTED |
| 2 | 3947.417222165521700000 | 3947.414585151760332111 | 3947.497560500152030405 | SUPPORTED |

Order 1 uses the exact UID pre-signed by B through delegated execution. New call-trace and historical presignature-state evidence corroborate its internal settlement call. Order 2 uses EIP-712, not presignature: its actual calldata signature independently recovers B. Valid technical authorization does not establish legitimate human consent.

Four new distinct transaction records are verified, all on NEAR. Two BNB settlements, two Ethereum payouts and the BNB presignature are reused from frozen research. No new company attribution, common human operator or verified unauthorized loss is established. H1/H2/H3 remain unresolved.

## Files and reproduction

`settlement_order_register.json` contains full UIDs, decoded signed orders, signature bytes and hash-bound metadata. `decoded_execution_ledger.json` contains ordered source transfers, protocol mappings, initiators, fees and destination amounts. `near_execution_register.json` contains the four NEAR execution records, heights, timestamps, decoded actions and receipt events. `authorization_verification.json`, `destination_balance_checks.json` and `financial_totals.json` provide separate control and accounting results.

Install `requirements.txt` in an isolated Python environment, then run `python analyse.py` and `python verify.py`. Verification is offline and imports frozen G011 receipts from the adjacent directory. `python replay.py /new/output/directory` optionally repeats all archived read-only acquisitions; service responses may change. `collect.py` documents selected acquisition modes. `acquisition_archive.json.gz` preserves all new requests, responses, errors and collection timestamps. `source_register.json` names and hashes each canonical archive record. `SHA256SUMS.json` hashes every published file except itself.

NPCsignals documents. It does not judge. Evidence, not velocity.
