# GRASS capture integrity record

## Source identity

Original X status:

`https://x.com/0xzynex/status/2093658526820212996`

Video endpoint:

`https://x.com/0xzynex/status/2093658526820212996/video/1`

The direct source screenshot captured on 2026-09-06 shows the Sep 4 Zynex post with the headline:

`HOLY SH*T MY GROK BOT BOUGHT $GRASS AT $30K CAP AND SOLD AT $2M`

The post further states `66x on one trade, completely autonomous, ETH chain` and includes safety-language referring to no honeypot, verified, renounced and `LP burned 95%`.

## Preserved video variants

Three files relating to the same public video presentation were available during the audit. They are deliberately kept as separate capture records because they are not byte-identical.

### A. Full user-supplied capture

Intended repository filename:

`grass-x-video-full-user-capture.mp4`

Properties:

- duration: `19.669313 s`
- H.264 video
- dimensions: `482 × 1058`
- AAC audio
- SHA-256: `228b407259d653c68c4481a734365013d0a9062eac15ff24bd978655fd93340b`

Classification:

`PRIMARY-CAPTURED / USER-SUPPLIED`

This is the preferred user-supplied full-length capture.

### B. Earlier full audit capture

Intended repository filename:

`grass-original-audit-capture.mp4`

Properties:

- duration: `19.413271 s`
- H.264 video
- dimensions: `896 × 782`
- AAC audio
- SHA-256: `a935e1e4d3722c073bd58693e8721d135c2f31e152f8b3fffff4be780c3ab330`

Classification:

`PRIMARY-CAPTURED / EARLIER AUDIT CAPTURE`

The different dimensions and byte hash indicate a different recording/export path, not a reason to merge the files.

### C. User-trimmed short capture

Intended repository filename:

`grass-x-video-user-trimmed.mp4`

Properties:

- duration: `9.386625 s`
- H.264 video
- dimensions: `476 × 1060`
- AAC audio
- SHA-256: `bbab2447f036108005e1519292f41600df63581d5e1c7e555da92d13c3ece307`

Classification:

`DERIVED / USER-TRIMMED`

This file is retained for provenance but is not used as the preferred raw full-length capture.

## Direct source screenshot

Intended repository filename:

`../x/grass-zynex-status-2093658526820212996.png`

SHA-256:

`82d23ae2c6708fe07290f1dd162f3e5ff958d3a0d648dcd4ad9098ad60fcea59`

Classification:

`PRIMARY-CAPTURED`

## Evidentiary effect

Resolving the exact source strengthens preservation of what was claimed. It does not upgrade the claimed historical agent performance.

The video and post still do not expose the agent wallet, buy transaction hash or sell transaction hash needed to reconstruct the claimed `0.3 ETH → ~19.7 ETH` trade.

Accordingly:

- `GRASS-01` remains `CONFIRMED / E3` for underlying asset movement only.
- `GRASS-02` remains `UNVERIFIED / E1` for the claimed agent P&L.
- `GRASS-03` remains `MATERIAL MISMATCH / E3` for the published safety / launch-architecture description.

## Binary deposition status

`LOCAL HASH VERIFIED / GITHUB BINARY UPLOAD PENDING`

The text record and hashes are committed. Binary files should be uploaded without editing, then checked against the hashes above before final repository freeze.
