# ZYROX post-freeze beneficiary/control research v0.115

**Date checked:** 2026-10-10 UTC

**Public baseline preserved:** v0.114 / ledger U453

**New research ledger:** U454–U465

**Assessment carried forward:** SUPPORTED COORDINATED OPERATIONAL STRUCTURE
**Frozen technical basis modified:** No

## Scope

This is a separate post-freeze research layer. It does not overwrite or amend `research/zyrox-investigation/evidence/ZYROX_Devsold_verification_v0_2.md`, does not redo seller accounting, and does not change the frozen 17-seller / 35-sale / 606.331808740 SOL/WSOL baseline.

The test was limited to the highest-value open beneficiary/control question around `HFAcfCGEcG323fFfaZtuSi6wua724q59QX5u3VkU1QjV` and the already documented PARTIAL / RE-ESTABLISHED endpoint wallets. The closed FEaT/H85K branch was not reopened. The previously completed 6hR7 identity/control test was not repeated because no new transaction-specific cross-wallet control edge was found.

Primary data were reproduced from finalized Solana mainnet `getSignaturesForAddress` and `getTransaction` responses using `jsonParsed` and `maxSupportedTransactionVersion=0`. Exact account pages at Solscan were used only as a public cross-check for curve/account/label display. The ordinary public-RPC/archive-index limitation remains: this is complete for the returned indexed histories, not a universal lifetime guarantee.

## Result

**A stronger re-established proceeds boundary is CONFIRMED at HFAc.** Twelve previously frozen positive-minimum intermediate endpoints emptied their balances to HFAc in twelve self-authorized System Program transfers. Their actual transfers total **9.897740861 SOL**. After conservatively charging each 0.000005 SOL sweep fee against the previously frozen FACv component, at least **8.563734158 SOL** of the prior PARTIAL / RE-ESTABLISHED minimum reaches HFAc.

This is not new sale revenue and is not added to the frozen global minimum. It moves an already counted boundary forward:

- frozen positive minimum at the twelve intermediate endpoints: **8.563794158 SOL**;
- twelve sweep fees: **0.000060000 SOL**;
- re-established minimum at HFAc: **8.563734158 SOL**;
- existing frozen G16-derived minimum already documented at HFAc: **7.723304078 SOL**;
- combined documented HFAc boundary: **16.287038236 SOL**.

The global conservative PARTIAL / RE-ESTABLISHED minimum remains **597.487092059 SOL**. CLEAN onward provenance remains **0 SOL**. Final beneficiary attribution remains **0 SOL**.

## Source-balance and transaction coverage

The twelve positive-minimum sources have bounded histories matching the continuation:

- ten sources have exactly two returned transactions: one frozen receipt and one full-balance sweep to HFAc;
- `ASD9…V8ED` has exactly three returned transactions: two frozen FrkA receipts and one full-balance sweep;
- `3eAt…1j82` has exactly three returned transactions: the frozen 1.500000000 SOL receipt, an unrelated 0.000001 SOL lookalike-prefix dust payment, and one full-balance sweep;
- every HFAc sweep below has the source wallet as sole signer and fee payer;
- no common external co-signer or fee payer appears across the twelve sweeps;
- no token, stake, bridge, router or exchange instruction appears in these continuation transactions.

`4jAbGBhcdrxDfDa6YLEjUCnmipMrbKtQZMej1hdpJ12E` also has a two-transaction history and sent 0.006313366 SOL to HFAc after its 0.000005 SOL fee. It is not ledgered here because its frozen individual FACv lower bound is zero; the transaction strengthens the collector pattern but does not create a positive proceeds-attribution amount.

## New ledger U454–U465

All `amount` values are actual SOL transferred. `FACv_proceeds_lower_bound_SOL` is the conservative source-specific component after the sweep fee. It is not an exact lamport allocation, CLEAN provenance, or additional income.

