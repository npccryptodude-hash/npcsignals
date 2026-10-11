# ZYROX Hp4q funder fingerprint checkpoint v0.120

**Baseline:** public commit `d38a3ace79547f70b8f03dfa3fc237c2dffe4651` / v0.119 / U477  
**This checkpoint:** v0.120 / U478–U492  
**Research date:** 2026-10-11 UTC  
**Primary:** `Hp4q9Tfeo5Cp7BuFNe6pRo3DqfPZVAiEampauGzPyyod`

## Result

All ten direct Hp4q funders reproduce the DSRGB fingerprint. Each address has exactly ten finalized transactions: four large-cycle receipts, a full-balance transfer to Hp4q less one 5,000-lamport fee, the same four upstream senders returning at low value, and a second full-balance transfer to Hp4q less one fee. Funding-to-forwarding latency is 0–5 seconds. Every outbound transaction is signed and fee-paid only by the sending wallet.

The ten immediate upstream wallets form overlapping four-recipient batches across the ten Hp4q funders. Every immediate upstream wallet funds four direct Hp4q funders and repeats the identical recipient set in the low-value cycle. This materially strengthens the coordinated launch-operations assessment and establishes a repeated operational template and coordinated batch construction. It does not establish shared private keys, common beneficial ownership, or a real-world identity.

## Duplicate and scope control

- The twenty direct funder → Hp4q transfers are already present in the frozen Hp4q manifest and receive no new U IDs.
- The large GhWZ batch transaction `3hMj…LsqQu` is already represented by frozen evidence F08 and receives no new U ID.
- The large FxLL, FHFPE, WFj2 and 9y3i batches and their low-value repeats are represented by U466–U473; they receive no new IDs here.
- New U478–U492 record only previously unrecorded transaction-level batch observations useful to the requested fingerprint comparison.
- Exact-address comparison against the 104-wallet export found Hp4q but none of the ten direct funders or ten immediate upstream batch wallets.
- Findings are independent Solana RPC results. No IsItBundled classification is promoted or merged into an NPCsignals finding.
- No exhausted IsItBundled or Proxima branch was reopened.

## Ten-funder comparison

For every row, the large cycle received exactly 9.164081154 SOL and forwarded 9.164076154 SOL; the low cycle received exactly 0.010006000 SOL and forwarded 0.010001000 SOL. Both differences are exactly the 0.000005000 SOL transaction fee, leaving a zero post-balance.

| Funder | Immediate upstream wallets | Large funding span / last-in→out | Same-slot maximum | Small repeat | History | Classification |
| --- | --- | ---: | ---: | --- | --- | --- |
| `G1W7…1TGN` | GhWZ, 69XR, WFj2, 9y3i | 1s / 0s | 2 | same four; full-balance | 10 tx | CONFIRMED full-balance relay |
| `9FAg…vVw9` | FxLL, 69XR, WFj2, 9y3i | 2s / 0s | 2 | same four; full-balance | 10 tx | CONFIRMED full-balance relay |
| `DSRG…Ny6w5` | FxLL, FHFPE, WFj2, 9y3i | 2s / 0s | 2 | same four; full-balance | 10 tx | CONFIRMED full-balance relay |
| `Bvfe…dKzf` | FxLL, FHFPE, A1WB, 9y3i | 2s / 3s | 3 | same four; full-balance | 10 tx | CONFIRMED full-balance relay |
| `5wjU…bpzb` | FxLL, FHFPE, A1WB, CUHx | 1s / 5s | 3 | same four; full-balance | 10 tx | CONFIRMED full-balance relay |
| `FXaa…nEoP` | FHFPE, A1WB, CUHx, DjHy | 1s / 5s | 2 | same four; full-balance | 10 tx | CONFIRMED full-balance relay |
| `DqEo…gcTK` | A1WB, CUHx, DjHy, AJrM | 1s / 5s | 2 | same four; full-balance | 10 tx | CONFIRMED full-balance relay |
| `Dsun…zjRV` | CUHx, DjHy, AJrM, GhWZ | 0s / 5s | 2 | same four; full-balance | 10 tx | CONFIRMED full-balance relay |
| `39PE…wSpN` | DjHy, AJrM, GhWZ, 69XR | 0s / 5s | 2 | same four; full-balance | 10 tx | CONFIRMED full-balance relay |
| `56n1…eQea` | AJrM, GhWZ, 69XR, WFj2 | 1s / 5s | 2 | same four; full-balance | 10 tx | CONFIRMED full-balance relay |

