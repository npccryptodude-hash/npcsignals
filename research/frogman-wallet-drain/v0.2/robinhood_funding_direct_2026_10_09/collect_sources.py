import concurrent.futures,json
from collect import collect,rpc,P,R
hs=['0x49e05a92a0b08841fac2b475877cd02732e957412d0e1a3cad706f489641c596','0xbf1158177a2f350f092b2426025b339bfeeaa77923e4e51c6bb216d3292b8171','0xa71e132f397b427cc6f1bb58252a5c56b2e0a5dde14733c840103ec3552456a7','0x38ccc85e35a54234662a915df3c21b875f5d3e0adac5d9caa9eb44cc9fabf5eb','0xae6a813e60f259eb90516ecc2fd26680d86bb0cab9a1b5b18c660c737fd68c8f','0x2b65933dc34cd4283fbe1d5a0c90d2e82a07ea88b96a7acbe639560eae8887a8','0x16d4895a9cf3a1e415c908b38108c7cdb271b87496c3199bde8eb7b544465f47']
jobs=[]
for h in hs:
    jobs.extend([rpc(h+'_tx','eth_getTransactionByHash',[h]),rpc(h+'_receipt','eth_getTransactionReceipt',[h])])
with concurrent.futures.ThreadPoolExecutor(max_workers=6) as e:list(e.map(collect,jobs))
jobs=[]
for h in hs:
    t=json.loads((R/(h+'_tx.response.txt')).read_text())['result'];jobs.append(rpc('block_'+t['blockNumber'],'eth_getBlockByNumber',[t['blockNumber'],False]))
    if h==hs[-1]:jobs.append(rpc('unwrap_trace','debug_traceTransaction',[h,{'tracer':'callTracer'}]))
with concurrent.futures.ThreadPoolExecutor(max_workers=6) as e:list(e.map(collect,jobs))
