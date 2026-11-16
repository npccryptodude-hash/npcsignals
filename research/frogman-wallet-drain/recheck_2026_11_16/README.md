# frogman / hyperliquid recheck / 16 november 2026

[summary](summary.json) · [per-account data](accounts_diff.json) · [ethereum / solana follow-up](ROUTE_REPORT.md)

all 36 addresses come from the unchanged 13 november checkpoint: 35 external-inventory accounts plus one separately audited account. requests and exact response bytes, utc retrieval times, headers and sha256 are retained in `raw/`. snapshots are sequential, not simultaneous. history end is fixed in [run metadata](run.json); the interval starts one second before each baseline history cutoff to avoid a boundary gap. full returned histories are also compared with baseline objects.

## observed change

```json
{
  "history_cutoff_utc": "2026-11-16T08:20:33.096000+00:00",
  "accounts": 36,
  "baseline_xmr1": "3586.887420",
  "current_xmr1": "3586.887420",
  "successful_spot_snapshots": 36,
  "accounts_with_coverage_issues": 0,
  "new_fills_returned": 0,
  "new_ledger_records_returned": 0,
  "changed_xmr1_accounts": [],
  "snapshot_start_utc": "2026-11-16T08:20:58.344498+00:00",
  "snapshot_end_utc": "2026-11-16T08:25:40.685886+00:00"
}
```

## per-account differences

buys and sells are gross xmr1 units; ledger count includes deposits, withdrawals and internal transfers. every nonzero or unknown ledger result must be inspected in accounts_diff.json; a zero means zero returned records, not proof of exhaustive platform history.

