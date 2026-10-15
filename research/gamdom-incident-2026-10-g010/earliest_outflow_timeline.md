# Earliest candidate outflow timeline

All times UTC, October 13, 2026. This is a selected route timeline, not the earliest transaction of the entire reported breach. Full event ordering and exact hashes are in incident_origin_ledger.json and transaction_register.json.

| Time | Observation | Scope |
| --- | --- | --- |
| 15:24:35 | E1 and B tracked token opening balances are zero. E1 native opening balance is also zero. | Historical state at block 26184449, before the requested window. |
| 16:00:23 | A initiates 738.148858772417648963 DAI to E1, hash 0xb2cca150592b3ba9344ff17a6f39888a40a855fc1619e8946b8b87e17217578f. | Earliest verified candidate principal edge in this reconstruction. |
| 16:16:47 | S1 sends 262237.892832 USDT and S2 sends 92182.438003 USDT to E1 in two transactions in block 26184708. | Earliest verified larger stablecoin cluster. |
| 16:34:31–16:34:35 | B's BNB-chain 370000-USDT deposit and matched Ethereum 369592.897320-USDT delivery. | Source-chain receipt newly verified; destination already known. |
| 17:42:23 | E1 returns 0.01 ETH to A. | Verified return, not additional incoming principal. |
| 17:43:53–17:43:59 | B's second BNB-chain deposit and matched 336199.051906277094220550-DAI delivery. | No original victim source independently identified. |
| 17:45:23 | Existing G006 A→B BUSD transfer. | Imported connection, not recounted. |
| 18:00:11 | Final selected E1 USDC→DAI swap. | Eleven seconds beyond requested endpoint, explicitly included to close accounting. |
| 18:05:35 | Closing historical state at block 26185250. | Collection envelope ends here, not a 18:00 state claim. |

The timeline does not independently locate the claimed Solana, TRON or XRP originating payments. No company acknowledgement time is substituted for on-chain authorization evidence.
