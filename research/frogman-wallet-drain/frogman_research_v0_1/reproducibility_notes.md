# Reproducibility notes

Run `python fetch_solana.py` from any directory to re-fetch the incident-window signatures found in the preserved address-history JSON. Run `python build_record.py` to rebuild the derived CSVs and calculations from captured receipts. Python standard library only. Fetch is read-only; it never signs or submits transactions. Raw snapshots, not live explorer labels, are authoritative for reproduced calculations.

Address histories were requested with limit=1000 and finalized commitment; victim response returned 850 and receiving response 26. Scripts select 1791316000 < blockTime < 1791324000 to include incident receipts. No pagination was needed for these returned histories; completeness of an RPC index is not an exhaustive guarantee of all associated token accounts. Raw getTransaction files include full signatures and balances. Receipt failures and unavailable EVM paths are preserved under access/.

Sum successful System Program transfers from 69Fn… to pool 4AV2… invoking program 9fhQ…: 13,240,973,780,900 lamports = 13,240.973780900 SOL. Ten deposits. Each fee 205,000 lamports and other balance cost 1,391,920 lamports. Final source postBalance 6,403,163 lamports.

BP: incoming 1,429,939,158,705,563 raw units; four debits of 357,484,789,676,390 raw units; three raw units remain. Mint decimals=9. Do not round before reconciliation.

Current fetch_solana.py reuses existing receipt files. Preserve them; fetch into a copied clean package if testing a second provider. Compare semantic receipt fields, not just JSON byte serialization. SHA256SUMS.txt hashes the snapshot files for integrity, not chain authenticity.

Web log URLs are retrieval locations, not on-chain evidence. Sotwe is a mirror, and direct X fetches failed. Relative posting times are not used as exact timestamps. Original X post IDs found in public references are preserved but their contents were not directly retrieved.

Ledger rows are instruction-level observations, not a chronological list of standalone transactions. Amount totals must filter actions/assets and exclude failed instructions, fees and intermediate routing as appropriate. Chain fee is not measured slippage. Token-account ownership fields do not identify a human.
