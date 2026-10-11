# ZYROX Arkham Hp4q funding checkpoint v0.119

**Baseline:** public commit `65b1c96ac1c6b256721171caa90889155a3f5d6b` / v0.118 / U465  
**This checkpoint:** v0.119 / U466–U477  
**Research date:** 2026-10-11 UTC  
**Primary:** `Hp4q9Tfeo5Cp7BuFNe6pRo3DqfPZVAiEampauGzPyyod`  
**Lead relay:** `DSRGBmu54ZFgsxncWoT2uEgQkBF1ZikZ4ko2dAQNy6w5`

## Result

The Arkham lead is substantially correct but partly duplicate. The two DSRGB → Hp4q transfers were already present in the frozen full Hp4q transaction manifest, so they receive no new U IDs. New RPC reconstruction verifies the four wallets that funded DSRGB, the same topology repeating 35 minutes later at low value, and a path from the previously documented launch wallet BZ9m through HuJg and WFj2 into DSRGB.

This is strong evidence that DSRGB participated in the same coordinated launch-funding system already documented for Hp4q. It is not evidence that all wallets share one private key, are owned by one person, or identify a beneficial owner. Every batch sender was the sole signer and fee payer for its own transaction; no signer crossed wallet boundaries.

## Scope and duplicate control

- Frozen `ZYROX_Devsold_verification_v0_2.md` already lists DSRGB among ten direct Hp4q funders and contains both DSRGB → Hp4q transactions in the full Hp4q manifest.
- Existing F05/F06 document `8ySb…PLv2` → BZ9m and BZ9m's batch transaction `5gpn…Kjpd`; the newly recorded U474 edge is the previously unrecorded HuJg output inside that known transaction.
- The 104-wallet export contains Hp4q. It does not contain DSRGB, the four direct DSRGB funders, HuJg, or BZ9m.
- Exact-address comparison found DSRGB and BZ9m in prior NPCsignals evidence. The other newly examined relay addresses were absent from the pre-v0.119 repository outside the new raw captures.
- No IsItBundled classification is promoted to an NPCsignals finding. The findings below come from independent finalized Solana RPC reconstruction.
- Frozen v0.114/U453 and all existing ledger entries are unchanged.

## Exact DSRGB reconstruction

Each row succeeded. The displayed sender was the only signer and the fee payer. Amounts are native System Program transfers.

