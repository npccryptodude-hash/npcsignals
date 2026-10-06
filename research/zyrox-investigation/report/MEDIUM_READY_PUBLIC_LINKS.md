# ZYROX: How the Launch Was Structured, How the Sell-Off Unfolded, and Where the Money Went

**NPCsignals | Verified draft v1.1 | 6 October 2026**  
**Evidence basis:** ZYROX technical report v0.114, ledger through U453. All times are UTC. This draft uses the existing verified record; it adds no research and changes no frozen findings.

## 1. Executive Summary

ZYROX launched on Solana on 30 September 2026. NPCsignals examined its promotional claims, early wallet activity, token consolidation, sales and the subsequent movement of sale proceeds. The investigation distinguishes transactions that can be verified directly from broader explanations that remain supported or unresolved.

The verified sale inventory contains **17 case-relevant sellers, 35 sales and 606.331808740 SOL/WSOL in proceeds**. SOL is Solana’s native asset; WSOL is its wrapped token form, used in trading. The first case-related sale occurred in the same timestamp-second as the launch, two slots later. All 35 documented case sales were completed within 40 minutes and 22 seconds.

Jointly signed transactions and the consolidation of tokens from 64 source wallets into one selling wallet demonstrate specific instances of operational cooperation. Taken together with the funding, routing and selling record, they support the assessment **SUPPORTED COORDINATED OPERATIONAL STRUCTURE**. They do not establish a common human operator or common ownership of the wallets.

All verified sale proceeds passed through mixed seller balances. A conservative accounting reconstruction establishes a **597.487092059 SOL PARTIAL / RE-ESTABLISHED minimum component** in documented onward flows. This is a lower bound on proceeds reaching specified wallet or routing destinations, not an identification of who ultimately benefited. **0 SOL is attributed to a finally identified beneficiary.**

Several promotional claims are materially at odds with the observed record: majority supply locking was not supported by technical lock evidence during the examined launch period; the $10 million target was not reached within the available price history; and rapid, substantial case-related selling did not support the operational reading of “no pump and dump.” Other claims remain limited by missing original posts, recipient records or allocation agreements.

