# Acquisition coverage and evidence levels

## Exact scope

Reused frozen G011: the two complete BNB settlement receipts, transaction inputs, headers; B's precise presignature receipt/input; prior-block delegated code; preserved valid outer and chain-56 EIP-7702 authorization signatures. G008 Ethereum authorization records remain unchanged. Reused G006: the two candidate Ethereum payout identities. No prior financial history or signature-envelope investigation is restarted.

New archive: complete metadata and receipt for each Ethereum candidate plus block headers; two chain-56 historical settlement runtimes and one domain call; Sourcify chain-56 exact-match source/ABI/runtime; BNB orderbook records for both actual UIDs; mainnet 404 controls; two deposit-address status records; four NEAR final-execution records and four transaction-inclusion block headers; three historical presignature-state calls; one callTracer result; four historical Ethereum DAI balances and four address-filtered DAI log queries spanning the two receipt blocks. Exact URLs, requests, timestamps, failures and canonical hashes appear in the source register. Additional unpinned upstream contract-source GETs are archived only for transparency; conclusions use the pinned Sourcify source/runtime match.

Ethereum receipt blocks 26184851 and 26184865: exhaustive canonical DAI Transfer coverage involving B within each single block, both sender and recipient topic filters, deduplicated by logIndex and ordered. Balance reconciliation is limited to those blocks. No claim of exhaustive between-block transfer coverage or downstream exclusive fund provenance is made.

Destination search is bounded to the G006 candidates: 16:45:35 and 16:48:23 UTC, 34 and 25 seconds after their respective BNB settlements. Timing is descriptive; the protocol's exact deposit-address mapping supplies the correspondence. No broad scan was required after the unique status results named those hashes.

Four new distinct NEAR transactions: two deposit calls and two atomic execute_intents calls. NEAR transaction-inclusion heights, timestamps and receipt outcome block hashes are preserved. Receipt execution can span blocks; inclusion header timestamps are not claimed to timestamp every child receipt. All reported receipt outcomes are successful and final. NEAR transaction/NEP-413 signatures are preserved but not independently Borsh/signature-reconstructed. RPC execution status is the verification source.

## Levels and reproducibility

- CONFIRMED: decoded on-chain Trade UIDs; recomputed domain/order hashes; EIP-712 owner recovery; precise UID's presignature event/state/internal call; historical bytecode match; canonical source/destination transfers; historical selected-block balances; NEAR deposit credits, intent events, withdrawal token/amount/memo.
- SUPPORTED: complete BNB→NEAR→Ethereum correspondence. Reproduction combines signed order metadata, unique source deposit receiver, public protocol status mapping and three-chain RPC executions. No common consensus identifier was verified across every boundary.
- UNRESOLVED: human consent, corporate attribution, custody, incident causation, unauthorized loss, cryptographic linkage of service index mappings.
- NOT ASSESSED: quote attestation issuer signatures, full NEP-413 cryptography, independent Solidity compilation, bridge validator threshold proofs, lifetime deposit-address uniqueness, downstream spending, USD valuation.

Acquisitions use NodeReal for BNB, Tenderly gateway for Ethereum, NEAR archival RPC, Sourcify and public protocol APIs. G011's independent-provider corroborations remain available but are not presented as second-provider corroboration of every new query. No independent state-root/Merkle/consensus replay is performed. API record integrity is captured as retrieved, not proven immutable. No access credentials were invented or authentication bypassed.
