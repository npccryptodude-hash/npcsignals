# GLITCH v0.5 — U-layer direct funding checkpoint

Source: User-supplied Work result dated 2026-10-13, based on finalized Solana mainnet getSignaturesForAddress and getTransaction. Work reports 20 unique receipts, all meta.err=null. Raw receipt JSON has not been archived here. This is evidence from Work's analysis, not a separate RPC revalidation by this GitHub update.

## U01–U10 → A–J

Ten upstream U wallets each reportedly funded four distinct A–J wallets; every A–J wallet received four transfers. Each transfer is 2,859,731 lamports. The twenty receipt statement refers to Work's examined history; reference signatures shown below comprise ten funding transactions, with four transfer instructions each.

| ID | Sender address | UTC (2026-10-12) | Signature | Recipients |
|---|---|---|---|---|
| U01 | `9bFbwPq8L4ECFxKwzU48Kr9Gzyw4vLR1agKtyoC86AnT` | 16:22:12 | `259sRomc7xTJp9midBkHQkVK5yZiLSWJWtENSk7nBYzfn4vznvTShED1GNUzrm9AUUPBdg8iietZajah53vrURfh` | C,D,E,F |
| U02 | `AAQGF5AMFnsmVvfpAuLpBjNhYAJrkrJLsrcgbegzHK7k` | 16:22:12 | `2CakHM7KMYXxr4uTVhUyaQ1jupctntU5AN8f2DZ81aorxZVDShGjzfmQW8bdTDet6kxH62PmzxG4feDLAauPJwF4` | B,C,D,E |
| U03 | `7k8M4HfpCA66eQYG7SevUfGEz44irQz2dB8YgRD32VfA` | 16:22:12 | `32F4vztozf7vQZGtLQs8aX3YdTtNbzqW565rDmz2Kb83iC1kRkANHEbyf39HqzW886BfwM5C9ktsJKmyYox9oX4M` | D,E,F,G |
| U04 | `E3G6yHhpKKVs9NiPB6JXHynVrjP94R4Fqqx61E6dEkQw` | 16:22:13 | `1etBSETCwpmi3YPNjpYjRp8qk3B5aAhPSLdPYVWz1HqfBQ97Zn7PUC87VhMeDUmcoH7Pp7svBrBJmYy5Dj86STj` | F,G,H,I |
| U05 | `ECdLDbVihBEJfBWnNv6Amdo419JrLmfpWoAKFHSoNmvn` | 16:22:13 | `2nVs4gYCCknXxP96gzmtk2zHVyir9WKyT9eCuZt9W2kzp7JKamcTaQtfb2npark3g5bBoJXdkGtT9MPPhesD7sHh` | E,F,G,H |
| U06 | `3jQpygnEBJyM7Z6SVMBLNLdw5YqvD9QX7fUocCRZTwkq` | 16:22:23 | `2v49WzQjKZEjbmf2AS7KigmZNNsN1fdWjqobiEJS5grW6MsKzqUUvhdkZViNBgHGedAFnUNUP2LB48D773CRvt8S` | A,B,I,J |
| U07 | `GicAwUoRc9w8JxEj7x1jRxDNhyLNVLZhEdeaPsWpecSP` | 16:22:23 | `2vi2sqrM5b9omfmgMYYkZocYdqcyrdsSmsYT4B6HUymN8FDDJYxSXnb9HUAypzfNc3EXV8Z2U7H3vjQt82MjDUx8` | G,H,I,J |
| U08 | `5YtPvdDeuBFzhrS6Pd4G5fQJ8Hj4YFqcpPZeEF4gYSwB` | 16:22:23 | `3Ja7Fk9xBYxBSQcErquKVjGamHxN5c9d3YpzhtXG1UnKpfhdsDKE1RMj8j2fWKiCna1mE7jY9PEeeHrUmpAsYPaX` | A,B,C,J |
| U09 | `5Hezry2fNHDmedqdcKDmbjSkyLRzhRXxAaqzgT5NRQZH` | 16:22:23 | `492vbXepVUn1aSv6LiqKF6YBiVjZLHRpFG1VDf3XxXmcfKev5RgBEYq66g2rXhXs4oBMiyBhgzE6uqtEm7U81CH5` | A,H,I,J |
| U10 | `6CwuMRzXGDGrD3QoEEM2RfxD1RJYmLhhxKnfpu1cFfCp` | 16:22:24 | `3fCVFUAgAbgisrshb5u5TGQwRs1B5aC66SLkfy7GbGRLqNUwnGDbXkJ8T3xyNTjTzgUDU8vDmXKyJdzLUQ3XzHLv` | A,B,C,D |

## Funding reconciliation

- Each A–J started with reported zero SOL balance.
- Each received 4 × 2,859,731 = 11,438,924 lamports.
- Each forwarded 4 × 2,858,481 = 11,433,924 lamports to F wallets in one transaction and paid 5,000 lamports transaction fee.
- Each final SOL balance reported as 0.
- Aggregate U → A–J = 114,389,240 lamports (0.114389240 SOL).
- Aggregate A–J → F = 114,339,240 lamports; A–J fees = 50,000 lamports.
- Aggregate F → seller = 114,289,240 lamports; F fees = 50,000 lamports.
- No numeric discrepancy in the user-supplied summary.

## Evidentiary limits

- CONFIRMED AS REPORTED BY WORK: overlapping direct funds, 40 transfers, 10 funders, 10 recipients, receipt finality.
- BOUNDED NEGATIVE TEXT SEARCH (Work-reported at commit 8108d0ce6e271883b0d4dd0ebc5514e029e1b028): no exact matches for A–J or U01–U10 in either ZYROX research directory. This does not exclude wider on-chain links.
- UNRESOLVED: human control, shared controller, original funding to U01–U10, any attribution to @KytroCrypto, any service/infrastructure attribution.
- NOT ASSESSED: fraudulent conduct.
- REPRODUCIBILITY GAP: complete instruction-level 40-row U → A–J ledger and raw receipt exports still required.
- Do not equate the 0.114389240 SOL funding cascade with the 132.890991957 WSOL sale proceeds, which involve substantial token holdings and other trade activity.

## Next actionable question

Check one prior funding hop for U01–U10 only; stop if sources are unavailable, shared service infrastructure is detected, or the trace loses evidentiary value. Keep all ZYROX files unchanged.
