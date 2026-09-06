# Source Index

This index records the principal public, technical, archived and captured sources used in the AI Performance Narrative Audit 2026.

The source index is intentionally conservative.

A source appearing here does not mean every claim associated with it is verified. Each finding must still be read together with its evidence grade, verdict scope, counterevidence and limitations in `evidence-ledger-v1.0.csv`.

---

## Source-status labels

- `PRIMARY-LIVE` — original source is directly accessible.
- `PRIMARY-CAPTURED` — original source was captured directly, but may no longer be live or may not yet be archived in the repository.
- `ARCHIVED-CORROBORATION` — archived or mirrored copy used to corroborate that public material existed.
- `SECONDARY-DISCOVERY` — third-party index or aggregator used for discovery or supporting chronology only.

Third-party repetition is not treated as independent verification unless it adds new evidence.

---

# 1. GRASS entry case

## GRASS token

**Contract:** `0x16391C40e85FB2246A2C8c17bfA2594C5d3EF84b`

**Network:** Robinhood Chain

**Chain ID:** `4663`

**Role in audit:** underlying asset referenced in the viral performance claim.

**Source status:** primary technical/on-chain evidence where independently retrievable.

**Important limitation:** market movement does not establish that the claimed autonomous agent executed the stated entry and exit.

## Zynex published/personal wallet

**Wallet:** `0x690d7552375Fcd23Bd2a5E1d74f7445FAdfc6c83`

**Role in audit:** wallet publicly associated with the creator/account during verification attempts.

**Finding relevance:** no transaction path identified from this wallet that independently reconstructs the claimed GRASS trade.

**Limitation:** the claim reportedly distinguished a personal wallet from separate agent wallets. Failure to find the trade in the personal wallet does not disprove the existence of another agent wallet.

## GRASS claim video

**Role in audit:** presentation evidence for the claim that a Grok bot entered near a $30K market cap and exited near a $2M market cap, with approximately `0.3 ETH` becoming `19.7 ETH`.

**Observed presentation details include:**

- `0.3 ETH` entry
- `+19.7 ETH`
- `66.7x`
- position marked closed
- safety labels including no honeypot / verified / renounced / LP burned 95%

**Source status:** `PRIMARY-CAPTURED`

**Raw-file SHA-256 recorded during audit:**

`a935e1e4d3722c073bd58693e8721d135c2f31e152f8b3fffff4be780c3ab330`

**Limitation:** the video does not expose the agent wallet, buy transaction hash or sell transaction hash.

## Pons v2 launch architecture

**Relevant technical point:** documented launch architecture uses a bonding-curve process followed by graduation into permanently locked full-range Uniswap v4 liquidity.

**Audit use:** comparison with the claim video's `LP burned 95%` safety description.

**Verdict relevance:** `MATERIAL MISMATCH`, not proof of fabrication or intent.

**Pons full launch deployer recorded in audit:**

`0x3711ceA4feaDE896C913C68F01Eda97Cb06D1A42`

**Source status:** `PRIMARY-LIVE` where protocol documentation remains available.

---

# 2. MEMEMOON provenance case

## Zynex MEMEMOON narrative

**Observed narrative elements:**

- `I GAVE MY GROK BOT 1 SOL...`
- MEMEMOON
- `0.5 SOL` buy
- entry around `$0.0000012`
- narrative score `0.94`
- `+800%` after about 11 seconds
- `42 new holders`
- `3 whales`
- `8 SOL liquidity`
- approximately `60x`

**Internal inconsistency observed:** the same system reportedly states a maximum position size of `0.1 SOL`, while the MEMEMOON story describes a `0.5 SOL` entry.

**X status recorded during audit:** `2093277608632893471`

**Source status:** original post/capture preferred; archive only as corroboration.

## Backwood duplicate narrative

**Account:** `@0xBackwood`

**Role in audit:** separate first-person post reproducing unusually specific MEMEMOON performance-story elements, with some details modified.

**Audit use:** content-provenance analysis.

**Verdict relevance:** supports a `PROVENANCE FAILURE` finding regarding originality of the public narrative.

**Not established:** common account control, coordinated fraud or fabrication of the underlying trade.

