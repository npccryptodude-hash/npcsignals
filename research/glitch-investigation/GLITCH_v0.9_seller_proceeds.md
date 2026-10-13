# GLITCH v0.9 — Seller proceeds reconciliation (Work-reported finalized RPC)

Subject seller: `8hiMXA1UHYUAeW6gd6q1XQLWzZkQL48znqgdgY1388B7`
Date: 2026-10-12 UTC. Source: user-supplied Work checkpoint reporting Solana Mainnet finalized getTransaction/getSignatureStatuses. **Raw receipts not re-fetched by this GitHub edit.**

## Outcome
Sale gross 132.890991957 WSOL was unwrapped into seller SOL during sale transaction `5nRVLSVpSVDsmJ22zLL1ywrThq7y4VpybrdJnetbSi2KwTaAao5o7fy9aRPdkjF8tuvLvW21Zn99pBuEqboTjMkE` at 17:51:19Z. Seller already held **23.928966155 SOL** before sale; funds are commingled. Two main direct external destinations:
- **R:** `DYxqyuLyttmd1XbTXeeZCKKEQN1MCGws3aSYLakYeb6f` received **6.644549597 SOL** in T5.
- **B:** `F2khA1QZooUzidyycMzpJ6x38eQBxuDq4UrvdUUiSwuo` received **150.173828355 SOL** in T9, through temporary stake account `AjvkzUxuEESWVEBWx5P6v1qpTPiyCCUn9yUKAoP1C81a` created and drained within same transaction. **Not** validator delegation.

Additional 0.003000000 SOL seller → `Astran35aiQUF57XZsmkWMtNCtXGLzs8upfiqXxth2bz` in T1.

## Transaction register

| TX | UTC | Signature | Signers / fee payer | Result |
|---|---|---|---|---|
| T1 | 17:51:19 | `5nRVLSVpSVDsmJ22zLL1ywrThq7y4VpybrdJnetbSi2KwTaAao5o7fy9aRPdkjF8tuvLvW21Zn99pBuEqboTjMkE` | seller / seller | OK |
| T2 | 17:51:19 | `3drVHM2dSwwKCsXi2pUmpJHh9xk6ZjJ3xxVfkAoNPZVCdbewxa3uysHSMPCvS6popnEgFLiJsdaohbE3Jip6tPCB` | seller / seller | FAILED custom 6001 |
| T3 | 17:51:19 | `5Xv1A2WZ26Mrxv7NnzZ7bYRrGe8sE2CFwxdDaRkPEo1DRTAysrHu8Rrqpp5LZNBECpdjT52aWTPnq3hQPysJPj6w` | seller / seller | FAILED custom 6001 |
| T4 | 17:51:19 | `4C7L1d4CgLn4UMA7wNa8T5QKB9f99scjwGssVaQqsuhgmVTSasswBwHiPmKSXw2L3H9XmHQq2XkCsmdHvdkffmAU` | seller / seller | FAILED custom 6001 |
| T5 | 17:51:19 | `29d75Pa2Pu33b7r3dQam1FyKQTAP1e1YzwpejkkhxCHYwneJSFwJW1AGgnrgcC5hu2TfU5U7D6b1ppJvC5nwuqrB` | seller / seller | OK |
| T6 | 17:51:19 | `635MeWxA75fy5FPUTPFPmKp4gtFqtre8QnsRL81KVB6XtawFUxwtHzD16pkDbZLxUiixNT74fDUP4eMBhyCkVGJV` | seller / seller | FAILED custom 6001 |
| T7 | 17:51:34 | `5biAqKoAK9SnHPV8wZ7YX78ZiEn5xWMyn7sJG7X6h9tzbGPxjWxAkNdsczVPUQ1SXJfxxVFoGqi7PYLbLREiKkXo` | N / N | OK |
| T8 | 17:52:29 | `4dwemkQu4jNdURt9kFZSnpbh8DYtV4fASJCTqeq7ePFUw9iFNw6eVxjo1FfridGb7EUk5vnw1KHhhcGnaWHDmSrB` | D / D | OK |
| T9 | 17:52:55 | `3VxsVR8DzZZFNPkfZJWyWqo2LUcgbXczJNESKypEiVehccgBzwFYjfZ3Mo4pnEVGMJHvxbTyX7Zkmj9SPYLMZis9` | seller and ST / seller | OK |

Failed T2/T3/T4/T6 only cost 15,000 lamports each, with no executed transfers.

## Instruction-level ledger P001–P025

