# Wallet attribution and control register

| ID | Full address | Verified role | Gamdom attribution | Unauthorized status |
| --- | --- | --- | --- | --- |
| A | 0xd5fbda4c79f38920159fe5f22df9655fde292d47 | Ethereum transaction initiator for DAI and ETH payments to E1. Existing BUSD payment to B in G006. | SUPPORTED third-party/explorer association inherited from G005. Independent ownership UNRESOLVED. | UNRESOLVED |
| S1 | 0x0067cc2416f792cf0ec5629f5506324ac508f859 | Direct transaction initiator/token sender for USDT, USDC, USD1 and ETH to E1. | Original report describes three Gamdom sources, but independently attributable ownership/deposit-withdrawal documentation is unavailable. UNRESOLVED. | UNRESOLVED |
| S2 | 0x580450dff316ae00d0fbef9621a304020a046ce2 | Direct initiator for USDT, USDC and successful ETH payments to E1. One later ETH attempt failed. | Etherscan displays Gamdom 2. This label is not ownership proof. UNRESOLVED independent attribution. | UNRESOLVED |
| E1 | 0x4b304741599c125a244e498d14562487d7109ab8 | Recipient of three-source consolidation and seven swap outputs; sends 0.01 ETH to A. | Report-linked candidate recipient, not an independently identified attacker. | UNRESOLVED |
| B/E2 candidate | 0xe5686aae44d392aa6a0637fd38393859502f8667 | BNB bridge transaction initiator and matching Ethereum recipient. Historical Ethereum DAI state independently measured. | Existing incident-associated candidate; no ownership or malicious-control conclusion. | UNRESOLVED |
| C | 0xacc0c1f672b03b9a5fed4535f840f09b85f40e98 | Existing G006/G008 swap initiator benefiting B. | UNRESOLVED. | UNRESOLVED |
| D | 0xe757683a51cfd002de479385c2f4c9db10a5e8d2 | Existing repeated pre-incident C funding. | UNRESOLVED. | UNRESOLVED |

## What the control observations establish

A is an exact address match, not a same-prefix guess. A directly pays E1, E1 later pays A, and A's previously verified BUSD transfer pays B. This connects the financial networks. It does not show a common human operator, private-key compromise, or the purpose of any payment.

B's BNB transaction objects identify B as initiator, with nonces 2 and 9. Relay's index calls 0x2aaaa9b71e479e6e2de7e091b09d61c25d2aaaa9 the user/sender, while the receipts show B initiating calls through 0x512000a034e154908efb1ec48579f4ffdb000512. The intermediary and API metadata must not be substituted for the initiating account. Token transfers traverse B → intermediary → 0x4cd00e387622c35bddb9b4c962c136462338bc31 within each deposit transaction. Count each debit once.

Ethereum B's USDT source 0xf70da97812cb96acdf810712aa562db8dfa3dbef and DAI source 0x2cff890f0378a11913b6129b2e97417a2c302680 show extensive multi-counterparty activity in the collected window. They are service-like financial counterparties, not newly identified victim wallets. Their observed roles and use by others do not prove ownership or shared control.

No C/D direct edge occurs in the selected E1 receipt event/native ledger. This is a bounded negative result, not an all-chain absence claim. Existing C→B routes remain preserved. No new shared authorizing key is recovered; G008's cryptographic evidence remains unchanged. New transaction senders are node representations, not independently recovered new signatures.

Reproduce by matching full addresses in incident_origin_ledger.json, the referenced receipt/transaction objects, and the frozen G006 BUSD row. No contract label is required for the exact-address result.
