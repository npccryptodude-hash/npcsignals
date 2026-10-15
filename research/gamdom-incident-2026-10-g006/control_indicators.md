# Operational control indicators

A = `0xd5FBDa4C79F38920159fE5f22DF9655FDe292d47`

B = `0xe5686AaE44d392aa6A0637FD38393859502F8667`

C = `0xaCc0c1f672B03B9a5fED4535f840f09B85f40E98`

## CI1 — Recipient funds the sender before first ordinary outgoing use
CONFIRMED explorer record: `0xdae446791f8dfde5acdab9f241051d0fa955937cf67cef385fd152a3503e4bdd`, Polygon block 95472585, October 13 17:56:30 UTC. Sender and protocol fee payer B; native value 20 POL to A; B nonce 0. A then signs G005's USDT0 transfer at 17:57:28 with nonce 0 and USDC transfer at 17:57:34 with nonce 1. The gas funding precedes those operations by 58/64 seconds.

This establishes a financial funding relationship and an activation sequence. It does not prove a common private key, a common human, malicious intent or unauthorized access. B did not pay the fees of A's transactions directly: A paid them using its native balance. Earlier native balance/other funds are not excluded without historical state.

## CI2 — Third address directs repeated operations to B
CONFIRMED receipt/internal-transfer observation: `0x8ab3a5fd769a031b1903511798f141db6d679360d9f6de385e9e0c1b7641a9dd`, Polygon block 95472497, 17:54:18 UTC. C initiates and pays the router transaction. Receipt shows C contributing 14.950094 USDT0 to Squid; the swap yields 148.787119217835216906 POL delivered through Multicall to B. This is a local Polygon swap, not independently established as a cross-chain deposit.

On Ethereum, C also initiates `0x1dad24aca5d8ba4f3ba098009241440f61db8ad47912206cd889921bb901b8db` at 18:38:23 (native input 0.695610686857784977 ETH) and `0xf933bc54a529d6dd39baf4311ce95a4cc2035f6442817813803da9189043b14f` at 18:39:23 (receipt shows 1,616.602607 USDT input). These operations deliver respectively 1,737.517467148324729025 and 1,614.740060520355464367 DAI to B.

Repeated initiation toward the same beneficiary supports an operational relationship. It does not establish that C possesses B's key. Router/Multicall operators are service infrastructure; their appearance is not a common-owner signal. Whether C is a service account, independent sender or participant is UNRESOLVED.

## CI3 — Additional A-to-B financial connection on Ethereum
CONFIRMED token log: `0xebbe5ad72e9f02479b8c989f2e072807a3263e45853611162ae7fbe5c51ca0c5`, block 26185149, 17:45:23 UTC. A is actual transaction sender, interacting with canonical BUSD. Log 442 transfers raw 10456137361559383267328 BUSD units (18 decimals) from A to B. No label is needed to establish this edge.

B subsequently signs a Squid operation at 18:35:11, `0x6117786557acfce0276de69788f5c21553141a9a6c2f220dabcf702a007ea085`, spending the same BUSD quantity and receiving 10,346.405126060613426143 DAI. Identical amount and temporal sequence are confirmed; exclusive fungible-token provenance would require complete balances and flows. This is an additional chain-level connection, not proof of shared ownership.

## CI4 — Explicit recipient approvals on Polygon
B authorizes router `0xce16F69375520ab01377ce7B88f5BA8C48F8D666` to spend exactly raw 12139456905 USDC (`0x42abb43d…afe768860`, nonce 1, log 602) and raw 19610310097 USDT0 (`0x5a134b6a…1fc3eac3`, nonce 3, log 484), immediately before G005's bridge operations. Full hashes are in control_transaction_ledger.csv. These demonstrate B authorizing contract spending, not that the router controls B or A.

## CI5 — Historical delegation on Ethereum
CONFIRMED historical transaction record: `0xf1d9478bfcccf3dcc7ea5211fd7924230226be0bee7a5b96d767cc9f7167e9a2`, Ethereum block 26184803, 16:35:59 UTC; type 4 EIP-7702, nonce 0, sender/to B. Explorer records delegation to `0x63c0c19a282a1B52b07dD5a65b58948A07DAE32B`. This is dated transaction evidence rather than reliance on a current authority badge. Independent authorization-signature recovery and contract implementation analysis were not completed; the implementation's human operator and authority beyond this record are not attributed.

Several B-origin approvals/order actions and four gas funding transactions are recorded separately. Service labels were not used to assign ownership. No matching authorization or shared key between A and B was found in the completed sample. No prior repeated A-to-B operational relationship before October 13 was established.

## CI6 — Counterfeit-looking transfer rows are not signer evidence
On October 14, Polygon transaction `0xc64a0085…4fbf0571` displays A as event sender of the exact previous USDC/USDT0-like amounts, but uses contracts `0x51735a0ba00fcd66511fe6fd92464f534e988dd1` and `0x96ecac3e9596c48ac28b1c3ee04cbbe581bd0194` and a different full recipient `0xe568c4CFA80D6c5A2c0D19941cC48B841Da88667`. Actual transaction sender is `0xBf76071a15cef3A25A356d821d45e3354C152356`.

Polygon `0xbfe573c6…7a36e821` similarly displays 20 units of a POL-named ERC-20 (`0xb23d10b159d052061a6d327ec5a185f0228d4e95`) to a different d5FB-looking address; actual transaction sender is `0x1181118751A4Be7fcC290bD1D50244A97D594e01`.

Ethereum `0x9a6c5ce3…1123073a` repeats 0.9581/1.492982 USDT-like amounts using contract `0x00a98f159dfd64297b179fc0d6eff233c68c6645`, a different e347-looking recipient, and actual sender `0xC34f77c6757B239D878ABC1cD2b6F364eFeB063D`. Its receipt contains over 1,000 logs; the relevant indexed event rows were not individually recovered from its full log list. Therefore preserve them as indexed observations, not fully verified event-level transfers.

The contract/address differences and actual transaction-sender differences are CONFIRMED. Address-poisoning intent or common ownership of these third parties is UNRESOLVED. All are excluded from operational frequency/amount statistics. Do not treat the displayed event `from` address as proof that A/B signed or approved these operations.
