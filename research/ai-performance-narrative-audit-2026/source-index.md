# Source Index

This index records the principal public, technical, archived and captured sources used in the AI Performance Narrative Audit 2026.

**Status:** aligned with frozen Evidence Ledger v1.0 on 2026-09-06.

A source appearing here does not mean every claim associated with it is verified. Each finding must be read together with its evidence grade, verdict scope, counterevidence and limitations in `evidence-ledger-v1.0.csv`.

Direct captures and their SHA-256 values are recorded in `evidence/CAPTURE-MANIFEST.md`. The current v1.0 binary set is deposited under `evidence/raw/` and byte-identity verified against the locally hashed audit files.

---

## Source-status labels

- `PRIMARY-LIVE` — original source is directly accessible.
- `PRIMARY-CAPTURED` — original source was captured directly and preserved or catalogued by the audit.
- `ARCHIVED-CORROBORATION` — archived or mirrored copy used to corroborate that public material existed.
- `SECONDARY-DISCOVERY` — third-party index or aggregator used for discovery, metadata recovery or chronology.
- `DERIVED` — analysis created from other evidence, such as arithmetic or cross-case synthesis.

Third-party repetition is not treated as independent verification unless it adds new evidence.

---

# 1. GRASS entry case

## GRASS token

**Contract:** `0x16391C40e85FB2246A2C8c17bfA2594C5d3EF84b`

**Network:** Robinhood Chain  
**Chain ID:** `4663`

**Role in audit:** underlying asset referenced in the viral performance claim.

**Important limitation:** asset movement does not establish that the claimed autonomous agent executed the stated entry and exit.

## Exact Zynex claim source

**Account:** `@0xzynex`  
**Status:** `2093658526820212996`  
**URL:** `https://x.com/0xzynex/status/2093658526820212996`  
**Video endpoint:** `https://x.com/0xzynex/status/2093658526820212996/video/1`  
**Source status:** `PRIMARY-CAPTURED`

The captured post states that the Grok bot bought GRASS at approximately `$30K` market cap and sold at approximately `$2M`, framed as `66x on one trade, completely autonomous, ETH chain`.

The preserved presentation includes:

- `0.3 ETH` entry
- approximately `+19.7 ETH`
- `66.7x`
- position marked closed
- safety labels including no honeypot / verified / renounced / LP burned 95%

The screenshot and three non-identical video captures are deposited under `evidence/raw/` and catalogued in `evidence/CAPTURE-MANIFEST.md`.

**Limitation:** no agent wallet, buy hash or sell hash is exposed by the video.

## Zynex published / personal wallet

**Wallet:** `0x690d7552375Fcd23Bd2a5E1d74f7445FAdfc6c83`

No transaction path from this wallet independently reconstructed the claimed GRASS trade.

**Limitation:** the public narrative distinguished a personal wallet from separate agent wallets. Failure to locate the trade in the personal wallet does not disprove another agent wallet.

## Pons v2 launch architecture

Primary Pons v2 material examined during the audit described a bonding-curve process followed by permanently locked full-range Uniswap v4 liquidity.

**Audit use:** comparison with the claim video's `LP burned 95%` wording.

**Verdict relevance:** `MATERIAL MISMATCH`, not proof of fabrication or intent.

**Recorded deployer:** `0x3711ceA4feaDE896C913C68F01Eda97Cb06D1A42`

## Historical 2025 Grass reference

A direct historical Zynex capture dated Jul 6, 2025 referred to `The next Grass` in an airdrop context.

**Audit use:** counterevidence only.

The reference concerns the older Grass ecosystem / airdrop context and is not used as evidence of prior knowledge of the 2026 GRASS token case.

---

# 2. MEMEMOON provenance case

## Zynex MEMEMOON narrative

**Recorded X status:** `2093277608632893471`

Observed narrative elements include:

- `0.5 SOL` buy
- entry around `$0.0000012`
- narrative score `0.94`
- `+800%` after about 11 seconds
- `42 new holders`
- `3 whales`
- `8 SOL liquidity`
- approximately `60x`

The same surrounding system narrative also reportedly stated a maximum position size of `0.1 SOL`.

## Backwood duplicate narrative

**Account:** `@0xBackwood`  
**Source status:** `PRIMARY-CAPTURED`

Direct captures obtained on 2026-09-06 preserve a separate first-person MEMEMOON narrative with multiple unusually specific overlapping details, while some parameters are changed.

**Audit use:** content provenance and internal-consistency analysis.

**Not established:** common account control, coordinated fraud or fabrication of the underlying trade.

The Backwood captures are deposited under `evidence/raw/x/`.

---

# 3. KITSUNE validation case

## Enko KITSUNE claim

Observed claim elements recorded during the audit included:

- token: KITSUNE
- entry: approximately `0.8 ETH`
- entry market cap: approximately `$1.5M`
- exit market cap: approximately `$120M`
- claimed result: `+62 ETH`
- approximately `5,820 holders`
- safety statements including no honeypot / verified / renounced / LP burned
- autonomous execution framing