---

# 3. KITSUNE validation case

## Enko KITSUNE claim

**Observed claim elements:**

- token: KITSUNE
- entry: approximately `0.8 ETH`
- entry market cap: approximately `$1.5M`
- exit market cap: approximately `$120M`
- claimed result: `+62 ETH`
- approximately `5,820 holders`
- safety statements including no honeypot / verified / renounced / LP burned
- autonomous execution framing

**Audit use:** independent reconstruction attempt.

**Result:** no unique contract, agent wallet, buy hash and sell hash were identified from the public material available to the audit.

**Verdict relevance:** `NON-REPRODUCIBLE` within the public evidence set.

**Not established:** that the claim was false or that the trade did not occur.

---

# 4. Amplification and FACTORY provenance

## RoundtableSpace amplification

**Account:** `@RoundtableSpace`

**Display name observed:** `0xMarioNawfal`

**Relevant status ID recorded during audit:** `2093824765785976942`

**Observed framing:** a Grok bot was described as autonomously launching memecoins on Pump.fun, killing failed launches and collecting creator fees from successful ones.

**Role in audit:** amplification layer.

**Important limitation:** amplification does not independently verify the underlying performance claims.

**Not established:** that RoundtableSpace created, approved or financially benefited from downstream tokens.

## FACTORY token

**Name:** Grok Token Factory / FACTORY

**Creator wallet recorded during audit:**

`HAh7q881D5qUiXuHCZQXx7PcQQWiyHWE3fVXF5j8khpV`

**Pump.fun profile name observed:** `ridarkdev`

**Metadata references observed during audit included:**

- `@enkoxbt`
- `github.com/enkoxbt`
- Enko-related public material
- RoundtableSpace status `2093824765785976942`
- language stating that fees were redirected to a GitHub identity

**Role in audit:** example in which public narrative and amplification material became part of downstream token provenance.

**Verdict scope:** token metadata provenance only.

**Not established:** that Enko or RoundtableSpace created, approved or financially benefited from FACTORY.

---

# 5. Pump.fun creator-fee infrastructure

## Pump.fun fee documentation

**Role in audit:** primary protocol evidence that creator fees and fee-sharing functionality exist.

**Relevant documented capabilities include:**

- creator fees
- creator fee sharing
- up to 10 shareholders
- allocation expressed through basis-point shares summing to 10,000
- social fee recipient mapping mechanisms
- GitHub identity support in fee-routing / claiming flows

**Source status:** `PRIMARY-LIVE`

**Audit rule:** protocol capability is distinct from mint-specific configuration and distinct again from verified payout.

### Three levels used in the audit

1. **Capability** — protocol supports the mechanism.
2. **Configuration** — a particular token is configured to use the mechanism.
3. **Payout** — a specific recipient actually received or claimed fees.

No specific payout is treated as verified without mint → configuration → recipient → claim transaction → recipient-wallet reconstruction.

---

# 6. SPIDER creator-onboarding case

## Creator statement

**Creator account:** `@phosphenq`

**Observed public statement:** creator said that someone else had turned the spider-bot concept into a coin overnight, that the creator did not deploy it, and that creator fees had been routed to them.

**Related earlier public narrative:** seven Grok/spider bots running a night shift on one computer.

**Token mint:**

`6m6hkSNrZ1FxuLLdbcf9UAraPvUZMgfcCSsx3hh4pump`

**Role in audit:** strongest counterexample to the assumption that creator participation was required before token launch.

**Source status:** `PRIMARY-CAPTURED` where screenshot evidence is preserved.

**Limitations:** public chronology does not rule out private contact before launch.

## Orbital onboarding posts

**Account:** `@Orbitalx0`

**Observed chronology:** token launch / claim messaging followed by public statements that the creator had onboarded.

**Audit use:** post-launch onboarding chronology.

**Payout status:** creator-fee routing and claims were publicly stated but not fully reconstructed end-to-end during this audit.

---

# 7. REAPER creator-onboarding case

## Creator account

**Account:** `@0xkkai`

**Token mint:**

`FRPV7Df98MRYLQus6LvJHkjWukUai9wonumScVcypump`

