# Remaining 35 ETH routing destination — resolved protocol path

Parent public checkpoint: `06b7e2fd3dc0fb310919d466166088c7d3147a68`. F0498–F0504 append to the existing ledger; F0169/F0170 remain unchanged.

| Layer | Exact record | Amount | Classification |
|---|---|---:|---|
| Ethereum inbound | 0x1845f4786137bfca9b6dbcaff87e95b867e02c0c79aca1e158f475f61747690f | 35 ETH | CONFIRMED, fresh F0169 reproduction |
| LI.FI swap / Across origin | 0x321064d6fcab77a911a2af5d452269588e621c590796716f5fa9f7528dd7f32a | 35 ETH → 91,241.354058 Ethereum USDC deposited | CONFIRMED |
| Across Arbitrum fill | 0xed65e3a6b4d1eedcfeaced2a4162d650a19cf7b15fc85a548103263467059801 | 91,232.216513 USDC | CONFIRMED |
| Hyperliquid bridge transfer / deposit credit | 0x107db810fd86893dc4cf8df03c1753236e04fc2d7b3f17304b34dfb840c1fa51 | 91,232.216513 USDC | CONFIRMED transaction and identical API credit |

Origin 0xdb5f641f9b335f48c550cd7023c2268b70a76ec7 funded 0xa3ca6199d8692ec40d0287e615b48d0e8cde9abe. The recipient is an EOA, not independently a named service. It called verified LI.FI Diamond 0x1231deb6f5749ef6ce6943a275a1d3e7486f4eae. LI.FI API identifies KyberSwap in the swap step; verified explorer source identifies swap router 0x6131b5fae19ea4f9d964eac0408e4408b66337b5 as MetaAggregationRouterV2. `Cow` is an integrator string, not an identification of the operator.

Across deposit **4737420** at Ethereum SpokePool 0x5c7bcd6e7de5423a257d81b442095a1a6ced35c5 matches the fill at Arbitrum SpokePool 0xe35e9842fceaca96570b734083f4a58e8f7c5f2a. The verifier derives event selectors from first-party interface signatures and matches every relay parameter, not timing or amount similarity. Across and LI.FI APIs independently return the exact source/fill hashes. Recipient on Arbitrum is the same full address 0xa3ca…9abe. Relayer as emitted is 0xef1ec136931ab5728b0783fd87d109c9d15d31f1 and repayment chain is Ethereum (1); neither establishes an owner or custody relationship.

USDC bridge input/output difference is **9.137545 USDC**. Quote fee metadata is not promoted into a verified decomposition or market spread. Ledger includes block numbers, UTC timestamps, gas, complete deposit/fill events and native/token transfer evidence. Empty origin account code is reproduced at the Ethereum case block; empty Arbitrum recipient code is reproduced at the dated current snapshot. Historical Arbitrum code lookup was unavailable. Current explorer proxy/implementation metadata is not a historical implementation or operator audit.

The exact USDC onward transfer to 0x2df1c51e09aecf9cacb7bc98cb1742757f163df7 matches Hyperliquid's API deposit credit by hash and amount. First-party Bridge2 documentation identifies that legacy USDC bridge address. The API also reports 91,232.21 USDC transferred internally to spot; this is not an external withdrawal, conversion or XMR1 redemption. No new fills or balances are asserted. Historical Arbitrum USDC state calls failed, so exclusive lifetime allocation of the sender's balance is not established. Account continuity and the exact outgoing transaction/credit are confirmed separately.

This is an additional Across route and Hyperliquid deposit account, distinct from the existing six Relay routes and their totals. Do not add routing stages or this observation to loss totals. Complete affected-wallet provenance, common ownership, named operators, private custody and final beneficiary remain UNRESOLVED. Privacy Cash remains separate.

## Scoped unlabeled-destination closure

The documented F0152–F0156 destination groups have been examined sequentially in separate public commits: 0x824a…cebe/0x7da9…7226 are EOA forwarders; 0x2625…b324 is an EOA forwarder and 0x0b3e…58a0 a mixed-flow EOA; 0x4521…ff58 is a dated 4 ETH holding boundary. The F0169/F0170 route is now linked through Across to a Hyperliquid credit. Named service identities for the forwarding/holding EOAs and pooled boundary 0x9be5…7516 remain unresolved, with no defensible further case allocation. No open destination in this scoped queue is forced into a named service. Next highest-priority target is remaining Robinhood funding/disposal gaps. No secondary branch researched and no article written.