**Source status:** `ARCHIVED-CORROBORATION`

**Audit result:** no unique contract, agent wallet, buy hash and sell hash were identified from the public material available to the audit.

**Verdict relevance:** `NON-REPRODUCIBLE / E1` within the public evidence set.

**Not established:** that the claim was false or that the trade did not occur.

A separate direct Enko capture from Aug 30 documenting a five-bot race is deposited under `evidence/raw/x/`. It is not the KITSUNE source and must not be substituted for KITSUNE evidence.

---

# 4. RoundtableSpace amplification

## Direct captured post

**Account:** `@RoundtableSpace`  
**Display name:** `0xMarioNawfal`  
**Recorded status:** `2093824765785976942`  
**Source status:** `PRIMARY-CAPTURED`

The captured post states that a Grok bot was taught to autonomously launch memecoins on Pump.fun, kill failed launches and collect creator fees from those that trade.

**Role in audit:** amplification layer.

**Important limitation:** amplification does not independently verify the underlying bot-performance or fee claims.

**Not established:** that RoundtableSpace created, approved or financially benefited from downstream tokens.

The direct capture is deposited under `evidence/raw/x/`.

---

# 5. FACTORY provenance

## FACTORY market captures

**Name:** `Grok Token Factory` / `FACTORY`

**Creator-wallet record:** `HAh7q881D5qUiXuHCZQXx7PcQQWiyHWE3fVXF5j8khpV`

Two GeckoTerminal screenshots preserved by the audit show:

- the FACTORY market
- `Grok Token Factory` labeling
- creator-wallet prefix `HAh7q...khpV`
- token description referencing `@enkoxbt`
- Pump.fun / PumpSwap context

**Source status:** captured third-party market interface.

The two screenshots are deposited under `evidence/raw/metadata/`.

Pump.fun's own Explore surface was also observed reproducing FACTORY provenance text referencing `@enkoxbt`, Enko GitHub material and RoundtableSpace status `2093824765785976942`. A primary-platform discovery note is preserved at `evidence/raw/metadata/factory-pumpfun-discovery-note.md`.

The exact stable Pump.fun asset URL/full mint was not recovered from the accessible primary output.

Accordingly:

`FACTORY-01 = E2 / SUPPORTED / PROVISIONAL`

**Not established:** that Enko or RoundtableSpace created, approved or financially benefited from FACTORY.

---

# 6. Pump.fun creator-fee infrastructure

## Primary fee documentation

Primary Pump.fun documentation was used to establish protocol-level creator-fee and fee-sharing capability.

Relevant documented capabilities include:

- creator fees
- creator fee sharing
- configurable recipients
- up to 10 shareholders
- allocation through basis-point shares summing to 10,000
- identity-linked fee mechanics documented by the protocol

**Source status:** `PRIMARY-LIVE`

### Audit separation

1. **Capability** — protocol supports the mechanism.
2. **Configuration** — a particular token is configured to use the mechanism.
3. **Payout** — a specific recipient actually received or claimed fees.

No specific payout is treated as verified without mint → configuration → recipient → claim transaction → recipient-wallet reconstruction.

---

# 7. SPIDER creator onboarding

## Creator statement

**Creator account:** `@phosphenq`

A direct captured Sep 2 post states in substance that:

- somebody turned the spider-bot concept into a coin overnight
- the creator did not deploy it
- the creator learned about it from a stranger in replies
- creator fees were routed to the creator

**Token mint:** `6m6hkSNrZ1FxuLLdbcf9UAraPvUZMgfcCSsx3hh4pump`  
**Source status:** `PRIMARY-CAPTURED`

## Orbital claim / onboarding material

A direct captured Orbitalx0 post shows:

- `Made claim`
- the same SPIDER mint
- `$SPIDER tech`

**Audit use:** public post-launch onboarding chronology.

**Payout status:** unverified at transaction level.

The SPIDER captures are deposited under `evidence/raw/x/`.

---

# 8. REAPER creator onboarding

## Creator account

**Account:** `@0xkkai`  
**Token mint:** `FRPV7Df98MRYLQus6LvJHkjWukUai9wonumScVcypump`  
**Source status:** `PRIMARY-CAPTURED`

Direct Sep 1 captures show Kai stating:

- someone launched `$REAPER` as a sign of support
- a token launched with his agent's name on it and nobody told him
- he found out because the agent flagged it
- he was taking communications and would keep building

## Orbital onboarding material

Direct Orbitalx0 captures show the same mint and later language:

`He tapped in and claimed`

**Audit use:** second directly captured case consistent with public post-launch creator onboarding.

**Important limitation:** the public record does not rule out private pre-launch communication.

**Specific creator-fee payout:** `UNVERIFIED` until reconstructed transaction-by-transaction.

The REAPER captures are deposited under `evidence/raw/x/`.

