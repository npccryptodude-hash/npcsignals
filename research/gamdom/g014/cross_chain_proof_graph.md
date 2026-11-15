# Final-edge classification

| Edge | Route 1 | Route 2 |
| --- | --- | --- |
| BNB settlement→deposit receiver→HOT locker | CONFIRMED, frozen G013 | CONFIRMED, frozen G013 |
| HOT locker signed deposit→NEAR credit | CONFIRMED, frozen G013 | CONFIRMED, frozen G013 |
| NEAR internal credit→intent→OMFT withdrawal/burn | CONFIRMED, frozen G013 | CONFIRMED, frozen G013 |
| NEAR OMFT withdrawal→exact Ethereum treasury payment | **SUPPORTED** | **SUPPORTED** |
| Ethereum transaction→B's canonical DAI credit | CONFIRMED, frozen chain receipts; new signature-scope verification | CONFIRMED, frozen chain receipts; new signature-scope verification |
| Full route | **SUPPORTED** | **SUPPORTED** |

The weakest edge remains source withdrawal→treasury payout. The historical factory lacks the current source's withdrawal-registry methods. No target-specific authenticated relayer message, signed instruction, historically authorized payout signer set or independent immutable execution mapping was recovered.

Human identity, company custody, key compromise and legitimate consent remain UNRESOLVED. H1 unauthorized extraction, H2 legitimate treasury settlement and H3 protective relocation are all consistent with technically valid settlement and remain unresolved. G014 establishes no unauthorized loss and changes no prior incident attribution.