The report does not establish intent to deceive, a common beneficial owner, a definitive ZYROX–Kytro control link or the legal elements of fraud. Its conclusions concern observable activity and the limits of attribution. [1](https://github.com/npccryptodude-hash/npcsignals/blob/64ac82545e900cf87f5bbbfaea31b00a68e8839b/research/zyrox-investigation/evidence/ZYROX_Devsold_verification_v0_2.md)

## 2. What ZYROX Promised

The strongest preserved claim sources are screenshots showing the name Zyrox and the handle **@Zyrox0x**. One, archived as [IMG_4205.jpeg](https://github.com/npccryptodude-hash/npcsignals/blob/64ac82545e900cf87f5bbbfaea31b00a68e8839b/research/zyrox-investigation/evidence/claims/IMG_4205.jpeg), contains the statements:

> “No rugpull, no pump and dump!”

> “Majority of the supply will be locked!”

> “Will drop early ca at 10k mc will push it to 10 M Mc guaranteed!”

Another, [IMG_4204.jpeg](https://github.com/npccryptodude-hash/npcsignals/blob/64ac82545e900cf87f5bbbfaea31b00a68e8839b/research/zyrox-investigation/evidence/claims/IMG_4204.jpeg), invites address submissions:

> “Drop $SOL Addresses, Airdropping Some Of The Supply 👇🏻”

These are **SCREENSHOT** sources. The preserved images document the visible account and wording, but the original post IDs and absolute posting times have not been verified. Archive timestamps are file-preservation times, not post timestamps. Neither image displays the full token mint or creator-wallet address. Their connection to this case comes from the documented ZYROX launch context; they do not independently identify the person operating the creator wallet.

“No presale” and “No KOL allocation” have weaker source support. They appear in an earlier analytical case record as a paraphrase, not in a recovered original post or in the two screenshots above. They are classified as **THIRD-PARTY CLAIM**, specifically an analytical handover rather than independent corroboration. KOL refers here to an influencer or promoter. The original claims remain unresolved.

The report therefore separates what the preserved account material visibly says from what earlier summaries report it as saying. No original primary post is substituted for a screenshot, and no analytical paraphrase is presented as a verified quotation by the account. [2](https://github.com/npccryptodude-hash/npcsignals/blob/64ac82545e900cf87f5bbbfaea31b00a68e8839b/research/zyrox-investigation/evidence/ZYROX_Devsold_verification_v0_2.md)

## 3. How the Launch Was Structured

The token examined is the Solana mint **FACvJMFBWQ1GYm9dgZ7XHvs85V1EcK2SqHf534kspump**, referred to below as FACv or ZYROX. A mint identifies the specific token; a matching name or ticker alone does not.

The creator wallet, abbreviated [**HZrAo**, created FACv and bought 100 million tokens](https://solscan.io/tx/5ubvNRPDbdXtHaiexB4zroZxUDFS9mwDmDwJ3HnvdGrxuiqxDDGsZnkjdAGVHysDZgiCFqVASoinDu1bADPAbowo) in the launch transaction. Other wallets made substantial purchases at or shortly after launch. Their principal roles were:

| Wallet alias | Documented role |
|---|---|
| HZrAo | FACv creator; bought 100 million tokens and later transferred them to G16 |
| Hp4q | Bought and sold 693.1 million tokens; participated in funding/routing and a joint authorization with Tmcg |
| Hrpa | Bought and sold approximately 26.9 million tokens |
| Tmcg | Bought 137,587,563.532596 tokens and sold them in 16 transactions |
| G16 | Bought tokens, received consolidation transfers and executed the largest individual case sale |
| P1 / CUo7 | Documented program/routing infrastructure involved in funding or forwarding; not identified owners of the participating wallets |

Funding records place relevant wallets in activity before launch. Within the available indexed history, the documented first observed funders of HZrAo, Hp4q, Hrpa, G16 and Tmcg were different. Tmcg’s first observed funding was a 0.040001000 SOL transfer to a zero balance at 17:15:51. Its later trade balance was funded through P1. These are separate findings: initial wallet funding and funding for a trade need not have the same source.

A wallet’s first funder is not automatically its creator or controller. Likewise, a program supplying funds to a transaction does not thereby own the recipient wallet. The record contains concrete funding and routing relationships, but those relationships do not by themselves reveal the people behind the keys.

Early purchases establish that the wallets traded at launch. They do not alone establish private access, a presale or a common operator. [3](https://github.com/npccryptodude-hash/npcsignals/blob/64ac82545e900cf87f5bbbfaea31b00a68e8839b/research/zyrox-investigation/evidence/ZYROX_Devsold_verification_v0_2.md)

## 4. The First 60 Seconds

The opening sequence is important because substantial selling began almost immediately. It can be reconstructed without assigning a motive to the sellers.

| Time on 30 September 2026 | Documented event |
|---|---|
| **17:18:06** | FACv creation and HZrAo’s 100-million-token creator buy |
| **17:18:06** | [Hp4q’s first sale, two slots after launch](https://solscan.io/tx/5jRjC6ULUHNd88x2gazxAUGcjA4yCGAqusvbqXHNkh7pASuSsyB8wn6CRd17wZ9D3rUkeYoxLd2qQopFgCinMi7T): 278,149,496.731053 tokens for 59.510477626 WSOL |
| **17:18:06** | [Tmcg’s purchase, after the first Hp4q sale](https://solscan.io/tx/3oj1pmRLg9F7LvBjJBjwXSLuvWnMDPf2p31yGKyfm6b7J9efz6xQJjcBQPdrQoozM1hLVaLjyHA8JZRB8wdfBQs2) in transaction order |
| **17:18:09** | Hp4q and Hrpa had completed three sales, receiving **142.089113597 SOL/WSOL** in total |
| **17:18:10–17:19:03** | [Tmcg executed its 16 documented sales](https://solscan.io/tx/2jzwkic7dKaLvgM81VvmjXtKoZykdwqDe4FTzzNknMBZDY5XLePFSbzKLcvfWYinbUhtjHWQ96iamMi7vCa4rqjK) |
| **17:19:03** | By 57 seconds after launch, 19 case sales had received **251.752785673 SOL/WSOL** |

A Solana slot is a unit of blockchain ordering. Transactions can share the same second-level timestamp while occurring in different slots or at different positions within a block. “Same second” therefore does not mean simultaneous execution, and the record does not provide an exact millisecond delay.

The timing establishes rapid early selling. It does not establish why the wallets sold, whether they followed one plan or whether their operators intended to mislead buyers. It also places these early sales **before** the highest documented aggregator-candle minute, rather than depicting all selling as an exit after one price peak. [4](https://github.com/npccryptodude-hash/npcsignals/blob/64ac82545e900cf87f5bbbfaea31b00a68e8839b/research/zyrox-investigation/evidence/ZYROX_Devsold_verification_v0_2.md)

## 5. Consolidation and Control Signals

A later stage of the launch involved a different, directly observable form of cooperation: tokens were collected into G16.

At 17:58:26–17:58:27, **64 source wallets transferred 581,307,162.351855 FACv to G16 in 11 transactions**. This included HZrAo’s 100 million tokens. The source keys authorized transfers from their respective token accounts. G16 participated as fee payer and co-signer in relevant consolidation transactions.

A token authority is the key or program permitted to authorize actions on a token account. A co-signer supplies an additional required signature. A fee payer pays the transaction fee. These roles can appear together, but they are not interchangeable descriptions of ownership.

Two core-wallet relationships are confirmed as **co-authorization**:

- [**HZrAo–G16:**](https://solscan.io/tx/29VDE2VcR724cRjzCBoWCFuWZLGrD7ySQiuMkwpgTVvsndw13TeHohwmhW1oM4jHTTLytDoD9QH7jKRP6nKY4Gsr) joint authorization in the documented consolidation event, with G16 paying the fee.
- [**Hp4q–Tmcg:**](https://solscan.io/tx/AgMVBsknEvB22wZFR2zqSbGtoJxxsdybi71ZQeH2BGSYC1qYUvnWoiCkmjYrvAL8HTkdqSgrqE6rwz6piJeh38u) co-signing in the finalized D06 tip/RecordMevBuy transaction, with Hp4q paying the fee and funding its own System transfer tips. Tmcg was a signer and the wallet account in the RecordMevBuy instruction. This event did not delegate token or stake authority over either wallet.

These findings show cooperation on particular actions. They do not show that one wallet could unilaterally control the other, or that one person held both keys.

The frozen comparison of six core wallets, including the separate GFKG creator CAxTx, found **no CONFIRMED CONTROL OVERLAP** between different core wallets. It found two co-authorization pairs, one shared-funder pair and routing/service overlap for the remaining pairs. CAxTx’s co-authorization with GFKG-related wallets remains a separate control context; GFKG economics are not included in the FACv sale totals.

The appropriate overall assessment is **SUPPORTED COORDINATED OPERATIONAL STRUCTURE**. Specific collaborative transactions are confirmed. A broader coordinated launch and sell-off is supported by the combined record, while common ownership and a jointly pre-planned launch remain unresolved. [5](https://github.com/npccryptodude-hash/npcsignals/blob/64ac82545e900cf87f5bbbfaea31b00a68e8839b/research/zyrox-investigation/evidence/ZYROX_Devsold_verification_v0_2.md)

## 6. The Sell-Off

The frozen case-relevant seller inventory contains:

| Measure | Verified total |
|---|---:|
| Seller wallets | **17** |
| FACv sales | **35** |
| ZYROX gross sold | **1,527,248,306.725914** |
| SOL/WSOL proceeds received | **606.331808740** |
| Time from launch to the last case sale | **40 minutes, 22 seconds** |

“Gross sold” measures the tokens exchanged across the recorded sales. It is not a count of distinct tokens. Tokens sold into a market can be bought and sold again, so total trading volume can exceed the original supply. The 1.527 billion figure must not be described as 152.7% of unique supply being sold.

The largest individual sale was G16’s at **17:58:28**:

[**581,529,004.875567 ZYROX → 145.975602514 WSOL.**](https://solscan.io/tx/2wyYPRdcJ3TGT7JFC9Yqg5hytrU6cp8SeanzcLG9NFKDpBt6F4yja5mWJdmiggiki21cBbJQR8EyiUVRrRYFPued)

That sale alone demonstrates that an amount equivalent to approximately 58.15% of the initial one-billion-token supply was spendable at that point. It followed the consolidation described above.

The proceeds total is sale revenue, not net profit or the seller’s net change in native SOL balance after all transaction costs. It does not deduct acquisition costs and does not establish how much any person earned. Nor does it necessarily represent economically independent underlying capital across every trade. HZrAo is not a direct seller in this inventory: its tokens were transferred to G16. That transfer cannot be described as personal realized profit for an identified creator. [6](https://github.com/npccryptodude-hash/npcsignals/blob/64ac82545e900cf87f5bbbfaea31b00a68e8839b/research/zyrox-investigation/evidence/ZYROX_Devsold_verification_v0_2.md)

## 7. Price Behaviour

To compare price observations consistently, the investigation uses **initial-supply-normalized fully diluted valuation**, or FDV: token price multiplied by the initial supply of one billion tokens. This is a valuation metric, not the cash available to sellers and not a reconstructed circulating market capitalization.

The highest documented aggregator candle implies approximately **$516,492 FDV** during **17:23:00–17:23:59**. An aggregator candle summarizes price observations over an interval. The exact transaction at the lifetime peak has not been established, so this figure is not presented as a fully verified lifetime ATH transaction.

Within the available price history, the token did not reach the promoted $10 million target. The highest documented normalized value was about 5.16% of that target. No enforceable mechanism guaranteeing the target was verified.

G16’s largest sale at 17:58:28 **coincided with an approximately 99.03% decline in the pool’s reserve-based marginal price within the same transaction**. Here, the reserve-based marginal price is the pool’s WSOL-to-FACv reserve ratio, measured before and after the transaction. It is not the seller’s average execution price or a guaranteed executable price for a finite trade. The pool’s WSOL reserve also fell by approximately 93.76%.

These transaction-level changes are consistent with significant sell pressure. They are not evidence that all pool liquidity was withdrawn: 9.815661462 WSOL remained after the transaction. A large swap and a withdrawal of liquidity-provider assets are different events.

The price proxy for **18:18:06**, one hour after launch, implies approximately **$5,313 FDV**, using the close of the **18:17:00–18:17:59** aggregator candle. It is not an exact price at the target second. The broader price path included rebounds and intervening trades. The report therefore does not attribute the entire market decline to one wallet or claim a complete causal reconstruction of the market. [7](https://github.com/npccryptodude-hash/npcsignals/blob/64ac82545e900cf87f5bbbfaea31b00a68e8839b/research/zyrox-investigation/evidence/ZYROX_Devsold_verification_v0_2.md)

## 8. Where the Money Went

The investigation starts its money accounting with actual sale receipts, then examines the WSOL accounts, conversion back to native SOL and subsequent transfers. Converting WSOL back to SOL is referred to as **unwrapping**.

The central limitation arises when proceeds enter a wallet that also contains other funds. From that point, a later payment cannot automatically be treated as ZYROX proceeds merely because its amount or timing looks similar.

| Measure | SOL or SOL-equivalent proceeds |
|---|---:|
| Verified sale proceeds | **606.331808740** |
| CLEAN onward provenance after seller-level mixing | **0** |
| Proceeds passing through mixed seller balances | **606.331808740** |
| Conservative PARTIAL / RE-ESTABLISHED minimum | **597.487092059** |
| Attributed to a finally identified beneficiary | **0** |

Zero CLEAN does not mean that the sale receipts or unwrap destinations are unknown. Those roots are documented. It means no CLEAN onward amount was established after unwrap into seller custody for the frozen 17-seller inventory. It is not a universal claim about unavailable transactions.

Mixing can still permit a conservative minimum to be established when the full balance accounting constrains what could have happened. If the documented outflow exceeds the funds available from other sources, some sale proceeds must be included in that outflow. The calculation can establish that minimum without identifying particular lamports or assuming that the oldest funds were spent first.

Applied seller by seller, the frozen accounting establishes **597.487092059 SOL** as a minimum component in documented onward flows. This is a **subset of the mixed proceeds**, not additional revenue and not a restoration of clean provenance. Each seller’s combined lower bound is counted once, rather than adding overlapping bounds at successive routing nodes.

The principal documented destinations are:

| Documented receiving or routing category | Conservative category minimum, SOL |
|---|---:|
| 6cn | 188.148898454 |
| P1 / CUo7 / 5B3 | 240.989588659 |
| F1dC | 148.663295380 |
| HFAc | 7.723304078 |
| Unidentified intermediate wallets | 8.563794158 |
| **Category minima combined** | **594.088880729** |
| Minimum established jointly but not assignable to an individual category | 3.398211330 |
| **Global minimum** | **597.487092059** |

These are minima at documented receiving or routing points, not an exact distribution of the whole proceeds total. P1/CUo7/5B3 is a grouped routing boundary; forwarding the same component through another node does not create additional proceeds. The jointly established remainder cannot safely be placed in a particular category.

An endpoint here means the last receiving point that the evidence can support, not necessarily the final destination. Attribution stops at mixed collectors or where exact onward allocation becomes unresolved. Later outgoing payments from those collectors are not assigned back to FACv.

**0 SOL is attributed to a finally identified beneficiary.** This is a statement about the absence of verified beneficiary attribution, not a claim that nobody benefited. Beneficial ownership remains unresolved. [8](https://github.com/npccryptodude-hash/npcsignals/blob/64ac82545e900cf87f5bbbfaea31b00a68e8839b/research/zyrox-investigation/evidence/ZYROX_Devsold_verification_v0_2.md)

## 9. Promises vs Observed Facts

The following classifications retain the frozen claim findings. “Not found” and “not verified” are limited to the reviewed evidence; they do not prove universal absence.

| Claim | Observed evidence | Status |
|---|---|---|
| No rugpull | Screenshot wording is documented. Significant sales and reserve-price declines are documented; liquidity-provider withdrawal is not established by those swaps. The source does not define “rugpull.” | **SOURCE CLAIM DOCUMENTED; BEHAVIOURAL CONTRADICTION / SUPPORT UNRESOLVED** |
| No pump and dump | Rapid early selling, substantial case-related sales, consolidation and significant transaction-level price declines. | **NOT SUPPORTED BY OBSERVED BEHAVIOUR; INTENT UNRESOLVED** |
| Majority supply locked | No relevant technical lock verified; more than half the initial supply was documented as transferable at several launch checkpoints. | **NOT SUPPORTED BY ON-CHAIN LOCK EVIDENCE** during the examined period |
| $10M market cap guaranteed | Highest documented normalized aggregator-FDV approximately $516,492; no enforceable guarantee verified. | **NOT ACHIEVED** within coverage; **NO GUARANTEE MECHANISM VERIFIED** |
| Airdropping some of the supply | No verified delivery from the examined case sources; no verified submission/recipient list. Consolidation and sales are not airdrops. | **NO VERIFIED DELIVERY; UNRESOLVED DUE TO SOURCE/RECIPIENT GAP** |
| No presale | No private pre-launch allocation verified in the examined record. Early purchases or prefunding alone are not presale evidence. | **NO VERIFIED PRESALE FOUND; claim status UNRESOLVED** |
| No KOL allocation | No publicly bound promoter wallet verified as receiving an allocation without a documented purchase. | **NO VERIFIED KOL ALLOCATION FOUND; claim status UNRESOLVED** |

The strongest discrepancies concern transferable supply versus the lock promise, the documented price level versus the $10 million target, and rapid substantial selling versus the operational reading of “no pump and dump.” The last assessment concerns observable behaviour, not a legal or intent-based finding of market manipulation.

The airdrop, presale and KOL findings should not be converted into categorical claims of non-delivery or undisclosed allocation. Their source and recipient gaps remain material. Promotion before launch is supported by the archived material; promotion continuing during the sales has not been verified with absolute post timestamps. [2](https://github.com/npccryptodude-hash/npcsignals/blob/64ac82545e900cf87f5bbbfaea31b00a68e8839b/research/zyrox-investigation/evidence/ZYROX_Devsold_verification_v0_2.md)

## 10. What the Evidence Supports

### CONFIRMED

The record confirms rapid early selling, 35 actual case-related sales, 606.331808740 SOL/WSOL in receipts, specific co-authorization events and the consolidation of tokens from 64 source wallets into G16. It also confirms particular money-flow transactions. The conservative lower bounds at documented onward destinations are verified accounting deductions from the frozen balance and transaction record; they are not exact allocations or ownership findings.

The boundaries of each fact matter. A signature confirms authorization of a particular action. A transfer confirms movement between accounts. Neither fact alone identifies a person or proves common ownership.

### SUPPORTED

The combined record supports a **coordinated operational structure**. This assessment rests on concrete jointly authorized actions, the consolidation network and the documented funding/routing and selling sequence, rather than launch timing alone.

It also supports a material mismatch between several promotional claims and observed behaviour. That conclusion is strongest for the lock promise, the $10 million target and the bounded behavioural test of “no pump and dump.” It is weaker where original wording or delivery evidence is missing.

### UNRESOLVED

The record does not establish a common human operator, common beneficial owner, final beneficiary, intent to deceive or legal fraud. A definitive ZYROX–Kytro control link also remains unresolved.

Specific cooperation could occur between separately owned wallets. Automated trading or shared execution services could also explain parts of the activity. These are possible alternatives, not verified explanations. Their relevance is that operational cooperation does not uniquely establish one owner or one prior plan. [1](https://github.com/npccryptodude-hash/npcsignals/blob/64ac82545e900cf87f5bbbfaea31b00a68e8839b/research/zyrox-investigation/evidence/ZYROX_Devsold_verification_v0_2.md)

## 11. What Remains Unresolved

Five questions remain material to any stronger assessment:

1. **Who operated the wallet keys, and can they be tied to @Zyrox0x?** The creator role is established on-chain; the human identity and primary public address binding are not.
2. **Who was the economic owner and final beneficiary?** Proceeds can be bounded to receiving and routing points, but no ultimate beneficiary has been identified.
3. **Was the launch and sell-off jointly pre-planned?** Specific collaborative transactions are documented. A shared plan covering the whole sequence is not.
4. **Is there direct evidence of deliberate deception?** Discrepancies between promotion and observed activity do not, by themselves, establish state of mind.
5. **Can original claims, private allocation agreements and airdrop delivery be documented?** These gaps affect the strength and scope of several claim findings.

Missing exact price-peak transactions, complete historical supply information and unavailable archival records add technical limits. Those limits do not erase the sales already verified, but they constrain claims about the entire market history and the people behind it. [1](https://github.com/npccryptodude-hash/npcsignals/blob/64ac82545e900cf87f5bbbfaea31b00a68e8839b/research/zyrox-investigation/evidence/ZYROX_Devsold_verification_v0_2.md)

## 12. Methodology and Evidence Standards

**CONFIRMED** means that the stated fact is directly supported by the verified record at its defined scope. **SUPPORTED** means that several concrete observations support an explanation without establishing it conclusively. **UNRESOLVED** means the available evidence cannot settle the question. These labels apply to individual claims, not to the case as one binary verdict.

The seller baseline counts unique sale transactions. Token transfers, consolidation, migration, routing and failed transactions are not counted as sales. A seller is included as case-relevant through documented case signals; this inventory is not a claim to cover every ordinary market seller.

Transaction order uses slots and transaction positions where second-level timestamps are insufficient. Token amounts, proceeds accounts and unwrap destinations come from the frozen transaction inventory. Available indexed history carries an archive-RPC limitation: unavailable older records or historical account states cannot be treated as negative evidence.

**Strict provenance** requires evidence that funds can be carried forward from their source. Once balances mix, timing, similar amounts or a shared collector do not establish exact allocation. A lower bound can be re-established only where balance and transaction accounting constrain it. Such a bound is not clean provenance, and it does not authorize attribution of later payments from a mixed collector.

Co-signing establishes joint authorization, not one owner. Funding establishes a source relationship, not control over the recipient. Routing through the same service or program establishes a technical relationship, not shared ownership. Public identity requires a concrete address binding; posting a token contract address is not proof of owning its creator wallet.

Price observations also retain their source distinctions. Aggregator candles, reserve-based marginal prices and execution prices are different measures. The report uses initial-supply-normalized FDV for consistent comparison, with historical supply and exact peak coverage explicitly limited.

Screenshots retain their source class. An archived screenshot with visible wording is not silently upgraded to a recovered original post, and an analytical reference to a claim is not treated as an authenticated statement by the promoter. The technical report and ledger remain the evidence base for the reader-facing account. [1–8](https://github.com/npccryptodude-hash/npcsignals/blob/64ac82545e900cf87f5bbbfaea31b00a68e8839b/research/zyrox-investigation/evidence/ZYROX_Devsold_verification_v0_2.md)

## 13. Conclusion

The evidence confirms specific operational cooperation, rapid case-related selling and token consolidation. It supports a broader coordinated operational structure and identifies multiple material discrepancies between promotional claims and observed on-chain behaviour.

Across the verified case inventory, 17 sellers completed 35 sales for 606.331808740 SOL/WSOL within 40 minutes and 22 seconds. Conservative accounting establishes a 597.487092059 SOL minimum component in documented onward flows, while final beneficiary attribution remains absent.

The record does not establish a common human operator, a common beneficial owner, a final beneficiary, intent to defraud or the legal elements of fraud. The defensible conclusion is therefore specific: operational cooperation and a rapid sell-off are documented, broader coordination is supported, and identity, ownership and intent remain unresolved.

### Evidence references

All references below point to the unchanged **[ZYROX_Devsold_verification_v0_2.md](https://github.com/npccryptodude-hash/npcsignals/blob/64ac82545e900cf87f5bbbfaea31b00a68e8839b/research/zyrox-investigation/evidence/ZYROX_Devsold_verification_v0_2.md), v0.114 / U453**, which contains the transaction manifests and ledger. They are section references to the technical evidence base, not claims of newly recovered public sources.

- **[1](https://github.com/npccryptodude-hash/npcsignals/blob/64ac82545e900cf87f5bbbfaea31b00a68e8839b/research/zyrox-investigation/evidence/ZYROX_Devsold_verification_v0_2.md)** v0.114, “Control / coordination assessment,” “SCAM / COORDINATION — evidensmatrise,” “Fem materielt uløste spørsmål” and “Money assessment — dokumentert videreføring, ikke beneficiary.” For the underlying amounts and chronology, use [4](https://github.com/npccryptodude-hash/npcsignals/blob/64ac82545e900cf87f5bbbfaea31b00a68e8839b/research/zyrox-investigation/evidence/ZYROX_Devsold_verification_v0_2.md), [6](https://github.com/npccryptodude-hash/npcsignals/blob/64ac82545e900cf87f5bbbfaea31b00a68e8839b/research/zyrox-investigation/evidence/ZYROX_Devsold_verification_v0_2.md) and [8](https://github.com/npccryptodude-hash/npcsignals/blob/64ac82545e900cf87f5bbbfaea31b00a68e8839b/research/zyrox-investigation/evidence/ZYROX_Devsold_verification_v0_2.md).
- **[2](https://github.com/npccryptodude-hash/npcsignals/blob/64ac82545e900cf87f5bbbfaea31b00a68e8839b/research/zyrox-investigation/evidence/ZYROX_Devsold_verification_v0_2.md)** v0.113, “Samlet claim-tabell,” for the seven frozen classifications and source quality; v0.108, “Checkpoint og claim-kilde,” and v0.109, “Claim-kilde,” for IMG_4205 wording; v0.110, “1. Best dokumenterte claim-kilde,” for IMG_4204 wording; v0.111, “1. Kildekritikk — to forskjellige påstander,” for E15 and unresolved presale/KOL originals. Source images: [IMG_4204.jpeg](https://github.com/npccryptodude-hash/npcsignals/blob/64ac82545e900cf87f5bbbfaea31b00a68e8839b/research/zyrox-investigation/evidence/claims/IMG_4204.jpeg) and [IMG_4205.jpeg](https://github.com/npccryptodude-hash/npcsignals/blob/64ac82545e900cf87f5bbbfaea31b00a68e8839b/research/zyrox-investigation/evidence/claims/IMG_4205.jpeg).
- **[3](https://github.com/npccryptodude-hash/npcsignals/blob/64ac82545e900cf87f5bbbfaea31b00a68e8839b/research/zyrox-investigation/evidence/ZYROX_Devsold_verification_v0_2.md)** v0.100, “First-funder test / dekningsgap,” for the recorded funders of HZrAo, G16, Hp4q and Hrpa; v0.101, U447 first-funding record and first-funder distinctions, for Tmcg’s subsequently resolved funding gap; v0.111, “3. Mint/create og første handler” and “4. Case-wallets — kjøp versus mottak uten kjøp,” for launch purchases; v0.114, “Kronologisk case-fortelling,” part A, for P1 trade funding versus wallet funding. The historical Tmcg gap in v0.100 is superseded by v0.101, not carried forward.
- **[4](https://github.com/npccryptodude-hash/npcsignals/blob/64ac82545e900cf87f5bbbfaea31b00a68e8839b/research/zyrox-investigation/evidence/ZYROX_Devsold_verification_v0_2.md)** v0.112, “Konsistent UTC-tidslinje” and “Salgsadferd — frozen tall”: launch slot 452029524/index 1330; first Hp4q sale slot 452029526/index 608; Tmcg buy index 610; three-sales subtotal at +3 seconds and 19-sales subtotal at +57 seconds.
- **[5](https://github.com/npccryptodude-hash/npcsignals/blob/64ac82545e900cf87f5bbbfaea31b00a68e8839b/research/zyrox-investigation/evidence/ZYROX_Devsold_verification_v0_2.md)** v0.100, “Klassifikasjonsregler / full 6×6 matrix,” “Alle tredje wallet-nøkkel-overlaps” and “Konklusjon / ledger / neste target”; v0.98, D06 role description, for the Hp4q/Tmcg tip/RecordMevBuy event; v0.110, “Prioriterte sources” and the 64-source consolidation manifest, for amounts and direction; v0.95 for the separate CAxTx/GFKG co-authorization context. D12 signature: 29VDE2VcR724cRjzCBoWCFuWZLGrD7ySQiuMkwpgTVvsndw13TeHohwmhW1oM4jHTTLytDoD9QH7jKRP6nKY4Gsr. D06 signature: AgMVBsknEvB22wZFR2zqSbGtoJxxsdybi71ZQeH2BGSYC1qYUvnWoiCkmjYrvAL8HTkdqSgrqE6rwz6piJeh38u.
- **[6](https://github.com/npccryptodude-hash/npcsignals/blob/64ac82545e900cf87f5bbbfaea31b00a68e8839b/research/zyrox-investigation/evidence/ZYROX_Devsold_verification_v0_2.md)** v0.71, “FACv CASE-RELEVANT SELLER BASELINE — FROZEN” and its 35-sale manifest, for 17 sellers, gross tokens and proceeds; v0.112, “Salgsadferd — frozen tall,” for the largest G16 sale and +40m22s completion. Largest-sale signature: 2wyYPRdcJ3TGT7JFC9Yqg5hytrU6cp8SeanzcLG9NFKDpBt6F4yja5mWJdmiggiki21cBbJQR8EyiUVRrRYFPued.
- **[7](https://github.com/npccryptodude-hash/npcsignals/blob/64ac82545e900cf87f5bbbfaea31b00a68e8839b/research/zyrox-investigation/evidence/ZYROX_Devsold_verification_v0_2.md)** v0.109, “Definisjon og marked,” “ATH-test” and “Dekning / varighet,” for normalized FDV, the 17:23 candle high, +60-minute proxy and coverage; v0.112, “Pris / reserve-respons,” G16 row at 17:58:28, for reserve-based price and WSOL-reserve percentage changes.
- **[8](https://github.com/npccryptodude-hash/npcsignals/blob/64ac82545e900cf87f5bbbfaea31b00a68e8839b/research/zyrox-investigation/evidence/ZYROX_Devsold_verification_v0_2.md)** v0.89, “FACv SALE-PROCEEDS PROVENANCE — FROZEN”: “Én samlet seller-tabell,” “Manglende Tmcg joint-bound — beregnet kun fra eksisterende regnskap,” “Globale summer og ikke-dobbelttelling,” “Hvor minimumskomponenten kan dokumenteres — category bounds, ikke eksakt fordeling” and “Freeze, evidens og ledger.” These sections establish the joint bound, category minima, joint-only remainder, 0 CLEAN and 0 identified final-beneficiary attribution; individual seller accounting remains in v0.72–v0.88.

