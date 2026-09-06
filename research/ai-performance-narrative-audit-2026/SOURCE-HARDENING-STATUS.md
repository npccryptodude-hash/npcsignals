# Source Hardening Status

## AI Performance Narrative Audit 2026

Updated: 2026-09-06

This file records the remaining work before Evidence Ledger v1.0 can be treated as a frozen public audit package.

---

## 1. Raw screenshots and video

### GRASS video

**Status:** LOCAL RECOVERED / HASH VERIFIED / GITHUB BINARY UPLOAD PENDING

The original GRASS claim video is present in the audit working environment.

- duration: `19.413271 s`
- dimensions: `896 × 782`
- video: H.264, 30 fps
- audio: AAC
- size: `3,424,968 bytes`
- SHA-256: `a935e1e4d3722c073bd58693e8721d135c2f31e152f8b3fffff4be780c3ab330`

The hash matches the value recorded earlier in the audit.

### Screenshots

**Status:** HASHED / GITHUB BINARY UPLOAD PENDING

Direct captures for REAPER, SPIDER, MEMEMOON, HIVEMIND, GBC, FACTORY, RoundtableSpace and GRASS counterevidence are recorded in `evidence/CAPTURE-MANIFEST.md`.

The GitHub text connector can preserve hashes and source records reliably, but binary deposition still requires a separate upload path.

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

The audit attempted to replace these with direct primary Solana creation evidence, but no primary RPC / explorer transaction record was obtained through the available source interfaces during this hardening pass.

The timing findings therefore remain `E2` and explicitly limited to the observed post-to-indexed-creation intervals.

No automation, coordination or causal attribution is inferred from timing.

---

## 4. KITSUNE source

**Status:** ARCHIVED CLAIM TEXT HARDENED / ORIGINAL X CAPTURE STILL DESIRABLE

The detailed KITSUNE claim is independently recoverable from current public profile mirrors for `@enkoxbt`, including Sotwe and TwStalker.

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

**Status:** PASS WITH DECLARED PROVISIONAL ITEMS

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

REAPER source status has been upgraded to `PRIMARY-CAPTURED` where direct captures now exist.

No case file should be interpreted beyond the `verdict_scope`, `not_established` and `limitation` fields in the ledger.

---

## 6. Freeze readiness

**Status:** NOT YET FROZEN

The analytical record is substantially complete.

The remaining items before final v1.0 freeze are operational/source-preservation tasks rather than unresolved narrative conclusions:

1. commit raw binary screenshots and GRASS video to `evidence/raw/`
2. verify repository-file hashes against `CAPTURE-MANIFEST.md`
3. obtain exact FACTORY primary asset URL/full mint if possible, otherwise retain E2 provisional classification
4. obtain primary Solana creation transactions for HIVEMIND/GBC if possible, otherwise retain the explicit secondary-index limitation
5. obtain direct original KITSUNE capture if possible, otherwise retain archived corroboration
6. run one final repository-wide check after binary deposition

If items 3–5 cannot be improved without disproportionate effort, the audit can still be frozen with those limitations explicitly preserved.

The audit should not delay publication by converting unavailable evidence into stronger assumptions.
