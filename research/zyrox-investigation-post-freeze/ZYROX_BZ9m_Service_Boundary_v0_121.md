# ZYROX BZ9m service-boundary checkpoint v0.121

**Baseline:** public commit `dfecd6c9d26b994d3d9887f15fac03fde007147d` / v0.120 / U492  
**This checkpoint:** v0.121 / U493  
**Research date:** 2026-10-11 UTC  
**Disposition:** PAUSED / EXHAUSTED at unlabeled signer-wallet boundary

## Result

The bounded service/custody test examined 62DW, HuJg, Aft6 and 5vaQ and followed their direct launch-funding sources one additional hop. No exchange, custodian, bridge, payment processor, infrastructure provider or other named service boundary could be independently confirmed.

The test did identify one new common upstream fact. Seven direct source wallets relevant to the four children—BZ9m, FfRJ, 42D8, Goys, HF7h, APZk and Av44—were all initially funded by `8ySbR18BZrfW98cKoroYLffSfUSwEJZyWQSrTkdyPLv2` in the same ten-recipient full-balance batch. The same ten-recipient topology repeated at low value about 35 minutes later. This strengthens the coordinated launch-operation topology but does not identify a service, beneficial owner, controller or real-world person.

## Scope and duplicate control

- Frozen v0.114/U453 is unchanged. U001–U492 are unchanged.
- No exhausted Hp4q, IsItBundled, Proxima, HFAc, 99Gc, FEaT/H85K or 6hR7 branch was reopened.
- The large `8ySb → BZ9m` edge is frozen F05. The expanded ten-recipient view of that same transaction is therefore documented without a new U ID.
- U493 records only the previously unrecorded low-value ten-recipient repeat, which independently confirms the common upstream construction.
- Investigation stopped at 8ySb. No broader fan-out or source-of-funds attribution beyond that unlabeled signer wallet was attempted.

## Earliest relevant funding of the four BZ9m children

All four children are signer-capable native-SOL wallets used only during the same 35-minute launch window. Each has exactly ten finalized transactions and currently returns a null account after its balance was cleared to zero.

| Child | Earliest source | Exact edge | UTC / slot:index | Recipient pre → post | Signer / fee payer |
| --- | --- | ---: | --- | ---: | --- |
| `62DW…SNrN` | BZ9m | 2.291022788 SOL | 2026-09-30T17:16:24Z / 452029143:591 | 0 → 2.291022788 SOL | BZ9m / BZ9m |
| `HuJg…N5y4` | BZ9m | 2.291022788 SOL | 2026-09-30T17:16:24Z / 452029143:591 | 0 → 2.291022788 SOL | BZ9m / BZ9m |
| `Aft6…sYow` | BZ9m | 2.291022790 SOL | 2026-09-30T17:16:24Z / 452029143:591 | 0 → 2.291022790 SOL | BZ9m / BZ9m |
| `5vaQ…YSAF` | BZ9m | 2.291022788 SOL | 2026-09-30T17:16:24Z / 452029143:591 | 0 → 2.291022788 SOL | BZ9m / BZ9m |

Signature for all four edges: `5gpnfRA4Z1zSY8VX756WB2qsur8STA9CeBetkQwJUijwParm6RsY7V2aTQgfoatG8cknxfpWNTDMM8yMpfmHKjpd`.

The full large-cycle source sets were:

| Child | Four direct sources | Same sources repeated at low value |
| --- | --- | --- |
| 62DW | BZ9m, FfRJ, Goys, HF7h | yes |
| HuJg | BZ9m, FfRJ, APZk, Av44 | yes |
| Aft6 | BZ9m, 42D8, Goys, HF7h | yes |
| 5vaQ | BZ9m, FfRJ, APZk, HF7h | yes |

## One-hop source test

Each of the seven direct sources has exactly four finalized transactions: one receipt from 8ySb, one self-signed four-recipient full-balance batch, then the same receipt-and-batch pair at low value. Each source received 9.164096154 SOL, sent 9.164091154 SOL and paid a 0.000005000 SOL fee to reach zero. In the repeat it received 0.010021000 SOL, sent 0.010016000 SOL and again reached zero after one fee.

| Source | Large outgoing transaction / slot:index | Direct child recipients in that batch | History / classification |
| --- | --- | --- | --- |
| BZ9m | `5gpn…Kjpd` / 452029143:591 | Aft6, 62DW, 5vaQ, HuJg | 4 tx; short-lived batch relay |
| FfRJ | `5L82…8txZ` / 452029144:177 | 62DW, 5vaQ, HuJg | 4 tx; short-lived batch relay |
| APZk | `4Xn6…Ja2a` / 452029144:699 | 5vaQ, HuJg | 4 tx; short-lived batch relay |
| Av44 | `4N2Z…E6PP` / 452029144:1562 | HuJg | 4 tx; short-lived batch relay |
| 42D8 | `3J1G…skci` / 452029146:893 | Aft6 | 4 tx; short-lived batch relay |
| Goys | `gBui…gGt` / 452029146:1364 | Aft6, 62DW | 4 tx; short-lived batch relay |
| HF7h | `3NSM…X1BU` / 452029147:167 | Aft6, 62DW, 5vaQ | 4 tx; short-lived batch relay |