| UTC / slot:index | Sender → recipient | SOL | Signature | Signer / fee payer |
| --- | --- | ---: | --- | --- |
| 2026-09-30T17:16:37Z / 452029194:299 | FxLL → DSRGB | 2.291020288 | `2rx4ZiAB2bNS6aMP7EkpjiguLvZoniT7gJkB9disoeUfNMn2cV9k2jfZT5iwzWv17CeBn7P8vJfsWHVqs7C2Z8xf` | FxLL / FxLL |
| 2026-09-30T17:16:37Z / 452029194:729 | FHFPE → DSRGB | 2.291020290 | `4wT4LUz5vFxGvkxS3JdsaBiyQRv69TAn8DTMdCCkVJ9bw2hQ6EWcjmpj8eBYjgMZkhzAShW2auPe3n83RUyXRk8B` | FHFPE / FHFPE |
| 2026-09-30T17:16:39Z / 452029201:11 | WFj2 → DSRGB | 2.291020288 | `5jce84jd2zLUVuTPMduHAB9XLUx8vTechLsuhwkZuJ3U9rnYWSmUhYuGh6PwjANiHvm7FktAPUqsDxzXV7X9C1M8` | WFj2 / WFj2 |
| 2026-09-30T17:16:39Z / 452029201:514 | 9y3i → DSRGB | 2.291020288 | `435gqXSJJJQymn5Nodhi6FUAstqAJcJoZobzW36YCAGySP2Cewhif2SjMdt5LXNHCixGTnXQ2uacekEkvAJK3eTe` | 9y3i / 9y3i |
| 2026-09-30T17:16:39Z / 452029203:105 | DSRGB → Hp4q | 9.164076154 | `2Z27xvW5Sp6WfYxHKpYueJt7mwj5YfbUgEBbMRkmugGCVAJvB2sRyXBLiB3oZU6LyBpbjGyMvD9px1pVERFi5CmN` | DSRGB / DSRGB |
| 2026-09-30T17:51:48Z / 452037073:47 | FxLL → DSRGB | 0.002501500 | `25pnhCXRR2xpDqMxobSrMSxcpoTzHDCVc5jc8bjZdAn7DGxkCiCNH38usmfEohidT7f2cREqxAVPkaixQvSriG1L` | FxLL / FxLL |
| 2026-09-30T17:51:48Z / 452037073:1117 | FHFPE → DSRGB | 0.002501500 | `43NCU8mAofqNGykBrpKgraqfnyJcPcXnn9LQ2SxwULq333S3RUPJ1ZcjdPqTB7R6SSvGE428x8HhLxp4x51NYs73` | FHFPE / FHFPE |
| 2026-09-30T17:51:49Z / 452037076:724 | WFj2 → DSRGB | 0.002501500 | `4zdzPPMdG9pdFJpdjZqWSopgmSsPHALDynkaCSnxRKudQMe8JcBGEEZpSHBKTDPcGrUAnh7fxaDkqht47f3quKCe` | WFj2 / WFj2 |
| 2026-09-30T17:51:49Z / 452037076:1008 | 9y3i → DSRGB | 0.002501500 | `5YdwMzQpqrTWFMyk9HpQsgVo8DVBpb3ohtKNKk9aW5swne2jEHGRHuaZ1yHTZCvERVf9uNs2N3NqUhqH4SwqBnMM` | 9y3i / 9y3i |
| 2026-09-30T17:51:49Z / 452037077:1215 | DSRGB → Hp4q | 0.010001000 | `3gnrB2GzbzCk8LS2xJKPnB3frLSqryYwMPpE6PPbSXrjK8hqxDS1X7QPdGWF8ENuzUgv1TeZQXVYYozCn2LEKNi` | DSRGB / DSRGB |

The first cycle gives DSRGB 9.164081154 SOL and DSRGB sends 9.164076154 SOL, exactly one 0.000005000 SOL fee lower. The second gives DSRGB 0.010006000 SOL and DSRGB sends 0.010001000 SOL, again one fee lower. This is a confirmed two-cycle full-balance relay pattern.

## Four direct funders and their provenance

All four direct funders have exactly ten finalized transactions: four deposits, one four-recipient fan-out, then the same five-step structure at low value. Each source signed and paid for its own batch transaction.

| Direct DSRGB funder | Four large-cycle inputs before its DSRGB payment | Classification |
| --- | --- | --- |
| `FxLL5ChvDv9cPzMjW376fHTTvtaGTkvqNbbffeanL1HE` | FEuo, 9ksT, J3TV, Bjyx | short-lived pooled relay |
| `FHFPEkNKvzR4DeWDNbbSVgjBnTbbL7iwCTYUQdbeTJRP` | 7gVX, 9ksT, J3TV, Bjyx | short-lived pooled relay |
| `WFj2DFNtzvZMVe82tXY6RcS2rJXkhvYDinoZxiUd1sV` | HuJg, 7QYf, FEuo, 9ksT | short-lived pooled relay |
| `9y3i9WJmusS8e1WT1SfJLYj43HmmNvgzyWwRSumbNWye` | 7QYf, FEuo, 9ksT, J3TV | short-lived pooled relay |

The seven unique second-layer sources are:

`FEuoLLHxHtLaotkGZPcxa4qqWRDxeEfxuXKc3rKK6Z97`, `9ksTeWyzGvdPqBoGXKmAEDUcPimjs7V7h4TU4vFwbZ1t`, `J3TV9vqv4pcir44c4J7WLNwRhGSYVGwM67t9hcasMMXc`, `BjyxCNeVmHLKUjK7yiDKhteWp94u752XowAtwJgrWNdi`, `7gVXyEyPXYbWcSXN3yHMnwHN8vYFSUGJG266pvmjgBbx`, `HuJgSFkbEGvfzmQgewAKRowAXZM3xMGjrxGyHQDTN5y4`, and `7QYfjfaHQVwqyTzbLsUow297TxLDZ42xWu37Fw9uSRjV`.

