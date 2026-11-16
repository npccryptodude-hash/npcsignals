# frogman / 4 eth route follow-up / 16 november 2026

## what changed in the evidence

the 13 november checkpoint established the 27 october spend and left the source replenishment unexplained. normal ethereum explorer history is now available; matching transaction, successful receipt and block records are retained for the later incoming transfers. this improves historical documentation, not a claim of new post-13-november transactions.

## ethereum states

| address role | native eth at pinned block | nonce |
|---|---:|---:|
| source | 3.999999999994704 | 1 |
| destination | 0.000451381159661993 | 1 |

pinned ethereum block: 26426355 / `0x5f2ff9c6731113eabc093bd6d04aa11a67e3ca27da8e1fc62c90c34868d1956f` / 2026-11-16T08:20:47+00:00. both nonces remain 1, as in the 13 november checkpoint. this rules out a second ordinary account-originated transaction through the pinned block, not all possible internal/token activity.

## replenishment after the original spend

| utc | sender | eth | transaction | rpc verification |
|---|---|---:|---|---|
| 2026-10-28T20:07:47+00:00 | `0x45215ba58ff03aff97e4a94c2eec8051b9691e6a` | 0.00001578538 | `0xfb61c21790cdfe3f34a301b62bdf35b49f2eaef6ed0199006f76a19793dd4019` | pass |
| 2026-10-28T20:05:23+00:00 | `0x45215ba58ff03aff97e4a94c2eec8051b9691e6a` | 1.260047574911976 | `0xdce724c09240b09a8184811197300223d23080ec2a196ddf6ef4c08a97e0edc4` | pass |
| 2026-10-28T20:03:11+00:00 | `0xe48bfa1f466733a3b7b8d031e9f110ee2e51b2c7` | 2.739936413710051 | `0x586e3c5bcee97852faef51c20b6021b5b324aadfe196e640f3ab2cd58fab7e68` | pass |
| 2026-10-27T05:50:35+00:00 | `0xbbaeb33962b53fd6633b0317a75859ad12cb2e3e` | 1E-9 | `0x0160e5afad9735ed3f41b582cea5cff72b5ca16fdde77d7d09b86bf68a6f8b81` | pass |

the two larger incoming payments plus a small additional payment explain replenishment; the separate 0.000000001-eth incoming payment is also retained. similar-looking sender addresses are distinct addresses; no common operator, refund identity or victim provenance is inferred. source internal-history request failed with http 500; destination internal history explicitly reports unprocessed records (status 2). neither result supports a zero-internal-activity claim. normal history lists are bounded to 1,000 entries, with fewer returned; indexer completeness is not independently guaranteed.

## mayan correspondence

the newly successful first-party mayan response directly identifies source transaction `0x38c7c72a6da978ee29e18649d5005d8978fbde862c0f78eb18fd70325e6939bf`, order `0x47ecec44471cd15a4550897590a825a94e50aa43900e893f88ca2fa0a75b5fcb`, recipient `AKS15GjeivY1yBN3at6DNSg7q6UBmsPFtA2jWzvTniep`, input 3.998918422844160119 eth and output 92.375240889 sol. it lists settlement signature `3acQkJbsmUo3cj5NoSngvGH2oWoZst9pujcHh41DvCKNZ9J3yR1usKNW1bDgj49cuGfMKHX2dmLjSePg733K4kHC`. this strengthens the supported cross-chain correspondence with an explicit protocol record; independent order-state/pda verification remains outstanding. its `redeem`/`unlock` fields concern this mayan bridge operation, not xmr1 redemption.

## solana continuation

the previously documented 92.375240889-sol recipient forwards into mixed recipient `EfaGnkjvYEtN9yCbetyUyZmmabmBzgeGEc9LMod6pV3y`. fresh transactions below show account activity at that mixed boundary. no exclusive allocation of the original 4-eth value is made.

| account queried | returned signatures | latest returned utc | native sol snapshot |
|---|---:|---|---:|
| oct27_destination | 3 | 2026-10-27T06:32:41+00:00 | 0 |
| mixed_boundary | 4 | 2026-10-27T06:50:00+00:00 | 0 |
| next_boundary | 5 | 2026-11-09T10:10:02+00:00 | 0 |

### parsed system transfers in the newly fetched mixed-boundary transactions