**Observed public framing:** creator reportedly described the token as having been launched by someone else as a sign of support, then later took communications / development involvement.

**Role in audit:** second observed case consistent with post-launch creator onboarding.

**Source status:** archive/capture dependent until the original posts are fully preserved in the repository.

**Important limitation:** pre-launch private coordination is not ruled out.

---

# 8. Repeat launch wallet

## Creator wallet

`HAh7q881D5qUiXuHCZQXx7PcQQWiyHWE3fVXF5j8khpV`

**Observed profile name:** `ridarkdev`

**Relevant identified launches during the audit included:**

- FACTORY
- RIDARK / Ridark Capital
- HIVEMIND
- OPENCODEX
- GBC / Grok Bot Cybertruck
- Grok Profit
- MARA

Only launches with source-level verification should be used for locked quantitative findings.

**Audit conclusion:** the same wallet launched more than one identified AI/Grok-linked token.

**Not established:**

- the wallet controller's real-world identity
- that every launch from the wallet was AI-related
- the proportion of AI-related launches across the wallet's full history
- a single coordinated operation with all referenced creators

The previously considered use of a partial launch count as a denominator was rejected because the full launch population was not reconstructed and the discovery process was selection-biased.

---

# 9. Timing sources

## HIVEMIND

**Miraqle X status ID:** `2094015933891178522`

**Decoded timestamp recorded during audit:** `2026-08-30 10:54:38 UTC`

**Orbital X status ID:** `2094086697256427897`

**Decoded timestamp recorded during audit:** `2026-08-30 15:35:49.532 UTC`

**Third-party indexed token creation time recorded during audit:** `2026-08-30 15:36:43 UTC`

**Observed interval:** approximately `53.468 seconds` from Orbital post to indexed token creation.

**Source caution:** token creation time was taken from a third-party index unless later replaced by a primary on-chain creation record.

**Audit rule:** short latency is an indicator only. It does not establish automation, common control, prior knowledge or causality.

## GBC / Grok Bot Cybertruck

**ScottyBeamIO X status ID:** `2093430437704319344`

**Decoded timestamp recorded during audit:** `2026-08-28 20:08:05.062 UTC`

**Indexed creation time recorded during audit:** `2026-08-28 20:24:07 UTC`

**Observed interval:** approximately `16 minutes 1.938 seconds`.

**Audit use:** counterevidence against a uniform sub-minute launch-latency hypothesis.

## OPENCODEX

**Orbital X status ID:** `2091933522256703710`

**Decoded timestamp recorded during audit:** `2026-08-24 16:59:52.608 UTC`

A previously observed indexed token-creation time suggested a roughly 33-second interval, but the creation source was not sufficiently verified for a locked timing conclusion.

**Status:** pending stronger primary-source verification.

---

# 10. Source handling rules

## Original sources first

Where possible, the repository should preserve:

1. original public URL
2. original screenshot or video
3. UTC timestamp
4. account / wallet / mint identifier
5. SHA-256 hash for captured files

## Archives as backup

Archives and mirrors may establish that public content existed, but should not silently replace stronger primary evidence.

## Discovery indexes

GeckoTerminal, token indexes, explorers and other aggregators may be useful for discovery and chronology.

Where an indexed timestamp or attribution has not been independently reconstructed from primary data, that limitation must remain explicit.

## Derived figures

Annotated or generated figures belong under `evidence/figures/` and must not replace raw evidence.

Raw screenshots and videos should remain unedited under `evidence/raw/` where possible.

---

# 11. Pending source-hardening work

Before the repository is treated as a final locked public evidence package, the following should be hardened where possible:

- exact original X URL for the GRASS entry claim
- direct original source capture for the MEMEMOON duplicate pair
- exact primary Pump.fun page / mint for FACTORY
- primary Pump.fun fee documentation snapshots
- direct original REAPER posts
- primary on-chain creation timestamps for HIVEMIND, GBC and OPENCODEX where obtainable
- original raw screenshots and videos added under `evidence/raw/`
- SHA-256 hashes recorded for all preserved raw files

Until then, findings that depend on incomplete source hardening retain the lower evidence grade or limitation already recorded in the ledger.