| ID | From → to | UTC / slot | Actual SOL | Source edge | FACv lower at HFAc | Full transaction | Signer / fee payer | Evidence and limitation |
|---|---|---|---:|---|---:|---|---|---|
| U454 | `ASD9zJkXM76iLQKcGrNpHL7k4L2dySZscmQqhjjrV8ED` → `HFAcfCGEcG323fFfaZtuSi6wua724q59QX5u3VkU1QjV` | 2026-10-01T19:40:55Z / 452384317 | 1.895694982 | U371 | 1.766603235 | `5odbrXfrEEhFaRp7MPMHx2ebYnGXJhykTppq9NEK3h4AA2B7Qp8XLkhTdKE8H8dEwMH3oZJYaxRbVLNKscmS3C2T` | ASD9 / ASD9 | CONFIRMED full-balance sweep less fee; beneficiary and common control UNRESOLVED |
| U455 | `3eAtcjSzwjZXBvDcJhUdPvrnxHhBMSm2N3wqN46x1j82` → HFAc | 2026-10-01T19:40:54Z / 452384314 | 1.499996000 | U373 | 1.397878513 | `4iAHJiMmZbgMVtHYneYq3oLkFUUfHtMko3oUrL9ikwU854Kx9eppbjLRwKFAJBJgM8LHnGX3kGtHLYbHR6i2kya8` | 3eAt / 3eAt | CONFIRMED sweep; includes 0.000001 SOL unrelated dust; no common control inference |
| U456 | `3VUzB89kmphS4ptNsUea2N5vBXKZer1oK29fYPdRgdbz` → HFAc | 2026-10-01T19:40:54Z / 452384316 | 1.495853129 | U375 | 1.382488642 | `5arZr2QALzP3oJYeXEXcumCJHHeSc1u8n7Rk9XySUw7kg3GmKT5K1DUbbnYyb1efT75yv6Gsa4157kw19Po925RU` | 3VUz / 3VUz | CONFIRMED full-balance sweep less fee; beneficial owner UNRESOLVED |
| U457 | `5jiyyMdc79vESWSfNpGY1c8GNNo84pWqXeEnDoegnWcL` → HFAc | 2026-10-01T19:40:54Z / 452384315 | 1.253183303 | U377 | 1.144129676 | `5MWWU1LFPxSPYLaC1C4ji3Qs3MuSBnymQRacoepU21iFxPaXNUYxfbUD3Ah1RjDiqu99PKp2XHZAizUKAHCA4RrZ` | 5jiy / 5jiy | CONFIRMED full-balance sweep less fee; beneficial owner UNRESOLVED |
| U458 | `AmV47hzxhAxVx6zkS8Sr7jEV8xPGApGCDQAXj8m3rdco` → HFAc | 2026-10-01T19:40:53Z / 452384312 | 0.791145868 | U379 | 0.673115902 | `3C4BqsJn8aQ8YArUxEKVRMf9aLU3uX8nyCvm4BnYiVQqgHcpsipxGDuSx7JFFDnMb7FerD5NgspzqStAVJuFsq9D` | AmV47 / AmV47 | CONFIRMED full-balance sweep less fee; beneficial owner UNRESOLVED |
| U459 | `CTcip75jgTWTwuYmxTVYxagA3gWUUXR9Dc2JnMYHSQC3` → HFAc | 2026-10-01T19:40:54Z / 452384314 | 0.655025365 | U381 | 0.539027418 | `3PxDyjAdXSxsZgZoW5x4cgmyZMskYt2595qZoWWSWAC2B1F6uqmbLFL7182dr4zAfuQGfxYxinyjzmnjs6AMvfUj` | CTcip / CTcip | CONFIRMED full-balance sweep less fee; beneficial owner UNRESOLVED |
| U460 | `HDLBnft93tW5MaBphvAsXm3q5DKVrFioixCUS3cdiy9F` → HFAc | 2026-10-01T19:40:53Z / 452384311 | 0.552421116 | U385 | 0.446888389 | `2viKAPRBpg5oeCMVy6XR2FaRbvr9pvpMGzoS9HFXjSkFRocDXZrZUoKrQW76cNsWpFEvR3ApwYApSTU6gWz47apx` | HDLB / HDLB | CONFIRMED full-balance sweep less fee; beneficial owner UNRESOLVED |
| U461 | `FM1aCKWwHX6chEeUNM3pjeTH1AN3vSitsy3L7eq6kkcr` → HFAc | 2026-10-01T19:40:53Z / 452384312 | 0.470089476 | U387 | 0.362103609 | `4JLUEXPqNUi7jffAq3vNanHHD9CcC2hAW1QFkTesixe5JpSnYpP1mRRw9AtoZtCzNZ3XHHKNjJtt6mSwwucXrsRm` | FM1a / FM1a | CONFIRMED full-balance sweep less fee; beneficial owner UNRESOLVED |
| U462 | `BRTrju1JzrTCQL4w6mPJQ8caY4Z3G5FUQDmXtaThMMoA` → HFAc | 2026-10-01T19:40:54Z / 452384316 | 0.419470922 | U389 | 0.316315755 | `5CridKwaHC8pJzXoJfdT257uTGNmdTdA7ju7rX2e3QCy3bd8xyz5BFFbPm8ETUZFX7K8u3Z41pNxnZt2oa9LpCHH` | BRTr / BRTr | CONFIRMED full-balance sweep less fee; beneficial owner UNRESOLVED |
| U463 | `3tpu3uxDqgYmqD3CWUDCBEbwShVE2b5xaeoGVsyoKD6Y` → HFAc | 2026-10-01T19:40:54Z / 452384316 | 0.352376069 | U391 | 0.226134042 | `XuEdReP4oaE5XeQoCqnNBoxK4Ben9dWhVtoADXUR9jCSUGVM7eTUmLDYjh241yE7nrCzMfpPjGKeHy9umospz4P` | 3tpu / 3tpu | CONFIRMED full-balance sweep less fee; beneficial owner UNRESOLVED |
| U464 | `2SFLrSe8icG4HHkZs2RmWUikyKLWTebWv9kgfXt5cFgc` → HFAc | 2026-10-01T19:40:53Z / 452384311 | 0.258293868 | U393 | 0.155680881 | `3PGQnaiVTS3XmQCMcxryTXqnidt52r9vuzGpWzsSb9c3cgwM3Wya6gShQ53ziS2bR4UYujDYn53HzTFxaB5nR47o` | 2SFL / 2SFL | CONFIRMED full-balance sweep less fee; beneficial owner UNRESOLVED |
| U465 | `Gyd8iEg2fZNAnhT9ar3hCpYQJBGUd622hSq43YkC39CY` → HFAc | 2026-10-01T19:40:53Z / 452384312 | 0.254190763 | U395 | 0.153368096 | `32epZDt62BdnCiaFTZUFK6mKZkXfwjNaMBGUtNfJHfvmgzUbUFZ9UZAfjmy9wgLRrFh8pSN1nkn77AeQkGLPSk3W` | Gyd8 / Gyd8 | CONFIRMED full-balance sweep less fee; beneficial owner UNRESOLVED |

