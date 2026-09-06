# Source Hardening Status

## AI Performance Narrative Audit 2026

Updated: 2026-09-06

**Overall status:** v1.0 SOURCE-HARDENING COMPLETE WITH DECLARED NON-BLOCKING LIMITATIONS

This file records the final source-hardening state used for the Evidence Ledger v1.0 freeze.

---

## 1. Raw screenshots and video

### Status

**DEPOSITED / BYTE-IDENTITY VERIFIED**

The current v1.0 raw-evidence set is committed under `evidence/raw/` and recorded in `evidence/CAPTURE-MANIFEST.md`.

The deposited set contains:

- 16 X screenshots under `evidence/raw/x/`
- 2 FACTORY / GeckoTerminal screenshots under `evidence/raw/metadata/`
- 3 GRASS video captures under `evidence/raw/video/`

For each deposited binary, the Git blob SHA-1 calculated from the original local file bytes was compared with the GitHub blob SHA after upload. All deposited binaries matched. The original SHA-256 values remain recorded in `CAPTURE-MANIFEST.md`.

This closes the former `GITHUB BINARY UPLOAD PENDING` item.

### GRASS primary source

The original GRASS claim is mapped to:

`https://x.com/0xzynex/status/2093658526820212996`

Video endpoint:

`https://x.com/0xzynex/status/2093658526820212996/video/1`

Three non-identical video captures are retained separately:

1. `grass-x-video-full-user-capture.mp4`
   - `19.669313 s`
   - `482 × 1058`
   - SHA-256 `228b407259d653c68c4481a734365013d0a9062eac15ff24bd978655fd93340b`
   - `PRIMARY-CAPTURED / USER-SUPPLIED`

2. `grass-original-audit-capture.mp4`
   - `19.413271 s`
   - `896 × 782`
   - SHA-256 `a935e1e4d3722c073bd58693e8721d135c2f31e152f8b3fffff4be780c3ab330`
   - `PRIMARY-CAPTURED / AUDIT-PRESERVED`

3. `grass-x-video-user-trimmed.mp4`
   - `9.386625 s`
   - `476 × 1060`
   - SHA-256 `bbab2447f036108005e1519292f41600df63581d5e1c7e555da92d13c3ece307`
   - `DERIVED / USER-TRIMMED`

The files differ at byte level and are not treated as interchangeable.

---

## 2. FACTORY primary Pump.fun source

**Status:** PARTIALLY HARDENED / EXACT ASSET RESOLUTION UNRESOLVED / NON-BLOCKING

Pump.fun's own public Explore surface independently displayed a `Grok Token Factory / FACTORY` card containing:

- creator prefix `HAh7q8`
- `@enkoxbt`
- Enko GitHub provenance
- RoundtableSpace status `2093824765785976942`

The exact stable Pump.fun coin URL and full mint were not recovered from the accessible primary-platform output.

Therefore `FACTORY-01` remains:

`E2 / SUPPORTED / PROVISIONAL`

No missing identifier is inferred.

See `evidence/raw/metadata/factory-pumpfun-discovery-note.md`.

---

## 3. HIVEMIND and GBC creation timestamps

**Status:** SECONDARY CREATION TIMESTAMPS RETAINED / NON-BLOCKING

The public X posts are directly captured. Current token-creation timestamps remain based on third-party indexed records:

- HIVEMIND: `2026-08-30 15:36:43 UTC`
- GBC: `2026-08-28 20:24:07 UTC`

A primary Solana creation transaction suitable for an evidence upgrade was not reconstructed during the source-hardening pass.

The timing findings therefore remain `E2` and are explicitly scoped to post-to-indexed-creation intervals.

No automation, coordination, common control or causal attribution follows from the timing.

---

## 4. KITSUNE source

**Status:** ARCHIVED CLAIM TEXT HARDENED / DIRECT ORIGINAL X CAPTURE UNRECOVERED / NON-BLOCKING

The detailed KITSUNE claim is recoverable through public mirrors for `@enkoxbt`, preserving the central claim parameters:

- 0.8 ETH entry
- approximately $1.5M to $120M market cap
- approximately +62 ETH
- 5,820 holders
- autonomous-execution framing
- safety language and a 0.8 ETH position cap

No unique contract, agent wallet, buy hash and sell hash were identified.

The verdict therefore remains:

`E1 / NON-REPRODUCIBLE`

A direct original capture would improve preservation, but would not by itself establish the historical P&L.

---

## 5. Final case-file / ledger consistency check

**Status:** PASS

The final text consistency pass aligned the core files with the Evidence Ledger, including:

- GRASS source status corrected to `2093658526820212996`
- GRASS timeline source no longer marked unresolved
- FACTORY timeline reduced from E3 to E2 to match the actual source strength
- REAPER raw-evidence filenames aligned with the manifest
- raw-evidence paths aligned with the files actually deposited

The central conclusions remain:

- GRASS asset movement: `CONFIRMED / E3`
- GRASS agent P&L: `UNVERIFIED / E1`
- GRASS technical description: `MATERIAL MISMATCH / E3`
- MEMEMOON provenance: `PROVENANCE FAILURE / E2`
- KITSUNE: `NON-REPRODUCIBLE / E1`
- RoundtableSpace amplification: `SUPPORTED / E2`
- FACTORY: `SUPPORTED / E2 / PROVISIONAL`
- Pump.fun fee capability: `CONFIRMED / E3`, capability only
- SPIDER onboarding: `SUPPORTED / E2`; payout `UNVERIFIED / E1`
- REAPER onboarding: `SUPPORTED / E2`; payout `UNVERIFIED / E1`
- repeat-launch wallet: repeated identified launches without a population-prevalence claim
- HIVEMIND timing interval: retained as E2 using indexed creation time
- uniform sub-minute launch hypothesis: `REJECTED / E2`
- one coordinated operation: `NOT ESTABLISHED / E2`
- recurring structural mechanism in observed cases: `STRONGLY SUPPORTED / E2`

No case file should be interpreted beyond the ledger fields `verdict_scope`, `not_established` and `limitation`.

---

## 6. Freeze status

**Status:** READY TO FREEZE v1.0

All blocking analytical and raw-evidence preservation tasks are complete.

The remaining FACTORY, HIVEMIND/GBC and KITSUNE items are explicitly retained as limitations and are non-blocking because no finding is upgraded to compensate for the missing evidence.

Future evidence that materially changes a locked finding should be recorded in a later ledger version rather than silently rewriting the v1.0 record.

The governing principle remains:

**A hypothesis survives only what we failed to falsify.**
