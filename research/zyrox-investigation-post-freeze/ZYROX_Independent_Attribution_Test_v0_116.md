# ZYROX bounded independent attribution test v0.116

**Date checked:** 2026-10-10 UTC  
**Public baseline preserved:** v0.114 / ledger U453  
**Prior post-freeze checkpoint:** v0.115 / ledger U465  
**This checkpoint:** v0.116 / ledger remains U465  
**Assessment carried forward:** SUPPORTED COORDINATED OPERATIONAL STRUCTURE

## Scope

This is a bounded independent-attribution test for:

- `HFAcfCGEcG323fFfaZtuSi6wua724q59QX5u3VkU1QjV` (`HFAc`); and
- `99GcqafMcohBvKDw9pR1TXQuAXzB4ZEU3JWLWz7eNtTm` (`99Gc`).

The test did not trace counterparties, reopen HFAc downstream provenance, expand the 99Gc transaction graph, reopen FEaT/H85K or 6hR7, or test Kytro. It does not modify the frozen v0.114/U453 technical basis or the v0.115/U465 provenance findings.

The only question tested was whether either exact address has an independently defensible public binding to an exchange, custodian, bridge/router, payment processor, infrastructure operator, public operator identity or known controlled wallet cluster.

## Sources and checks

The exact addresses were checked on 2026-10-10 against:

- Solscan account/entity display;
- SolanaFM account display, including domains and stake metadata;
- Arkham public address/entity display;
- exact-address public web searches;
- exact-address GitHub code, repository, issue, discussion and commit searches.

These are attribution checks, not proof that no private or unindexed attribution exists. Absence from a public label surface is a null result, not evidence of ownership or non-ownership.

## HFAc result

- Solscan displays an on-curve account, zero balance/account no longer present on-chain, System Program transaction activity and no named service/entity label.
- SolanaFM displays an account with zero balance, zero assets, zero domains and no named entity or operator binding.
- Arkham displays an on-curve Solana System Account and no assigned entity, exchange, custodian, bridge, processor or public operator identity.
- Exact-address public web search returned no relevant result.
- Exact-address GitHub search returned zero code, repository, issue, pull-request, discussion, user, commit, package, wiki, topic and marketplace results.
- No first-party documentation, verified address list, public disclosure or independently supported third-party label binding HFAc to a service or operator was found.

**Classification:** operationally relevant / identity unresolved. The v0.115 collector/routing role remains SUPPORTED at account-relationship scope. No service attribution, control attribution or beneficial-owner attribution is added.

## 99Gc result

- Solscan displays an on-curve System Program account and no named service/entity label.
- SolanaFM displays an account with zero indexed assets, zero domains, no delegated stake and no named entity or operator binding.
- Arkham displays an on-curve Solana System Account and no assigned entity, exchange, custodian, bridge, processor or public operator identity.
- Exact-address public web search returned no relevant result.
- Exact-address GitHub search returned zero code, repository, issue, pull-request, discussion, user, commit, package, wiki, topic and marketplace results.
- No first-party documentation, verified address list, public disclosure or independently supported third-party label binding 99Gc to a service or operator was found.

**Classification:** operationally relevant / identity unresolved. The v0.115 classification as a persistent mixed wallet of unknown role remains unchanged. No service attribution, control attribution or beneficial-owner attribution is added.

## Evidence outcome

- **CONFIRMED:** both addresses are on-curve Solana System accounts on the checked explorer surfaces. No public entity label is displayed by Solscan, SolanaFM or Arkham.
- **SUPPORTED:** HFAc remains a case-relevant operational collector/routing boundary under v0.115 transaction evidence. 99Gc remains a case-relevant mixed downstream account of unknown role.
- **UNRESOLVED:** service identity, operator identity, controlled-wallet cluster, common private-key control, beneficial owner and final beneficiary.
- **New service / exchange / custody boundary:** none.
- **New cross-wallet signer / fee-payer / authority signal:** none encountered.
- **Beneficiary attribution advanced:** no; identified-beneficiary attribution remains 0 SOL.
- **ZYROX–Kytro linkage advanced:** no; no transaction-specific connection was encountered.

## Close

Under the stated hard-stop rule, both HFAc and 99Gc are exhausted for this bounded independent-attribution test and are closed as **operationally relevant / identity unresolved**. No further on-chain fan-out is justified from this null attribution result.

A genuine next lead exists only if new external evidence appears, such as first-party service documentation, a verified address/entity assignment, a public operator disclosure, or a new transaction-specific common external signer, fee payer or authority. Without such evidence, there is no defensible next attribution target.

**Checkpoint:** post-freeze research v0.116 / U465. Next available ledger ID remains U466. Frozen public technical basis v0.114 / U453 remains byte-for-byte unchanged.