## graph_edge U454–U465

```json
{"id":"U454","from":"ASD9zJkXM76iLQKcGrNpHL7k4L2dySZscmQqhjjrV8ED","to":"HFAcfCGEcG323fFfaZtuSi6wua724q59QX5u3VkU1QjV","edge_type":"provenance_continuation","asset":"SOL","amount":"1.895694982","timestamp":"2026-10-01T19:40:55Z","tx":"5odbrXfrEEhFaRp7MPMHx2ebYnGXJhykTppq9NEK3h4AA2B7Qp8XLkhTdKE8H8dEwMH3oZJYaxRbVLNKscmS3C2T","signer":["ASD9zJkXM76iLQKcGrNpHL7k4L2dySZscmQqhjjrV8ED"],"fee_payer":"ASD9zJkXM76iLQKcGrNpHL7k4L2dySZscmQqhjjrV8ED","authority":"native sender; sole signer and fee payer; full-balance sweep less 0.000005 SOL fee","source_edge_ref":"U371","provenance_status":"PARTIAL / RE-ESTABLISHED PROVENANCE","FACv_proceeds_lower_bound_SOL":"1.766603235","FACv_proceeds_upper_bound_SOL":"1.895694982","evidence_status":"CONFIRMED transaction and conservative bounded continuation; no beneficial-owner inference"}
{"id":"U455","from":"3eAtcjSzwjZXBvDcJhUdPvrnxHhBMSm2N3wqN46x1j82","to":"HFAcfCGEcG323fFfaZtuSi6wua724q59QX5u3VkU1QjV","edge_type":"provenance_continuation","asset":"SOL","amount":"1.499996000","timestamp":"2026-10-01T19:40:54Z","tx":"4iAHJiMmZbgMVtHYneYq3oLkFUUfHtMko3oUrL9ikwU854Kx9eppbjLRwKFAJBJgM8LHnGX3kGtHLYbHR6i2kya8","signer":["3eAtcjSzwjZXBvDcJhUdPvrnxHhBMSm2N3wqN46x1j82"],"fee_payer":"3eAtcjSzwjZXBvDcJhUdPvrnxHhBMSm2N3wqN46x1j82","authority":"native sender; sole signer and fee payer; full-balance sweep including unrelated 0.000001 SOL dust and less fee","source_edge_ref":"U373","provenance_status":"PARTIAL / RE-ESTABLISHED PROVENANCE","FACv_proceeds_lower_bound_SOL":"1.397878513","FACv_proceeds_upper_bound_SOL":"1.499996000","evidence_status":"CONFIRMED transaction and conservative bounded continuation; no beneficial-owner inference"}
{"id":"U456","from":"3VUzB89kmphS4ptNsUea2N5vBXKZer1oK29fYPdRgdbz","to":"HFAcfCGEcG323fFfaZtuSi6wua724q59QX5u3VkU1QjV","edge_type":"provenance_continuation","asset":"SOL","amount":"1.495853129","timestamp":"2026-10-01T19:40:54Z","tx":"5arZr2QALzP3oJYeXEXcumCJHHeSc1u8n7Rk9XySUw7kg3GmKT5K1DUbbnYyb1efT75yv6Gsa4157kw19Po925RU","signer":["3VUzB89kmphS4ptNsUea2N5vBXKZer1oK29fYPdRgdbz"],"fee_payer":"3VUzB89kmphS4ptNsUea2N5vBXKZer1oK29fYPdRgdbz","authority":"native sender; sole signer and fee payer; full-balance sweep less fee","source_edge_ref":"U375","provenance_status":"PARTIAL / RE-ESTABLISHED PROVENANCE","FACv_proceeds_lower_bound_SOL":"1.382488642","FACv_proceeds_upper_bound_SOL":"1.495853129","evidence_status":"CONFIRMED transaction and conservative bounded continuation; no beneficial-owner inference"}
{"id":"U457","from":"5jiyyMdc79vESWSfNpGY1c8GNNo84pWqXeEnDoegnWcL","to":"HFAcfCGEcG323fFfaZtuSi6wua724q59QX5u3VkU1QjV","edge_type":"provenance_continuation","asset":"SOL","amount":"1.253183303","timestamp":"2026-10-01T19:40:54Z","tx":"5MWWU1LFPxSPYLaC1C4ji3Qs3MuSBnymQRacoepU21iFxPaXNUYxfbUD3Ah1RjDiqu99PKp2XHZAizUKAHCA4RrZ","signer":["5jiyyMdc79vESWSfNpGY1c8GNNo84pWqXeEnDoegnWcL"],"fee_payer":"5jiyyMdc79vESWSfNpGY1c8GNNo84pWqXeEnDoegnWcL","authority":"native sender; sole signer and fee payer; full-balance sweep less fee","source_edge_ref":"U377","provenance_status":"PARTIAL / RE-ESTABLISHED PROVENANCE","FACv_proceeds_lower_bound_SOL":"1.144129676","FACv_proceeds_upper_bound_SOL":"1.253183303","evidence_status":"CONFIRMED transaction and conservative bounded continuation; no beneficial-owner inference"}
{"id":"U458","from":"AmV47hzxhAxVx6zkS8Sr7jEV8xPGApGCDQAXj8m3rdco","to":"HFAcfCGEcG323fFfaZtuSi6wua724q59QX5u3VkU1QjV","edge_type":"provenance_continuation","asset":"SOL","amount":"0.791145868","timestamp":"2026-10-01T19:40:53Z","tx":"3C4BqsJn8aQ8YArUxEKVRMf9aLU3uX8nyCvm4BnYiVQqgHcpsipxGDuSx7JFFDnMb7FerD5NgspzqStAVJuFsq9D","signer":["AmV47hzxhAxVx6zkS8Sr7jEV8xPGApGCDQAXj8m3rdco"],"fee_payer":"AmV47hzxhAxVx6zkS8Sr7jEV8xPGApGCDQAXj8m3rdco","authority":"native sender; sole signer and fee payer; full-balance sweep less fee","source_edge_ref":"U379","provenance_status":"PARTIAL / RE-ESTABLISHED PROVENANCE","FACv_proceeds_lower_bound_SOL":"0.673115902","FACv_proceeds_upper_bound_SOL":"0.791145868","evidence_status":"CONFIRMED transaction and conservative bounded continuation; no beneficial-owner inference"}
{"id":"U459","from":"CTcip75jgTWTwuYmxTVYxagA3gWUUXR9Dc2JnMYHSQC3","to":"HFAcfCGEcG323fFfaZtuSi6wua724q59QX5u3VkU1QjV","edge_type":"provenance_continuation","asset":"SOL","amount":"0.655025365","timestamp":"2026-10-01T19:40:54Z","tx":"3PxDyjAdXSxsZgZoW5x4cgmyZMskYt2595qZoWWSWAC2B1F6uqmbLFL7182dr4zAfuQGfxYxinyjzmnjs6AMvfUj","signer":["CTcip75jgTWTwuYmxTVYxagA3gWUUXR9Dc2JnMYHSQC3"],"fee_payer":"CTcip75jgTWTwuYmxTVYxagA3gWUUXR9Dc2JnMYHSQC3","authority":"native sender; sole signer and fee payer; full-balance sweep less fee","source_edge_ref":"U381","provenance_status":"PARTIAL / RE-ESTABLISHED PROVENANCE","FACv_proceeds_lower_bound_SOL":"0.539027418","FACv_proceeds_upper_bound_SOL":"0.655025365","evidence_status":"CONFIRMED transaction and conservative bounded continuation; no beneficial-owner inference"}
{"id":"U460","from":"HDLBnft93tW5MaBphvAsXm3q5DKVrFioixCUS3cdiy9F","to":"HFAcfCGEcG323fFfaZtuSi6wua724q59QX5u3VkU1QjV","edge_type":"provenance_continuation","asset":"SOL","amount":"0.552421116","timestamp":"2026-10-01T19:40:53Z","tx":"2viKAPRBpg5oeCMVy6XR2FaRbvr9pvpMGzoS9HFXjSkFRocDXZrZUoKrQW76cNsWpFEvR3ApwYApSTU6gWz47apx","signer":["HDLBnft93tW5MaBphvAsXm3q5DKVrFioixCUS3cdiy9F"],"fee_payer":"HDLBnft93tW5MaBphvAsXm3q5DKVrFioixCUS3cdiy9F","authority":"native sender; sole signer and fee payer; full-balance sweep less fee","source_edge_ref":"U385","provenance_status":"PARTIAL / RE-ESTABLISHED PROVENANCE","FACv_proceeds_lower_bound_SOL":"0.446888389","FACv_proceeds_upper_bound_SOL":"0.552421116","evidence_status":"CONFIRMED transaction and conservative bounded continuation; no beneficial-owner inference"}
{"id":"U461","from":"FM1aCKWwHX6chEeUNM3pjeTH1AN3vSitsy3L7eq6kkcr","to":"HFAcfCGEcG323fFfaZtuSi6wua724q59QX5u3VkU1QjV","edge_type":"provenance_continuation","asset":"SOL","amount":"0.470089476","timestamp":"2026-10-01T19:40:53Z","tx":"4JLUEXPqNUi7jffAq3vNanHHD9CcC2hAW1QFkTesixe5JpSnYpP1mRRw9AtoZtCzNZ3XHHKNjJtt6mSwwucXrsRm","signer":["FM1aCKWwHX6chEeUNM3pjeTH1AN3vSitsy3L7eq6kkcr"],"fee_payer":"FM1aCKWwHX6chEeUNM3pjeTH1AN3vSitsy3L7eq6kkcr","authority":"native sender; sole signer and fee payer; full-balance sweep less fee","source_edge_ref":"U387","provenance_status":"PARTIAL / RE-ESTABLISHED PROVENANCE","FACv_proceeds_lower_bound_SOL":"0.362103609","FACv_proceeds_upper_bound_SOL":"0.470089476","evidence_status":"CONFIRMED transaction and conservative bounded continuation; no beneficial-owner inference"}
{"id":"U462","from":"BRTrju1JzrTCQL4w6mPJQ8caY4Z3G5FUQDmXtaThMMoA","to":"HFAcfCGEcG323fFfaZtuSi6wua724q59QX5u3VkU1QjV","edge_type":"provenance_continuation","asset":"SOL","amount":"0.419470922","timestamp":"2026-10-01T19:40:54Z","tx":"5CridKwaHC8pJzXoJfdT257uTGNmdTdA7ju7rX2e3QCy3bd8xyz5BFFbPm8ETUZFX7K8u3Z41pNxnZt2oa9LpCHH","signer":["BRTrju1JzrTCQL4w6mPJQ8caY4Z3G5FUQDmXtaThMMoA"],"fee_payer":"BRTrju1JzrTCQL4w6mPJQ8caY4Z3G5FUQDmXtaThMMoA","authority":"native sender; sole signer and fee payer; full-balance sweep less fee","source_edge_ref":"U389","provenance_status":"PARTIAL / RE-ESTABLISHED PROVENANCE","FACv_proceeds_lower_bound_SOL":"0.316315755","FACv_proceeds_upper_bound_SOL":"0.419470922","evidence_status":"CONFIRMED transaction and conservative bounded continuation; no beneficial-owner inference"}
{"id":"U463","from":"3tpu3uxDqgYmqD3CWUDCBEbwShVE2b5xaeoGVsyoKD6Y","to":"HFAcfCGEcG323fFfaZtuSi6wua724q59QX5u3VkU1QjV","edge_type":"provenance_continuation","asset":"SOL","amount":"0.352376069","timestamp":"2026-10-01T19:40:54Z","tx":"XuEdReP4oaE5XeQoCqnNBoxK4Ben9dWhVtoADXUR9jCSUGVM7eTUmLDYjh241yE7nrCzMfpPjGKeHy9umospz4P","signer":["3tpu3uxDqgYmqD3CWUDCBEbwShVE2b5xaeoGVsyoKD6Y"],"fee_payer":"3tpu3uxDqgYmqD3CWUDCBEbwShVE2b5xaeoGVsyoKD6Y","authority":"native sender; sole signer and fee payer; full-balance sweep less fee","source_edge_ref":"U391","provenance_status":"PARTIAL / RE-ESTABLISHED PROVENANCE","FACv_proceeds_lower_bound_SOL":"0.226134042","FACv_proceeds_upper_bound_SOL":"0.352376069","evidence_status":"CONFIRMED transaction and conservative bounded continuation; no beneficial-owner inference"}
{"id":"U464","from":"2SFLrSe8icG4HHkZs2RmWUikyKLWTebWv9kgfXt5cFgc","to":"HFAcfCGEcG323fFfaZtuSi6wua724q59QX5u3VkU1QjV","edge_type":"provenance_continuation","asset":"SOL","amount":"0.258293868","timestamp":"2026-10-01T19:40:53Z","tx":"3PGQnaiVTS3XmQCMcxryTXqnidt52r9vuzGpWzsSb9c3cgwM3Wya6gShQ53ziS2bR4UYujDYn53HzTFxaB5nR47o","signer":["2SFLrSe8icG4HHkZs2RmWUikyKLWTebWv9kgfXt5cFgc"],"fee_payer":"2SFLrSe8icG4HHkZs2RmWUikyKLWTebWv9kgfXt5cFgc","authority":"native sender; sole signer and fee payer; full-balance sweep less fee","source_edge_ref":"U393","provenance_status":"PARTIAL / RE-ESTABLISHED PROVENANCE","FACv_proceeds_lower_bound_SOL":"0.155680881","FACv_proceeds_upper_bound_SOL":"0.258293868","evidence_status":"CONFIRMED transaction and conservative bounded continuation; no beneficial-owner inference"}
{"id":"U465","from":"Gyd8iEg2fZNAnhT9ar3hCpYQJBGUd622hSq43YkC39CY","to":"HFAcfCGEcG323fFfaZtuSi6wua724q59QX5u3VkU1QjV","edge_type":"provenance_continuation","asset":"SOL","amount":"0.254190763","timestamp":"2026-10-01T19:40:53Z","tx":"32epZDt62BdnCiaFTZUFK6mKZkXfwjNaMBGUtNfJHfvmgzUbUFZ9UZAfjmy9wgLRrFh8pSN1nkn77AeQkGLPSk3W","signer":["Gyd8iEg2fZNAnhT9ar3hCpYQJBGUd622hSq43YkC39CY"],"fee_payer":"Gyd8iEg2fZNAnhT9ar3hCpYQJBGUd622hSq43YkC39CY","authority":"native sender; sole signer and fee payer; full-balance sweep less fee","source_edge_ref":"U395","provenance_status":"PARTIAL / RE-ESTABLISHED PROVENANCE","FACv_proceeds_lower_bound_SOL":"0.153368096","FACv_proceeds_upper_bound_SOL":"0.254190763","evidence_status":"CONFIRMED transaction and conservative bounded continuation; no beneficial-owner inference"}
```

