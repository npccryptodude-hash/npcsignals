# GLITCH v0.10 — B downstream and ZYROX 6hR7 attribution lead

Source: user-supplied Work finalized Solana Mainnet RPC checkpoint, 2026-10-13. Raw JSON not exported here.

B wallet: `F2khA1QZooUzidyycMzpJ6x38eQBxuDq4UrvdUUiSwuo`.
Seller → B earlier: 150.173828355 SOL. B balance before seller inflow: 127.361453351 SOL. B also received 157.926482647 SOL from 37 later successful stake-withdrawal transactions, so B's full balance was commingled.

## Primary outgoing transaction

Signature: `61v1KxQkjSpMTenBBKE3nCSyh4EBZFV8gffPdaNojEjXvvzavdCqEbHqWQ8ewf3eWPTiqrsLbUErdpbPzDFGp13B`.
UTC 2026-10-12T17:52:55Z; slot 456135573, index 47. B sole signer and fee payer. Finalized, meta.err=null, status Ok.

- P026 outer:1 → `6hR7GwHpdHbJgNJAagm64KMsMYu8mR6ExzmbE5N8wv1N`: 435460959353 lamports.
- P027 outer:2 → `6rYLG55Q9RpsPGvqdPNJs4z5WTxJVatMB8zV3WJhs5EK`: 200000 lamports.
- P028 outer:3 → `D2L6yPZ2FmmmTKPgzaMKdhu6EWZcTpLy1Vhx8uvZe7NZ`: 200000 lamports.
- P029 outer:4 → `DttWaMuVvTiduZRnguLF7jNxTgiMBZ1hyAumKUiL2KRL`: 200000 lamports.
- P030 outer:5 → `astrazznxsGUhWShqgNtAdfrzP2G83DzcWVJDxwV9bF`: 200000 lamports.
- P031 transaction fee: 5000 lamports.

B balance: 127361453351 + 150173828355 + 157926482647 = 435461764353; less 435460959353, four × 200000 and fee 5000 = zero. No account-close or WSOL transfers in this outgoing transaction. Reported 37 incoming transactions all in preceding slot 456135572, after seller receipt, and individually finalized.

## High-priority possible ZYROX connection

Existing NPCsignals ZYROX research references a known `6hR7` wallet as an investigated operational node, including a prior closed identity/control test (see `research/zyrox-investigation-post-freeze/ZYROX_Beneficiary_Control_Research_v0_115.md`). The full 6hR7 address in the GLITCH receipt is `6hR7GwHpdHbJgNJAagm64KMsMYu8mR6ExzmbE5N8wv1N`.

**CRITICAL:** The archived ZYROX notes inspected during this update refer to the abbreviated `6hR7` label; the exact full ZYROX pubkey has not yet been retrieved and compared byte-for-byte. Therefore exact ZYROX-GLITCH wallet overlap is a **HIGH-PRIORITY CANDIDATE, NOT YET CONFIRMED**. Retrieve the fully qualified ZYROX 6hR7 address from original ZYROX evidence ledger and compare exactly.

Even if exact overlap is confirmed, it would establish common *wallet infrastructure/counterparty*, not Kytro identity, shared human control, exclusive GLITCH proceeds attribution, or fraud.

## Next bounded task
1. Retrieve exact ZYROX 6hR7 pubkey from primary ZYROX research evidence and test exact equality.
2. If exact match, review its documented ZYROX role/transactions and the new GLITCH inbound receipt.
3. Do not independently follow further downstream addresses before reporting findings.
