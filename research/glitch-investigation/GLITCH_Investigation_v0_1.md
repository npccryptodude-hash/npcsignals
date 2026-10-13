# NPCsignals — GLITCH Launch Investigation v0.1

**Research checkpoint:** 13 October 2026 UTC; G0001–G0065.  
**Mint:** `9XxtEBjxj2Z7DZ775foA1iq2zeZdYMKXD6fq8qCNpump`  
**Repository baseline inspected:** `a0f7ae3256d13c6e17bf110a880754a1004ece2c`.  
**Latest ZYROX technical reference:** v0.122/U494, read together with v0.121 and the frozen evidence guide. The ZYROX README still points to v0.121; the later technical checkpoint exists.  
**Scope:** first verified checkpoint, a selected creator/launch-buyer/collector sample. Acquisition stops here for review.

## Four milestone answers

| Question | Finding | Status and boundary |
| --- | --- | --- |
| Who created/funded GLITCH? | Creator and fee payer `Ft2XtprBymZsGwYUMjsLN6z8WZzguTVa5rFYSuN41S8i`; creation 16:32:33 UTC / 18:32:33 CEST. Ten direct wallets sent 2.404695940 SOL before creation. | CONFIRMED transaction roles and funding; ultimate source, real-world identity and Kytro control UNRESOLVED. |
| Can 68.5% be reproduced? | Screenshot confirms FEYN displayed 90 wallets/68.5%. Independently verified first Jito bundle bought about 79%; entire creation block bought 79.8740588272887%. | Scanner membership/calculation UNRESOLVED. Different times and metrics; 79% neither reproduces nor automatically refutes 68.5%. |
| Largest collapse sellers? | `8hiMX…88B7` sold 594,968,303.379290 tokens for 132.890991957 SOL/WSOL at 17:51:19 UTC / 19:51:19 CEST, after creator-linked co-signed consolidation. | CONFIRMED largest in selected sample; exhaustive market ranking UNRESOLVED. |
| Exact ZYROX connections? | Zero exact matches among 71 selected GLITCH signers/direct creator funders and bounded ZYROX reference corpus. Shared non-signing infrastructure accounts and comparable transaction structures exist. | OBSERVED bounded negative result; no common control inferred. Initial buyer upstream funding and final recipients are incomplete. |

## 1. Creation and initial funding

G0001–G0002: finalized transaction `5xrGXTXnf7ZDe731C7EB5cNVnERshsZhT3E66udWiXmCtzaBGSVbmFygDovhJmzSrvUpG6m1PBRWQcq6S8UT18FV`, slot 456113658, block index 598, contains Pump.fun `CreateV2` and `BuyV2`. The creator and mint account sign; creator pays the fee. Executing launch program: `6EF8rrecthR5Dkzon8Nwu78hRvfCKubJ14M5uBEwF6P`. The mint uses Token-2022, six decimals, and mints exactly 1 billion tokens to the curve account. Mint authority is revoked in this transaction; metadata update authority is cleared.

Bonding curve: `9dN1wCpxZ1TcC92ikrsMGvSBJnKKUBkQnCHQHLcdYeNy`; curve token account: `JDLGEZQ4n7uPGmFMgNMWujTuESWf4A59P9QPi35m77eN`. Creator receives 70,000,000 tokens and transfers 2.093718844 SOL to the curve as the purchase component; fees/account setup are additional. This is not a human identity finding.

Ten direct payments occurred at 16:23:16–16:23:17 UTC, about nine minutes before creation. Each source had 240,474,594 lamports, sent 240,469,594, paid 5,000 and ended at zero. Their sum equals creator's 2,404,695,940-lamport pre-creation balance. Independent upstream histories of these sources are not yet reconstructed.

