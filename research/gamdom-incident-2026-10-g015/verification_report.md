# Verification report

Run `python verify.py` within this repository. The standard-library-only verifier checks every SHA-256 manifest entry, all 266 frozen evidence files, referenced input hashes, 34 unique source movements, exact decimal-to-integer quantities, chain/contract totals, the BNB conservation identity, earliest selected movement and selected baseline comparisons. It validates imported signature success flags without claiming a new signature-recovery audit. It then rebuilds analytical JSON and derived reports in a disposable directory from the saved inputs and requires byte agreement. No network access is used by the verifier.

A manifest checks file integrity, not truth, canonical inclusion or company ownership. Source receipts retain their earlier RPC/explorer limitations. Public documents retain authentication, temporal and completeness limitations. No raw acquisition response is silently replaced by an empty result.

Pre-publication validation must pass before branch publication. Remote publication is separately confirmed by fetching the actual commit, comparing all new file bytes and checking the parent tree for changes outside G015. This report does not claim a future remote verification has already occurred; the final delivery records its observed outcome and exact SHA.
