# Remaining blockers and closed limitations

## Resolved

The missing historical balance is no longer an access blocker. Tenderly's public Polygon endpoint returned fixed-block balanceOf and dated events. The archive balances and bounded ledger reconcile exactly; the explorer's transaction-local token storage display corroborates the anchor debit.

## Remaining

- No second successful RPC provider: PublicNode and dRPC returned HTTP 403; 1RPC HTTP 405; Ankr returned an authentication error. Additional BlastAPI/OnFinality requests failed, while Tatum returned a paid-plan restriction for eth_call. Exact saved responses are in evidence. No payment, authentication bypass or new credential was attempted.
- Provider identity and chain ID are recorded, but no cryptographically verified state proof or independent node replay is available. The separate explorer display is not guaranteed to use independent infrastructure.
- The 3,148.255812-USDT0 opening balance predates the bounded ledger. Its full prior composition and retention of the April swap output are unresolved. Positive old balances are not assigned to specific later spending.
- Most bounded events have not received separate transaction-sender/route classification. Selected receipts are explicitly distinguished from event-only rows.
- Wallet ownership, permission context, shared keys, ultimate beneficiary, Gamdom-specific unauthorized status and H1/H2/H3 remain unresolved.

No failed lookup is treated as transaction absence. No current balance substitutes for historical state. The search-index fetch of the April explorer URL failed; the browser and raw RPC receipt subsequently verified it.

Highest-value next independent lead: reconstruct the canonical/native funding and dated authorizations of 0x37c29b046d2253ac7291bcf131282e0441cc9282 around its September 8/10/23 D-funding operations, beginning with the verified 13,083.760000-USDC input. Stop at independently verified edges and do not infer a human or exchange owner from labels.