The compact machine-readable manifest `raw/hp4q_funder_fingerprint_manifest_2026-10-11.json` preserves, for each address, every inbound and outbound signature, amount, UTC timestamp, slot/index, signer, fee payer, fee, pre/post balance, funding span, upstream set and canonical RPC JSON hash.

## Batch-construction fingerprint

| Feature | Result across ten direct funders |
| --- | --- |
| Four inbound sources | 10/10 |
| Inputs are four-recipient batch transactions | 10/10 |
| Funding clustered within 0–2 seconds | 10/10 |
| Full pre-balance forwarded minus exact 5,000-lamport fee | 10/10, both cycles |
| Zero balance after forwarding | 10/10, both cycles |
| Same four upstream wallets repeat | 10/10 |
| Low-value follow-up cycle | 10/10 |
| Short history of exactly ten transactions | 10/10 |
| Common signer/fee payer across separate funders | none |
| Authority instruction or shared on-chain authority | none observed |

The ten immediate upstream senders are FxLL, FHFPE, WFj2, 9y3i, A1WB, CUHx, DjHy, AJrM, GhWZ and 69XR. Each sends one four-recipient large batch totaling 9.164081154 SOL after receiving 9.164086154 SOL, then repeats the same recipients with a 0.010006000 SOL batch after receiving 0.010011000 SOL. In both cases its own 5,000-lamport fee clears the account to zero.

This creates a sliding, overlapping construction: each immediate upstream wallet serves four Hp4q funders, and each Hp4q funder is served by four immediate upstream wallets. Equal amounts alone are not used as a control inference; the stronger evidence is the repeated transaction topology, exact balance/fee arithmetic, preserved recipient sets, narrow timing and full two-cycle replay.

## Direct connection to known launch infrastructure

The previously known BZ9m F06 batch funded Aft6, 62DW, 5vaQ and HuJg. Bounded follow-up confirms that Aft6 and 5vaQ are themselves ten-transaction, two-cycle, full-balance batch relays:

| Relay | Large four-recipient batch | Low-value repeat | Immediate downstream |
| --- | --- | --- | --- |
| `Aft6…sYow` | 9.164091154 SOL pre; 9.164086154 SOL sent; 0 after fee | 0.010016000 pre; 0.010011000 sent; 0 after fee | A1WB, CUHx, DjHy, AJrM |
| `5vaQ…YSAF` | 9.164091154 SOL pre; 9.164086154 SOL sent; 0 after fee | 0.010016000 pre; 0.010011000 sent; 0 after fee | DjHy, AJrM, GhWZ, 69XR |

Together with the already verified 62DW and HuJg branches, the four BZ9m children feed the immediate batch layer covering the ten-funder Hp4q fan-out. These nodes also pooled deposits from other sources, so continuous exclusive allocation of a particular BZ9m deposit is not established. The supported conclusion is common launch infrastructure and coordinated operation, not source-of-funds ownership after commingling.

## New ledger U478–U492

Each record represents one newly documented four-recipient batch transaction. `total_amount` is the sum of the four native SOL outputs. The source is the sole signer and fee payer; `pre_balance`, `post_balance` and `fee` are source-account values.

