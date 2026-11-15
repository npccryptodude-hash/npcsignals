# Ethereum E1 and E2 routes

## E1: independently reconstructed financial path

Recipient: 0x4b304741599c125a244e498d14562487d7109ab8. Discovery source: original FairGambling report's direct Etherscan link. Its description is a lead, not authorization or ownership evidence.

`principal_by_source.json` gives exact per-source totals. A supplies 738.148858772417648963 DAI and 1.695247971538047708 ETH. S1 supplies 316809.689210 USDT, 468830.099059 USDC, 20077.942698961878 USD1 and 74.266886368632320300 ETH. S2 supplies 109231.124988 USDT, 34171.291810 USDC and 10.994221771600303228 ETH successfully.

Seven receipts show E1 stablecoin inputs to 0x9008d19f58aabd9ed0d60971565aa8510560ab41 and DAI outputs back to E1. Their full hashes and event indices are in the ledger: 0x00ce1e32059de820e307f65aaac3d790a95fcab2a48b82be768c9f5ab07b2441; 0x2b2a4ce1aa3f910d44b1425718429c8c7d1c5440729acf046fd26586b72356bb; 0xf00e7510ce52f85fbde1066922dc9f18fadb5710892d972bf62532c21792d52e; 0xf13d17c1b8a167aa087ed6402e1788de0244772dd39b78b9d377e38232bd7af9; 0x3ea5d430d9966ecc19a58ff3433129eaea619cd4f95038e9e34b6ad403bc8000; 0xc9a9ae19e7ec220ac5e310a986cd819542a5259406a2f307600e7b8ea4c4b842; 0xced9badc65a23f72a9462d427ae8350c87710bf3d4b32b8763738ba6375d1367.

The final conversion is at 18:00:11, just outside the requested 18:00 boundary, and is included to close the route. It is not an additional original outflow. Swaps execute through third-party transaction initiators; these are not automatically the beneficial owner or authorizing key.

At block 26184625, immediately before A's first observed token arrival, E1's four tracked token balances and nonce are zero. A holds exactly the DAI amount it then transfers. This does not prove E1 had no earlier native funding, previous other-token history or other-chain activity. E1's nonce is 3 at the closing state, and its self-transaction is separately classified. No new EIP-7702 authorization audit is claimed.

## B/E2 candidate: matched BNB-to-Ethereum routes

| BNB deposit transaction | UTC | BNB USDT debit, 18 decimals | Ethereum execution | Verified output |
| --- | --- | --- | --- | --- |
| 0xb4e697fc1cb8406ca6e18ee3a1b4f975428e2642caa57076df5d9b166848c1b1 | 16:34:31 | 370000.000000000000000000 | 0x70a41ee50eb9277365900b8a23e8e30fe20ba4818b2db1a4e626b1fb11f92b14 at 16:34:35 | 369592.897320 USDT to B |
| 0xcc827fd1fef937ac1942dd53a7f049061b827bf5292e1aa9a7e79610c00f200b | 17:43:53 | 336943.421822265793499428 | 0xf110d179d86cd74ee3b7e6bda3fa1724258274571d66c1909a05fcbc899d66a1 at 17:43:59 | 336199.051906277094220550 DAI to B |

The source event's final 32-byte word is found in the corresponding destination input: `0x8b16de100c87b160d3c08211ceeabd83103b45340f1df249db9e7b149620d81b` and `0x9014a78b4543d4173c4f22cebc8d83d8d3e7aedf7ac284282a1c09c65f1ac4e6`. These are opaque on-chain correlators, not a newly verified signature or proof of bridge solvency. Relay's independently queried public index maps the same pairs. verify.py checks source debits, deposit amounts and destination credits. No shared-infrastructure ownership inference is used.

G006 already establishes conversion of the first USDT receipt into 369254.438406208540569231 DAI, four additional DAI payments, and later routes. G010 does not reverify or recount those completed transactions. New archive state confirms B held 816635.912748421658923307 DAI at block 26185250, with zero tracked-token opening balances at 26184449. The later 869368.076253071235248671 figure is G006's observed net delta, not a new G010 later balance query.

Thus B is an evidence-backed E2 candidate, but the approximately $870000 media description is not fully reproduced as a Relay-only route: the origins of the four payments and B's BNB funding remain unresolved. Two matched deposits alone cannot establish the reported majority or an original unauthorized principal.

## The BUSD connection

E1 sends A 0.01 ETH at 17:42:23 in 0x90d15c162609522d1229818adfe352d48270db57050e7179a0c0d779a6c1fc0e. Frozen G006 records A→B 10456.137361559383267328 BUSD at 17:45:23 in 0xebbe5ad72e9f02479b8c989f2e072807a3263e45853611162ae7fbe5c51ca0c5. This is an exact financial connection between the E1 and B networks, not an amount-only resemblance. The rounded 10456.137362 lead is consistent with that exact amount.

We do not establish that the 0.01 ETH was A's only available gas, that BUSD was the next nonce, that these were stolen funds, or that A/B/E1 have one operator. The BUSD principal is not included in E1 inflows or counted again after its later conversion.