## HFAc role, controls and downstream boundary

HFAc has **32** returned successful transactions: **31** incoming System Program transfers totaling exactly **32.335580032 SOL**, followed by one HFAc-signed transaction. HFAc is on-curve. Solscan displayed no named exchange/service label and currently shows zero balance/account not present on-chain.

At 2026-10-01T19:45:12Z, HFAc was sole signer and fee payer in transaction `4yrQXHrpi5Po27RJXsaGLDLNzGcWrbqtU8w7z9dDXvhtm4e4HfmL8p3pvty1pk8JM4hSz1tADf5VuQxkVszKT2aZ`:

- pre-balance: **32.335580032 SOL**;
- HFAc → FEaT: **27.485238778 SOL**;
- HFAc → `99GcqafMcohBvKDw9pR1TXQuAXzB4ZEU3JWLWz7eNtTm`: **4.850336254 SOL**;
- fee: **0.000005000 SOL**;
- post-balance: **0 SOL**.

The FEaT recipient already held **14.582065593 SOL** before the receipt. The `99Gc` recipient already held **2.199135509 SOL** before the receipt. HFAc had itself combined 31 inflows. No instruction or segregated account assigns any specific FACv component to either output. Proceeds provenance therefore stops at HFAc as **UNRESOLVED MIXED FUNDS**.

