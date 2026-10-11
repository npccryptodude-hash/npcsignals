# ZYROX IsItBundled lead — v0.117

## Scope and checkpoint

Reviewed 2026-10-11 from public repository commit `6f5e17d265ea45edffb78a89a80b844a69760a42`.

- Frozen technical basis: **v0.114 / U453**, unchanged.
- Latest pre-existing post-freeze research: **v0.116 / U465**.
- This file is a separate lead review. No seller accounting was reopened.
- No new independently verified transaction edge was found, so **no U466 filler entry is created**. Next available ledger ID remains **U466**.
- Current assessment remains **SUPPORTED COORDINATED OPERATIONAL STRUCTURE**. Common beneficial owner, final beneficiary, human operator, intent, fraud, and a transaction-specific ZYROX–Kytro control link remain UNRESOLVED.

## Sources and capture manifest

| Source | Capture UTC | Archived artifact | Evidence class |
|---|---|---|---|
| `GET https://isitbundled.com/api/v1/token/FACvJMFBWQ1GYm9dgZ7XHvs85V1EcK2SqHf534kspump` | 2026-10-11T05:52:22Z | `raw/isitbundled_token_FACv_2026-10-11T055222Z.json` | Immutable third-party API response |
| `https://isitbundled.com/FACvJMFBWQ1GYm9dgZ7XHvs85V1EcK2SqHf534kspump` | 2026-10-11T05:52:22Z | `raw/isitbundled_report_capture_2026-10-11T055222Z.md` | Rendered third-party report capture |
| Rendered “Copy 104 wallets” table, account-link order | 2026-10-11T05:52:22Z | `raw/isitbundled_zyrox_104_wallets_2026-10-11T055222Z.csv` | Exact addresses and displayed order; site classifications not primary evidence |
| `GET /api/v1/wallets` for five screenshot abbreviations | 2026-10-11T05:52:22Z | `raw/isitbundled_wallet_resolution_2026-10-11T055222Z.json` | Third-party API resolution with exact-address collision check |
| Solana mainnet JSON-RPC `getTransaction` for the three launch-slot transactions | 2026-10-11T05:59:14Z | Transaction signatures and deterministic summary below | Primary chain data recheck |

The IsItBundled API documentation was also read at <https://isitbundled.com/api>. It says shortened wallet queries need at least a four-character prefix and three-character suffix; a shortened collision or miss returns a null address. The five screenshot identifiers resolved uniquely in one batch request.

## Exact shortened-address resolutions

| Screenshot form | Exact address | IsItBundled role response for FACv | Previously present in frozen technical report? |
|---|---|---|---|
| `BM9C…jvMN` | `BM9CcyErJcu2mjrFvUsRRrD3snGeHDDVirJLvL6EjvMN` | no token-specific API role; one prior bundler launch in the database | No |
| `J7gN…KSu6` | `J7gN6Tds5XG2E8zAocKqjLLdcjBVBT4Btomk4LRLKSu6` | `proxima`, `handoff` | Yes |
| `Wksb…JmLt` | `Wksb8WrEFFSeCcyhmxHGK79iFxbA89x8yeWSqgYJmLt` | `proxima`, `handoff`, `sniper` | Yes |
| `Hze7…yQ7U` | `Hze7aNNaW1VewzesJLAUvgrvoKkaMSTX4N4Qu7CSyQ7U` | `proxima`, `handoff` | Yes |
| `Hp4q…yyod` | `Hp4q9Tfeo5Cp7BuFNe6pRo3DqfPZVAiEampauGzPyyod` | `bundle`, `proxima` | Yes |

These are exact API resolutions. The role labels remain IsItBundled classifications and do not by themselves prove common control or ownership.

## Deterministic overlap with the frozen report

All 104 report-table addresses were compared as exact strings with full Solana addresses in `research/zyrox-investigation/evidence/ZYROX_Devsold_verification_v0_2.md`.

- Exact overlap: **88 / 104**.
- Not previously present: **16 / 104**.
- The 88 overlaps are displayed positions 2–89; position 1 (`BM9C…jvMN`) and positions 90–104 are outside the frozen full-address set.
- This high exact overlap shows that the external table substantially describes the already documented launch/consolidation population. It does not independently validate every role label or one-operator conclusion.