| account | address | 13 nov xmr1 | 16 nov xmr1 | delta | buys | sells | new ledger | latest returned activity (utc) | coverage issues |
|---|---|---:|---:|---:|---:|---:|---:|---|---|
| arbi-01 | 0x9cb119168265469a849e1864c87a57999a4bc01f | 107.794491 | 107.794491 | 0.000000 | 0 | 0 | 0 | 2026-10-07T01:46:01.572000+00:00 | none detected |
| arbi-02 | 0x3e2d81f7a5659e4760ba929ef88eed40ef6640a1 | 47.146974 | 47.146974 | 0.000000 | 0 | 0 | 0 | 2026-10-07T02:21:34.429000+00:00 | none detected |
| arbi-03 | 0xd7efd720adf271b7173dd01a9b81668892bee6b1 | 179.224455 | 179.224455 | 0.000000 | 0 | 0 | 0 | 2026-10-07T01:50:11.437000+00:00 | none detected |
| arbi-04 | 0x68d6e20a28f9d50ebf798ccf9fae9e3d5e4f1ac4 | 166.663254 | 166.663254 | 0.000000 | 0 | 0 | 0 | 2026-10-07T01:53:15.828000+00:00 | none detected |
| arbi-05 | 0x888795f84f5f81352a7639f1254662ae5897e223 | 166.263534 | 166.263534 | 0.000000 | 0 | 0 | 0 | 2026-10-07T01:57:17.668000+00:00 | none detected |
| arbi-06 | 0xa3ca6199d8692ec40d0287e615b48d0e8cde9abe | 164.28492 | 164.28492 | 0.00000 | 0 | 0 | 0 | 2026-10-07T02:05:54.096000+00:00 | none detected |
| arbi-07 | 0x4079067aa1bdff060c6c45155966d81c79e754e9 | 163.055781 | 163.055781 | 0.000000 | 0 | 0 | 0 | 2026-10-07T02:10:44.555000+00:00 | none detected |
| arbi-08 | 0x68b3a77db46418905c7eaf63324d4adcce06a680 | 162.326292 | 162.326292 | 0.000000 | 0 | 0 | 0 | 2026-10-07T02:14:17.319000+00:00 | none detected |
| arbi-09 | 0xd9249de6224382ce7791600d1d1f9e5fdf633abb | 160.417629 | 160.417629 | 0.000000 | 0 | 0 | 0 | 2026-10-07T02:18:37.635000+00:00 | none detected |
| arbi-10 | 0xd8d06aecfb5de45d0dcb655de57650d0231b0ef5 | 9.213546 | 9.213546 | 0.000000 | 0 | 0 | 0 | 2026-10-07T02:19:51.745000+00:00 | none detected |
| arbi-11 | 0x3b80eeb4bdcebdd93dbbbe16758020e07f41a65c | 68.821791 | 68.821791 | 0.000000 | 0 | 0 | 0 | 2026-10-07T02:29:14.118000+00:00 | none detected |
| arbi-12 | 0x1137e3fdf575bd635db491c2b60b5dac7ae74371 | 68.731854 | 68.731854 | 0.000000 | 0 | 0 | 0 | 2026-10-07T02:29:48.603000+00:00 | none detected |
| arbi-13 | 0x1b1c3046fa9dfc9d5ef66bf00d62a777044f829c | 68.581959 | 68.581959 | 0.000000 | 0 | 0 | 0 | 2026-10-07T02:31:29.735000+00:00 | none detected |
| arbi-14 | 0x97bfc50655ae2f06ed26ec5c67f476d2bdd0308f | 68.631924 | 68.631924 | 0.000000 | 0 | 0 | 0 | 2026-10-07T02:32:36.742000+00:00 | none detected |
| arbi-15 | 0x3bc6095627e177e7c4c7bf3f0e3c5182625ed81d | 68.581959 | 68.581959 | 0.000000 | 0 | 0 | 0 | 2026-10-07T02:33:53.782000+00:00 | none detected |
| arbi-16 | 0x278d8d16f49e88f3d706a804c6da24c6feccb3f0 | 69.931014 | 69.931014 | 0.000000 | 0 | 0 | 0 | 2026-10-07T02:44:14.018000+00:00 | none detected |
| arbi-17 | 0x122bc1c10b2ddba24dfa793ea7fa3fb2f934ce58 | 87.288855 | 87.288855 | 0.000000 | 0 | 0 | 0 | 2026-10-07T02:47:01.405000+00:00 | none detected |
| arbi-18 | 0x9b3b38f9969dee372c31549f33f66f8384d237a5 | 87.059016 | 87.059016 | 0.000000 | 0 | 0 | 0 | 2026-10-07T02:48:04.119000+00:00 | none detected |
| arbi-19 | 0x8ff77d08460a885e10131f124422dfe1c00ad4c3 | 86.989065 | 86.989065 | 0.000000 | 0 | 0 | 0 | 2026-10-07T02:52:17.158000+00:00 | none detected |
| arbi-20 | 0xe120d6d7042fabb3376f27e0e3351d7f3b913c0e | 86.629317 | 86.629317 | 0.000000 | 0 | 0 | 0 | 2026-10-07T02:54:07.488000+00:00 | none detected |
| arbi-21 | 0x6c3b32b002c3674e60c725345356be212fcba3c4 | 86.229597 | 86.229597 | 0.000000 | 0 | 0 | 0 | 2026-10-07T02:54:33.925000+00:00 | none detected |
| arbi-22 | 0xd97415ed800e8a16bb20953fe03be0becb0cd77c | 85.400178 | 85.400178 | 0.000000 | 0 | 0 | 0 | 2026-10-07T02:58:17.095000+00:00 | none detected |
| arbi-23 | 0x70dd5d5d1f65052f852f4918169a45b2cf97bf0b | 86.719254 | 86.719254 | 0.000000 | 0 | 0 | 0 | 2026-10-07T03:01:38.564000+00:00 | none detected |
| arbi-24 | 0x7140d59403a0383a5e929f53d664549a176b23f2 | 86.769219 | 86.769219 | 0.000000 | 0 | 0 | 0 | 2026-10-07T03:03:05.857000+00:00 | none detected |
| arbi-25 | 0xbe46fb8d0e5bf321716b3f1ea09ea1dcf1d4a2b8 | 86.579352 | 86.579352 | 0.000000 | 0 | 0 | 0 | 2026-10-07T03:04:39.276000+00:00 | none detected |
| arbi-26 | 0xc0396d9e21be49b5986e413ff2ab5297a1e6e346 | 85.120374 | 85.120374 | 0.000000 | 0 | 0 | 0 | 2026-10-07T03:06:54.308000+00:00 | none detected |
| arbi-27 | 0x6eef320de5c0db6bae5a80bbce3cb821efd5f5d7 | 84.84057 | 84.84057 | 0.00000 | 0 | 0 | 0 | 2026-10-07T03:07:02.328000+00:00 | none detected |
| arbi-28 | 0x4f55dc5c4fd5a8bbbfc64ef00ee4266ce214de34 | 84.870549 | 84.870549 | 0.000000 | 0 | 0 | 0 | 2026-10-07T03:08:02.013000+00:00 | none detected |
| arbi-29 | 0xc4b267ef5c98a4d3fee2b2279b2ac07abad93ef2 | 169.950951 | 169.950951 | 0.000000 | 0 | 0 | 0 | 2026-10-07T03:09:37.542000+00:00 | none detected |
| arbi-30 | 0xcccabc637364d6a6fe1ecf347b59d8e73ad4e9cc | 172.669047 | 172.669047 | 0.000000 | 0 | 0 | 0 | 2026-10-07T03:13:16.262000+00:00 | none detected |
| arbi-31 | 0x7cac0d851934a0cc58560a430a3f7ae907e3fb49 | 170.060874 | 170.060874 | 0.000000 | 0 | 0 | 0 | 2026-10-07T03:15:55.015000+00:00 | none detected |
| arbi-32 | 0xcf92ef3e2517968f04f372f0c2dd0d6873b2e230 | 71.140167 | 71.140167 | 0.000000 | 0 | 0 | 0 | 2026-10-07T03:25:39.019000+00:00 | none detected |
| arbi-33 | 0xceb5c49b9340f34f0c41a37a88c34806efcc1042 | 77.895435 | 77.895435 | 0.000000 | 0 | 0 | 0 | 2026-10-07T03:27:57.766000+00:00 | none detected |
| arbi-34 | 0x6da83a14fac1dd16e299c8537811abcefc783637 | 76.606338 | 76.606338 | 0.000000 | 0 | 0 | 0 | 2026-10-07T03:31:51.076000+00:00 | none detected |
| arbi-35 | 0xdf2633a6737599b879e9e74a96402dec400e44c1 | 74.307948 | 74.307948 | 0.000000 | 0 | 0 | 0 | 2026-10-07T03:37:25.691000+00:00 | none detected |
| additional-36 | 0xa8f219e59033fe2593151d951a142c1f958fd949 | 0.089937 | 0.089937 | 0.000000 | 0 | 0 | 0 | 2026-10-07T02:22:42.840000+00:00 | none detected |