| Direct source | SOL to creator | Source transaction |
| --- | ---: | --- |
| `6kBBXS6R3nyzqwgdNfqTKUu5MwPRC3v311DytkAqACLm` | 0.240469594 | [receipt](https://solscan.io/tx/2T2gsJqGk7MXiGmfBnnZJ318KWB3p5ynELvbPRSnG8zgC7TXrPaR74Dmojj3RLLAbX6bYvEjPCsZQswzQP8R5Jmo) |
| `2paR79X5Fwi4kQojMpnYL9R4eiQsFgJDP2vSghwCMa5A` | 0.240469594 | [receipt](https://solscan.io/tx/2mgtSytbNQfhqbNRWVfRQDsbM2quVU9SNyg4EQC9otoSVZ8UVpvB42g2THtT7QrU46jdZgeyb2FxCw6ZUQCSrBnU) |
| `3pphH126VJn6sQfwbJatgaVSmyU7wbAj6yG4XwDFjdYr` | 0.240469594 | [receipt](https://solscan.io/tx/2qUxYrTfYBDAv696HBTVSdSL8WYQbHmGStv5wjhGD9q9jiJiby1uPXVXxHewAVsdh4X13hnr2bWCCuSHd8ejSfwD) |
| `AQvsJsnRE69G2V4n6HYCfCNZCvCGyAaKXRpQMCuK4VmM` | 0.240469594 | [receipt](https://solscan.io/tx/3GMWdJQPsMBndUiBucev6dfvM6ARHFv8MrBwTVtDPJGYVq74WbgUycqQjnmnfgccxm2WnP7aKEQxET2En2n9xZet) |
| `37sxXQz2XWsG29MfTxWsDcg9BCuPhVnwpGrqAWCyKHH6` | 0.240469594 | [receipt](https://solscan.io/tx/3TrRfeiGetg6QB4rwLSDNgvKGy8JaRTKYDRvUHtqATmzS5ADdHPbPmdwsJbVzKKDXRL3bBb8peKCvkRi83nAH7P5) |
| `39TnHRt9EmGSHAjt9eDPHB6fTTpKyumhdxNENdYoaoTy` | 0.240469594 | [receipt](https://solscan.io/tx/3zNGqZbRmDendsh9uYbkbpjPgs5vRq8uJMoMU8Nw97UAham6PnULq53kqWjLRfiSceb1JvEoYZXAXAf8FJQTj9cr) |
| `8xd9LBACWwr7qNs4sui5euZcgNCnei6satWSHjTx9CuV` | 0.240469594 | [receipt](https://solscan.io/tx/5V1pdV367tEuFCRPXuLLmErTYgNTXYKf5yujF8oHXe4zffEExMtNBtzU3ukaqawrPcjPa4LRb7eDhgqb51d8zynW) |
| `5KSo58dWoqBkBKSQeFLo8CGdRYcG6gL77KeqWkm241y4` | 0.240469594 | [receipt](https://solscan.io/tx/5i3Je3TUMyjz4CpzuHmhYRFGJ6GS8KsErENzTsFNG3hX1H6Wk9AxtNZNvU24g3XuQhecPEMuCGngS4HMPQtexEMi) |
| `8edSzsD9CEXTJZsEe2DujZzobUzsWw4RDkJgNyPs2xi8` | 0.240469594 | [receipt](https://solscan.io/tx/5zNtTJpBDeeYXKY3met3qPdEhiLJk1nmPrtJb4ymLam63kU1fieULf5hfNsUXebHcA5rfVQyZtkQY26ny55oKLYa) |
| `3UiFG9bMQKKjqdvfhjkuQ2NYr9V2FoLPpFuEKnjkTtZz` | 0.240469594 | [receipt](https://solscan.io/tx/Z6wCyK2TbFj3nD8PytB2JRZR251yu7rKC5jan6WnT7C7hDgXxzFfn5L38UaKL6TeHPas4xCyJ6bYaUGCLu25CPD) |

The token existed approximately 56 minutes before the X screenshot's implied promotional time. Approximate X publication time is derived from a 19:31 device clock and “2 m” post age; it is not an authenticated exact timestamp.

## 2. Launch structure and FEYN test

G0003–G0004: Jito's historical index maps all five consecutive creation/purchase transactions, indices 598–602, to bundle `966d3f6823e380916b62969250922a54de23cab92f24cda941919cef4824fc92`. Its [bundle record](https://bundles.jito.wtf/api/v1/bundles/bundle/966d3f6823e380916b62969250922a54de23cab92f24cda941919cef4824fc92) and [Explorer](https://explorer.jito.wtf/bundle/966d3f6823e380916b62969250922a54de23cab92f24cda941919cef4824fc92) have the same signatures, order, slot and timestamp as finalized chain receipts. The final signer Ejw8 pays a 0.003 SOL tip to `DfXygSm4jCyNCybVYYK6DwvWqjKee8pbDmJGcLWNDXjh`; aggregate CU reconcile to 671,721.

Six buyers, including creator, acquired 789,999,999.999972 GLITCH in that bundle: 78.9999999999972% of minted supply. Additional successful purchases later in the creation block raise total acquisitions to 798,740,588.272887 tokens across nine buyers. These are acquired quantities, not end-of-day holdings or a classification of people.

| Block index | Buyer | GLITCH purchased | First bundle | Receipt |
| ---: | --- | ---: | --- | --- |
| 755 | `E75k6cT4qcZmmyyxV1hDhnq5y7sFfsjeg1v2X2tecpUt` | 620638.079369 | False | [receipt](https://solscan.io/tx/3uwxvtnXZHekmEU5bX1ALiSzt2WfTcsLD6HQhmRq7URiDJsPxVn5QQw8vb6fX4Sv842RvLUVMdom8v8gwDPYxkb5) |
| 919 | `J4yxNcBtAXaet4ZBiA4wxeL9qVjFxFAQxBKoWoUwceTP` | 2425511.777116 | False | [receipt](https://solscan.io/tx/43oq7CdvBLUjw9B6FLQD9CFw9BHxgqUkBK8jwdJNtMFEN1LqFwmW2x18JRPDCrCK9nSyjMtVbHxP2d7EVpCFEwDx) |
| 599 | `EsuRd54G5mRxeqKGdGbShG8yogurrkXGFcu2QSx5mcBU` | 190622668.439097 | True | [receipt](https://solscan.io/tx/4cQf7zfNx11uTyjmPnWaX9sGJvwQmzT9hd6fbadD3XLhhUtBh9cL5dwTvkXjL5gScxHYscpjn8bGxubXLmrZ4zLe) |
| 599 | `FjJia4dCbyKhyjtbPN6iHBwDDExAvQsWQEevDCVwQ5LH` | 144975615.105732 | True | [receipt](https://solscan.io/tx/4cQf7zfNx11uTyjmPnWaX9sGJvwQmzT9hd6fbadD3XLhhUtBh9cL5dwTvkXjL5gScxHYscpjn8bGxubXLmrZ4zLe) |
| 600 | `F3HZouf2iccrUjYuEaK3rJ99CbhmPaBTbQnTUosXnmLP` | 154453936.332848 | True | [receipt](https://solscan.io/tx/4d9LDtNQ1yFQCPxF38xmD3Z4Gs8mDC1tSTwea9yw6uMchWPnzCd1vworf2M1fEQzfgVvywnVaotcSJ98QHpepZzV) |
| 1076 | `8jsPACiiC3x7d8gWN9yUUcvjqhJDpnEcV5BP8wPdD2Eg` | 5694438.416430 | False | [receipt](https://solscan.io/tx/5RRxfeeA6mJq7Kbg4PymS4fkigTsr9c73f71drHuYQVbgTJXYdUHffE6F2aMMy3kQuxZQiQRFjAZGDYKEpbCEad9) |
| 598 | `Ft2XtprBymZsGwYUMjsLN6z8WZzguTVa5rFYSuN41S8i` | 70000000.000000 | True | [receipt](https://solscan.io/tx/5xrGXTXnf7ZDe731C7EB5cNVnERshsZhT3E66udWiXmCtzaBGSVbmFygDovhJmzSrvUpG6m1PBRWQcq6S8UT18FV) |
| 602 | `Ejw8BaPVzV1DcZn3UdVHYaxUpZtqxCDST2z4yHHwoYVC` | 115081971.615604 | True | [receipt](https://solscan.io/tx/Kn3gjGM6Phr4sWjxKJECMFNgzPKLVn3DdC9czAHqCFbG91ryj7Nc7fKu3o7LYF8g53cALd5fnVYz9ETvS41uBgC) |
| 601 | `FZeJ34vnUSnzLfyXwvDLV3yE8y3Ar4E8ndGKdSfWqG3v` | 114865808.506691 | True | [receipt](https://solscan.io/tx/grL1UNz52Sbt8TazosamF6aEJzpT8DHYsvDDHi1Znhoj89QsxVo8MnMVGH57dm5FNLjws94wW6T1iqsBbVB2R9A) |

**CONFIRMED common bundle membership** establishes ordered joint submission of valid transactions. It does not identify the submitter or show common ownership of signing keys.

**UNRESOLVED exact migration:** the creator bundle contains purchases, without a verified decoded migration receipt. Selected initial sales invoke the PumpSwap AMM by 16:32:34 UTC, so pool trading was already possible by then. Pool address/authority appearing in parsed trade balances: `56TU1AiJ2zx9WCTkUEM7Na19kf9sYZVH9Gx1nRZ7Kogf`; base vault `BQ7788Jp1qtCaAMUnqPAfyFdP4EMwjStUdAMPkEbna36`; quote vault `96XzgQ9i8fBrRscUUwfNmWzuTqfhJFMGreHDXADMUAZL`. Exact completion, migration reserves and LP allocation await L002. “Bundled curve completion” is not independently confirmed by the five-transaction bundle alone.

G0005: inspected `IMG_4844.jpeg` shows FEYN's “SCAM DETECTED”, bundled completion, relay funding and majority launch-block claims. It labels 90 wallets, 68.5% bought including 0.56% by transfer. Those labels remain **CLAIMED**. Report/resolve retrieval returned HTTP 403; no historical wallet export was obtained. [FEYN's own documentation](https://feyn.fun/docs) describes a deduplicated classifier-selected set and distinguishes transfer receipts, repeated gross buys, net buys and holdings. The displayed percentage cannot be equated to unique launch-block ownership without the time-specific report and member transactions.

## 3. Selling and collapse

G0006: five non-creator launch-buyer wallets sold 719,984,443.670321 tokens in eight verified sales at 16:32:34–16:32:50 UTC, receiving 228.907626257 SOL/WSOL gross. These sales happened almost an hour before the observed X call. A later small F3HZ sale is separately listed; it is not evidence of a major dump.

G0007/G0065: at 17:51:18 UTC, eight signed transfer transactions consolidate 563,883,825.641435 tokens from 48 sending wallets to `8hiMXA1UHYUAeW6gd6q1XQLWzZkQL48znqgdgY1388B7`. There are 49 unique signers including collector. One transaction explicitly includes creator's 70 million tokens and five other senders. This confirms authorization of these transfers. It does not establish that all senders are FEYN insiders or have the same beneficial owner.

G0008: one second later collector sends 594,968,303.379290 tokens into the pool and receives 132.890991957 WSOL in `E7JyKtcHWFDKx81SsFpSNrKcNPNhhesbUbL3gGjvUNXh`. Parsed account closure unwraps that receipt to collector. The sale includes already-held tokens as well as the consolidated quantity. Pool fees are separate from seller receipts.

### Verified sales, ordered by token input in this selected sample

| UTC timestamp | Seller | Tokens sold | SOL/WSOL gross receipt | Signature |
| --- | --- | ---: | ---: | --- |
| 2026-10-12T17:51:19Z | `8hiMXA1UHYUAeW6gd6q1XQLWzZkQL48znqgdgY1388B7` | 594968303.379290 | 132.890991957 | [receipt](https://solscan.io/tx/5nRVLSVpSVDsmJ22zLL1ywrThq7y4VpybrdJnetbSi2KwTaAao5o7fy9aRPdkjF8tuvLvW21Zn99pBuEqboTjMkE) |
| 2026-10-12T16:32:36Z | `Ejw8BaPVzV1DcZn3UdVHYaxUpZtqxCDST2z4yHHwoYVC` | 115081971.615604 | 32.098522652 | [receipt](https://solscan.io/tx/2ankbMJfVTCmUsq2cQ1G8puSX5Sqw92CsPt871KnZZigQUsG6wSyqpamUsQsdRJbhd9mUnUApTCnjCvM2WpiJ9oZ) |
| 2026-10-12T16:32:35Z | `FZeJ34vnUSnzLfyXwvDLV3yE8y3Ar4E8ndGKdSfWqG3v` | 114865808.506691 | 32.908617469 | [receipt](https://solscan.io/tx/22z8G45RB3LQAbA7n21fUFmX4LS7pkvxQ1nZd6dKejNSqw7tbMcy6QUpU6RzhX7bUzCNBTGdeQcZW3DapUuJxkVx) |
| 2026-10-12T16:32:34Z | `EsuRd54G5mRxeqKGdGbShG8yogurrkXGFcu2QSx5mcBU` | 97992524.152174 | 32.474800695 | [receipt](https://solscan.io/tx/4EPZ4vZBj9mjPBroXpf68jNWMEcdc3aFyufqChydCrryxdr9mYNzatXhFU5zUYSVqhU4aGmJ1GAgqWCULUA3wtQo) |
| 2026-10-12T16:32:50Z | `EsuRd54G5mRxeqKGdGbShG8yogurrkXGFcu2QSx5mcBU` | 92630144.286923 | 28.850292042 | [receipt](https://solscan.io/tx/3JDURL4SA4qHQ7c6i78E1EiweSSawgianXz4qj4yfkVXZCaGLnde8RyTfAKPWG8Uh5DuNsAZqEUuZuhN82EZGkN7) |
| 2026-10-12T16:32:45Z | `F3HZouf2iccrUjYuEaK3rJ99CbhmPaBTbQnTUosXnmLP` | 82659355.621957 | 26.922564393 | [receipt](https://solscan.io/tx/4rRFnhdtsdX9BXKr4hoHxLdLBx3ZAnJJQquUaS5dtet2mKVp8oNq1Rmc1eJaWrW9EaJVCxy5RXt74zVtJqb74wbe) |
| 2026-10-12T16:32:42Z | `FjJia4dCbyKhyjtbPN6iHBwDDExAvQsWQEevDCVwQ5LH` | 78611075.052268 | 25.703369343 | [receipt](https://solscan.io/tx/qDHEfwZRcsZY9P5AY42ywXk7gerUeGbUYzpKKdGEqEgzKFYRfkVgYu6ZtZfHtGBGmBHb1mybY2bYYXtDPYRvECD) |
| 2026-10-12T16:32:44Z | `F3HZouf2iccrUjYuEaK3rJ99CbhmPaBTbQnTUosXnmLP` | 71779024.381240 | 25.104745543 | [receipt](https://solscan.io/tx/1i6VBXDF6h1f9J1mGAqfFLVqLXctp4vVEdraqCk1hPrUKLEZjwV8CCR8zSvSvVAdGm9NewZ8eVGSL5ME8uR67cx) |
| 2026-10-12T16:32:34Z | `FjJia4dCbyKhyjtbPN6iHBwDDExAvQsWQEevDCVwQ5LH` | 66364540.053464 | 24.844714120 | [receipt](https://solscan.io/tx/2rFzH9g154H24MidJw9JMdSKhydkDhbS9Y4pnkJJGgycy5xzidVSaatHkSQUeZkkybj8mET8V9mDKdv2Lykfrni7) |
| 2026-10-12T17:29:18Z | `F3HZouf2iccrUjYuEaK3rJ99CbhmPaBTbQnTUosXnmLP` | 15556.329651 | 0.038584124 | [receipt](https://solscan.io/tx/3gMZsE1bgPp5f8qJi5g3UGCjw3ewZ3BMRveX3P8k3rttnBGP3D9J7VCn3NUpA82V8jp2off1qWQNsZ3XPDY5Fi7V) |

The ten selected sales total 1,314,968,303.379262 tokens and 361.837202338 SOL/WSOL gross receipts. **Gross volume can exceed minted supply because tokens are retraded. These are not unique-supply or net-profit totals.** No USD proceeds are assigned without a timestamped exchange-rate source.

G0009: in the collector sale, pool base reserves change from 113,687,990.759888 to 708,656,294.139178 tokens; quote reserves change from 142.680283066 to 8.444240582 WSOL. The quote/base reserve ratio falls 99.0505423933477% within that transaction. Concentrated selling and a severe reserve-ratio reduction are therefore supported by finalized records. This statistic is not the displayed USD market-cap decline or an execution-price measure.

### Outgoing principal and attribution boundary

G0010: collector transfers 6.644549597 SOL to `DYxqyuLyttmd1XbTXeeZCKKEQN1MCGws3aSYLakYeb6f` at 17:51:19 UTC. At 17:52:55 UTC it creates stake account `AjvkzUxuEESWVEBWx5P6v1qpTPiyCCUn9yUKAoP1C81a` with 150.173828355 SOL, authorizes itself as staker/withdrawer and withdraws the same principal to `F2khA1QZooUzidyycMzpJ6x38eQBxuDq4UrvdUUiSwuo`. The stake route is an observed transfer mechanism; motive is unknown.

The 150.173828355 SOL amount exceeds this sale's receipt and passes through a mixed wallet balance. **Do not assign the whole withdrawal to GLITCH.** The report records the outgoing transfers, with no clean-provenance or final-beneficiary attribution. Existing selected sale receipts also retain same-transaction onward WSOL movements in `data/transfers.csv`; those destinations are not presumed owned by sellers.

## 4. ZYROX comparison

G0011: read-only equality checks examine 71 GLITCH signers/direct creator funders against both ZYROX text evidence paths at the pinned baseline. There are **zero sampled actor-address matches**. Some programs, protocol accounts, Jito tips and Astra-named execution-payment destinations occur in both corpora. This is shared infrastructure, not proof of common control. No shared direct funding source among the examined creator sources is established. Other initial buyers' full funding trees were not tested.

The [comparison matrix](ZYROX_GLITCH_COMPARISON.md) separates exact equality from structural similarity and untested upstream relationships. Negative results apply only to this selected actor set. Existing ZYROX bytes and checkpoints remain unchanged.

## 5. Off-chain claims and availability

Original user files were available and independently inspected. Seven relevant claim screenshots are preserved with SHA256 hashes; source-only market images are not published with private position/trade overlays. Device clocks are observations; October 12 date and CEST interpretation come from capture provenance supplied by the user.

| Evidence | Observation | Classification |
| --- | --- | --- |
| IMG_4835 / 4840 | 19:16–19:28 Telegram readiness, early CA/holding promise and countdown | OBSERVED displayed publication; future-performance promises CLAIMED |
| IMG_4843 | 19:31 screenshot with full mint and “THE NEXT 1000x RUNNER IS $GLITCH!”; post age 2 m | Published appearance OBSERVED; exact publication time UNRESOLVED |
| IMG_4844 | FEYN 90-wallet/68.5% and warning output | OBSERVED display, underlying classifications CLAIMED |
| Source-only market images | 215,550 USD/823 holders at 19:35; 12,380 USD/876 holders approximately 20:05 | OBSERVED interface values; latter precise capture time supplied |
| IMG_4857 | Telegram good-run explanation, CA at 20k/rise above 300k and “jeets selling”; edited 19:39 label; capture clock 20:07 | OBSERVED text/edit label; valuation and cause CLAIMED; prior revision unavailable |
| IMG_4855 | 20:06 profile viewport shows older posts without original GLITCH call | No longer visible in observed viewport; deletion UNKNOWN |
| IMG_4861 | 21:22 loading error, **Replies tab selected** | Inaccessible replies feed; cannot establish missing Posts-tab publication |

Original X status URL/message IDs were not found in screenshots or exact-mint public search. Live X profile retrieval was disabled; Telegram fetch was inaccessible, and the profile's channel link was truncated. The attempted `SolanaInsiderVIP` Telegram URL was only a candidate expansion, not a verified canonical channel. There is **no confirmed deletion** and no inferred motive.

Search-indexed pump pages show inconsistent valuation snapshots with no trustworthy market-event time; they are excluded from recovery evidence. Subsequent price recovery remains **NOT ASSESSED**.

## 6. Limits and stop condition

The standalone Methodology v2.0 was not recovered; its retrieval failure is documented in [reproduction notes](REPRODUCIBILITY.md). Explicit requested evidence categories and ZYROX transaction/accounting conventions were applied, without claiming a certified review of an unavailable complete document.

The selected verified sample does not establish all insider membership, every seller, ultimate funding, complete proceeds provenance, human identities, net profit, intent, fraud or definitive Kytro wallet control. [Unresolved leads](UNRESOLVED_LEADS.md) give concrete next queries. Findings stop at this checkpoint for review; nothing is published to Medium, X or the website.
