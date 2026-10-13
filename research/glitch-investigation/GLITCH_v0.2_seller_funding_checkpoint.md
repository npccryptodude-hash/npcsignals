# GLITCH v0.2 — Seller funding and ZYROX overlap check

**Evidence status:** User-supplied Work result, reporting finalized Solana RPC receipts. Signatures and fields below are preserved verbatim; raw receipts were not downloaded or independently decoded in this GitHub documentation pass.

**Base:** GLITCH v0.1 checkpoint at commit `d817ee10efa4178cc5f665ab606ed7240c32304c`.

**Target seller:** `8hiMXA1UHYUAeW6gd6q1XQLWzZkQL48znqgdgY1388B7`.

## F001–F010: Initial SOL funding

Work reports 46 finalized transactions in the seller's history (one page, limit 1000), no pagination needed. Prior observed seller SOL balance zero. Ten distinct funder wallets each sent **0.011428924 SOL**, all between **2026-10-12 16:22:25–16:22:27 UTC** (18:22:25–18:22:27 CEST). Sum **0.114289240 SOL**. Each funder was sole signer / fee payer, paid **5000 lamports** fee, and reportedly ended with 0 lamports. Their prior source of funds remains unexamined.

| ID | UTC | Funder | Transaction signature | SOL received |
|---|---|---|---|---|
| F001 | 16:22:25 | `6dCi4dzSrsTX7sWAdyxbYr4rxj8rcUgxBGqiqZGEhEBe` | `2hGm4ByesADXLrwnVq5xW187jaCgNnXMSHUMFer8tXFUkf7L6QmhtEX3bb5UQq36HMGFigYct6jBpkoBtScBrJMt` | 0.011428924 |
| F002 | 16:22:26 | `B15ETWARs7xCzfZKnrgKvgrqKnSysgBRK7ZrC6WaSv3y` | `57t3D65AarcMjMSRgdzDF9H79X7oKBh8Fc3DRNzrgYrPgknJgRS3HWkFo9c8gDzDpTqAekyTQAnpcUegnXaUjKGv` | 0.011428924 |
| F003 | 16:22:26 | `922XaYT17M7b37YvptkbhmvViWBrdF2Amg5ZxVQhtcE6` | `5michrvBLhksGvdVMRFpJyN2fTzD8VaRCR51vwCBBPra5x5kWrUuNh8dxZSttj7yFqUMQ8MRW8QhzXcjyqK1qQY7` | 0.011428924 |
| F004 | 16:22:26 | `57Ragkj62qpfru5nocCA9jG3qt3GvYY83d8UzEnJWGHR` | `56cMbyipdHNt2B2yvWL6Vkz8LbYStVb1u36JLUe7eXamhH2rcgNR1t6azACji3dHBG5ZoPSdAPsNGbKLGkyyRBmm` | 0.011428924 |
| F005 | 16:22:26 | `BsH2DnbSocfdTA5rmAYStvroFhP9natf48kArdMnJrjH` | `4sZYG1qVoHXhtVhK8wsVTy1PeMxgMwidRG1RomyoLWdy2JG3bJgXn2EXzFtmTB6vmGXnurE4DN9emhEcfQbJWsBa` | 0.011428924 |
| F006 | 16:22:26 | `Dxf4ywkjNHyk7Whi95oHZ2iBWgaqDGi6Mwvw6agFPkSR` | `5AQNdZbAwDiszySCsnKG6CXoK8wjkw8f4ekSvb2vxbxG6RnGSP8dtZdNXogN5sa8utDy2KgyFqxfxCP1PtVeF6ok` | 0.011428924 |
| F007 | 16:22:26 | `7NZYS2KgM87J3QsLczRfvomxxRSRVVF1wto96x8ijHkS` | `YbJ5U5gCbEYzD9y3PHhump78XkGiP3xNSi4bvmqDg8y7xVgGfL48GUppH1wTqm14Lgg8d5MWNtZwdx44xuS9BPR` | 0.011428924 |
| F008 | 16:22:26 | `5Li861JE22SYv8zQdisXkjDWu81RAKzMR8qZsPA5RVEG` | `4RNyMMoHoGk4ku5kQhsHPXdrLwfPKmfPMN4yhuCJgje6cb8k8h8MMSQdPZXfADi7rKkpLKer5HVMm3hJrxwaASh1` | 0.011428924 |
| F009 | 16:22:27 | `2CZAHT8tg13JrR6cUwfh8RB7VxgTkVVXW6GskSE8f1AB` | `5cvAThLvZtniAvPRG6FVQy7XFXtpVunfMu5Mfkc6C21ZtDm7oPzU6fRYQhAwfTAERXuNXwjVbubCjgdQASApVEsu` | 0.011428924 |
| F010 | 16:22:27 | `E9Uvd7PnHSumFp8U2cATRpNbTYCNgmWxGMNuLMdMYN8y` | `2s7ehGKNeS4hptU3eQJyZ3cndy6r7B82W85qXuGcWFAodJxj9dMSM5evF1QuBdXqjpx7QUQ8zMntet1scUE9XTHh` | 0.011428924 |

