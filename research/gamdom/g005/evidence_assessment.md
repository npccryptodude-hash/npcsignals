# Evidence assessment

CONFIRMED means directly inspected primary evidence at the stated scope. Explorer receipts/logs are primary blockchain representations, but this checkpoint has no direct node receipt download or second-node validation. Checksums authenticate our saved records, not truth of a website.

| Finding | Level | Reproduce |
|---|---|---|
| Two Polygon transfers with full IDs and raw amounts | CONFIRMED movement | Open G005-T01/T02 URLs; check success, block, UTC time and Transfer logs; divide raw values by 10^6. |
| Two bridge executions yield DAI to same full address | CONFIRMED movement | Open source/destination URLs and Axelarscan GMP pages; match payload hash, destination chain, token amount and final DAI recipient. |
| Candidate sender belongs to Gamdom | SUPPORTED | PolygonScan label is present; owner-signed evidence absent. |
| Recipient is attributed to incident | SUPPORTED | vxdb links Arkham entity; address page belongs to that entity; diagram 0xe56 is consistent but truncated identifier alone is insufficient. |
| Six movements are theft | UNRESOLVED | Need owner-verified victim set and unauthorized transaction schedule. |
| Company publicly acknowledged automation-server connection and hot-wallet loss | CONFIRMED statement | Read S06/S07 and original DOM time metadata. Technical root cause independently UNRESOLVED. |
| Customer liabilities covered / withdrawals functioning | UNRESOLVED | Need liabilities and controlled reserves at common cutoff; independently verified withdrawals after restart. |
| Common human operator or ultimate beneficiary | UNRESOLVED | No identifying control evidence. |
| Full eight-network loss reconstruction | NOT ASSESSED | Completed reconstruction covers selected Polygon and Ethereum transactions only. |

## Negative findings and closed uses
- G001–G004 contain no incident hashes; preserved unchanged.
- The latest normal outgoing receipt inspected for Ethereum B70 candidate is dated August 20, 2026; exclude that transaction from October incident. This does not exclude ERC-20/internal/delegated activity, other chains or other wallets.
- Arkham entity and recipient transfer tables displayed old builder payments with sequential near-zero hashes ending 5000–500f. No incident attribution is made from these rows; cause of presentation anomaly UNRESOLVED. Inflow toggle did not expose a useful incident ledger. The entity visualizer led to sign-in. No authenticated Arkham access was attempted.
- Small same-prefix/suffix addresses visible on Polygon are distinct full addresses; dust movements are not merged into the victim/recipient identities.
- No independently verified recovery, reimbursement or customer withdrawal was obtained. Absence in this sample is not evidence of absence globally.

## Customer-funds claim
Original company post asserts user funds are safe. Founder describes hot-wallet losses and protective cold-wallet movements. These statements support an incident acknowledgement but do not prove customer liability coverage. A company may absorb a hot-wallet loss without reducing customer balances. Downtime does not establish insolvency. Neither safety nor insolvency is independently established here. Needed: controlled reserves, custody liabilities, timestamped reconciliation and receipt-backed withdrawals; no customer account access or test deposit was performed.
