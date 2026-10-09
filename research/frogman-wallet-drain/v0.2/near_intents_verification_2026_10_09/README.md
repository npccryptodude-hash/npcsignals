# NEAR Intents verification — 2026-10-09

Parent public checkpoint: `3fd049cf06370614885df57294136e44b3338900`, main, through F0480. New ledger: F0481–F0486. Frozen v0.1 and all existing F0001–F0480 files and objects are preserved. This is an additive evidence block, not an article.

## CONFIRMED: one Ethereum → Solana route through NEAR Intents

**2 ETH → 44.473890045 native SOL**, with transaction-specific Ethereum → NEAR credit and NEAR → Solana withdrawal links. The composite route and its two underlying edges describe one flow. They are not three separate transfers of new losses. Treasury sweeping, internal credit, token exchange and settlement must not be counted as additional loss amounts.

| Stage | Transaction / identifier | Role |
| --- | --- | --- |
| Ethereum origin, existing F0157; enriched F0481 | `0xedfd6d0be46db66dcf6f3e9d60875c766ec164f1a3339408fe703bc5e9427ce5` | `0x114e6c4f7d341aee968045c22548cbdc25c44a7a` deposits 2 ETH to `0xbe8647262afcee826c55135e272eb13d81cade3f` |
| Ethereum sweep, existing F0158; enriched F0482 | `0xcb2039fffcaa68d8526f2bce2d492bbd595168d9bc3c73c9dcf7d8b27561df77` | Deposit address sends 2 ETH to documented NEAR Intents treasury `0x2cff890f0378a11913b6129b2e97417a2c302680` |
| Ethereum → NEAR edge, F0483 | `7SgVFAvXE5t9Fvo4B6oTnnfQdv6KACWJukyWGzy1A889` | `bridge-mng.near` calls `omft.near`; exact Ethereum origin hash appears in BRIDGED_FROM memo; internal account receives 2 ETH-equivalent credit |
| Intent settlement, F0484 | `2H4dQdGGq1kvKVsFhBXVEy1HmV9UeFtBTnUkgysrpkQe` | `intents.near` executes the canonical intent and withdrawal |
| Intent hash | `B6K3ESzy61mufynMNqXT3hezs5FAjuX1YZMqPTFFG6N3` | Identical in the first-party 1Click API and NEAR execution events |
| NEAR → Solana edge, F0485 | `664ymqCCGaTribMUr5Ezix1L8b5DdXSeRFx48qu1PpNUGjZSTZdy7YEqVbhSCdYZfzBCQGCj16iFMt1f19tmVweK` | Finalized OmniBridge settlement transfers 44.473890045 SOL to `JA3iQS6ZSv6L2jhnKR2XMCJThJVorvNydUmYDf6Bwhs6` |
| Composite route, F0486 | API correlation `9dfbff7b-657b-49de-8cfa-1f0a9babe5c6` | End-to-end reconstruction; no additional loss accounting |

`cross_chain_edges.json` records the two underlying edges separately. `route_reconstruction.json` records the composite route. `protocol_correspondence.json` preserves decoded account roles, native events, messages, fee allocations and nonces. The merged timeline appends six rows while preserving the prior 480 row objects exactly.

## Origin reproduction and service endpoint

Fresh Ethereum RPC reproduces both successful transactions, their receipts and containing blocks. The original deposit is block 26137150, UTC 2026-10-07T01:13:59Z. The sweep is block 26137155, UTC 2026-10-07T01:14:59Z. Both transfer exactly 2 ETH with empty input and no receipt logs. Historical `eth_getCode` returns empty code at both recipients, so these are plain address transfers, not origin-side router calls with decoded protocol events.

Primary NEAR Intents treasury documentation explicitly lists `0x2cff890f0378a11913b6129b2e97417a2c302680` for Ethereum and other listed EVM chains. This confirms a service endpoint role for the reproduced sweep. It does not prove a private custody relationship, shared wallet owner or final beneficiary.

