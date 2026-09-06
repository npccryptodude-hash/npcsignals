# FACTORY primary Pump.fun discovery note

Source-hardening check performed on 2026-09-06.

## Primary-platform observation

Pump.fun's own public Explore surface returned a `Grok Token Factory / FACTORY` listing whose visible card text included:

- creator prefix `HAh7q8`
- `GROK TOKEN FACTORY (@enkoxbt)`
- a description of Grok Bot agents as persistent cloud machines
- `GitHub - https://github.com/enkoxbt`
- `X post - https://x.com/roundtablespace/status/2093824765785976942`
- a web reference to Enko's X account

Primary platform URL observed during the check:

`https://pump.fun/explore`

Search-indexed Pump.fun Explore URLs also reproduced the same FACTORY card and provenance text.

## What this improves

This is stronger than relying only on GeckoTerminal for the existence of the provenance text because the text was independently visible on Pump.fun's own public surface.

## Remaining limitation

The source-hardening pass did not obtain a stable exact Pump.fun coin URL or a full mint identifier for this specific FACTORY listing from the accessible Pump.fun page output.

The visible `HAh7q8` value is consistent with the creator-wallet prefix recorded elsewhere in the audit, but a prefix is not a full mint and must not be treated as one.

Accordingly, `FACTORY-01` remains conservatively held at `E2 / SUPPORTED / PROVISIONAL` until the exact primary asset page and full mint, or equivalent primary technical evidence, are preserved.

## Source status

Primary-platform discovery observation, with exact-asset resolution still incomplete.