---

# 9. Repeat launch wallet

## Creator wallet

`HAh7q881D5qUiXuHCZQXx7PcQQWiyHWE3fVXF5j8khpV`

**Observed profile label:** `ridarkdev`

The audit identified multiple AI/Grok-linked launches in the same creator-wallet research cluster.

The strongest current case set includes FACTORY and later narrative-linked assets used in the HIVEMIND / GBC analysis, subject to each source's individual limitations.

Additional candidates encountered during discovery included RIDARK, OPENCODEX, Grok Profit and MARA.

These candidates are not used to inflate a quantitative count unless individually source-hardened.

**Audit conclusion:** repeated narrative-linked launches are present among the identified subset.

**Not established:**

- complete launch count
- percentage matching the pattern
- natural-person identity of the wallet controller
- automated selection or deployment
- common control with referenced creators
- creator authorization

No denominator-based prevalence estimate is made.

---

# 10. HIVEMIND timing sources

## Miraqle

**Recorded status:** `2094015933891178522`  
**Decoded timestamp:** `2026-08-30 10:54:38 UTC`  
**Source status:** `PRIMARY-CAPTURED`

A direct capture preserves the HIVEMIND 16-agent / 2 SOL to 31 SOL narrative.

## Orbitalx0

**Recorded status:** `2094086697256427897`  
**Decoded timestamp:** `2026-08-30 15:35:49.532 UTC`  
**Source status:** `PRIMARY-CAPTURED`

A direct capture describes HIVEMIND as a 16-agent autonomous trading desk, references Miraqle and GitHub, states `Redirecting all fees`, and provides a CA in the reply.

## Indexed token creation

**Third-party indexed time:** `2026-08-30 15:36:43 UTC`  
**Observed interval:** approximately `53.468 seconds`  
**Source status:** `SECONDARY-DISCOVERY`

**Audit rule:** short latency does not establish automation, coordination, prior knowledge or causality.

The Miraqle and Orbital captures are deposited under `evidence/raw/x/`.

---

# 11. GBC / Grok Bot Cybertruck timing sources

## ScottyBeamIO source narrative

**Recorded status:** `2093430437704319344`  
**Decoded timestamp:** `2026-08-28 20:08:05.062 UTC`  
**Source status:** `PRIMARY-CAPTURED`

A direct Aug 28 capture states that `@ScottyBeamIO` built a full Grok Bot agent setup for a Cybertruck and describes the multi-agent architecture.

## Indexed token creation

**Third-party indexed time:** `2026-08-28 20:24:07 UTC`  
**Observed interval:** approximately `16 minutes 1.938 seconds`  
**Source status:** `SECONDARY-DISCOVERY`

**Audit use:** counterevidence against a uniform sub-minute launch-latency hypothesis.

The direct source capture is deposited under `evidence/raw/x/`.

---

# 12. OPENCODEX pending timing candidate

**Orbital status:** `2091933522256703710`  
**Decoded timestamp:** `2026-08-24 16:59:52.608 UTC`

A previously observed indexed creation time suggested a roughly 33-second interval.

The creation source was not sufficiently verified for a locked v1.0 timing conclusion.

**Status:** `PENDING` and excluded from the locked timing inference.

---

# 13. Source handling rules

## Original sources first

Where possible, preserve:

1. original public URL
2. original screenshot or video
3. UTC timestamp
4. account / wallet / mint identifier
5. SHA-256 hash

## Archives as backup

Archives and mirrors may establish that public content existed, but do not silently replace stronger primary evidence.

## Discovery indexes

GeckoTerminal, token indexes, explorers and other aggregators may be useful for discovery and chronology.

Where an indexed timestamp or attribution has not been independently reconstructed from primary data, that limitation remains explicit.

## Derived figures

Annotated or generated figures belong under `evidence/figures/` and must not replace raw evidence.

Raw screenshots and videos remain unedited under `evidence/raw/` where available.

---

# 14. Frozen v1.0 source-hardening state

The blocking source-preservation work is complete:

- current direct screenshots are deposited under `evidence/raw/x/`
- FACTORY metadata screenshots are deposited under `evidence/raw/metadata/`
- GRASS videos are deposited under `evidence/raw/video/`
- deposited binaries were byte-identity checked against the original local audit files
- exact original GRASS X mapping is resolved

The following remain declared non-blocking limitations:

- exact stable primary Pump.fun FACTORY asset URL/full mint not recovered; retain `FACTORY-01 = E2 / SUPPORTED / PROVISIONAL`
- primary Solana creation transactions for HIVEMIND and GBC not reconstructed; retain E2 indexed-timestamp limitation
- direct original KITSUNE X capture not recovered; retain `NON-REPRODUCIBLE / E1`
- OPENCODEX remains pending and is not used as a locked timing finding

Any material future source upgrade that changes a verdict, evidence grade or scope should be recorded in a later ledger version rather than silently rewriting v1.0.
