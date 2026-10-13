# NPCsignals GLITCH / ZYROX — v0.15 cross-case operational control test

Date: 2026-10-13. **Document review, not a fresh Solana RPC pull.** Sources: GitHub GLITCH v0.11–v0.13 and user-provided Work checkpoints through 8HCSEe history (244 unique finalized receipts reported). The 216-row raw instruction ledger was not furnished into this repo update. Preserve the frozen ZYROX baseline.

## Single question

Does the exact shared wallet `6hR7GwHpdHbJgNJAagm64KMsMYu8mR6ExzmbE5N8wv1N` show the **same operational control role in both token launches**, or only shared financial-counterparty/settlement activity?

## Cross-case evidence matrix

| Test | ZYROX | GLITCH | Decision |
|---|---|---|---|
| Exact same wallet | Full address matched ZYROX C3 | Same address received 435.460959353 SOL from B | CONFIRMED wallet overlap |
| Inbound funding | 6cn→6hR7 468.432649156 SOL U238, F1dC→6hR7 175.588375882 SOL U223 | B→6hR7 435.460959353 SOL via signature `61v1KxQkjSpMTenBBKE3nCSyh4EBZFV8gffPdaNojEjXvvzavdCqEbHqWQ8ewf3eWPTiqrsLbUErdpbPzDFGp13B` | Different counterparties, same receiving wallet |
| Wallet's active payments | 6hR7 sole signer / fee payer for funding creator HZrAo 0.033895331 SOL U310 and BbBZ 2.947003195 SOL U232, plus CAxTx U233 | 6hR7 sole signer / fee payer for 400 SOL→USDT swap, 5000 USDT→SOL swap, and USDT payments to EnVAvXw | Active transacting wallet in both cases; **not** proof of launch control |
| Launch authority | No cited proof that 6hR7 signed creator mint or possessed creator keys | No cited proof it signed GLITCH mint or seller private-key operations | UNRESOLVED |
| Common signer / control | No cited direct shared authority over creator/other source accounts | GLITCH sale signed by seller; B→6hR7 signed by B; later 6hR7 payments signed by 6hR7 | No cross-wallet control established |
| Counterparty recurrence | 6hR7→EnVAvXw 100.022387 USDT Oct 2, 0.823595201 SOL Oct 4 | 6hR7→EnVAvXw 1051.358017 USDT Oct 12 | CONFIRMED repeated payer/recipient relationship |
| Earlier payment network | 6hR7→8HCSEe history begins Jan 17, 2025: 28 USDC payments totaling 22231.278986; 4 USDT totaling 587.234148; 11 SOL totaling 1.521890816 | No reported 8HCSEe activity on GLITCH date Oct 12 | Pre-existing network; cannot be automatically treated as launch-specific |

## Correction carried forward

Oct 3 transfer of 150.005059 USDC from 6hR7 was to owner `8HCSEeC98fR2BcDs8mkyiRq3ahSc7GNEqNEsW5oWote2`, **not** EnVAvXw. This was fixed non-destructively in GLITCH v0.13, with old ZYROX v0.44 statement flagged as unsupported. No false USDC S→EnVAvXw transfer should appear in summary counts.

## Classification

- **CONFIRMED:** same on-chain wallet appears in the two case networks; received SOL from documented case-linked counterparties; directly signed outgoing instructions relevant to each case; repeated recipient-owner links.
- **SUPPORTED (limited):** shared operational *payment/settlement* node — wallet-level functional description only.
- **UNRESOLVED:** one human/entity operating both launches; 6hR7's beneficial owner and role as merchant/service; launch contract/program authority; direct control of ZYROX creator HZrAo, GLITCH seller, or B; Kytro attribution; allocation of commingled funds.
- **NOT ASSESSED:** exhaustive signer/co-signer graph, RPC independence and all downstream balances.

**Conclusion:** There is strong cross-case *transaction-network overlap*, not yet sufficient evidence of common **launch control**. The pre-existing Jan 2025 bilateral 6hR7→8HCSEe payment relationship substantially weakens any assumption that 2026 recurrence must reflect a new coordinated launch operation.

## Stop / next falsifiable test

Archive/reproduce full historical receipts and 216-row ledger. Then test narrowly whether a **specific creator/seller critical transaction** in each case was signed or authorized by the same external entity/key. If no transaction-specific cross-wallet control edge is found, freeze control attribution as UNRESOLVED and do not continue arbitrary graph expansion. Do not publicly allege fraud or Kytro identity.
