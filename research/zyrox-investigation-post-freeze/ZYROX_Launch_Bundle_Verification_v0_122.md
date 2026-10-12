# ZYROX launch-bundle verification v0.122

**ZYROX research baseline:** public commit `1ebc01f4dddd6350990750b8ca8b76408a449297` / v0.121 / U493  
**Repository tip recovered before work:** `64c5d714bf3a01ddce3e2b38e82f76191dca6ecd` (unrelated later research; no ZYROX-path changes)  
**This checkpoint:** v0.122 / U494  
**Research date:** 2026-10-12 UTC  
**Scope:** four known launch transactions and one recovered bundle ID only

## Result

The historical Jito record is independently reproduced. The ZYROX creator transaction, Hp4q purchase, intermediate migration and Hrpa purchase are the four ordered transactions in Jito bundle:

`bf5d05ae5acb728d02bd0f6e15c8e944f0dbe77874c5a6e6291b374cbcd011ed`

The Jito historical index maps each exact transaction signature to that same bundle ID. Its bundle endpoint lists exactly those four signatures in the same order as finalized Solana block indices 1330–1333. This is **CONFIRMED common Jito bundle membership**, not merely same-slot timing.

## Recovery and duplicate control

- Public `main` had advanced from `1ebc01f…` to `64c5d71…`, but no file under either ZYROX research path changed.
- No v0.122 checkpoint, U494 entry, bundle manifest or launch-bundle collector had been saved before the interruption.
- Existing v0.117, v0.118 and v0.121 findings were compared before this entry was created. They did not contain the historical bundle ID.
- Frozen v0.114/U453 and all existing entries U001–U493 are unchanged.
- No wallet history, funding branch, seller accounting, beneficiary branch or Kytro material was opened.

## Evidence sources and reproducibility

The bundle evidence comes from Jito's own historical Explorer/index infrastructure, not from IsItBundled or another third-party scanner:

- Explorer record: <https://explorer.jito.wtf/bundle/bf5d05ae5acb728d02bd0f6e15c8e944f0dbe77874c5a6e6291b374cbcd011ed>
- Historical bundle API: <https://bundles.jito.wtf/api/v1/bundles/bundle/bf5d05ae5acb728d02bd0f6e15c8e944f0dbe77874c5a6e6291b374cbcd011ed>
- Per-transaction lookup pattern: `https://bundles.jito.wtf/api/v1/bundles/transaction/{signature}`
- Jito documentation: <https://docs.jito.wtf/lowlatencytxnsend/>. It defines bundles as sequential and atomic, and directs readers with a bundle ID to Jito Explorer.
- Independent chain source: finalized Solana JSON-RPC `getBlock`, `getTransaction` and block rewards from <https://api.mainnet-beta.solana.com>.

The saved collector queries only this slot, these four signatures and this bundle ID. The generated manifest retains the exact Jito responses, Solana block metadata, signer/fee-payer roles, fees, compute units, instruction summaries, direct tip transfer and canonical hashes of the four finalized transaction responses.

Jito Block Engine `getBundleStatuses` returned no retained historical value, and `getInflightBundleStatuses` returned `Invalid`. Jito documents the latter as a recent/in-flight status method. Those live status responses cannot adjudicate a ten-day-old bundle and are preserved only as a data-availability limitation; they do not contradict the historical landed record.

## Verified transaction order

All four transactions finalized in slot `452029524` at `2026-09-30T17:18:06Z`.

| Block index | Role | Exact signature | Signer(s) | Fee payer | Fee / CU |
| ---: | --- | --- | --- | --- | ---: |
| 1330 | Creator create + buy | `5ubvNRPDbdXtHaiexB4zroZxUDFS9mwDmDwJ3HnvdGrxuiqxDDGsZnkjdAGVHysDZgiCFqVASoinDu1bADPAbowo` | HZrAo; FACv mint account | HZrAo | 88,487 lamports / 209,287 |
| 1331 | Hp4q launch purchase | `52ZjUbg4bzdQoAsFeJuLgqM5b5kmeQpgp79ndnAi13D7W795N8A7BLon9t7LhENRi5wUGcqMb5RWzNDs2AB9nKkw` | Hp4q | Hp4q | 105,294 lamports / 163,270 |
| 1332 | Intermediate migration / AMM creation | `2MP6ABDBuCgMyAysTyNYjuFdR1AJ9eHJn4tzr1ae7DgHsYhEAsGgetnWVVpaatbZ1Dunk5Ns96PHxPm6q8gawdLB` | Hrpa | Hrpa | 5,250 lamports / 331,222 |
| 1333 | Hrpa AMM launch purchase | `4JrhsmKT44mQpZh5kTYFMcFWXi2Hu8Lg3U5BkUS4WEw66pWeR7GkiR299KY2WFD5XZQTH5pvBMW957WrdjjRh5Xf` | Hrpa | Hrpa | 434,656 lamports / 142,114 |