| ID | TX / index | From → to | Raw amount | Interpretation |
|---|---|---|---:|---|
| P001 | T1 O:3 | seller → N `A5dM6FcPcLoqaXG6JpLAAN5cgAtK5W5XuXocLkgkfRSv` | 895880 lamports | temporary funding |
| P002 | T1 I:4.1 | seller → W `E7JyKtcHWFDKx81SsFpSNrKcNPNhhesbUbL3gGjvUNXh` | 1488440 lamports | WSOL rent deposit, returned |
| P003 | T1 I:5.1 | seller token account `2kCcBigGMmdbqRUGfzprxiwMX9EQvKdPUQWRrjf8qpwx` → pool `BQ7788Jp1qtCaAMUnqPAfyFdP4EMwjStUdAMPkEbna36` | 594968303379290 raw GLITCH (6 decimals) | sale |
| P004 | T1 I:5.2 | pool quote `96XzgQ9i8fBrRscUUwfNmWzuTqfhJFMGreHDXADMUAZL` → W | 132890991957 raw WSOL (9 decimals) | gross sale receipts |
| P005 | T1 I:5.3 | pool quote → `94qWNrtmfn42h3ZjUZwWvK1MEo9uVmmrBPd2hpNjYDjb` | 33626264 raw WSOL | separate pool payment |
| P006 | T1 I:5.4 | pool quote → `DjWdbKx2qi7zWL8Yhrp6diW16FtsjWNvDwkJuyPgVtac` | 1277798000 raw WSOL | separate pool payment |
| P007 | T1 I:5.5 | pool quote → `GAFuhgcd328SkkBYHpfadzmef9hTGAFRCi9QoCnsZQug` | 33626263 raw WSOL | separate pool payment |
| P008 | T1 O:6 | W → seller | 132892480397 lamports | internal WSOL close: receipts plus rent |
| P009 | T1 O:7 | seller GLITCH account → seller | 1513840 lamports | rent recovered |
| P010 | T1 O:8 | seller → `Astran35aiQUF57XZsmkWMtNCtXGLzs8upfiqXxth2bz` | 3000000 lamports | external |
| P011 | T1 fee | seller → network | 15000 lamports | transaction fee |
| P012 | T2 fee | seller → network | 15000 lamports | failed |
| P013 | T3 fee | seller → network | 15000 lamports | failed |
| P014 | T4 fee | seller → network | 15000 lamports | failed |
| P015 | T5 O:0 | seller → R | 6644549597 lamports | external |
| P016 | T5 fee | seller → network | 5000 lamports | fee |
| P017 | T6 fee | seller → network | 15000 lamports | failed |
| P018 | T7 O:2 | N → seller | 890880 lamports | temporary-funding return |
| P019 | T7 fee | N → network | 5000 lamports | fee paid by N |
| P020 | T8 O:2 | `DYxqMo2QsGr8dqnJfZWyhQkm26NY2mqQFUzVbbLH6b6f` → seller | 1000 lamports | independent inbound |
| P021 | T8 fee | same D sender → network | 5050 lamports | sender fee |
| P022 | T9 O:1 | seller → ST | 150173828355 lamports | temporary stake-account funding |
| P023 | T9 O:2 | ST initialized, seller staker/withdrawer | 0 | no transfer |
| P024 | T9 O:3 | ST → B | 150173828355 lamports | external withdrawal |
| P025 | T9 fee | seller → network | 10000 lamports | two signers |

## Seller balance reconciliation (SOL)

| Point | Seller SOL balance |
|---|---:|
| Before T1 | 23.928966155 |
| After T1 | 156.817561072 |
| After T2 | 156.817546072 |
| After T3 | 156.817531072 |
| After T4 | 156.817516072 |
| After T5 | 150.172961475 |
| After T6 | 150.172946475 |
| After T7 | 150.173837355 |
| After T8 | 150.173838355 |
| After T9 | 0 |

T1 check: 23.928966155 + 132.890991957 + 0.001513840 - 0.000895880 - 0.003000000 - 0.000015000 = 156.817561072. WSOL deposit 0.001488440 funded and returned in same transaction, net zero. Seller's own T1–T9 fees sum 90000 lamports.

B held 127.361453351 SOL before T9 and 277.535281706 SOL after it; recipient funds thus also commingled.

## Attribution boundaries and next steps

- Reported from finalized Solana Mainnet RPC: history 46 entries (one page), sale and eight later transactions, five successful + four failed, status separately checked. No downstream R/B histories traced.
- Two dominant recipients: R = 6.644549597 SOL; B = 150.173828355 SOL. Another 0.003 SOL to Astran service/payment address. Transfers out exceed 132.89 SOL gross GLITCH receipt because seller had pre-existing funds. **No exclusive attribution of any outgoing SOL to that one sale**.
- Work observed at finalized slot 456501665: seller, W, ST and B returned nonexistent account; R System Program owned. This says nothing about subsequent B proceeds.
- UNRESOLVED: exchange/service labels, downstream distributions, beneficial owners, human identity, net trading profit, Kytro linkage.
- NOT ASSESSED: fraud.
- Only examine **one downstream hop from R and B** as a separately authorized next research task, preserving exact records and evidence limits.
