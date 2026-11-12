# frogman — primary transaction spot checks / 12 november 2026

**npc / investigation / 001**  
**scope:** two independently inspected arbitrum explorer transaction receipts  
**status:** confirmed on-chain deposits; post-deposit activity not rechecked

## verified transaction records

| id | utc | block | from | usdc amount | transaction |
|---|---|---:|---|---:|---|
| arbi-01 | 2026-10-07 01:45:30 | 512421104 | `0x9cb119168265469a849E1864c87a57999A4Bc01f` | 60,416.783132 | [arbiscan](https://arbiscan.io/tx/0xc0e57329de131312e346161d70d2e7eb4626f12b4ed642af6b1def28d813669f) |
| arbi-02 | 2026-10-07 02:21:11 | 512429504 | `0x3E2d81f7A5659e4760bA929ef88eed40EF6640a1` | 26,823.206875 | [arbiscan](https://arbiscan.io/tx/0x963c56253dedcfd5ff9f944c91eb9cb9e94d12701d9165f66a40b9aa0b4cfc1f) |

both transactions show successful usdc token transfers to `0x2Df1c51E09aECF9cacB7bc98cB1742757f163dF7` (labelled hyperliquid deposit bridge 2), using arbitrum usdc contract `0xaf88d065e77c8cC2239327C5EDb3A432268e5831`.

## independent reconciliation

- **arbi-02:** 26,823.206875 usdc matches the exact separately documented npcsignals mayan-related hyperliquid credit amount. amount agreement and recipient label support the match, but the full route and first-party account credit should still be cross-checked by transaction hash.
- **arbi-01:** 60,416.783132 usdc confirms the external source's rounded 60,417 usdc deposit, not the account's subsequent fills or ultimate controller.
- **two confirmed transactions do not validate the complete 35-account inventory** or its reported 2,029,874 usdc total.

## verification boundaries

confirmed: successful arbitrum transactions, exact usdc amounts, originating wallets, block times, token contract and deposit-bridge recipient.

not checked here: hyperliquid first-party credit matching for arbi-01, all 35 unique accounts, post-october transfers, current xmr1 balances, redemption to native monero, human attribution.

## educational trace

```mermaid
flowchart LR
 A["arbitrum wallet / 0x9cb1…c01f"] -->|"60,416.783132 usdc / verified"| B["hyperliquid deposit bridge 2"]
 C["arbitrum wallet / 0x3e2d…40a1"] -->|"26,823.206875 usdc / verified"| B
 B -. "first-party account credits to be checked" .-> D["hyperliquid accounts"]
 D -. "november status unknown" .-> E["xmr1 holdings / redemptions"]
```

**source dates:** the transactions occurred 7 october; the verification review was conducted 12 november. this is not evidence of new november fund movements.

## next steps

1. inspect remaining 33 deposit receipts from the published external ledger.
2. retrieve complete address inventory and compare with the npcsignals v0.2 findings.
3. verify hyperliquid account credits, fills and withdrawals from first-party records at a timestamped current checkpoint.
4. avoid promoting third-party reported balances to independently confirmed findings without reproduction.


## additional verified receipts — 12 november 2026

The following three receipts were inspected directly on Arbiscan. Each shows a successful Arbitrum USDC transfer to Hyperliquid Deposit Bridge 2 (`0x2Df1c51E09aECF9cacB7bc98cB1742757f163dF7`).

| id | utc 7 oct 2026 | block | originating address | exact usdc | full transaction hash |
|---|---|---:|---|---:|---|
| arbi-03 | 01:49:41 | 512422057 | `0xd7efd720aDf271B7173Dd01a9b81668892Bee6B1` | 100,542.304581 | [arbiscan](https://arbiscan.io/tx/0xd09044916f0e5402351d6edc68cc7afa48a00e08800791a02e0f48f554f1255e) |
| arbi-04 | 01:52:53 | 512422775 | `0x68d6E20a28F9d50Ebf798ccf9fae9e3D5e4F1ac4` | 93,738.289817 | [arbiscan](https://arbiscan.io/tx/0x953cb3206cf345b500e518316a07151f10835663ce4e55f8e972d2d78e78ff87) |
| arbi-05 | 01:56:40 | 512423646 | `0x888795F84f5F81352a7639f1254662ae5897E223` | 93,549.620787 | [arbiscan](https://arbiscan.io/tx/0x0ddf411d8745a28b5efdd1c42ab0a1526c53f1c92b622b36c0f6baf595dc3a9c) |

**progress:** 5 of 35 externally reported deposit transactions checked individually, 30 outstanding. The Arbitrum transfers alone do not verify first-party Hyperliquid credit/fills, current account holdings, redemption, common control or attribution. Do not add the five deposits to the external 2,029,874 USDC figure: they are a subset.
