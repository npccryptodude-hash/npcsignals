# NPCsignals — Binance U300 Evidence Package v1.0 checkpoint

**Date:** 2026-10-14. **Evidence source:** User-provided completed Work summary. Work reports a downloadable evidence package containing seven original JSON-RPC receipt responses, separate finality evidence, a 17-row CSV/JSON ledger, balance reconciliations, source records, file hashes and a passing offline verification script. **The underlying downloadable package was not attached/copied to GitHub in this commit**. This file records the results but is *not* a substitute for the receipt archive.

## Primary confirmed transfer

- Sender (ZYROX U300): `8zHcWujHhyJri3CRTcWUGmT5WSRdwW7xrns3WTTkPGvS`
- Recipient (Binance-labelled): `5tzFkiKscXHK5ZXCGbXZxdw7gTjjD1mBwuoFbhUvuAi9`
- Amount: **22.896954041 SOL**, native System Program transfer, outer:2 zero-based
- UTC: **2026-10-14 06:00:01**; slot **456730989**
- Full signature: `4m6gaPuwQnwN7KFSeCi3SzaqJzyj6JPzL5sMjq2c3gYuniYAqg3kZMPsseDdomzVJaVjZF3LPXYyHXAqeKKfSuYb`
- Successful finalized receipt independently re-fetched and checked by Work, separate finalized status
- Authority, sole signer and fee payer: U300 sender
- Transaction fee: **9,000 lamports**
- Sender pre/post: 25.216560668 → 2.319597627 SOL; source delta matches transfer + fee
- Receiver balance increased by 22.896954041 SOL

## Network linkage

- Exact U300 address matched current ZYROX primary ledger blob.
- Five GLITCH-route transactions independently reproduced by Work. They are relevant to the address-level path; do not equate transactionally linked wallets with common individual control.

## Attribution limits

- **CONFIRMED**: Transaction, receipt/finality, sender authority and balance reconciliation; case-related U300 address linkage.
- **SUPPORTED**: Binance infrastructure as recipient, labelled hot wallet in Bitquery and “Binance 2” on Solscan. **Exact address in Binance official public list was not recovered**.
- **UNRESOLVED**: Whether Binance credited a customer or performed an internal custodial sweep; whether Binance also controlled U300; identity of instructing customer/beneficial owner; common human control.
- **BOUNDED NEGATIVE**: Screen of 786 preserved receipts found no additional successful parsed transfer to exact destination. Not exhaustive full history.

## Provider-ready next action

Package is **ready for referral to an authorized investigator**, *as a Binance infrastructure inbound-transfer lead*, not proof of a customer deposit or wrong-doing. An authorized request to Binance should ask to verify: (1) whether it controlled receiving and sending addresses at historical UTC; (2) recipient operational purpose; (3) booking classification (customer deposit, internal sweep, other); (4) linked internal transaction/account records as law permits; (5) exact full signature/slot/time reconciliation.

Official Binance law-enforcement guidelines: https://www.binance.com/en/support/law-enforcement/guidelines

No Binance contact made; no identity attribution. Do not publicly identify a person or assert custodial customer credit.

## Preservation gap

Work's downloadable v1.0 export contains original receipts, finality, checksums and replay script. **Export ZIP/files are not yet uploaded into this GitHub repository**; separately archive original bytes and SHA-256 checksums before any external referral.