The first lookup mistakenly used the shared treasury address in 1Click's quote-specific deposit-address status endpoint and returned HTTP 404. The proper case deposit address `0xbe864…ade3f` returns SUCCESS with the exact original Ethereum transaction, intent hash, both NEAR transactions and Solana signature. The treasury lookup failure is a scoped negative result, not evidence against the subsequently reproduced route.

## Canonical NEAR credit and execution

NEAR archival RPC independently reproduces both API-named transactions and successful receipt outcomes. Query routing hints are not treated as signer evidence; the returned transactions identify actual signers and receivers.

The credit transaction is signed by `bridge-mng.near`, received by `omft.near` and invokes `ft_deposit`. Its arguments and `eth.omft.near` transfer event explicitly name the original Ethereum transaction in:

`BRIDGED_FROM:{"networkType":"eth","chainId":"1","txHash":"0xedfd6d0be46db66dcf6f3e9d60875c766ec164f1a3339408fe703bc5e9427ce5"}`

The resulting `intents.near` NEP-245 mint credits exactly `2000000000000000000` units of `nep141:eth.omft.near` to internal account `b303273a5d9c81dd6fc7e2552698b9bda2c96cf996b05197382b4cd9d6545081`. The internal account is identified by protocol evidence; it is not independently assigned to the human owner of the Ethereum sender.

The second transaction is signed by and received by `intents.near` and invokes `execute_intents`. Its DIP-4 events contain the exact 1Click intent hash, case account, executed token differences, two application-fee transfers, withdrawal funding and `ft_withdraw`. Actual receipt outcomes reproduce the token exchange and debit/credit counterparties; no solver identity is inferred from timing.

The primary swap counterparty is `crux-solver.near`. `solver-priv-liq.near` participates in the auxiliary withdrawal-funding conversion. Both accounts appear in signed intent messages, execution events and corresponding internal token transfers. These are CONFIRMED on-chain solver-account roles, not independently identified human or business operators. The transaction submitter `intents.near`, internal case account and two solvers are distinct roles.

The withdrawal is sent to `omni.bridge.near` using `sol.omft.near`. The executed intent's message names the exact Solana recipient and external ID `46a08ded-a2b9-44ad-ac30-ab5614d0434b`. OmniBridge's native InitTransferEvent reports:

- origin nonce **606162**;
- destination nonce **437739**;
- amount **44473890045**;
- recipient `sol:JA3iQS6ZSv6L2jhnKR2XMCJThJVorvNydUmYDf6Bwhs6`;
- sender `near:intents.near`;
- asset `near:sol.omft.near`.

Core credit, execution and withdrawal event block headers are reproduced independently; exact heights and nanosecond timestamps are preserved. Initial ordinary RPC and FastNear requests timed out. Several concurrent archival header requests returned 429; required execution and withdrawal headers were successfully fetched in subsequent sequential attempts. Access failures are not absent transactions or failed settlements.

## Independent Solana settlement and exact nonce correspondence

Solana mainnet RPC reproduces the API-named signature using finalized commitment: slot **454072421**, UTC **2026-10-07T01:15:35Z**, transaction error null. Mainnet genesis is independently checked.

Pinned first-party Near-One OmniBridge source identifies program `dahPEoZGXfyV58JqqH85okdHmpN8U2q8owgPUXSCPxe` and the Borsh layout for `SignedPayload<FinalizeTransferPayload>`. The reproduced instruction discriminator matches `finalize_transfer_sol`. Independent decoding reproduces:

- NEAR origin-chain enum **1**;
- origin nonce **606162**;
- destination nonce **437739**;
- amount **44473890045 lamports**;
- payload fee-recipient account `omni-relayer.bridge.near`.

Both nonces match the canonical NEAR InitTransferEvent exactly. The instruction recipient matches the NEAR withdrawal and API; the inner System Program transfer pays the exact amount. Recipient balance increase and bridge vault balance decrease independently equal the transfer.

Observed Solana roles are separate:

| Role | Account |
| --- | --- |
| OmniBridge program | `dahPEoZGXfyV58JqqH85okdHmpN8U2q8owgPUXSCPxe` |
| Case settlement vault/source | `6tckHFBpiJ8YgYN8FUskvtvTpXQZ55g5LHeo1kvELoDQ` |
| Solana signer / fee payer | `DuSs7rCr7oTLHjM29QQ8NwDViaahTU58qqxaJVyAkgbn` |
| NEAR fee-recipient label in signed payload | `omni-relayer.bridge.near` |
| Destination recipient | `JA3iQS6ZSv6L2jhnKR2XMCJThJVorvNydUmYDf6Bwhs6` |

The first-party source names the SOL vault field and program transfer behavior. Historical instruction and transfer data establish the case-specific vault role; no broader authority or deployed-code audit is claimed. The fee-recipient field does not independently prove that the Solana payer controls that NEAR account. The settlement also posts a Wormhole message with logged sequence 808334, but that later message/VAA is not required for, or independently audited as part of, this origin-to-payout linkage.

## Reproduced accounting and fees

The 2 ETH internal credit is exactly allocated in executed NEP-245 transfer events:

| Allocation | ETH |
| --- | --- |
| Primary solver `crux-solver.near` | 1.988998011 |
| Protocol fee-account transfer | 0.000001989 |
| Application fee recipient `b2d6d5dfb2c2ead9f0ced70886c91b8cc32a12640e897b878a7d74afe0ca6a14` | 0.01 |
| Application fee recipient `dde5bb6ba7cee1b4343211a31b4ee3809fac0ca13b38a398c8ec401df658ccdc` | 0.001 |
| Total | **2** |

The application-fee amounts match the quoted 50 + 5 basis points. No human, custody business or final beneficiary is assigned to either fee account.

The case intent's SOL token differences reconcile `44473976022 − 85977 = 44473890045` raw units, yielding **44.473890045 SOL** for withdrawal. The 85,977-unit funding debit is separate from the API's quoted withdrawFee of 86,107; no forced reconciliation or invented 130-unit charge is asserted. The executed wrapped-NEAR/storage funding parameter is `1953125000128365688403` yoctoNEAR, equivalent to `0.001953125000128365688403 NEAR`; its full later consumption was not independently reproduced.

Ethereum execution gas is calculated separately from each receipt. Solana transaction network fee is 5,000 lamports, paid by the observed payer; other small payer transfers are not added to the recipient payout or labeled as case loss. Quoted refund fees were not shown charged on this successful route. Quoted versus actual output differences and API USD prices are not treated as independently reproduced fees, market spread or additional losses.

## Classification and next target

CONFIRMED: one end-to-end Ethereum → Solana routing reconstruction, exact Ethereum → NEAR credit, canonical intent execution, solver-account roles, exact NEAR → Solana nonce/recipient/amount correspondence, recipient payout and documented treasury endpoint.

UNRESOLVED: complete upstream provenance from the affected wallet, common control, named solver/operator identity, private custody relationship and final beneficiary. Standalone quote, signed-intent and MPC signature verification, deployed-code audit and consensus inclusion proofs were not performed. Successful native execution and exact event/message correspondence establish the scoped transaction linkage without those broader claims. Existing SUPPORTED and CLAIMED findings elsewhere remain unchanged.

The saved NEAR Intents candidate is resolved transaction-specifically as far as the evidence allows. Next target: remaining unlabeled destinations. No secondary branch was researched in this block. Privacy Cash remains separate; no withdrawal linkage was found or branch reopened. No article was written.

## Reproduce

Run `python verify_near.py` offline. It verifies successful Ethereum receipts/block inclusion, empty historical code, exact API and canonical NEAR correspondence, fee allocations, primary and auxiliary solver transfers, decoded bridge nonces, finalized native SOL transfer and balance arithmetic. `master_timeline_F0001_F0486.json` preserves the prior 480 row objects.

Request metadata and exact response bytes are under `access/`; the read-only collector replays the saved request manifest without creating quotes or executing swaps. The Explorer API documentation requires partner JWT access; its specification was retrieved, but authenticated historical listing was unnecessary because public status and native chain evidence resolve this candidate. No credential, channel, swap, intent submission or funds movement was created. Public signatures in raw quotes/transactions are chain evidence, not private keys. `SHA256SUMS.json` indexes this block's authored and source bytes.