| utc | source | destination | sol | signature |
|---|---|---|---:|---|
| 2026-10-27T06:50:00+00:00 | `EfaGnkjvYEtN9yCbetyUyZmmabmBzgeGEc9LMod6pV3y` | `ArZcf7nspPt6Ety41KtCpop6p16EHZPsE5NLm3umW2Qi` | 0.005142749 | `2jYbopNmfJu2GCZXA9zMAsvCnuG8tgifhhkXRgbM5iJjecte7etY6rawARwnwZTqZMZTjY6amR67x1RsqQExavK5` |
| 2026-10-27T06:45:55+00:00 | `G82yUFd62JL9RLAN1r8eTGDmGMWbo1bXLTsjnqHZGTda` | `EfaGnkjvYEtN9yCbetyUyZmmabmBzgeGEc9LMod6pV3y` | 0.00001 | `38fX5LJYT3x2TgYxDuZf4w9YKqEFj45RfRHgaJ4v8nhgqvXDzkNw1x5bSq3N4bfeRQ9pp8SXBET2ovEb2XikmMqd` |
| 2026-10-27T06:43:49+00:00 | `EfaGnkjvYEtN9yCbetyUyZmmabmBzgeGEc9LMod6pV3y` | `G82K2R2RgJyBwfezs6ey2TXPzjR7oNEGr9WTMWinGTda` | 216.46 | `3ZQkoKFT8yRAVL9JNcLrBbgN45Yerj9k1841Gm2bmAzKENKYXEuUhATXzcLxVFy5j5ZfCRyk6p7cyHpnovkVcnQe` |
| 2026-11-09T10:10:02+00:00 | `G82K2R2RgJyBwfezs6ey2TXPzjR7oNEGr9WTMWinGTda` | `ArZcf7nspPt6Ety41KtCpop6p16EHZPsE5NLm3umW2Qi` | 0.0100047 | `4D1s2B77CQBiRYWznVuyjParBnatKFkjGiBacxjXEnvfjdzDKNaEKKgD8CrGRMnqGf6gQo542JMFsRDbd2ubqwPJ` |
| 2026-11-09T10:10:02+00:00 | `35qjvq7J6VLW51F3ixNFRfbmwXezgPjYk2gcsDBcmUkK` | `ArZcf7nspPt6Ety41KtCpop6p16EHZPsE5NLm3umW2Qi` | 0.006954563 | `4D1s2B77CQBiRYWznVuyjParBnatKFkjGiBacxjXEnvfjdzDKNaEKKgD8CrGRMnqGf6gQo542JMFsRDbd2ubqwPJ` |
| 2026-11-09T10:10:02+00:00 | `DH5cicA9dUKWRv9euDJNP2Z5aJtFXftiUQaNfvWYaBvP` | `ArZcf7nspPt6Ety41KtCpop6p16EHZPsE5NLm3umW2Qi` | 0.010004233 | `4D1s2B77CQBiRYWznVuyjParBnatKFkjGiBacxjXEnvfjdzDKNaEKKgD8CrGRMnqGf6gQo542JMFsRDbd2ubqwPJ` |
| 2026-11-09T10:10:02+00:00 | `Bu8AuWpZEbkZCT4hcD4c9HK1HwcbchskoPD89zPSgbyB` | `ArZcf7nspPt6Ety41KtCpop6p16EHZPsE5NLm3umW2Qi` | 0.005244319 | `4D1s2B77CQBiRYWznVuyjParBnatKFkjGiBacxjXEnvfjdzDKNaEKKgD8CrGRMnqGf6gQo542JMFsRDbd2ubqwPJ` |
| 2026-11-09T10:10:02+00:00 | `8k5AumzewbqQtJLjwKbcvMQWih2LakmPyhyeXA4zyLZo` | `ArZcf7nspPt6Ety41KtCpop6p16EHZPsE5NLm3umW2Qi` | 0.00100458 | `4D1s2B77CQBiRYWznVuyjParBnatKFkjGiBacxjXEnvfjdzDKNaEKKgD8CrGRMnqGf6gQo542JMFsRDbd2ubqwPJ` |
| 2026-11-09T10:10:02+00:00 | `4PbQ4osEBFkdzEEYkxRvo67TGNuMWsYuiBt6p8h1XjCo` | `ArZcf7nspPt6Ety41KtCpop6p16EHZPsE5NLm3umW2Qi` | 0.0010044 | `4D1s2B77CQBiRYWznVuyjParBnatKFkjGiBacxjXEnvfjdzDKNaEKKgD8CrGRMnqGf6gQo542JMFsRDbd2ubqwPJ` |
| 2026-11-09T10:10:02+00:00 | `J4R8nTf8kasmyZnVcajq4MAdeJXrwfSLNBeavd7g6T3s` | `ArZcf7nspPt6Ety41KtCpop6p16EHZPsE5NLm3umW2Qi` | 0.0010044 | `4D1s2B77CQBiRYWznVuyjParBnatKFkjGiBacxjXEnvfjdzDKNaEKKgD8CrGRMnqGf6gQo542JMFsRDbd2ubqwPJ` |
| 2026-10-27T06:48:13+00:00 | `eS46geUXwWx37vpecfzwX782JYbwsfM2YX3JGzZ99qW` | `G82K2R2RgJyBwfezs6ey2TXPzjR7oNEGr9WTMWinGTda` | 0.00001 | `5yGdNvLYAEaeY8NFxqzM2LweEjhytfh9F36b8heMRqDMCXsiCsK8aLWJEavUppk3M48Pp5k7V89ZKEn8UmtxXyWT` |
| 2026-10-27T06:46:10+00:00 | `G82K2R2RgJyBwfezs6ey2TXPzjR7oNEGr9WTMWinGTda` | `eS4n56zrQ4ESznC8mDxQhsY4JoCpEt1jDczgcQ299qW` | 458.52 | `3osAJhCGJySEfub4sm2Mv7S7nqwDaF6fnTQmJoSALD2LwoAqAE7zowVGiU5TdZqBe4ZbfgD8EohJ7J97soPFG1jJ` |

the next boundary also shows a 458.52-sol outgoing transfer on 27 october and a multi-source small-balance sweep on 9 november (0.0100047 sol from that address). these are account-level facts beyond mixed funding; no exclusive allocation is made. the mixed account forwarded 216.46 sol to `G82K2R2RgJyBwfezs6ey2TXPzjR7oNEGr9WTMWinGTda` on 27 october. a fresh bounded history/balance query for that next address is retained. this is an account-level continuation past a mixed-funding boundary, not a deterministic attribution of 216.46 sol to the 4-eth branch. no human beneficiary or platform label is assigned.

## publication effect

the historical narrative can now explain the source replenishment and show a stronger protocol-supported mayan correspondence and later mixed-account transfer. these are older events newly documented in this recheck. the remaining internal-history and cross-chain verification limits must stay visible. the endpoint is not a proven final beneficiary. no medium publication was performed.
