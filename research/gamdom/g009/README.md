# NPCsignals — Gamdom G009.2

Independent Upstream Funding & Historical Balance Reconstruction — 15 October 2026.

Starting commit: `ff920e52ed487b2f0d0a729c6f61f2d31fce4c2a`. G005, G006 and G008 are unchanged. This versioned sibling directory is named g009 as requested; no G007/G009.1 publication is implied.

## Strongest genuinely new finding

D held **1,579.018972 canonical USDT0** at the end of Polygon block 95434112. After the 674.470970 transfer to C in block 95434113, its balance was **904.548002 USDT0**. Archive `balanceOf` calls and a separately accessed PolygonScan transaction-local storage display agree. The anchor is transaction index 19, log 179; the bounded canonical log queries return no other D transfer in that block.

At block 95399999, before the recent 600-USDT0 deposit and four routed inflows, D already held **936.499001 USDT0**. Those pre-existing holdings exceeded the anchor transfer amount. A recent deposit was not necessary to make the transfer possible. Exclusive attribution of mixed fungible units remains unresolved.

## Exact bounded reconciliation

3,148.255812 opening + 65,861.140478 inflows − 68,104.848288 outflows = **904.548002 USDT0** closing. All values use integers with six decimals. The interval covers blocks 93000000–95434113, beginning August 31 at 19:37:07 UTC and ending October 13 at 01:54:20 UTC. Opening state is read at block 92999999, not assumed zero. All three reconciliation windows have zero residual against archive state.

The saved export contains **753 canonical Transfer events**: 647 incoming and 106 outgoing. This is a bounded single-provider export, not a lifetime history or cryptographically verified chain-state proof. Full transaction/receipt metadata was additionally verified for **12 new transactions**, plus the existing anchor. Ten of the new transactions deliver USDT0 to D; two establish earlier D-to-C payments.

The queried history contains **80 D→C events before the anchor**, including a larger 1,348.792079 payment independently receipt-verified for October 8. The relationship was not newly created on October 13. This does not establish common ownership or legitimacy.

## Publication decision

Evidence checkpoint: **PUBLISH**. Article: **HOLD**. H1/H2/H3 remain UNRESOLVED. No Gamdom ownership, unauthorized status, loss total or human operator is established here.

Run `python3 verify.py` offline. Reproduction collectors and every raw RPC request/response are preserved. Read coverage_report.md before interpreting completeness, signatures or absence.