The 16 addresses not previously present are:

`BM9CcyErJcu2mjrFvUsRRrD3snGeHDDVirJLvL6EjvMN`, `27HFmP7ccLadGswvQfvea4o3juLw75cPF4V6jWpHM3MX`, `4JSJp3yuLRFwboNw2G5k2vJkonYvPB71SjRcJpvuRMJ3`, `mwamTohZTS8VVDXhJBwEFzmWbbaax5sSYY8e8Vxu6HG`, `DB9rg75K41gaij6h7tELhLJ3age91bJEroGCzGt6BpTf`, `Cm5iFPf6ZkCbhLQxP4FQamoS9MQ37ap7M11Sd6exRGNu`, `Ejou6sqNEfSq9n45gyekRrwnN7FWjPNsFdu4g2Uvh3aU`, `9xcgNY7J6giBfCLkCRYw9B2srhUtatE15A5uM8pxqfQS`, `D12RJL1sdxptto6VprUg3syu7pUsLF4p3TgZHu7UMPBd`, `Fn9n3ftUzjhcmoLwXbTqJdATzamCp3xPEu4LmLSS8ELr`, `33Q8VPWS6JVm5P37T9PEgTL6DQUC1vbEXnJ3UxHhcibN`, `3YQafFQk7qJfkgbnUipgb32BoaQdPwjvGLECNsZtaFZD`, `Enxo61QiYSLZ114N8uaR7XJSf5bXqaiZSg66262tLjdL`, `2ma47ERFyP3xgMUkJN1UyxFtRog9VXc8JyPFmPwAE5yc`, `F1G2hw4fgb5mwk7ShiVKZM93f18exihenWMSJea28Qcp`, and `FBjEn5QHQa9SXtYxrBrCTWueENfK1iy1KXqRMLCx24JR`.

The site describes positions 90–98 as sniper/known-bundler rows and positions 99–104 as `Linked`. Those labels are third-party assertions. No case-specific control or proceeds edge for the 16 was independently established in this bounded review, so no ledger entries are added.

## Launch-slot reconstruction

Solana mainnet JSON-RPC rechecks returned all three transactions in slot **452029524**, blockTime **1790788686 = 2026-09-30T17:18:06Z**.

| Buyer / role | FACv acquired | Share of initial 1B | Same-tx direct market payment already verified in frozen report | Signer and fee payer |
|---|---:|---:|---:|---|
| HZrAo creator | 100,000,000.000000 | 10.0000000000000% | 3.083247688 SOL | HZrAo; mint also signs account creation |
| Hp4q | 693,100,000.000000 | 69.3100000000000% | 81.922111372 SOL | Hp4q / Hp4q |
| Hrpa | 26,899,999.998698 | 2.689999998698% | 12.703877261 SOL/WSOL | Hrpa / Hrpa |
| **Total** | **819,999,999.998698** | **81.9999999998698%** | **97.709236321 SOL/WSOL** | Three separate payer domains |

The API/report's **82%** and **97.71 SOL** are therefore reproduced as rounded launch-slot figures using the initial one-billion-token denominator. The mint transaction creates one billion FACv, assigns 100M to the creator-controlled token account, and leaves 900M in program custody before the two other launch-slot buys.

Important window limit: the site's rendered report says “3 buys in the launch block” and also labels 82% as “first second”. Solana `blockTime` Has second resolution. Tmcg's independently documented 137,587,563.532596 FACv buy occurs two slots later but still has the same `17:18:06` blockTime, after Hp4q's first sale. Thus **82% is confirmed for the launch slot**, while interpreting it as every acquisition with the same UTC second would be methodologically incorrect without a finer site definition.

No common external signer or fee payer exists across the three launch-slot transactions: each buyer signs and pays for its own transaction. This recheck does not prove shared private-key control.

## Funding-together / temporary-relay claim

The site reports `fundedTogether: 3` and `throwawayFunded: 3`. Its rendered rows show first funding at 17:16:22 for HZrAo, 17:16:39 for Hp4q, and 17:16:44 for Hrpa, all within UTC minute 17:16 and 82–104 seconds before launch.

Existing frozen work already independently documents:

