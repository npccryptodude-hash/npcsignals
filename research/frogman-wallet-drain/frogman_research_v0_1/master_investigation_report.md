# NPCsignals: Frogman wallet-drain investigation

Version v0.1 | Research cutoff: 8 October 2026 | Not an article

## A. Current case status

A reproducible Solana record has been established from direct finalized JSON-RPC responses. This package preserves 28 transaction receipts, two address-history responses, a 102-row instruction/fee ledger (F0001–F0102), ten deposit records, six asset-disposal records, token-account authorities and an aligned UTC/SGT timeline. The 46-minute Solana window is reconstructed. The EVM timeline, asset disposals and cross-chain exits are incomplete because queried explorers and APIs returned access errors or timed out. No EVM case transaction was independently reproduced in this run. The ledger is not a complete all-chain accounting.

Wallet attribution is SUPPORTED by public analyst reports and a trader-directory page. The directory shows abbreviated addresses and labels its own verification method; its underlying attribution transactions were not obtained. Unauthorized access and the estimated loss are public claims consistent with Frogman's statements; the chain alone cannot establish authorization or the human operator.

Affected Solana wallet: `9wMSNoA7TzhwUjqsACVGEvzAxAibCHnsZTgXEAGov8zQ`.
Receiving Solana wallet: `69FnU8vszZSZF6DZCT6VHdsvm3DvvojDgbwqzHJ4cCFS`.
Reported affected EVM wallet: `0x14AA2A71dbb5eF87b81F92205E2699AA4aa65794`.
Reported downstream EVM address: `0x427C4b37de0714821B09C4FC655a713AbbCfbA83` (CLAIMED incident role).

## B. New CONFIRMED findings

### Earliest reproduced suspicious Solana outflow

6 October 2026 **20:14:54 UTC**, equivalent to 7 October **04:14:54 SGT**. Signature:
`57wSAHgVrsNf7hDvnnEDnpjb6fF1nWj6h9bGKLB5ivKRLwT7TZia4USS1u1GZWsndXK3TB6LKGy3Aj62jMhMu1aj`.

The affected wallet signed and paid 0.000080000 SOL. A transfer of **1,429,939.158705563** units of mint `BPxxfRCXkUVhig4HS1Lh7kZqV6SPJhzfEk4x6fVBjPCy` moved from token account `CRrQL2iwTQB2CDr5UjuXBFBcumFr6vsBwTuQkA48SgJe` to `6sTr8zMe9oxxVSxh4KpM5qFVjh1cFSy2NeqEr9SzeaA6`, whose recorded token-account owner is the receiving wallet. The parsed instruction calls the source authority `multisigAuthority`; that parser label is not proof of a multi-human arrangement.

The returned affected-wallet history contains 850 entries extending to August. Its immediately preceding history entry is at 2026-10-06T09:06:40Z. This supports identifying 20:14:54 as the first suspicious outflow in the captured incident window, not a universal assertion about every related account or previous compromise activity.

### Additional transfers and failed attempt

20:15:05 UTC: 16,031,410.560000 units of mint `ZesMGYmokFiEuDvNzWeMhB7jxF6eUW8c512vwSKSTNK` debited from the affected token account; receiving balance increased by 15,871,096.454400. Difference **160,314.105600** units, exactly 1% of the debit. The mechanism of this difference requires mint-extension verification; do not call it slippage. Public token listing supports the name Just a Backpack, separate from BP.

20:15:14 UTC: **7,859.974642 USDC** transferred to the receiving wallet's token account.

20:15:34 UTC: **0.293808325 SOL** transferred directly to the receiving wallet. Signature `2ZjeSc8CfVQnkRzm9oYSvNSYzNLVwYAFCpBRoQyu8eBnTUhT9GTQHhzU4AnGvZtcNhQS2wUUfrTeyhJogDunUJtG`.