`99Gc` was tested only for bounded endpoint classification. It is an on-curve System wallet with 51 returned transactions from 2026-08-16 through 2026-10-07, continuing activity after the HFAc receipt, nonzero prior balance, and no public Solscan service label. Exact-address public searches returned no authoritative exchange, bridge, custodian or operator binding. It is classified as a **persistent mixed wallet of unknown role**, not an exchange/service endpoint. Its fan-out was not followed.

No HFAc transaction has an external signer/co-signer or external fee payer acting for HFAc. HFAc controls its own split transaction; each intermediate source controls its own sweep. That is a transaction-specific account relationship and a stronger collector boundary, not proof that one private key, person or beneficial owner controls all wallets.

## Evidence classification and close

- **CONFIRMED:** twelve exact full-balance continuation edges U454–U465; actual aggregate 9.897740861 SOL; conservative FACv component 8.563734158 SOL at HFAc; HFAc self-authorized split of its complete 32.335580032 SOL balance.
- **SUPPORTED:** HFAc is a common operational collector/routing boundary for multiple previously documented seller branches. This strengthens the existing coordinated-operational interpretation at the account-relationship level, not common ownership.
- **UNRESOLVED:** HFAc operator, intermediate-wallet operator(s), common private-key control, beneficial owner, final beneficiary, and specific service/custody identity.
- **New named service/exchange/custody boundary:** none.
- **New cross-wallet control signal:** none. All debits are separately self-authorized; no common co-signer, fee payer or authority was found.
- **Beneficiary attribution advanced:** no. The traceability boundary advanced to HFAc, but identified-beneficiary attribution remains 0 SOL.
- **ZYROX–Kytro linkage:** unchanged; no new transaction-specific connection.
- **Closed as exhausted:** HFAc downstream provenance at the mixed split; `99Gc` as a persistent mixed unlabeled wallet; FEaT/H85K remains closed; 6hR7 remains unchanged and closed absent new direct evidence.
- **Next concrete lead:** an independently verifiable exchange/custody/operator address binding for HFAc or `99Gc`, or a new transaction with a common external signer/fee payer/authority. Without that, further on-chain fan-out is not defensible beneficiary attribution.

**Checkpoint:** post-freeze research v0.115 / U465. Next available ledger ID U466. Frozen public technical basis v0.114 / U453 remains byte-for-byte unchanged.