The bundle record reports `blockIndex: 1330`, four signatures, `landedCu: 845893`, validator identity `E1r4Psq84tHfQ6aPTvvDka4U3u8zPVD7gEUrH25RdxHL` and a 3,000,000-lamport landed tip. The four independently retrieved transactions consume exactly 845,893 compute units in aggregate. Finalized block rewards identify the same validator identity as the block's fee-reward recipient. The current RPC no longer returns the historical epoch leader schedule, so no stronger leader attribution is claimed.

## Jito tip

The tip is directly reproducible in the Hrpa purchase transaction at block index 1333:

- top-level System Program instruction 8 transfers **3,000,000 lamports / 0.003 SOL** from Hrpa to `ADaUMid9yfUytqMBgopwjb2DTLSokTSzL1zt6iGPaS49`;
- the current Jito Block Engine `getTipAccounts` response includes that destination;
- the amount equals the historical bundle record's `landedTipLamports` value;
- a separate top-level transfer of 0.003 SOL to `astraZW5GLFefxNPAatceHhYjfA1ciq9gvfEg2S47xk` is preserved as a separate execution-service payment and is **not** counted as the Jito tip.

No separate Jito-tip transfer is present in the other three transactions.

## Program and attribution boundary

None of the four bundle transactions invokes or even includes program `8gxk64hYgGAEnHVhRMvBGVvBXZM5WhkGkaQ6DVgVV2kn` in its resolved account list. The creator and curve purchases use Pump.fun program `6EF8…F6P`; the migration also invokes Pump.fun AMM `pAMM…xEA`; the final purchase uses the AMM program.

This does not reverse prior findings that other case transactions invoked `8gxk…V2kn`. It establishes only that `8gxk` was not the execution program for these four bundled launch transactions. No first-party evidence binds `8gxk` or this bundle to Proxima, so Proxima attribution remains **UNRESOLVED**.

## Classification

### CONFIRMED

- All four exact signatures finalized contiguously at block indices 1330–1333 in slot 452029524.
- Jito's historical index maps each signature to the same bundle ID.
- The historical bundle endpoint lists exactly the same four signatures in finalized block order.
- The bundle landed with a 0.003 SOL Jito tip paid in the Hrpa purchase transaction to a current Jito tip account.
- Bundle CU, tip amount, slot, time and validator field reconcile with independently retrieved Solana data.
- The four launch transactions do not invoke `8gxk…V2kn`.

### SUPPORTED interpretation

Common bundle membership establishes coordinated, ordered launch execution at the Jito transaction-bundle level. It materially strengthens the technical finding that the creator action, Hp4q purchase, migration and Hrpa purchase were submitted as one execution unit rather than merely landing coincidentally in one slot.

### UNRESOLVED

- The identity of the person or system that assembled and submitted the bundle.
- Whether one operator controlled more than one signing key.
- Shared private-key control, common beneficial ownership, final beneficiary and real-world identity.
- Any definitive Proxima attribution or ZYROX–Kytro control link.

Bundle inclusion requires valid signatures but does not show who possessed each private key, who submitted the already signed transactions, or who beneficially owned the wallets.

## New ledger U494

```jsonl
{"id":"U494","edge_type":"jito_launch_bundle_membership","bundle_id":"bf5d05ae5acb728d02bd0f6e15c8e944f0dbe77874c5a6e6291b374cbcd011ed","slot":452029524,"timestamp":"2026-09-30T17:18:06Z","transaction_indices":[1330,1331,1332,1333],"transactions":["5ubvNRPDbdXtHaiexB4zroZxUDFS9mwDmDwJ3HnvdGrxuiqxDDGsZnkjdAGVHysDZgiCFqVASoinDu1bADPAbowo","52ZjUbg4bzdQoAsFeJuLgqM5b5kmeQpgp79ndnAi13D7W795N8A7BLon9t7LhENRi5wUGcqMb5RWzNDs2AB9nKkw","2MP6ABDBuCgMyAysTyNYjuFdR1AJ9eHJn4tzr1ae7DgHsYhEAsGgetnWVVpaatbZ1Dunk5Ns96PHxPm6q8gawdLB","4JrhsmKT44mQpZh5kTYFMcFWXi2Hu8Lg3U5BkUS4WEw66pWeR7GkiR299KY2WFD5XZQTH5pvBMW957WrdjjRh5Xf"],"jito_tip_lamports":3000000,"tip_payer":"HrpahQoW21MEA8qbsR9Z8oeN8NLFmTKukYSjok2Ktou9","tip_account":"ADaUMid9yfUytqMBgopwjb2DTLSokTSzL1zt6iGPaS49","evidence_status":"CONFIRMED common Jito bundle membership and ordered launch execution; common wallet control, beneficial ownership, submitter identity and Proxima attribution UNRESOLVED"}
```

## Stop condition

The historical Jito-bundle lead is now **closed as confirmed**. It warrants no further technical lookup unless a new primary record identifies the bundle submitter or links the execution infrastructure to a named operator.

**Checkpoint:** post-freeze research v0.122 / U494. Next available ledger ID U495. Frozen v0.114/U453 remains byte-for-byte unchanged. No final article was written.