Full signatures, four-recipient outputs, UTC times, amounts, fees, signers, fee payers, pre/post balances and canonical RPC JSON hashes are preserved in `raw/bz9m_service_boundary_manifest_2026-10-11.json`.

## Common upstream: 8ySb

The first transaction for every direct source above is the same 8ySb batch:

- **Large batch:** 2026-09-30T17:16:24Z, slot/index 452029143:263, signature `5FjePPLz2TRTk4Axzso1mTR4QpdbhLbM7zK7Nco122CyNyQ749v9VwTKoxGU1otHtXNErYTDEmFgGZBdezuBDhat`.
- 8ySb was sole signer and fee payer.
- Pre-balance 91.640966540 SOL; ten outputs of 9.164096154 SOL; 0.000005000 SOL fee; post-balance zero.
- The ten recipients were BZ9m, FfRJ, APZk, Av44, 2sA7, 6cuP, 8hWH, 42D8, Goys and HF7h.
- **Low repeat:** 2026-09-30T17:51:46Z, slot/index 452037068:1107, signature `2b7koW521Hmhy2R95t4bvpBBUBCZbb8v2MH5L1Ctg1ni5XrMGXBU5R6cQGaz7UYuyeyq2hU3bhtEXcmeRNpufkhX`.
- Pre-balance 0.100215000 SOL; ten outputs of 0.010021000 SOL; 0.000005000 SOL fee; post-balance zero.
- 8ySb has 24 finalized transactions, all between 2026-09-30T17:16:07Z and 17:51:46Z. It is a short-window launch wallet, not a persistent service wallet.

## Service/custody attribution test

| Test | Result |
| --- | --- |
| First-party service documentation or public disclosure | none found |
| Official address-list match | none found |
| Independently corroborated explorer/entity label | none established |
| Protocol-owned account or contract | no; observed activity is signer-authorized native System Program transfer activity |
| Bridge/payment-processor-specific instruction pattern | none observed |
| Current finalized account state | all twelve examined accounts return null after zero-balance closure |
| Confirmed exchange/custody/service boundary | none |

Exact-address public searches returned no relevant attribution result. A third-party label, if later encountered, would remain insufficient without independent corroboration.

The common 8ySb signer/fee payer is significant only for its own two batch transactions. The seven direct sources each signed and paid for their own outgoing batches. No shared authority instruction or external co-signer appeared across those separate source wallets.

## New ledger U493

```jsonl
{"id":"U493","source":"8ySbR18BZrfW98cKoroYLffSfUSwEJZyWQSrTkdyPLv2","recipients":["BZ9mPLztWYrv9xcWtgwnQTVYJVpFXRgRGcbptzHYHSLR","FfRJ6bYnGcXjJpQRVeesSiBsq8QKFy5ezwZn4YSyXTW8","APZkkh6Yu8j9ZXeCWw3j1yXpm5Fy3iPLZBgJeHbuZXcV","Av44pncd7FBXFatYavC8invaTwiR4jX2SSHxsxLLaaLz","2sA7dcvJzNeWm4c3b48Q6D4FqtFcTfPyS1r5biZHvcMp","6cuPyJc7VsGSRGZYmejH7TXJmhhnNdiaRf5cBjc9QLhV","8hWHXHsaxR5UAaTZSvRkT4i6wFwdLxds24FohaExYZax","42D8pXeLYUmmt3i3Rn3mLxqNLwqzi9VVf28QooFe4o21","Goys2utQAtyLfZPTE5Mmn9qiKVUoKtCiBJGqrfLXYie7","HF7hfuVHbRTYtujsan8u9Di1YTGfchz6XuWVjffmYbEU"],"edge_type":"launch_fee_refill_batch_observation","asset":"SOL","total_amount":"0.100210000","per_recipient_amount":"0.010021000","timestamp":"2026-09-30T17:51:46Z","slot":452037068,"transaction_index":1107,"tx":"2b7koW521Hmhy2R95t4bvpBBUBCZbb8v2MH5L1Ctg1ni5XrMGXBU5R6cQGaz7UYuyeyq2hU3bhtEXcmeRNpufkhX","pre_balance":"0.100215000","post_balance":"0.000000000","fee":"0.000005000","signer":["8ySbR18BZrfW98cKoroYLffSfUSwEJZyWQSrTkdyPLv2"],"fee_payer":"8ySbR18BZrfW98cKoroYLffSfUSwEJZyWQSrTkdyPLv2","evidence_status":"CONFIRMED transaction; common launch source; service and ownership attribution unresolved"}
```

## Final attribution boundary

- **Beneficiary/control:** not advanced. Common funding and repeated construction do not prove shared keys or beneficial ownership.
- **ZYROX–Kytro:** not advanced. No Kytro evidence or attribution arose naturally in this test.
- **Closed as exhausted:** BZ9m-child service/custody test; direct-source histories; one-hop 8ySb common-source test; prior Hp4q fingerprint, IsItBundled and Proxima branches.
- **Remaining unresolved boundary:** `8ySb…PLv2`, an unlabeled 24-transaction signer wallet active only in the launch window. No independently documented service or identity boundary exists at or before the permitted stop point.
- **Recommendation:** PAUSE. Do not begin another ZYROX branch without genuinely new external evidence.

**Checkpoint:** post-freeze research v0.121 / U493. Next available ledger ID U494. Frozen v0.114/U453 remains byte-for-byte unchanged. No final article was written.
