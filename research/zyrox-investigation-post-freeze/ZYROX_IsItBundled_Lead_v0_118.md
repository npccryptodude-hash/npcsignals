# ZYROX IsItBundled lead — v0.118

## Checkpoint

- Continued from public commit `b5bdc7c158dab0a8c82a3aa970c9606f1464e3c1`.
- Frozen technical basis **v0.114 / U453** remains unchanged.
- Existing post-freeze report **v0.117 / U465** remains unchanged.
- No new independently verified transaction edge was found. Ledger remains **U465**; next available ID remains **U466**.
- This is a research checkpoint, not an article.

## Publication integrity

The public 104-wallet CSV and wallet-resolution JSON were checked before publication. They contain public Solana addresses, report ordering, request/capture metadata and IsItBundled API fields only. They contain no API key, credential, private key, personal data or real-world identity attribution.

The published blobs are byte-identical to the reviewed local files:

- `isitbundled_wallet_resolution_2026-10-11T055222Z.json`: SHA-256 `60381885bb15c410fa5a33eb8a16235b0a0c0504627278e359c1f77873836816`
- `isitbundled_zyrox_104_wallets_2026-10-11T055222Z.csv`: SHA-256 `2a5a3aeb86de7a5a0de7135bb0253967609515b9c386d4026f25b1e670e87340`

All `bundle`, `proxima`, `handoff`, `sniper` and related role fields remain explicitly classified as **IsItBundled third-party labels**, not independently verified NPCsignals control or ownership findings.

## Bounded 66-pair verification

The public IsItBundled API documentation at <https://isitbundled.com/api> exposes:

- token summary endpoints for one token or up to 100 tokens; and
- wallet classification endpoints for up to 100 wallets.

The documented token response contains summary metrics but no handoff-pair array, seller signature, buyer signature, slot/index, raw token amount, matching tolerance or time-window rule. The wallet endpoint returns address-level roles and historical counters, not source/destination transaction pairs.

The live ZYROX report returned an application error during this recheck. The already archived rendered capture and token API response remain the available immutable evidence. Neither contains a machine-readable 66-pair manifest.

Result: the claim of **66 same-amount sell/buy matches** remains **UNRESOLVED / THIRD-PARTY ASSERTION**. It cannot be independently reconstructed without a transaction-level manifest or a reproducible matching rule. No sample was selected from timing or amount similarity alone, and no wallet fan-out was performed.

## Proxima verification

Proxima's first-party documentation was captured in `raw/proxima_first_party_docs_capture_2026-10-11T062752Z.md`.

The documentation confirms product capabilities to:

- create up to 100 wallets;
- fund multiple wallets through proxy-wallet routes or optional CEX funding;
- configure layered launches using Front MEV, optional Back MEV, temporary holders and final holders;
- distribute launch funding and configure automated buy/sell and volume operations.

This strengthens the general service-capability context behind IsItBundled's heuristic. It does **not** independently bind Proxima to program `8gxk64hYgGAEnHVhRMvBGVvBXZM5WhkGkaQ6DVgVV2kn`, its deployer/upgrade authority `GVt5…7C3h`, or any ZYROX address. No first-party Proxima program-address list or public operator disclosure was found in the bounded check.

Evidence remains separated:

- **CONFIRMED NPCsignals:** case transactions invoked `8gxk…V2kn`; frozen U271 documents GVt5 as deployer and upgrade authority; specific wallet transaction roles remain as previously ledgered.
- **CONFIRMED service capability:** Proxima's own documentation describes multi-wallet creation, proxy funding, layered launch execution and automated trading.
- **SUPPORTED only:** the observed ZYROX structure is operationally consistent with this class of tooling.
- **UNRESOLVED:** whether `8gxk…V2kn` is an official Proxima program; whether all 87 IsItBundled-labelled wallets belong to one account or human operator; common private-key control; beneficial ownership; final beneficiary.

## Launch and overlap status

No completed work was repeated.

- Exact IsItBundled list: **104 unique addresses**.
- Exact overlap with frozen report: **88 / 104**.
- Launch slot: **452029524**, `2026-09-30T17:18:06Z`.
- Launch-slot acquisitions: **819,999,999.998698 FACv / 1,000,000,000**, or **81.9999999998698%**.
- Same-transaction direct market payment total: **97.709236321 SOL/WSOL**.
- No common external signer or fee payer across the three launch-slot transactions.

## Result and stop condition

- No new cross-wallet control signal.
- No new beneficiary or identity attribution.
- No new service, exchange or custody endpoint attributable to ZYROX proceeds.
- No transaction-specific ZYROX–Kytro link.
- No U466 ledger entry is warranted.

The IsItBundled lead is exhausted on the currently public evidence. A genuine continuation requires one of:

1. the provider's transaction-level 66-pair manifest and matching rule;
2. first-party Proxima documentation binding `8gxk…V2kn` or GVt5 to the service; or
3. a new transaction-specific signer, fee-payer, authority or beneficiary edge.

Absent such evidence, do not fan out through the 16 newly listed wallets or reinterpret IsItBundled role labels as ownership.
