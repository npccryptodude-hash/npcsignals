# GLITCH early launch documentary follow-up v0.2

Date: 2026-10-13. No ChatGPT Work available. Review of existing GitHub files and public indexed sources; no new RPC receipt retrieval.

## Directly documented activity within ~17 seconds of creator transaction

- **16:22:10–16:22:27 UTC**: structured SOL cascade ended in ten equal transfers to eventual large seller `8hiMXA1UHYUAeW6gd6q1XQLWzZkQL48znqgdgY1388B7`. This proves funding connectivity, **not** that every relay wallet bought tokens.
- **16:32:33 UTC**: creator `Ft2XtprBymZsGwYUMjsLN6z8WZzguTVa5rFYSuN41S8i` received 70m GLITCH as reported from `5xrGXTXnf7ZDe731C7EB5cNVnERshsZhT3E66udWiXmCtzaBGSVbmFygDovhJmzSrvUpG6m1PBRWQcq6S8UT18FV`. This is a documented creator transaction, not automatically independently established as earliest token launch trade.
- **16:32:50 UTC (17 seconds later)**: GLITCH v0.2 documents a distinct wallet `sF1WgsX2YVfEP3Nu7hKzp6beWe78WKZUNifeTE2HWuS` selling GLITCH for 6.708180714 WSOL; transaction `yH7hEtrWaAN5df8GgVzAZVbwQVKXTrLTBSFHMcVWQZVfjHKi5FHYD2JojrSFppD7FA1i82MTENqwxwitZCtP6Uv`, with a seller-owned token account and proceeds movement.
- **Same slot, next transaction** `2RRBTvJ43pasWVzrseXVJT3DpXdsAMwKvPgksrH1gtin7z12A1uzsg4vG7fMJd3FM6pBoj4WUXi2rD2deiJzciDa`: eventual major seller signed a follow-on close-account / GLITCH purchase funded by that path (as reported in v0.2). Need exact token buy amount, source provenance, payer, token-account owner, original receipts to identify the full swap mechanics.
- **17:35:52 UTC**: same seller sold 13,019,227.226265 GLITCH for 25 WSOL; `21K6WSXFtEKbi6mJ7qhRgXojXyrJvZxsQJgks9S7Cg3xSZaU92tME545q7KhQK5g7LczCHwNbwpKHvteBiNHMy3x`.
- **17:51:18–19 UTC**: 70m creator→seller-owned token account followed by huge seller sale of ~594.97m tokens for ~132.89 WSOL; confirm exact inventory provenance before alleging 70m were included in sale.

## New cross-check question

The `sF1...` early-seller and subsequent eventual-seller purchase at 16:32:50 are **more directly relevant to early launch trading** than the ten SOL relay wallets, whose token buys have not been documented. Compare these two full finalized receipts with the creator tx to measure order, direct funding/value-path and actual net acquired amount.

## Public source verification

MEXC official wallet list displays exact `ASTyfSima4LLAdDgoFGkgqoKowG1LZFDr9fAQrg7iaJZ` as USDT Solana wallet:
https://support.mexc.com/hc/ja/articles/13459541357209-MEXC%E3%82%A6%E3%82%A9%E3%83%AC%E3%83%83%E3%83%88%E3%82%A2%E3%83%89%E3%83%AC%E3%82%B9
No contemporaneous indexed source for an exact GLITCH fair-launch promise by @KytroCrypto was recovered in this public search.

## Evidence quality guardrails

Do not claim “90 insider wallets bought 68.5%” based solely on FEYN screenshot. Do not count funding relay addresses as buyer addresses. Do not infer that a prior funding sender controls its recipient wallet. The v0.2 report explicitly states the `sF1...` transfer does not establish shared human ownership of `sF1...` and final seller.

## Priority when archival RPC resumes

Replay creator `5xr...`, early `sF1.../yH7...`, eventual seller buy `2RR...`, and seller's historical token-account owner at 16:32:50. Then enumerate real GLITCH buys from launch in slot order with token deltas, rather than treating a funding cascade as evidence of buyer clustering. In parallel archive full eight MEXC signatures as required by v0.16. Keep bank/customer identification unresolved without authorized records.