Each also has exactly ten transactions with the same four-in/one-out-batch pattern repeated at low value. Full exact signatures, UTC timestamps, slots, transaction indexes, transfers, signers, fee payers and canonical JSON hashes are preserved in `raw/arkham_hp4q_case_manifest_2026-10-11.json`; per-address RPC captures remain available in the working evidence archive.

### FHFPE first funder

Arkham's `FHFPE…TJRP` lead resolves to `FHFPEkNKvzR4DeWDNbbSVgjBnTbbL7iwCTYUQdbeTJRP`. Its first canonical receipt is from `7gVXyEyPXYbWcSXN3yHMnwHN8vYFSUGJG266pvmjgBbx`:

- 2.291021540 SOL at 2026-09-30T17:16:25Z, slot/index 452029147:1079, signature `5GmJZ9dmFpkaaDRFXqyxfmQNAzF4k3RbVCKVnpmo2rZqyL7URj6bf6BswiynCiVLBhydgK36dTpNEi1kTmrNsM7Z`; 7gVX was sole signer and fee payer.
- Three later deposits arrived from 9ksT, J3TV and Bjyx at 17:16:37Z. FHFPE then batch-paid DSRGB and three peers.
- The same sources repeated the topology with 0.002502750 SOL deposits at 17:51:47–48Z before FHFPE paid DSRGB 0.002501500 SOL.

7gVX is itself a ten-transaction pooled relay. No public service or real-world identity attribution is supported for it or FHFPE.

## Connection to known launch infrastructure

The known F06 transaction from BZ9m was a four-recipient batch, not only the previously summarized BZ9m → 62DW edge. It also sent HuJg 2.291022788 SOL:

| UTC / slot:index | Edge | SOL | Signature | Signer / fee payer |
| --- | --- | ---: | --- | --- |
| 2026-09-30T17:16:24Z / 452029143:591 | BZ9m → HuJg | 2.291022788 | `5gpnfRA4Z1zSY8VX756WB2qsur8STA9CeBetkQwJUijwParm6RsY7V2aTQgfoatG8cknxfpWNTDMM8yMpfmHKjpd` | BZ9m / BZ9m |
| 2026-09-30T17:16:36Z / 452029190:279 | HuJg → WFj2 | 2.291021538 | `392mgdb1JWHCTPVr8b9FxwvsNe4Gkn1nCuhKWrCCHmSw3BTfbcM1yNBM996qZwwmCs26ncys3pQ2cErW2c9PLnci` | HuJg / HuJg |
| 2026-09-30T17:51:46Z / 452037068:1264 | BZ9m → HuJg | 0.002504000 | `y566A6m9h1k6XM1VLrWueSdfVstoSmbPbxpL1oyVhZCC6mxPWn4z6s2DbunbfBp5zU3W9KGrjkeeoVaWdaJ4vz3` | BZ9m / BZ9m |
| 2026-09-30T17:51:47Z / 452037071:509 | HuJg → WFj2 | 0.002502750 | `4Es351F61evy3B2qkdAFymLqDuL9p3U63E6STf4unjEnS5AuoptFE6B5wEMHBaq8ijm1iQUGjnRbjZWVAqnWBNmc` | HuJg / HuJg |

This connects the DSRGB branch to the previously documented BZ9m launch fan-out through the operational path BZ9m → HuJg → WFj2 → DSRGB → Hp4q in both cycles. HuJg received four equal-size deposits before paying four downstream relays, so the specific BZ9m deposit cannot be allocated to the later WFj2 output. The path is therefore evidence of common launch orchestration, not continuous single-source provenance.

## New ledger U466–U477

U466–U473 are new direct DSRGB funding edges. U474–U477 are the newly recorded BZ9m/HuJg operational-path edges. The two DSRGB → Hp4q edges are duplicates of the frozen manifest and receive no new IDs.

