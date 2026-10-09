# Robinhood direct-sender funding: bounded reconstruction

Public parent: `b47247e70aa72290a74273b973b6a749314f13dc`. Additive F0505–F0522. No prior file or ledger object is rewritten.

Eight native-value origin deposits by `0x427c4b37de0714821b09c4fc655a713abbcfba83` total **64.34 ETH**. Fresh successful receipts reproduce each bridge entry. **Funding provenance into each entry remains UNRESOLVED**: the public Robinhood RPC returns historical-state errors for all attempted prior/post balances and nonces. No clean or mixed allocation is invented from these failures.

Three affected-address token transfers (F0187–F0189) are independently reproduced. The bounded indexed-event search covers Robinhood blocks 81901837–82032267 and topic positions 1/2. It recovers previously documented CASHCAT disposals and three previously unledgered V4 disposal transactions:

| Transaction | V4 debit from 0x427c | Wrapped-native burn within transaction |
|---|---:|---:|
| 0x38ccc85e35a54234662a915df3c21b875f5d3e0adac5d9caa9eb44cc9fabf5eb | 6,852,833.215636530804886001 | 12.435733791211368507 |
| 0xae6a813e60f259eb90516ecc2fd26680d86bb0cab9a1b5b18c660c737fd68c8f | 3,852,833.215636530804886001 | 6.643500634823265966 |
| 0x2b65933dc34cd4283fbe1d5a0c90d2e82a07ea88b96a7acbe639560eae8887a8 | 3,000,000 | 5.070932600792816593 |

The V4 debits sum to the observed affected-address V4 transfer, but equality is not exclusive provenance. The first V4 transaction has a different outer sender; the second is a self-addressed transaction by 0x427c; the third calls another swap contract. Receipt token debits and burns are CONFIRMED. Their native payout recipient and allocation into later Across inputs remain UNRESOLVED without traces or state reconciliation. This is **PARTIAL / RE-ESTABLISHED token-level reconstruction**, not CLEAN bridge funding.

The exact 0.500012122639901441 wrapped-native withdraw call by 0x427c at nonce 9 is reproduced with matching burn. A fresh first CASHCAT disposal receipt also records a 56.829682146234507264 wrapped-native burn. Neither burn is silently converted into an independently traced native credit.

At the dated current Robinhood snapshot, 0x427c has the EIP-7702 designator `0xef010063c0c19a282a1b52b07dd5a65b58948a07dae32b`. MetaMask's first-party deployment list associates that target address with its stateless DeleGator implementation (SUPPORTED framework association). This is not proof of wallet software, custody, compromise, historical delegation state or operator identity. The zero-value outer sender 0x07ae remains a different role and account.

## Evidence limits

Robinhood's current first-party network documentation names `robinhoodchain.blockscout.com`; this canonical explorer returned HTTP 403. The older explorer returned HTTP 502. These are saved access limitations, not proof of absent activity. The canonical public RPC does not expose the attempted debug tracer and does not provide the attempted historical state. Indexed-token log coverage is not native/internal account history or a lifetime balance audit.

No common fee funder, signer owner, shared operator, private custody relationship or beneficiary is established. Protocol/framework metadata from Ethereum does not establish an identically addressed Robinhood deployment. Seven zero-value outer routes remain separate and are the next funding block. No final article, loss addition, Privacy Cash reopening or new withdrawal finding.