```jsonl
{"id":"U478","source":"A1WB3R9phm4psgGbww8QUX9QJ8nAPF3Q8R9zza3onE5Q","recipients":["BvfeNd5UWXJZWbURNrmF3JF34q463cXZqP2HYgddKzf","5wjUCbqsQ77LgV1TKMvy1hbg2Wvh9NkT8inJFCFybpzb","FXaanteZQPdeaD45JEEtG4Yu7BgFY8tGG4KCdjbmnEoP","DqEoiLwJLV8LgtwpLmtcsZvLgELPJ8LnUpTEwHyigcTK"],"edge_type":"launch_batch_observation","asset":"SOL","total_amount":"9.164081154","timestamp":"2026-09-30T17:16:37Z","slot":452029194,"transaction_index":1239,"tx":"3bsxP27VYw76M5shGVPusoLH8m1nijLtCwvCwvDCFjxbRHE1q6QLgpPcQLi3ZZTEJVUPAntSL5GSBJ58JszndSRC","pre_balance":"9.164086154","post_balance":"0.000000000","fee":"0.000005000","signer":["A1WB3R9phm4psgGbww8QUX9QJ8nAPF3Q8R9zza3onE5Q"],"fee_payer":"A1WB3R9phm4psgGbww8QUX9QJ8nAPF3Q8R9zza3onE5Q","evidence_status":"CONFIRMED transaction; ownership unresolved"}
{"id":"U479","source":"CUHxdgLrY8jQ7piS84t4MTsjR8Do6AQDaSADzKTL7bAJ","recipients":["5wjUCbqsQ77LgV1TKMvy1hbg2Wvh9NkT8inJFCFybpzb","FXaanteZQPdeaD45JEEtG4Yu7BgFY8tGG4KCdjbmnEoP","DqEoiLwJLV8LgtwpLmtcsZvLgELPJ8LnUpTEwHyigcTK","Dsun394GT7QanqtP6dF3qwYpPaXyANKHDPLnjSqrzjRV"],"edge_type":"launch_batch_observation","asset":"SOL","total_amount":"9.164081154","timestamp":"2026-09-30T17:16:38Z","slot":452029196,"transaction_index":637,"tx":"3ni9HsjSsa397RX8gBaf9TexQFuoYYTyQeX4zBkYrUQXcoU6qqg4crZqQ7ySLXKutNjjkVbiofrbSft4X7M6EQZr","pre_balance":"9.164086154","post_balance":"0.000000000","fee":"0.000005000","signer":["CUHxdgLrY8jQ7piS84t4MTsjR8Do6AQDaSADzKTL7bAJ"],"fee_payer":"CUHxdgLrY8jQ7piS84t4MTsjR8Do6AQDaSADzKTL7bAJ","evidence_status":"CONFIRMED transaction; ownership unresolved"}
{"id":"U480","source":"DjHyjwXsKdZpuem3byVf94VreFKiQyB88UJeVVbMZEfP","recipients":["FXaanteZQPdeaD45JEEtG4Yu7BgFY8tGG4KCdjbmnEoP","DqEoiLwJLV8LgtwpLmtcsZvLgELPJ8LnUpTEwHyigcTK","Dsun394GT7QanqtP6dF3qwYpPaXyANKHDPLnjSqrzjRV","39PE8B1Si5oNcUFjCdthTuE3c4UQjup5ff94QYjWwSpN"],"edge_type":"launch_batch_observation","asset":"SOL","total_amount":"9.164081154","timestamp":"2026-09-30T17:16:38Z","slot":452029196,"transaction_index":1051,"tx":"53RwHQgNaenMNb8pb4GLLb5FJzrWXCmoyhG4RmPSvdo58aYKyLFurfcGWvYUpXNA5uKxEJgi6tf72un53JMsGd4S","pre_balance":"9.164086154","post_balance":"0.000000000","fee":"0.000005000","signer":["DjHyjwXsKdZpuem3byVf94VreFKiQyB88UJeVVbMZEfP"],"fee_payer":"DjHyjwXsKdZpuem3byVf94VreFKiQyB88UJeVVbMZEfP","evidence_status":"CONFIRMED transaction; ownership unresolved"}
{"id":"U481","source":"AJrMJtKoWt8qPkLd57dsAGZwJwTGGjUacYnhQz1aG3fZ","recipients":["DqEoiLwJLV8LgtwpLmtcsZvLgELPJ8LnUpTEwHyigcTK","Dsun394GT7QanqtP6dF3qwYpPaXyANKHDPLnjSqrzjRV","39PE8B1Si5oNcUFjCdthTuE3c4UQjup5ff94QYjWwSpN","56n1cx1DYspMkH9fSXwY81Q71CZsiK2oyj91iH8veQea"],"edge_type":"launch_batch_observation","asset":"SOL","total_amount":"9.164081154","timestamp":"2026-09-30T17:16:38Z","slot":452029197,"transaction_index":129,"tx":"3UZnvtam3KWt5kWcMaxWEy6HtgXuwyLENCzb7581c6FSKXoWMYVsmxzZyFRjZPS2jd2PepFo9a8YwurvmPNN5ipG","pre_balance":"9.164086154","post_balance":"0.000000000","fee":"0.000005000","signer":["AJrMJtKoWt8qPkLd57dsAGZwJwTGGjUacYnhQz1aG3fZ"],"fee_payer":"AJrMJtKoWt8qPkLd57dsAGZwJwTGGjUacYnhQz1aG3fZ","evidence_status":"CONFIRMED transaction; ownership unresolved"}
{"id":"U482","source":"69XRi8jSGmVrq8PK5rpS16u4fRaaMiRSTAFXWvNpLPjN","recipients":["39PE8B1Si5oNcUFjCdthTuE3c4UQjup5ff94QYjWwSpN","56n1cx1DYspMkH9fSXwY81Q71CZsiK2oyj91iH8veQea","G1W7jRq6eDMfEnVjSXgcqb547pyMs3bqUUupTzYh1TGN","9FAguDq5G22C9YLm8gqdkrSq3gGiykdnc7V8EBxvvVw9"],"edge_type":"launch_batch_observation","asset":"SOL","total_amount":"9.164081154","timestamp":"2026-09-30T17:16:38Z","slot":452029200,"transaction_index":296,"tx":"4UFqZsR7XCPhw1Qi3EzkuibyUtkZzu8fntMz7BHuHpWxVMXJPpTep5wDH4fsH8xETKFoBALhUb13CwgsP4KyqjhK","pre_balance":"9.164086154","post_balance":"0.000000000","fee":"0.000005000","signer":["69XRi8jSGmVrq8PK5rpS16u4fRaaMiRSTAFXWvNpLPjN"],"fee_payer":"69XRi8jSGmVrq8PK5rpS16u4fRaaMiRSTAFXWvNpLPjN","evidence_status":"CONFIRMED transaction; ownership unresolved"}
{"id":"U483","source":"A1WB3R9phm4psgGbww8QUX9QJ8nAPF3Q8R9zza3onE5Q","recipients":["BvfeNd5UWXJZWbURNrmF3JF34q463cXZqP2HYgddKzf","5wjUCbqsQ77LgV1TKMvy1hbg2Wvh9NkT8inJFCFybpzb","FXaanteZQPdeaD45JEEtG4Yu7BgFY8tGG4KCdjbmnEoP","DqEoiLwJLV8LgtwpLmtcsZvLgELPJ8LnUpTEwHyigcTK"],"edge_type":"launch_fee_refill_batch_observation","asset":"SOL","total_amount":"0.010006000","timestamp":"2026-09-30T17:51:48Z","slot":452037074,"transaction_index":71,"tx":"33XM44DtehGGLXDc4iLm8hQ6W3XhWm1yKTYW4M1RBfKaWh9VJE29JX3FRM597qkgymZiSfMtP1Yb8eKdAu1FRh6j","pre_balance":"0.010011000","post_balance":"0.000000000","fee":"0.000005000","signer":["A1WB3R9phm4psgGbww8QUX9QJ8nAPF3Q8R9zza3onE5Q"],"fee_payer":"A1WB3R9phm4psgGbww8QUX9QJ8nAPF3Q8R9zza3onE5Q","evidence_status":"CONFIRMED transaction; functional label inferred from repeated topology"}
{"id":"U484","source":"CUHxdgLrY8jQ7piS84t4MTsjR8Do6AQDaSADzKTL7bAJ","recipients":["5wjUCbqsQ77LgV1TKMvy1hbg2Wvh9NkT8inJFCFybpzb","FXaanteZQPdeaD45JEEtG4Yu7BgFY8tGG4KCdjbmnEoP","DqEoiLwJLV8LgtwpLmtcsZvLgELPJ8LnUpTEwHyigcTK","Dsun394GT7QanqtP6dF3qwYpPaXyANKHDPLnjSqrzjRV"],"edge_type":"launch_fee_refill_batch_observation","asset":"SOL","total_amount":"0.010006000","timestamp":"2026-09-30T17:51:48Z","slot":452037074,"transaction_index":1215,"tx":"5vcE6gWht6Tfz67qeb9NCdcq3zT4xmmCD9rZVafV3wKUBqo9JBpH3VpwbS1GUUpz4NqQeY4fDHDZz4AwG5vvQzVg","pre_balance":"0.010011000","post_balance":"0.000000000","fee":"0.000005000","signer":["CUHxdgLrY8jQ7piS84t4MTsjR8Do6AQDaSADzKTL7bAJ"],"fee_payer":"CUHxdgLrY8jQ7piS84t4MTsjR8Do6AQDaSADzKTL7bAJ","evidence_status":"CONFIRMED transaction; functional label inferred from repeated topology"}
{"id":"U485","source":"DjHyjwXsKdZpuem3byVf94VreFKiQyB88UJeVVbMZEfP","recipients":["FXaanteZQPdeaD45JEEtG4Yu7BgFY8tGG4KCdjbmnEoP","DqEoiLwJLV8LgtwpLmtcsZvLgELPJ8LnUpTEwHyigcTK","Dsun394GT7QanqtP6dF3qwYpPaXyANKHDPLnjSqrzjRV","39PE8B1Si5oNcUFjCdthTuE3c4UQjup5ff94QYjWwSpN"],"edge_type":"launch_fee_refill_batch_observation","asset":"SOL","total_amount":"0.010006000","timestamp":"2026-09-30T17:51:49Z","slot":452037075,"transaction_index":707,"tx":"2sBMACbjkFsgrJzjtFifFDLzCYZjQwZsZ6Fi43iFShbXxkY29MxpFs3GmJVHR92rpuBE1VJeod7yrz16mN6hXcGX","pre_balance":"0.010011000","post_balance":"0.000000000","fee":"0.000005000","signer":["DjHyjwXsKdZpuem3byVf94VreFKiQyB88UJeVVbMZEfP"],"fee_payer":"DjHyjwXsKdZpuem3byVf94VreFKiQyB88UJeVVbMZEfP","evidence_status":"CONFIRMED transaction; functional label inferred from repeated topology"}
{"id":"U486","source":"AJrMJtKoWt8qPkLd57dsAGZwJwTGGjUacYnhQz1aG3fZ","recipients":["DqEoiLwJLV8LgtwpLmtcsZvLgELPJ8LnUpTEwHyigcTK","Dsun394GT7QanqtP6dF3qwYpPaXyANKHDPLnjSqrzjRV","39PE8B1Si5oNcUFjCdthTuE3c4UQjup5ff94QYjWwSpN","56n1cx1DYspMkH9fSXwY81Q71CZsiK2oyj91iH8veQea"],"edge_type":"launch_fee_refill_batch_observation","asset":"SOL","total_amount":"0.010006000","timestamp":"2026-09-30T17:51:49Z","slot":452037075,"transaction_index":1173,"tx":"W8HmXeUKsrpbAYefAxqGNHgSYUyeLy8LFTUSztJpUTgXgpFsYKZDuUFe2e33bnWxMy8U7YZRjRDxVHKzpeE42Ua","pre_balance":"0.010011000","post_balance":"0.000000000","fee":"0.000005000","signer":["AJrMJtKoWt8qPkLd57dsAGZwJwTGGjUacYnhQz1aG3fZ"],"fee_payer":"AJrMJtKoWt8qPkLd57dsAGZwJwTGGjUacYnhQz1aG3fZ","evidence_status":"CONFIRMED transaction; functional label inferred from repeated topology"}
{"id":"U487","source":"GhWZD17VzcdiSRUHuegmQ89pgDFS7G3jRPGSdiUGGZCn","recipients":["Dsun394GT7QanqtP6dF3qwYpPaXyANKHDPLnjSqrzjRV","39PE8B1Si5oNcUFjCdthTuE3c4UQjup5ff94QYjWwSpN","56n1cx1DYspMkH9fSXwY81Q71CZsiK2oyj91iH8veQea","G1W7jRq6eDMfEnVjSXgcqb547pyMs3bqUUupTzYh1TGN"],"edge_type":"launch_fee_refill_batch_observation","asset":"SOL","total_amount":"0.010006000","timestamp":"2026-09-30T17:51:49Z","slot":452037075,"transaction_index":1631,"tx":"59ySt8XmGKodDxf3tgRoHQvsi5tCKNvPCADkf6hxiFj6PLf5SG5NNLd8hv4acFXzYS95w1JEkJEwKv1WWRCwH3x3","pre_balance":"0.010011000","post_balance":"0.000000000","fee":"0.000005000","signer":["GhWZD17VzcdiSRUHuegmQ89pgDFS7G3jRPGSdiUGGZCn"],"fee_payer":"GhWZD17VzcdiSRUHuegmQ89pgDFS7G3jRPGSdiUGGZCn","evidence_status":"CONFIRMED transaction; functional label inferred from repeated topology"}
{"id":"U488","source":"69XRi8jSGmVrq8PK5rpS16u4fRaaMiRSTAFXWvNpLPjN","recipients":["39PE8B1Si5oNcUFjCdthTuE3c4UQjup5ff94QYjWwSpN","56n1cx1DYspMkH9fSXwY81Q71CZsiK2oyj91iH8veQea","G1W7jRq6eDMfEnVjSXgcqb547pyMs3bqUUupTzYh1TGN","9FAguDq5G22C9YLm8gqdkrSq3gGiykdnc7V8EBxvvVw9"],"edge_type":"launch_fee_refill_batch_observation","asset":"SOL","total_amount":"0.010006000","timestamp":"2026-09-30T17:51:49Z","slot":452037076,"transaction_index":480,"tx":"zx9ae1wqJ7Ya4aSKUPyux8BmR3w2Jsv6M77r5CJpfiu53Ejz7HCxPRzcSy2HuNixNHoGztyrrNQMCaAADNieWEH","pre_balance":"0.010011000","post_balance":"0.000000000","fee":"0.000005000","signer":["69XRi8jSGmVrq8PK5rpS16u4fRaaMiRSTAFXWvNpLPjN"],"fee_payer":"69XRi8jSGmVrq8PK5rpS16u4fRaaMiRSTAFXWvNpLPjN","evidence_status":"CONFIRMED transaction; functional label inferred from repeated topology"}
{"id":"U489","source":"Aft6HWo4f4j32ALBLXWsU8LtxMHT4eWwaysVLW2msYow","recipients":["A1WB3R9phm4psgGbww8QUX9QJ8nAPF3Q8R9zza3onE5Q","CUHxdgLrY8jQ7piS84t4MTsjR8Do6AQDaSADzKTL7bAJ","DjHyjwXsKdZpuem3byVf94VreFKiQyB88UJeVVbMZEfP","AJrMJtKoWt8qPkLd57dsAGZwJwTGGjUacYnhQz1aG3fZ"],"edge_type":"launch_infrastructure_batch_observation","asset":"SOL","total_amount":"9.164086154","timestamp":"2026-09-30T17:16:36Z","slot":452029188,"transaction_index":1416,"tx":"eZs3vZAdxzjGCvda2HtrEKcCw7GkcDSZPgLuMwkgjKFjvsNfXighwqPuBwCccUVqSuanQn1y1HtqJyWBTs6u6r5","pre_balance":"9.164091154","post_balance":"0.000000000","fee":"0.000005000","signer":["Aft6HWo4f4j32ALBLXWsU8LtxMHT4eWwaysVLW2msYow"],"fee_payer":"Aft6HWo4f4j32ALBLXWsU8LtxMHT4eWwaysVLW2msYow","evidence_status":"CONFIRMED transaction; pooled inputs prevent exclusive allocation"}
{"id":"U490","source":"Aft6HWo4f4j32ALBLXWsU8LtxMHT4eWwaysVLW2msYow","recipients":["A1WB3R9phm4psgGbww8QUX9QJ8nAPF3Q8R9zza3onE5Q","CUHxdgLrY8jQ7piS84t4MTsjR8Do6AQDaSADzKTL7bAJ","DjHyjwXsKdZpuem3byVf94VreFKiQyB88UJeVVbMZEfP","AJrMJtKoWt8qPkLd57dsAGZwJwTGGjUacYnhQz1aG3fZ"],"edge_type":"launch_fee_refill_infrastructure_batch_observation","asset":"SOL","total_amount":"0.010011000","timestamp":"2026-09-30T17:51:47Z","slot":452037070,"transaction_index":1000,"tx":"5ByKwAh1NEUoUmiSLeFK4w1XmvmyuJrxFn5AKLZEC4MKtXrCsQjCg6mh5C7WaWDTvm4Jb5VzMGDc9inLu6Edfapo","pre_balance":"0.010016000","post_balance":"0.000000000","fee":"0.000005000","signer":["Aft6HWo4f4j32ALBLXWsU8LtxMHT4eWwaysVLW2msYow"],"fee_payer":"Aft6HWo4f4j32ALBLXWsU8LtxMHT4eWwaysVLW2msYow","evidence_status":"CONFIRMED transaction; pooled inputs prevent exclusive allocation"}
{"id":"U491","source":"5vaQEDDUw8NX5DDnpaxmDMxKGFCx7nXqkW43r7b6YSAF","recipients":["DjHyjwXsKdZpuem3byVf94VreFKiQyB88UJeVVbMZEfP","AJrMJtKoWt8qPkLd57dsAGZwJwTGGjUacYnhQz1aG3fZ","GhWZD17VzcdiSRUHuegmQ89pgDFS7G3jRPGSdiUGGZCn","69XRi8jSGmVrq8PK5rpS16u4fRaaMiRSTAFXWvNpLPjN"],"edge_type":"launch_infrastructure_batch_observation","asset":"SOL","total_amount":"9.164086154","timestamp":"2026-09-30T17:16:36Z","slot":452029189,"transaction_index":1231,"tx":"3YYDMgwv7vTuCYaixG4dQkLdYFmqn2Jdcj8ZK3PqsZjV3Qgn6xQ79BvGVpUuzDRqTGLMEgzS2LgEuTg3bHUxT6cA","pre_balance":"9.164091154","post_balance":"0.000000000","fee":"0.000005000","signer":["5vaQEDDUw8NX5DDnpaxmDMxKGFCx7nXqkW43r7b6YSAF"],"fee_payer":"5vaQEDDUw8NX5DDnpaxmDMxKGFCx7nXqkW43r7b6YSAF","evidence_status":"CONFIRMED transaction; pooled inputs prevent exclusive allocation"}
{"id":"U492","source":"5vaQEDDUw8NX5DDnpaxmDMxKGFCx7nXqkW43r7b6YSAF","recipients":["DjHyjwXsKdZpuem3byVf94VreFKiQyB88UJeVVbMZEfP","AJrMJtKoWt8qPkLd57dsAGZwJwTGGjUacYnhQz1aG3fZ","GhWZD17VzcdiSRUHuegmQ89pgDFS7G3jRPGSdiUGGZCn","69XRi8jSGmVrq8PK5rpS16u4fRaaMiRSTAFXWvNpLPjN"],"edge_type":"launch_fee_refill_infrastructure_batch_observation","asset":"SOL","total_amount":"0.010011000","timestamp":"2026-09-30T17:51:47Z","slot":452037071,"transaction_index":241,"tx":"22vpnZRcU2DvuEUAGoG8m2GhbhVmFkqJpCe48AyARjtpfmtajokkHGNFLjB3aVPDy37dY9T4KH2ooscvY5h2mTc2","pre_balance":"0.010016000","post_balance":"0.000000000","fee":"0.000005000","signer":["5vaQEDDUw8NX5DDnpaxmDMxKGFCx7nXqkW43r7b6YSAF"],"fee_payer":"5vaQEDDUw8NX5DDnpaxmDMxKGFCx7nXqkW43r7b6YSAF","evidence_status":"CONFIRMED transaction; pooled inputs prevent exclusive allocation"}
```

## Attribution assessment and closure

- **Coordinated launch operations:** strengthened materially. The complete ten-funder layer shares the same two-cycle, full-balance, fee-exact batch template.
- **Common infrastructure:** confirmed. All ten funders participate in one overlapping immediate-upstream batch mesh, and the known BZ9m children feed that mesh.
- **Common signer, fee payer or authority:** not found across separate wallets. Each wallet signs and pays only for itself; no shared authority instruction was observed.
- **Beneficiary/control attribution:** not advanced beyond unknown operators of the coordinated launch system. Structure does not prove shared private keys or beneficial ownership.
- **Service boundary:** no defensible exchange, custodian, service or real-world identity attribution was found for the newly examined wallets.
- **Exhausted:** the direct ten-funder fingerprint comparison, the immediate-upstream recipient-set comparison and the repeated low-value-cycle test are complete. Further fan-out of unrelated counterparties is not justified.
- **Next concrete lead:** if beneficiary attribution is still required, test the earliest common funding sources entering the four BZ9m children for an independently labeled custody/service boundary; do not extend through commingled balances as continuous provenance.

**Checkpoint:** post-freeze research v0.120 / U492. Next available ledger ID U493. Frozen v0.114/U453 remains unchanged. No final article was written.
