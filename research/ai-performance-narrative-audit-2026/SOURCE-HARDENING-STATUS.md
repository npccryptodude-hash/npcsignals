# Source Hardening Status

## AI Performance Narrative Audit 2026

Updated: 2026-09-06

This file records the remaining work before Evidence Ledger v1.0 can be treated as a frozen public audit package.

---

## 1. Raw screenshots and video

### GRASS primary source

**Status:** SOURCE MAPPING RESOLVED / LOCAL CAPTURES HASH VERIFIED / GITHUB BINARY UPLOAD PENDING

The original GRASS claim is now mapped to:

`https://x.com/0xzynex/status/2093658526820212996`

Video endpoint:

`https://x.com/0xzynex/status/2093658526820212996/video/1`

Three non-identical video captures are retained separately:

1. Full user-supplied capture
   - duration: `19.669313 s`
   - dimensions: `482 × 1058`
   - SHA-256: `228b407259d653c68c4481a734365013d0a9062eac15ff24bd978655fd93340b`
   - classification: `PRIMARY-CAPTURED / USER-SUPPLIED`

2. Earlier full audit capture
   - duration: `19.413271 s`
   - dimensions: `896 × 782`
   - SHA-256: `a935e1e4d3722c073bd58693e8721d135c2f31e152f8b3fffff4be780c3ab330`
   - classification: `PRIMARY-CAPTURED / AUDIT-PRESERVED`

3. User-trimmed capture
   - duration: `9.386625 s`
   - dimensions: `476 × 1060`
   - SHA-256: `bbab2447f036108005e1519292f41600df63581d5e1c7e555da92d13c3ece307`
   - classification: `DERIVED / USER-TRIMMED`

The captures differ at byte level and are not treated as interchangeable files.

See `evidence/raw/video/grass-capture-integrity.md` and `evidence/CAPTURE-MANIFEST.md`.

### Screenshots

**Status:** HASHED / GITHUB BINARY UPLOAD PENDING

Direct captures for GRASS, REAPER, SPIDER, MEMEMOON, HIVEMIND, GBC, FACTORY, RoundtableSpace and GRASS counterevidence are recorded in `evidence/CAPTURE-MANIFEST.md`.

The GitHub connector can preserve hashes and source records reliably, but binary deposition remains a separate operational step.

---

## 2. FACTORY primary Pump.fun source

**Status:** PARTIALLY HARDENED / EXACT ASSET RESOLUTION PENDING

Pump.fun's own public Explore surface was independently observed returning a `Grok Token Factory / FACTORY` card containing:

- creator prefix `HAh7q8`
- `@enkoxbt`
- Enko GitHub provenance
- RoundtableSpace status `2093824765785976942`

This confirms that the provenance text was visible on the primary Pump.fun platform and not only on GeckoTerminal.

However, the accessible page output did not expose a stable exact coin URL and full mint for this specific listing.

Therefore `FACTORY-01` remains conservatively:

`E2 / SUPPORTED / PROVISIONAL`

See `evidence/raw/metadata/factory-pumpfun-discovery-note.md`.

---

## 3. HIVEMIND and GBC creation timestamps

**Status:** SECONDARY TIMESTAMPS RETAINED / PRIMARY ON-CHAIN RECONSTRUCTION PENDING

The public X source timestamps are directly captured and stable.

Current creation timestamps remain based on third-party indexed token records:

- HIVEMIND: indexed creation `2026-08-30 15:36:43 UTC`
- GBC: indexed creation `2026-08-28 20:24:07 UTC`

The audit attempted to replace these with direct primary Solana creation evidence, but no primary RPC / explorer transaction record suitable for an upgrade was obtained through the available source interfaces during this hardening pass.

The timing findings therefore remain `E2` and explicitly limited to the observed post-to-indexed-creation intervals.

No automation, coordination or causal attribution is inferred from timing.

---

## 4. KITSUNE source

**Status:** ARCHIVED CLAIM TEXT HARDENED / ORIGINAL X CAPTURE STILL DESIRABLE

The detailed KITSUNE claim is independently recoverable from current public profile mirrors for `@enkoxbt`.

The recovered text preserves the key claim parameters:

- 0.8 ETH entry
- approximately $1.5M to $120M market cap
- approximately +62 ETH
- 5,820 holders
- autonomous execution framing
- safety-language and a 0.8 ETH position cap

No unique token contract, agent wallet, buy hash and sell hash were identified.

Therefore the historical P&L finding remains:

`E1 / NON-REPRODUCIBLE`

A direct original X capture would improve source preservation but would not establish the trade itself.

---

## 5. Case-file / ledger consistency check

**Status:** PASS AFTER FINAL TEXT CONSISTENCY CORRECTIONS

The central case files and Evidence Ledger use the same core distinctions:

- GRASS asset movement: `CONFIRMED`, separate from agent P&L
- GRASS agent P&L: `UNVERIFIED`
- MEMEMOON provenance: `PROVENANCE FAILURE`, content provenance only
- KITSUNE: `NON-REPRODUCIBLE`
- RoundtableSpace: amplification / downstream provenance only
- FACTORY: `E2 / SUPPORTED / PROVISIONAL`
- Pump.fun fee capability: `E3 / CONFIRMED`, protocol capability only
- SPIDER: post-launch onboarding supported; payout unverified
- REAPER: post-launch onboarding supported; payout unverified
- repeat-launch wallet: repeated identified launches supported without population prevalence or identity attribution
- timing: HIVEMIND short interval retained; uniform sub-minute hypothesis rejected
- common coordinated operation: `NOT ESTABLISHED`

Final consistency corrections included:

- replacing the stale GRASS source mapping in the Evidence Ledger with status `2093658526820212996`
- updating `timeline.csv` so GRASS no longer says the source is unresolved
- downgrading the FACTORY timeline entry from E3 to E2 to match the ledger and case limitations
- aligning REAPER raw-evidence target filenames with `CAPTURE-MANIFEST.md`

No case file should be interpreted beyond the `verdict_scope`, `not_established` and `limitation` fields in the ledger.

---

## 6. Freeze readiness

**Status:** ANALYTICALLY READY / BINARY PRESERVATION OPEN

The analytical record is substantially complete and has passed the final text consistency check.

Remaining items are source-preservation or optional source-upgrade tasks:

1. commit raw binary screenshots and GRASS videos to `evidence/raw/`
2. verify repository-file hashes against `CAPTURE-MANIFEST.md`
3. obtain exact FACTORY primary asset URL/full mint if possible, otherwise retain E2 provisional classification
4. obtain primary Solana creation transactions for HIVEMIND/GBC if possible, otherwise retain the explicit secondary-index limitation
5. obtain direct original KITSUNE capture if possible, otherwise retain archived corroboration

Items 3–5 are non-blocking if the present limitations are retained.

Binary deposition is the remaining operational step for an ideal archival freeze; inability to deposit a binary through the current connector does not justify strengthening or weakening the analytical conclusions.

The audit should not delay publication by converting unavailable evidence into stronger assumptions.
