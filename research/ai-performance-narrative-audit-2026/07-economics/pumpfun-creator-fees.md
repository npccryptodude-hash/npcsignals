# Pump.fun creator-fee infrastructure

## Purpose

This file separates protocol capability from token-specific configuration and actual payout.

## Primary protocol finding

Pump.fun documentation examined during the audit supports creator-fee and fee-sharing functionality.

The documented system includes mechanisms for sharing creator fees across multiple recipients and for mapping social identities to fee recipients.

The exact primary documentation references should remain indexed in `source-index.md` and captured under `evidence/raw/protocol/` where permitted.

## Three verification levels

### 1. Capability

Question: Does the protocol support creator fees or fee sharing?

For Pump.fun, this capability is **CONFIRMED** from primary documentation.

### 2. Configuration

Question: Was a specific token configured to route fees to a particular recipient?

This must be established token by token.

Protocol capability cannot answer it.

### 3. Payout

Question: Did the intended recipient actually claim or receive the fees?

This requires transaction-level reconstruction where possible.

A public statement that fees were redirected or claimed is not equivalent to verified payout.

## Finding ECON-01

**Verdict:** CONFIRMED  
**Evidence grade:** E3  
**Scope:** protocol capability only

Pump.fun provides creator-fee / fee-sharing infrastructure capable of supporting creator-linked economic participation.

## Not established

This finding does not establish:

- that any specific token used the mechanism in a particular way
- that a named creator was configured as recipient
- that a creator claimed fees
- the amount of any payout
- that token creation and creator onboarding were coordinated in advance

## Analytical significance

The infrastructure makes post-launch creator onboarding economically possible without requiring that the creator launched the token.

That is a capability finding, not proof of a specific payout path.
