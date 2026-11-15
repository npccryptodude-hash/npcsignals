# B's funding and the two bridge deposits

Canonical BNB USDT: 0x55d398326f99059ff775485246999027b3197955, 18 decimals. B: 0xe5686aae44d392aa6a0637fd38393859502f8667. S1: 0x0067cc2416f792cf0ec5629f5506324ac508f859. A: 0xd5fbda4c79f38920159fe5f22df9655fde292d47.

## First bridge

| UTC, October 13 | Block | Direct S1 → B amount | Full transaction hash |
| --- | --- | --- | --- |
| 16:14:31 | 127432896 | 315446.159624488300 USDT | 0xeb1fa312ebbb67c02ea851f01f3f9fcd215ba9fdda05e9d95e6446bf0e341a54 |
| 16:22:43 | 127433989 | 50211.089809526480 USDT | 0xffd2e281af7709dd8a15a47774a71eca2bc16fec067f1c28310bfb0c085e1405 |
| 16:24:30 | 127434225 | 7639.697926630939 USDT | 0x60bc674d4b2250d5aa01bf5a9d89e0d1f702873219c5a3fd2deb5e74b7469e8b |

Each succeeds, is initiated and fee-paid by S1, calls the canonical token directly, and has matching transfer(address,uint256) input and Transfer log. Receipts, transaction objects, block headers, hashes at transaction indices and recovered signatures agree. A separately accessed Binance RPC receipt corroborates the first payment's block/status/logs.

At block 127435561 B holds **373296.947360645719 USDT**. In block 127435562 it deposits **370000 USDT** in the already verified G010 transaction 0xb4e697fc1cb8406ca6e18ee3a1b4f975428e2642caa57076df5d9b166848c1b1. Closing state is **3296.947360645719 USDT**. The bounded canonical queries return only this B token debit in the bridge block. Thus the pre-block state and ordered events support the exact pre-transaction token balance, not merely a current balance.

The three S1 transfers are the complete observed funding set since the zero opening state. No single inbound amount alone equals or exceeds 370000. The ledger identifies the funding pool without assigning exclusive identity to fungible units.

## S1 upstream and prior behavior

S1 has historical account nonce 184438 at block 127199999, before the incident day. A selected successful direct payment of 299.994429116174300000 USDT at 12:11:04 on October 13, hash 0x950ad12176972dd4817193f530afdc19c517f0cf65861764eee985bdbf834c41, independently establishes prior BNB token activity. This is an already active source, not a newly created wallet inferred from its first B payment.

At block 127399999 S1 holds 150737.457476729472612980 USDT. A bounded log reconstruction through its first B payment gives: opening 150737.457476729472612980 + incoming 309709.045833346051352658 − outgoing 400619.885745775188358000 = closing 59826.617564300335607638 USDT. The closing value equals historical state. This includes the 315446.159624488300-USDT B payment once.

The largest incoming transfer in that bound is **150000 USDT** from **0xb4c10deb192b36374343af0cead0ff2a3b65cfb5** at **15:37:59**, block 127428024, transaction **0x9b2c7efebfb9360f8e1468c480e72674e750a0660dc4892df12fa0fa4f25666f**. The actual initiator is that same address, interacting directly with USDT. No swap or bridge occurs in this inspected receipt. The sender's preceding provenance and owner are not established. Do not call this deposit the exclusive source of the later B payments: S1 is a mixed pool with prior holdings, other inflows and other outflows.

The earlier intraday comparison, blocks 127400000–127429999, contains 63 canonical USDT outflows to 49 distinct recipients, totaling 83550.182842892018336000 USDT; maximum single outflow 30039.043168179440000000. The first B payment is larger than that sample maximum. The sample is a few hours, not a lifetime distribution or statistical anomaly score.

## Intervening flows and second bridge

B spends the first residual of 3296.947360645719 USDT into settlement contract 0x9008d19f58aabd9ed0d60971565aa8510560ab41 at 16:45:01, transaction 0xe4eea89ea32d675baa724d2e3926ffd3d4fbbe8d4f73ce381799bf9550a92347. It then receives **3947.417222165521700000 USDT** from S1 at 16:47:09 in **0xe609048f70d245909f8c4d6a641935fb71dc958fb4d85abbf311e6a0a2238169**, and spends that exact amount into the same settlement contract at 16:47:58 in **0xcda9343de4eb5ad1e96d210d3e215bdf55cb33fba1c5f3fe3a6456afbe6781d2**. Historical B state is zero after both debits. Solver/intermediary onward USDT transfers are preserved but not counted twice. No corresponding destination consideration is independently matched here; this is not a proven Ethereum DAI conversion path.

At **17:39:24**, block **127444208**, A directly sends B **336943.421822265793499428 USDT** in **0x7bf1dc151bd41f0e065869eb4798224a109fbd0fc09ae070ae067f3f9026264e**. This receipt is corroborated by a separately accessed BNB Chain RPC. A's balance before and after is the full amount and zero respectively. Its transaction nonce is zero. Direct archive state already shows the same full holdings at block 127199999, before October 13, and no canonical A events are returned in the bounded intervening queries. The earlier source of A's holdings is unresolved.

B is zero immediately before A's payment, holds exactly that payment before the second deposit, and is zero after the already verified G010 bridge transaction **0xcc827fd1fef937ac1942dd53a7f049061b827bf5292e1aa9a7e79610c00f200b** at 17:43:53, block 127444806. No other B canonical event is returned in that bridge block. Therefore the second deposit's immediate USDT source is A, not an unspent part of S1's first funding pool.

## Principal and valuation

Unique candidate source debits to B: S1 supplies 377244.364582811240700000 USDT in four payments and A supplies 336943.421822265793499428 USDT once. Total 714187.786405077034199428 USDT. The two Relay deposits total 706943.421822265793499428 USDT; two settlement debits total 7244.364582811240700000 USDT. Neither downstream category is added again to original principal. The earlier b4c→S1 deposit is upstream context, not another independent loss.

No historical USD conversion is applied, no verified loss total is asserted, and no receipt is classified as theft solely because its timing falls inside reported incident hours.
