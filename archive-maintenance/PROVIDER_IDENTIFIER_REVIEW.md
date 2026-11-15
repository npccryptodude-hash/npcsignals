# provider access identifiers / final review

[acceptance review](ACCEPTANCE_REVIEW.md) · [machine-readable locations](PROVIDER_IDENTIFIER_REVIEW.json)

## result

the earlier generic credential warning is resolved to **two nodereal access-key values that the provider itself publishes as shareable demonstration keys**. exact equality was checked in memory against the official public-key table; no value, partial suffix or usable credential-bearing endpoint is reproduced here. these are authentication-format public demonstration keys, not merely wallet addresses or transaction ids. this finding does not establish whether either endpoint currently works or whether a key belongs to a private account elsewhere.

| opaque review id | official public-table context | repository occurrence |
| --- | --- | --- |
| provider-id-1 | ethereum mainnet demo key | gamdom G011 collector, source register and compressed rpc archive |
| provider-id-2 | bsc mainnet and opbnb public demo key | gamdom G011 extension, source register and rpc archive; G012 and G013 collectors, source registers and compressed acquisition archives |

the first value was used with a bsc hostname in the historical collector, although the official table labels its public example for ethereum. this is a provenance/context distinction, not a new chain test. an old saved response or a variable called public does not alone prove safe ownership; the provider’s explicit publication is the basis for classification.

## exact affected files

- `research/gamdom/g011/collect.py`
- `research/gamdom/g011/extend.py`
- `research/gamdom/g011/source_register.json`
- `research/gamdom/g011/rpc_archive.json.gz`
- `research/gamdom/g012/collect.py`
- `research/gamdom/g012/source_register.json`
- `research/gamdom/g012/acquisition_archive.json.gz`
- `research/gamdom/g013/collect.py`
- `research/gamdom/g013/source_register.json`
- `research/gamdom/g013/acquisition_archive.json.gz`

the compressed contents were inspected locally, not copied to another public location. no candidate-key request, account login, quota test, revocation or rotation was performed. two specific values were found across these ten files; repeated occurrences are not additional independent keys.

## distinctions and primary support

- **public identifiers:** chain addresses, transaction signatures and unkeyed public rpc hostnames identify public records or services; they are not account secrets merely because they look opaque. bnb chain’s official endpoint list includes the unkeyed nodereal bsc hostname.
- **intentionally public demonstration access:** both flagged values exactly occur in nodereal’s explicitly shareable public-key table. live validity is unknown and was not tested.
- **format examples:** the separate endpoint-format documentation contains an illustrative example and warns that account-specific keys are confidential. its example is not the basis for classifying these two values.
- **potential active private access:** no flagged value remained unmatched to the provider’s public table in this scoped review. this is not a certificate that all historical commits or every possible credential format have been cleared.

primary documents, retrieved 15 november 2026:

- [nodereal public api overview](https://docs.nodereal.io/reference/getting-started-with-your-api)
- [nodereal endpoint and confidentiality guidance](https://docs.nodereal.io/reference/find-api-key-endpoint)
- [bnb chain public endpoint list](https://docs.bnbchain.org/bnb-smart-chain/developers/json_rpc/json-rpc-endpoint/)

## owner decision

**owner decision recorded:** retain these provider-published demonstration values in the frozen historical evidence, provided no information shows private-account ownership. see [owner acceptance](OWNER_ACCEPTANCE.md). this review supplies no reason to rotate a privately owned credential, and the owner cannot revoke a provider’s shared demonstration key on the provider’s behalf.

if the owner has separate account records showing that either value is account-bound or was privately issued, treat that new evidence as a blocker: approve revocation/rotation first, then choose an explicitly versioned redacted derivative and historical treatment. deletion from the current tree would not erase git history. no such action is taken here.
