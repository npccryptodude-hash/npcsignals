# Verification report

Run `python3 verify.py` offline. `verification_results.json` records the completed result. The verifier rebuilds all six derived JSON outputs, checks every acquisition-record digest, source/destination bridge correlators and amounts, each ledger receipt's block/index/header relationships, success/failure status, and nine exact balance reconciliations. It compares all 138 frozen tracked files with the starting Git commit.

39 new transaction hashes have receipt, transaction and header representations: 37 successful and two failed. Two G006 Ethereum receipts are extended only to resolve their BNB provenance and are not counted as new transactions. Failed transaction values remain in transaction metadata as attempted values, with zero principal in the movement ledger.

The acquisition archive contains 230 records. Collection scripts perform only read-only RPC/HTTP requests. `source_register.json` preserves exact methods, parameters, endpoint URLs and collection times. `package.py` deterministically compresses parsed acquisition records without deleting their local originals. The repository publishes the archive rather than redundant raw cache files. `analyse.py` derives ledgers from that archive using integer arithmetic. JSON raw amounts are strings to preserve uint256 precision. No workbook or rounded dollar ledger is substituted.

Checksums authenticate saved evidence integrity, not website truth or chain consensus. No new signature recovery, state-root proof, full archive-node replay or second-provider Ethereum state validation is claimed. Historical symbol verification corrected a provisional token-name alias before publication. An explorer's displayed failed ETH attempts are explicitly excluded from principal.

Evidence classifications: transaction movements, historical states and exact address/identifier matches are CONFIRMED at the documented primary-representation scope. Third-party Gamdom association and report-to-route identification are SUPPORTED only where noted. Independent ownership, unauthorized status, ultimate beneficiary, full E2 provenance and total losses are UNRESOLVED. Unexamined networks are NOT ASSESSED.

The publication procedure must add only this G010 sibling, use the actual current remote parent, validate checksums/calculations before updating main, fetch the resulting remote commit, compare every published byte and read back pinned files. Successful local verification or blob upload alone is not successful publication. Final remote verification is reported separately after completion.