## F011–F013: Additional receipt-reported seller financing and trade activity

- **F011 — 2026-10-12 16:32:50 UTC:** `sF1WgsX2YVfEP3Nu7hKzp6beWe78WKZUNifeTE2HWuS` sold GLITCH, reportedly received `6.708180714 WSOL`. Same transaction created token account `2Lg8mHafjJbbJ5XW6yaMh4nUqUu1wwq7Jb7jTktKSz2s` with seller as SPL token-account owner, then moved proceeds via account closure. Reported SOL balance: `6.711708434` including rent. `sF1...` was sole signer and fee payer, fee `12000` lamports. Signature: `yH7hEtrWaAN5df8GgVzAZVbwQVKXTrLTBSFHMcVWQZVfjHKi5FHYD2JojrSFppD7FA1i82MTENqwxwitZCtP6Uv`. **This documents an asset/value path but not common human ownership between signers and seller.**
- **F012 — 2026-10-12 16:32:50 UTC, same slot:** next transaction closed the seller-owned token account into seller WSOL account and funded a GLITCH buy. Seller sole signer / fee payer; fee `5100` lamports. Signature: `2RRBTvJ43pasWVzrseXVJT3DpXdsAMwKvPgksrH1gtin7z12A1uzsg4vG7fMJd3FM6pBoj4WUXi2rD2deiJzciDa`.
- **F013 — 2026-10-12 17:35:52 UTC:** seller sold `13,019,227.226265 GLITCH`, received exactly `25 WSOL` from pool quote account. Seller sole signer / fee payer, fee `9801` lamports. Signature: `21K6WSXFtEKbi6mJ7qhRgXojXyrJvZxsQJgks9S7Cg3xSZaU92tME545q7KhQK5g7LczCHwNbwpKHvteBiNHMy3x`. This is **trading revenue, not external wallet funding**.

## X001: ZYROX overlap test — exact match versus infrastructure

Work reported exact-address checks at the cited GLITCH base commit against:
- `research/zyrox-investigation`
- `research/zyrox-investigation-post-freeze`

**No exact address match reported** for seller, the ten original funders, or `sF1WgsX2YVfEP3Nu7hKzp6beWe78WKZUNifeTE2HWuS` in those two ZYROX directories. This is a **bounded negative textual match**, not exclusion of wider on-chain connections.

Two addresses were reportedly shared with ZYROX as **infrastructure references**:
- Jito-tip address `ADuUkR4vqLUMWXxW9gh6D6L8pMSawimctcNZ5pGwDcEt`
- Payment address `Astran35aiQUF57XZsmkWMtNCtXGLzs8upfiqXxth2bz`

These matches **do not demonstrate common wallet control or shared beneficiary**. They must not be described as direct overlap of case-controlled wallets.

## Interpretation and limitations

- **OBSERVED (Work-reported receipt fields):** Ten equal SOL inflows within approximately three seconds, total 0.114289240 SOL; token-account financing; earlier 25 WSOL GLITCH sale.
- **INFERRED (investigation lead, not proven):** Equal-size, near-simultaneous funder transfers may be compatible with organized provisioning; timing/amount alone cannot prove common controller.
- **UNRESOLVED:** Origin of the ten funders' assets; funder common control; nature of `sF1...` relationship; Kytro attribution; ultimate beneficial owner; realized net P/L; full FEYN 90-wallet/68.5% reproduction.
- **NOT ASSESSED:** Fraud or legal liability.
- **Reproducibility gap:** Store the raw finalized `getTransaction` JSON for all 13 signatures and the precise ZYROX address-search procedure if available; only report-level detail preserved here.

## Recommended single follow-up

Inspect the funding history of **only the ten F001–F010 funders** to test whether they converge to one or more common upstream sources. Capture exact signatures, amounts, times, signers and fees. Do not infer shared human control; do not run broader graph traversal without a new checkpoint.