## interpretation and publication readiness

the official info api documents a general 500-element/distinct-block pagination threshold and a fills-specific 2,000 response / 10,000 most-recent history limit. this comparison flags 500 or more records and missing baseline records; it never equates a failed request with zero activity. source: https://hyperliquid.gitbook.io/hyperliquid-docs/for-developers/api/info-endpoint .

where interval histories are empty, baseline histories remain present, and balances reconcile unchanged, the supported wording is: “no new fills or non-funding ledger activity was returned for these 36 addresses through the recorded history cutoff; the dated spot snapshots show the reported balances.” server-side retention, all other addresses, protocol-specific off-platform redemptions and native monero receipts are not independently proven. no native monero no-redemption claim is justified.

the bounded historical reconstruction remains publication-ready subject to final editorial review. this refresh supports a dated account-status paragraph only for successfully checked accounts. it does not resolve privacy cash withdrawal provenance, human control, exploit attribution, or the mixed-funding destination boundaries. the ethereum history improvement is new documentation of older events, not automatically activity since 13 november. no medium publication was performed.

## preservation and reproduction

the original checkpoint and all pre-existing files remain unchanged. `collect.py` and `collect_route.py` are read-only network collectors; do not rerun into this directory. `python build_report.py` reproduces account differences offline from retained responses. [baseline account inventory](baseline_accounts.json).