```jsonl
{"id":"U466","from":"FxLL5ChvDv9cPzMjW376fHTTvtaGTkvqNbbffeanL1HE","to":"DSRGBmu54ZFgsxncWoT2uEgQkBF1ZikZ4ko2dAQNy6w5","edge_type":"launch_funding_relay","asset":"SOL","amount":"2.291020288","timestamp":"2026-09-30T17:16:37Z","tx":"2rx4ZiAB2bNS6aMP7EkpjiguLvZoniT7gJkB9disoeUfNMn2cV9k2jfZT5iwzWv17CeBn7P8vJfsWHVqs7C2Z8xf","signer":["FxLL5ChvDv9cPzMjW376fHTTvtaGTkvqNbbffeanL1HE"],"fee_payer":"FxLL5ChvDv9cPzMjW376fHTTvtaGTkvqNbbffeanL1HE","evidence_status":"CONFIRMED transaction; ownership unresolved"}
{"id":"U467","from":"FHFPEkNKvzR4DeWDNbbSVgjBnTbbL7iwCTYUQdbeTJRP","to":"DSRGBmu54ZFgsxncWoT2uEgQkBF1ZikZ4ko2dAQNy6w5","edge_type":"launch_funding_relay","asset":"SOL","amount":"2.291020290","timestamp":"2026-09-30T17:16:37Z","tx":"4wT4LUz5vFxGvkxS3JdsaBiyQRv69TAn8DTMdCCkVJ9bw2hQ6EWcjmpj8eBYjgMZkhzAShW2auPe3n83RUyXRk8B","signer":["FHFPEkNKvzR4DeWDNbbSVgjBnTbbL7iwCTYUQdbeTJRP"],"fee_payer":"FHFPEkNKvzR4DeWDNbbSVgjBnTbbL7iwCTYUQdbeTJRP","evidence_status":"CONFIRMED transaction; ownership unresolved"}
{"id":"U468","from":"WFj2DFNtzvZMVe82tXY6RcS2rJXkhvYDinoZxiUd1sV","to":"DSRGBmu54ZFgsxncWoT2uEgQkBF1ZikZ4ko2dAQNy6w5","edge_type":"launch_funding_relay","asset":"SOL","amount":"2.291020288","timestamp":"2026-09-30T17:16:39Z","tx":"5jce84jd2zLUVuTPMduHAB9XLUx8vTechLsuhwkZuJ3U9rnYWSmUhYuGh6PwjANiHvm7FktAPUqsDxzXV7X9C1M8","signer":["WFj2DFNtzvZMVe82tXY6RcS2rJXkhvYDinoZxiUd1sV"],"fee_payer":"WFj2DFNtzvZMVe82tXY6RcS2rJXkhvYDinoZxiUd1sV","evidence_status":"CONFIRMED transaction; ownership unresolved"}
{"id":"U469","from":"9y3i9WJmusS8e1WT1SfJLYj43HmmNvgzyWwRSumbNWye","to":"DSRGBmu54ZFgsxncWoT2uEgQkBF1ZikZ4ko2dAQNy6w5","edge_type":"launch_funding_relay","asset":"SOL","amount":"2.291020288","timestamp":"2026-09-30T17:16:39Z","tx":"435gqXSJJJQymn5Nodhi6FUAstqAJcJoZobzW36YCAGySP2Cewhif2SjMdt5LXNHCixGTnXQ2uacekEkvAJK3eTe","signer":["9y3i9WJmusS8e1WT1SfJLYj43HmmNvgzyWwRSumbNWye"],"fee_payer":"9y3i9WJmusS8e1WT1SfJLYj43HmmNvgzyWwRSumbNWye","evidence_status":"CONFIRMED transaction; ownership unresolved"}
{"id":"U470","from":"FxLL5ChvDv9cPzMjW376fHTTvtaGTkvqNbbffeanL1HE","to":"DSRGBmu54ZFgsxncWoT2uEgQkBF1ZikZ4ko2dAQNy6w5","edge_type":"launch_fee_refill_relay","asset":"SOL","amount":"0.002501500","timestamp":"2026-09-30T17:51:48Z","tx":"25pnhCXRR2xpDqMxobSrMSxcpoTzHDCVc5jc8bjZdAn7DGxkCiCNH38usmfEohidT7f2cREqxAVPkaixQvSriG1L","signer":["FxLL5ChvDv9cPzMjW376fHTTvtaGTkvqNbbffeanL1HE"],"fee_payer":"FxLL5ChvDv9cPzMjW376fHTTvtaGTkvqNbbffeanL1HE","evidence_status":"CONFIRMED transaction; functional label inferred from repeated topology"}
{"id":"U471","from":"FHFPEkNKvzR4DeWDNbbSVgjBnTbbL7iwCTYUQdbeTJRP","to":"DSRGBmu54ZFgsxncWoT2uEgQkBF1ZikZ4ko2dAQNy6w5","edge_type":"launch_fee_refill_relay","asset":"SOL","amount":"0.002501500","timestamp":"2026-09-30T17:51:48Z","tx":"43NCU8mAofqNGykBrpKgraqfnyJcPcXnn9LQ2SxwULq333S3RUPJ1ZcjdPqTB7R6SSvGE428x8HhLxp4x51NYs73","signer":["FHFPEkNKvzR4DeWDNbbSVgjBnTbbL7iwCTYUQdbeTJRP"],"fee_payer":"FHFPEkNKvzR4DeWDNbbSVgjBnTbbL7iwCTYUQdbeTJRP","evidence_status":"CONFIRMED transaction; functional label inferred from repeated topology"}
{"id":"U472","from":"WFj2DFNtzvZMVe82tXY6RcS2rJXkhvYDinoZxiUd1sV","to":"DSRGBmu54ZFgsxncWoT2uEgQkBF1ZikZ4ko2dAQNy6w5","edge_type":"launch_fee_refill_relay","asset":"SOL","amount":"0.002501500","timestamp":"2026-09-30T17:51:49Z","tx":"4zdzPPMdG9pdFJpdjZqWSopgmSsPHALDynkaCSnxRKudQMe8JcBGEEZpSHBKTDPcGrUAnh7fxaDkqht47f3quKCe","signer":["WFj2DFNtzvZMVe82tXY6RcS2rJXkhvYDinoZxiUd1sV"],"fee_payer":"WFj2DFNtzvZMVe82tXY6RcS2rJXkhvYDinoZxiUd1sV","evidence_status":"CONFIRMED transaction; functional label inferred from repeated topology"}
{"id":"U473","from":"9y3i9WJmusS8e1WT1SfJLYj43HmmNvgzyWwRSumbNWye","to":"DSRGBmu54ZFgsxncWoT2uEgQkBF1ZikZ4ko2dAQNy6w5","edge_type":"launch_fee_refill_relay","asset":"SOL","amount":"0.002501500","timestamp":"2026-09-30T17:51:49Z","tx":"5YdwMzQpqrTWFMyk9HpQsgVo8DVBpb3ohtKNKk9aW5swne2jEHGRHuaZ1yHTZCvERVf9uNs2N3NqUhqH4SwqBnMM","signer":["9y3i9WJmusS8e1WT1SfJLYj43HmmNvgzyWwRSumbNWye"],"fee_payer":"9y3i9WJmusS8e1WT1SfJLYj43HmmNvgzyWwRSumbNWye","evidence_status":"CONFIRMED transaction; functional label inferred from repeated topology"}
{"id":"U474","from":"BZ9mPLztWYrv9xcWtgwnQTVYJVpFXRgRGcbptzHYHSLR","to":"HuJgSFkbEGvfzmQgewAKRowAXZM3xMGjrxGyHQDTN5y4","edge_type":"launch_infrastructure_operational_path","asset":"SOL","amount":"2.291022788","timestamp":"2026-09-30T17:16:24Z","tx":"5gpnfRA4Z1zSY8VX756WB2qsur8STA9CeBetkQwJUijwParm6RsY7V2aTQgfoatG8cknxfpWNTDMM8yMpfmHKjpd","signer":["BZ9mPLztWYrv9xcWtgwnQTVYJVpFXRgRGcbptzHYHSLR"],"fee_payer":"BZ9mPLztWYrv9xcWtgwnQTVYJVpFXRgRGcbptzHYHSLR","evidence_status":"CONFIRMED transaction; downstream allocation stops at HuJg commingling"}
{"id":"U475","from":"HuJgSFkbEGvfzmQgewAKRowAXZM3xMGjrxGyHQDTN5y4","to":"WFj2DFNtzvZMVe82tXY6RcS2rJXkhvYDinoZxiUd1sV","edge_type":"launch_infrastructure_operational_path","asset":"SOL","amount":"2.291021538","timestamp":"2026-09-30T17:16:36Z","tx":"392mgdb1JWHCTPVr8b9FxwvsNe4Gkn1nCuhKWrCCHmSw3BTfbcM1yNBM996qZwwmCs26ncys3pQ2cErW2c9PLnci","signer":["HuJgSFkbEGvfzmQgewAKRowAXZM3xMGjrxGyHQDTN5y4"],"fee_payer":"HuJgSFkbEGvfzmQgewAKRowAXZM3xMGjrxGyHQDTN5y4","evidence_status":"CONFIRMED transaction; not allocated to any single HuJg deposit"}
{"id":"U476","from":"BZ9mPLztWYrv9xcWtgwnQTVYJVpFXRgRGcbptzHYHSLR","to":"HuJgSFkbEGvfzmQgewAKRowAXZM3xMGjrxGyHQDTN5y4","edge_type":"launch_fee_refill_operational_path","asset":"SOL","amount":"0.002504000","timestamp":"2026-09-30T17:51:46Z","tx":"y566A6m9h1k6XM1VLrWueSdfVstoSmbPbxpL1oyVhZCC6mxPWn4z6s2DbunbfBp5zU3W9KGrjkeeoVaWdaJ4vz3","signer":["BZ9mPLztWYrv9xcWtgwnQTVYJVpFXRgRGcbptzHYHSLR"],"fee_payer":"BZ9mPLztWYrv9xcWtgwnQTVYJVpFXRgRGcbptzHYHSLR","evidence_status":"CONFIRMED transaction; downstream allocation stops at HuJg commingling"}
{"id":"U477","from":"HuJgSFkbEGvfzmQgewAKRowAXZM3xMGjrxGyHQDTN5y4","to":"WFj2DFNtzvZMVe82tXY6RcS2rJXkhvYDinoZxiUd1sV","edge_type":"launch_fee_refill_operational_path","asset":"SOL","amount":"0.002502750","timestamp":"2026-09-30T17:51:47Z","tx":"4Es351F61evy3B2qkdAFymLqDuL9p3U63E6STf4unjEnS5AuoptFE6B5wEMHBaq8ijm1iQUGjnRbjZWVAqnWBNmc","signer":["HuJgSFkbEGvfzmQgewAKRowAXZM3xMGjrxGyHQDTN5y4"],"fee_payer":"HuJgSFkbEGvfzmQgewAKRowAXZM3xMGjrxGyHQDTN5y4","evidence_status":"CONFIRMED transaction; not allocated to any single HuJg deposit"}
```

## Control and attribution assessment

- **Confirmed:** two repeated, tightly timed multi-layer batches; every DSRGB cycle is a full-balance sweep less exactly one fee; DSRGB is part of the Hp4q launch-funding machinery.
- **Strong operational coordination:** identical four-in/four-out topology repeats across layers and values, and a known BZ9m launch batch feeds the newly mapped branch.
- **Not confirmed:** common private-key control, one beneficial owner, any named person or organization, or continuous provenance of BZ9m's particular deposit after HuJg commingling.
- **Boundary:** all newly mapped accounts are short-lived self-signing relays with no supported exchange, custodian, service or real-world identity label. Attribution stops at unknown operators of the coordinated launch system.

## Unresolved gaps and next step

The new lead warrants one bounded follow-up: compare the repeated batch-construction fingerprint across the other nine direct Hp4q funders to determine whether the same transaction builder/topology generated the complete fan-out. It does not presently warrant an identity claim or reopening exhausted IsItBundled/Proxima branches.

**Checkpoint:** post-freeze research v0.119 / U477. Next available ledger ID U478. Frozen v0.114/U453 remains unchanged. No final article was written.
