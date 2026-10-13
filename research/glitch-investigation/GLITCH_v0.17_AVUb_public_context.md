# GLITCH / ZYROX — v0.17 AVUb public-context check

Date: 2026-10-13. Verification of indexed public Solana explorer and official MEXC address publication. No fresh RPC history sweep.

## Confirmed published MEXC address
MEXC official list directly includes `ASTyfSima4LLAdDgoFGkgqoKowG1LZFDr9fAQrg7iaJZ` under SOL USDT/USDC:
https://support.mexc.com/hc/ja/articles/13459541357209-MEXC%E3%82%A6%E3%82%A9%E3%83%AC%E3%83%83%E3%83%88%E3%82%A2%E3%83%89%E3%83%AC%E3%82%B9
Work previously reported eight finalized USDT transfers totalling 477.442575 USDT to `8HCSEeC98fR2BcDs8mkyiRq3ahSc7GNEqNEsW5oWote2`; their raw signatures remain to be archived. The address attribution does not attribute a particular MEXC customer.

## AVUb activity with independent third parties
Wallet `AVUbPESe87nx9DqhJp2Xi5x8omd4bT9TRod9dk2P31yD`.

1. Public Solana Mainnet explorer: 2026-05-26 11:58:26Z, finalized transaction `zFk7sMcmf4dVYSXzH2FrAzZRFMRv2LmCg1iV4XFfLD5d55a5uPZzz9Srv3Z8H1WNv7yA1eUudybUyNxqyesvKXs`. 2,000.01 USDC from owner `2a3QXuCXpwpKRAnmX67M4iaGpUVVMwSUgeRpuzhcphyT` to `EfYzVpDkA9fQjJmytfWuqsNSgTBetS1u6rdtLgNx5rbD`, explorer identifies token owner AVUb. Transfer signer 2a3Q; fee payer `9kHTT3RgH51FhMzKjxk8XXHoNnVjEjK5JnwTVSP8rXTy`. Source https://explorer.solana.com/tx/zFk7sMcmf4dVYSXzH2FrAzZRFMRv2LmCg1iV4XFfLD5d55a5uPZzz9Srv3Z8H1WNv7yA1eUudybUyNxqyesvKXs . Explorer notes current account data may differ from historical; recheck pre/post token-owner in RPC before historical attribution.
2. Public Mainnet explorer: 2026-09-13 14:40:31Z, finalized transaction `S3zVstAMUuPGAntHs71Uknyvgv8hwXKgHpSo3t6PqWrdPc9nhML4XorsukS5YNKg1niG9DNF9ELirdpHqPu3QZy`. SOL 2.47967343 from signer `6Ri8g4BMemCnT3dYqJvF5gPzmgyKCX8jUm5cZQDbRcro` to AVUb; fee payer `FU8KibWzoNfnsytAfc3fRG8AZMMB4hS7Pfx9NyNSXt1D`. Source https://explorer.solana.com/tx/S3zVstAMUuPGAntHs71Uknyvgv8hwXKgHpSo3t6PqWrdPc9nhML4XorsukS5YNKg1niG9DNF9ELirdpHqPu3QZy

## Cautions
AVUb has incoming from independent source addresses before GLITCH. This does not establish a shared operator, service affiliation, or private-key ownership. The separate 8HCSEe→AVUb transfer of 159.006259 USDC dated 2026-10-03 was only provided with abbreviated signature `56DhD8…8to2`. Its fee payer/cosigner `6nvUkyJG5j6rH3Hfm15mJNgPMJ1cxHQapfm5K3k647iv` has no independently confirmed entity label from public searches in this pass.

Next: recover full 56DhD8 signature and finalized receipt, compare 6nvUky fee payer pattern to distinct transactions, test AVUb account's historical owner at event slots. No unsupported human attribution.
