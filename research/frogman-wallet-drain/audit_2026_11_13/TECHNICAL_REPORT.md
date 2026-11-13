# frogman / technical main report / 13 november 2026

## conclusion

all 35 externally listed hyperliquid accounts are now documented individually. their verified arbitrum usdc transfers total **2,029,874.462280 usdc** and match first-party hyperliquid deposit credits exactly, by transaction hash and amount, on every account.

**537 xmr1 buy fills** purchased **3,589.31 xmr1 gross**. recorded xmr1 fees total **2.512517**, producing **3,586.797483 xmr1 net**. each account's net quantity reconciles exactly to its newly retrieved spot balance. returned fills contain **zero xmr1 sells**. returned non-funding ledgers contain only the 35 matched deposits and 35 internal transfers to spot, with no returned external withdrawal or token-transfer entry.

spot-state observations span **2026-11-13T08:17:14.308354+00:00 to 2026-11-13T08:21:23.802410+00:00**. the common conservative history cutoff is **2026-11-13T08:17:10.300000+00:00**, the earliest per-account history end time. these are current first-party observations, not signed hypercore consensus proofs or proof of lifetime api completeness. later activity after any particular query is outside its scope.

## exact accounting

| measure | verified amount |
|---|---:|
| arbitrum usdc deposited / hyperliquid credited | 2,029,874.462280 |
| internal usdc transferred to spot | 2,029,874.280000 |
| usdc execution cost | 2,029,710.635700 |
| spot usdc remaining | 163.644300 |
| perpetual account usdc remaining | 0.182280 |
| total residual usdc | 163.826580 |
| xmr1 purchased gross | 3,589.310000 |
| xmr1 sold in returned fills | 0 |
| xmr1-denominated execution fees | 2.512517 |
| net xmr1 / queried balances | 3,586.797483 |

usdc execution cost plus the two residual usdc balances equals the deposit total exactly. the small difference between deposit credits and internal transfers is now reconciled to reported perpetual account value, rather than assigned to an invented fee. xmr1 fees are already reflected in net token balances and must not be deducted again.

## overlap and external reconciliation

all six previously audited relay accounts appear in the 35-account set, with their original 561,850.214994 usdc deposits. the separate mayan-linked account, 26,823.206875 usdc, is also present. the archive additionally already contained an across-linked credit to `0xa3ca6199d8692ec40d0287e615b48d0e8cde9abe` for 91,232.216513 usdc; the recent seven-account summary had omitted this additional credit from its coverage description. its older fills were not claimed verified in that block. this audit reconciles all 35 histories, including 27 accounts beyond these eight previously credit-documented accounts.

| external claim | independent result | interpretation |
|---|---|---|
| 35 accounts | 35 distinct account addresses with exact credit matches | reproduced for the published set; not proof the set is exhaustive |
| 2,029,874 usdc | 2,029,874.462280 usdc | agrees when rounded to whole units |
| 3,586.8 xmr1 | 3,586.797483 xmr1 | agrees when rounded to one decimal |
| evm-side grouping: 745,551 usdc | rows 01–10 total 745,551.169439 usdc | arithmetic grouping confirmed; source-chain attribution still requires route-specific evidence |
| solana-side grouping: 1,284,323 usdc | rows 11–35 total 1,284,323.292841 usdc | receipt subtotal confirmed; not proof of victim provenance across privacy cash |
| 29 privacy cash withdrawals / 12,693 sol | not deterministically linked to the ten deposits | inferred by external source; remains unproven here |
| 41 accounts in another public statement | no complete comparable address set obtained | unresolved coverage difference; do not add six accounts to this total |

## activity and redemption boundary

latest returned account activity across the 35 is **2026-10-07T03:37:25.691000+00:00**. no post-13-october fills or non-funding ledger updates appear in the returned histories. the separate recent-window responses are documented alongside the original full-window responses. this is a positive inspection of returned histories and reconciling current balances, stronger than an unsuccessful search, but still bounded by api coverage and query times.

no native monero receipt is verified. xmr1 balance reconciliation and no returned external transfer do not independently audit wagyu's off-platform records, reserves, redemption requests, private arrangements or the monero chain. no assertion that native monero redemption is impossible is made.

## historical reconstruction and integrity

ten original privacy cash deposits remain **13,240.973780900 sol**. the original solana files and all older raw evidence are unchanged. previous route-specific checks for relay, across, chainflip, mayan, near intents, li.fi routing and robinhood origin/settlement mechanics were rerun offline in an isolated copy. see `offline_verifiers.json` and `relay_recheck.json` for actual results.

one older integrity failure is material to disclose: `v0.2/inbound_sender_attribution_2026_10_10/access/explorer_label.response.txt` differs from its historical sha256 manifest. its associated verifier fails at the checksum assertion. the response is an explorer label page concerning an upstream funding-side account, not one of the 35 deposit/credit/fill records. no new identity/service-label conclusion relies on it. neither original file nor original manifest was repaired. the difference was subsequently explained: lf-to-crlf conversion reproduces its historical digest exactly, and the verifier passes in an isolated copy with the reconstructed bytes. see `integrity_normalization_recheck.json`; original files remain unchanged. a dependency failure for the relay verifier was resolved by an isolated pycryptodome installation; the actual retry passed.

## publication decision

ready for a bounded, source-linked account and historical money-flow article, provided this scope is retained. not a solved compromise-method, attacker-identity, full victim-loss allocation, all-account inventory or native-monero-destination report. the exact 35-account totals are now reproducible; broader privacy cash provenance, other destination branches and recovery remain unresolved. [limitations](LIMITATIONS.md) specifies remaining work and technical failures. the medium draft is delivered separately and is not part of this repository.

## additional findings after the 35-account reconciliation

a separate near/relay branch adds one independently matched hyperliquid account with 55.569140 usdc and 0.089937 net xmr1. this gives 36 distinct audited accounts overall, while the external 35-account table remains unchanged. a 27 october spend disproves the current applicability of the old untouched 4-eth holding description; it leads to a new mayan order and a supported solana settlement association. [complete additional findings and boundaries](ADDITIONAL_FINDINGS.md) · [supplementary source-wallet checks](SUPPLEMENTARY_ENDPOINT_CHECKS.md).