20:16:37 UTC: failed attempted transfer of 331,588.680000 units of mint `6dPweBFhc13AjGQ5MBYJUs9EYDJ3zXfGPi61zDAVEwDb`. Signature `3gqaBzu1hyGxSTWtJYQD7jHtD8cq8fks7VJUqcrLGJq4YpW7HEDsnpdqqxEnHZYp6msqmde6qzQQvpZmkePCBpak`. Logs report insufficient lamports during associated-token-account creation (810,880 available versus 1,574,800 required). The transfer did not commit; 80,000 lamports of network fee did. Failed instructions are explicitly identified in the ledger and must not be counted as completed asset movements.

### Asset disposals

Four transactions reduced the receiving BP balance by **357,484.789676390** units each, at 20:18:14, 20:20:41, 20:21:48 and 20:23:43 UTC. Total disposed: **1,429,939.158705560**, leaving **0.000000003 BP** relative to the captured incoming amount.

Observed gross WSOL receipts into the receiving wallet's temporary WSOL account total **13,060.251206492 SOL-equivalent**. Native balance increases across those transactions total **13,053.563922993 SOL**. These are different measures: network fees, routing transfers, tips and account effects must be reconciled before equating either to an economic sale price. The gross figure sums receipts into one audited account, not every intermediate transfer in the route. `asset_disposal.csv` gives all four full signatures and program addresses.

20:35:35 UTC: disposal of the received ZesMG… mint balance yielded gross WSOL receipts of **122.213570003**, with a native wallet increase of **122.212870496 SOL**.

20:35:41 UTC: the receiving wallet's **7,859.975842 USDC** was debited and **64.925550449 SOL** arrived from `Grr9WnZdcetQywtFXog81UhqmnJyvFhb4AT3ipw44mZP`. That address signed and paid the network fee; the receiving wallet was not a transaction signer. This establishes execution roles in this transaction, not shared beneficial ownership. Protocol identity and authorization mechanism remain UNRESOLVED.

### Privacy Cash deposits

Ten successful `Transact` calls invoke `9fhQBbumKEFuXtMBDw8AaQyAjCorLGJQiS3skWZdQyQD`, matching the project's published mainnet program ID. Inner System Program transfers move funds from the receiving wallet into pool account `4AV2Qzp3N4c9RfzyEbNZs2wqWfW4EwKnnxFAZCndvfGh`. Exact total **13,240.973780900 SOL**.

| UTC on 6 October | SOL deposited |
|---|---:|
| 20:36:06 | 550 |
| 20:39:06 | 1,000 |
| 20:41:15 | 1,000 |
| 20:44:38 | 1,000 |
| 20:47:25 | 1,666 |
| 20:50:20 | 1,666 |
| 20:52:15 | 1,700 |
| 20:55:03 | 1,700 |
| 20:58:40 | 1,700 |
| 21:00:54 | 1,258.973780900 |

All signatures are preserved in `privacy_cash_deposits.csv`. Each transaction charges 0.000205000 SOL network fee plus 0.001391920 SOL allocated to two new accounts. The final captured receiving-wallet balance is **0.006403163 SOL**, an incident-time receipt value, not a current live balance.

The first BP disposal is co-signed by the receiving wallet and `sighWH8KaiT7QhtV4w29ReVF8kG6D5yG3EQP1KYyGVF`. This is CONFIRMED cooperation within that transaction; the second signer's protocol role and human identity are UNRESOLVED. The affected wallet and receiving wallet do not co-sign any of the 28 captured receipts. This scoped negative does not establish separate beneficial ownership.

## C. New SUPPORTED findings

The two starting-wallet associations with Frogman are supported by public attribution sources, without independently recovered proof of ownership. The ZesMG… token's public listing supports Just a Backpack as its name. BP disposal programs include the known Jupiter address and two other exact program IDs; names for those other routers remain provisional until matched to primary technical documentation. Observable program IDs are CONFIRMED regardless of naming uncertainty.

The public incident timing is broadly consistent with the Solana receipts. Frogman's approximate 04:30 statement is not substituted for the earlier exact transaction time. His self-reported absence of an obvious phone/mail breach does not eliminate those attack vectors.

## D. UNRESOLVED questions