- `8y1Y…Hq2p → HZrAo` at 17:16:22;
- `G1W7… 1TGN → Hp4q` at 17:16:39;
- `GmJg…gX8v → Hrpa` at 17:16:44;
- longer transaction-specific paths from shared upstream node BbBZ into the creator, Hp4q, and Hrpa branches.

This supports the factual existence of timed relay funding and the previously classified shared upstream relationship. It does **not** newly establish one private-key operator or beneficial owner, and the already ledgered funding paths are not duplicated.

## Proxima attribution status

The site labels the token `madeWithProxima`, reports 87 Proxima wallets, and links its proof to program `8gxk64hYgGAEnHVhRMvBGVvBXZM5WhkGkaQ6DVgVV2kn`.

The frozen report already independently verifies case transactions invoking `8gxk…V2kn`, program-derived CUo7 transfers, and a deployer/upgrade-authority role for GVt5. That chain evidence supports **use of the identified program infrastructure in relevant transactions**. It does not validate the site's stronger phrasing that 87 wallets were controlled by one real-world operator. No new shared external signer, fee payer, account authority, or private-key controller across all 87 wallets was found here.

Classification remains:

- **CONFIRMED:** specific 8gxk program invocation and already ledgered transaction roles.
- **SUPPORTED:** coordinated operational structure already documented in v0.114.
- **UNRESOLVED:** whether all 87 site-labelled wallets share one human/private-key operator or beneficial owner.

## “66 hidden-selling pairs” status

The rendered report asserts 66 same-amount sell/buy matches and shows a `Hand-offs 66` filter. The public token API provides only summary counts; the rendered page did not expose a machine-readable list of 66 source/destination transaction-signature pairs or the full matching tolerance/window.

The frozen report independently verifies many early purchases and the later 64-wallet FACv consolidation into G16. Those are not automatically equivalent to 66 matched market sell/buy pairs. Without the complete pair manifest and transaction-specific reconstruction, the claim remains **UNRESOLVED / THIRD-PARTY ASSERTION**. Timing and amount similarity alone are not promoted to control, ownership, or intent evidence.

## Metric reconciliation

The site presents three distinct states:

1. `Bundle already sold: 88%` — a sale-only fraction of what the site classifies as bundle holdings.
2. `100% sold or moved` — combines sales and token movements.
3. `Insiders hold now: 0%` / API `insidersHoldPct: 0` and `flaggedHoldPct: 0` — current-balance fields at the report snapshot.

These fields use different operations and possibly different wallet sets/time windows. They are not substituted for the frozen 17-seller / 35-sale accounting, 606.331808740 SOL/WSOL receipts, or beneficiary attribution. The site's 806.3-SOL buys and 848.5-SOL sales are broad caught-wallet trade totals and must not be treated as net profit or final-beneficiary receipts.

The rendered seven-minute peak of approximately $466.7K is also retained as a separate site/chart metric. It does not overwrite the frozen report's independently documented approximately $516,492 initial-supply-normalized aggregator candle, which uses a different source/method.

## Evidence result

### New independently confirmed facts

- Exact resolution of the five shortened screenshot identifiers.
- Exact export of all 104 report-table wallet addresses and displayed order.
- 88 exact address overlaps with the frozen technical report.
- Reproduction of the 82% launch-slot figure and 97.71-SOL rounded spend from primary transaction data.

These are research/report facts, not new transaction edges. No U466 entry is warranted.

### Not advanced

- No new case-specific control signal.
- No new beneficiary or identity attribution.
- No new service/custody endpoint.
- No transaction-specific ZYROX–Kytro link.
- No independent verification of the 66 claimed matched sell/buy pairs.
- No upgrade from SUPPORTED coordination to common owner/operator.

## Recommendation / next concrete lead

Pursue only a transaction-level export or reproducible manifest for the 66 alleged sell/buy pairs: seller signature, buyer signature, slot/index, exact raw FACv amount, market/program, signer, fee payer, pre/post balances, and the site's matching rule. Test a bounded sample first against the already verified 64 source-wallet purchase/consolidation data. If the provider cannot supply exact pairs and methodology, close the 66-pair assertion as non-verifiable rather than fan out through the 16 newly listed sniper/linked wallets.

The frozen v0.114/U453 file was not edited. Ledger remains U465; next ID U466.
