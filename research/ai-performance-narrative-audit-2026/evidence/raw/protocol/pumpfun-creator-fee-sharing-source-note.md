# Pump.fun creator-fee sharing primary source note

Captured during source hardening on 2026-09-06.

## Primary source

Repository: `pump-fun/pump-public-docs`  
Path: `docs/instructions/CREATOR_FEE_SHARING.md`  
URL: `https://github.com/pump-fun/pump-public-docs/blob/main/docs/instructions/CREATOR_FEE_SHARING.md`

## Directly verified technical points

The primary documentation describes a creator-fee-sharing lifecycle that includes:

1. `create_fee_sharing_config`
2. `update_fee_shares_v2`
3. `transfer_creator_fees_to_pump_v2`
4. `distribute_creator_fees_v2`

The documentation states that a sharing configuration can contain a non-empty shareholder list of at most 10 entries and that the `share_bps` values must sum to `10_000`.

The documented distribution instruction pays the creator vault to shareholders according to their configured basis-point shares.

## Audit use

This source supports `ECON-01` at the protocol-capability level.

It establishes that Pump.fun has technical creator-fee / multi-recipient sharing infrastructure.

It does **not** establish that SPIDER, REAPER, FACTORY or any other specific token was configured in a particular way or that any named creator received a payout.

The audit therefore retains the separation:

`capability ≠ configuration ≠ payout`

## Source status

`PRIMARY-LIVE`