EVM first outflow, all MarsCoin/Cash Cat disposals, the remaining reported assets, swap USD valuation, slippage, receiving chains, bridge fills, current balances, identity, beneficiary, access method and any forensic device results. SIM swap, email, malicious signature/dApp, browser/session, QR, physical access, WiFi and conference involvement remain individually UNRESOLVED. No theory is established by the routing pattern.

See `unresolved_questions.md` and `public_claim_tests.csv`.

## E. Provenance breakpoints

1. **Intact token path:** the BP transfer into the receiving token account and its four debit transactions are deterministically recorded, without evidence here of additional BP funding.
2. **Mixed balances:** third-party tiny USDC transfers reached the receiving account, totaling 0.001200 USDC before its conversion. A third-party transfer of 0.000001000 SOL arrived at 20:16:24 UTC. Incoming unrelated-token activity also appears at 20:23:21. These are preserved, not silently assigned to the incident. Amounts and address similarity do not establish their purpose or operator. The pool total is the confirmed wallet-to-pool total; it is not a claim that every lamport derives exclusively from Frogman.
3. **Broken private linkage:** provenance reaches each Privacy Cash deposit. No deterministic withdrawal recipient is established. Pool withdrawal history was not comprehensively scanned in this run. A public analyst's negative withdrawal scan is CLAIMED, not our independently verified result.
4. **EVM not reconstructed:** bridge and collector boundaries are candidate boundaries only. A bridge deposit does not establish its destination without a verified message/order/fill link. Do not describe any EVM path as intact from this record.

No probabilistic withdrawal attribution is made.

## F. Highest-priority next nodes

1. Recover transaction history for the affected EVM address on Robinhood Chain, Ethereum, BNB Chain and other publicly indicated chains; identify chain IDs from receipts rather than address labels. Test the candidate `0x427C…bA83` independently.
2. Reproduce the EVM 362.26 ETH ingress and every alleged exit with hashes, contract IDs and bridge order/fill identifiers. Priority: Relay and the collector, then Mayan reconciliation.
3. Examine `Grr9…4mZP` and program `61DFfeTKM7trxYcPQCM78bJ794ddZprZpAwAnLiwTpYH` for the USDC conversion authority mechanism; protocol-level fee payer is not ownership proof.
4. Verify Token-2022 mint extensions for ZesMG… and identify the failed-transfer mint.
5. Acquire protocol response/withdrawal evidence only where defensible linkage is available. No withdrawal match by amount alone.

## G. Public claims not reproduced

The EVM exits, 37 ETH collector, 4 ETH live hold and EVM routing total remain CLAIMED with transaction reproduction UNRESOLVED. Claim figures sum to **362.25 ETH**, 0.01 less than 362.26; rounding and gas may account for this, but are not verified. The Mayan detail lists 22.5 + 10.25 + 1.999 = **34.749 ETH**, consistent with a rounded 34.75 headline. The earlier commentary incorrectly treated the 1.999 ETH as additional beyond that headline; this is corrected here.

The public Relay quoted fill amounts 100,542 + 91,284 + 91,353 total **283,179**, against a displayed 283,180 USDC. No underlying exact fill values were obtained; this is a rounded-summary reconciliation question, not proof of incorrect tracing.

The rounded 13,241 SOL deposit claim **was independently reproduced** as 13,240.973780900 SOL. The negative withdrawal-scan claim was not reproduced. No exchange deposit, freeze, return, recovery or law-enforcement action was independently established in searched case-specific sources. A search result describing a Chainflip return in a separate Bitget incident was excluded.

## H. Publication recommendation

Not mature enough for a complete all-chain forensic account. The Solana transfer/disposal/deposit subsection is reproducible, subject to the stated attribution and mixed-balance limits. Complete EVM reconstruction and cross-chain reconciliation before publishing a comprehensive money-trail article. No final article has been written.

Attention is not evidence. Visibility is not evidence of relevance. A transaction path is not proof of identity. A fund-flow reconstruction is not proof of compromise method.
