# Cross-chain routes

## R1 — Polygon USDC to Ethereum DAI
Source `0xcc4d20d29b582aa480c14d075ac01529721f532cc762d0f70bdedc2957ed6d3c`, block 95473230, 2026-10-13 18:12:37 UTC. Recipient wallet spends exactly 12,139.456905 USDC received in G005-T02. Explorer logs show Squid transfers, fee 15.174321 USDC, conversion of 12,124.282584 USDC into 12,119.633447 axlUSDC, then burn and Axelar ContractCallWithToken toward Ethereum. Source gateway log index 834 / event index 11.

Destination `0x5bd4efdc04ef4b8dddc999416d2e2a849c9ae0c3b271fd707dd376b8bb778a70`, Ethereum block 26185295, 18:14:35 UTC. USDC delivery and Curve swap produce 12,117.648333297552877028 DAI to the same full address. Payload hash BFC3AB0BA53FAD559671936E7230BF697F120C91F0D5C1A04FF0A017E4BA62A5 matches source and destination CrossMulticallExecuted. Axelarscan independently maps these transactions. The relayer sender is service infrastructure, not evidence of wallet owner identity.

## R2 — Polygon USDT0 to Ethereum DAI
Source `0x82196a6151133e81723f685da79ea7c07d5400f004129f83165cf2accd216d4c`, block 95473325, 18:15:00 UTC. Exactly 19,610.310097 USDT0 enters Squid. Logs show 24.512887 USDT0 fee, 19,585.797210 USDT0 swapped for 19,563.422653 USDC; subsequent conversion/burn of 19,545.712075 axlUSDC. Source gateway log index 398 / event index 17.

Destination `0x3aed0e9c1b2b9e90e8361f5db8a812cea84b6fbd7da7ba544d8b0ab6f940b982`, Ethereum block 26185305, 18:16:35 UTC. Curve swap yields 19,542.478208761477069197 DAI to the same full address. Matching payload hash 7BBC2A44C3F651BB1B9A537C8E7F658F4DCA99413E59644AB1E41259D0B7B61F appears at both ends. Axelarscan maps the execution.

Both routes: CONFIRMED movement; incident attribution SUPPORTED; unauthorized origin UNRESOLVED. Matching quantities do not by themselves establish exclusive provenance if pre-existing balances exist. No cross-chain control over a human identity is inferred.

## Hyperliquid / THORChain / Solana
Original vxdb diagram alleges Solana via Mayan to Ethereum, then two approximately 250k DAI branches, one through a contract where the source says the trail stops, another toward Arbitrum, Hyperliquid, THORChain and Baltex. Diagram includes an additional approximately 135k from an unconfirmed source. These are leads only.

The earlier THORChain screenshot shows about 125.5k USDC on a source labelled Ethereum, about 1.499 BTC (output 1.49928635 BTC), and truncated hashes `0x29bf…47a3f5` / `0aae42…2759ca`. The later diagram calls 0x25C Arbitrum. Chain discrepancy and incomplete hashes prevent receipt matching. No Hyperliquid account or THORChain deposit independently verified. Do not merge these routes with R1/R2 solely because labels share an entity.

Next tracing boundary: Ethereum onward token history for the full 0xe5686AaE address, plus complete original THORChain IDs. BSC and the remaining victim networks were not reconstructed in this checkpoint. No connection to Frogman is claimed.
