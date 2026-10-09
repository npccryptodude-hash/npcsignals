"""Reproduce bounded funding states, histories and protocol execution attempts."""
import concurrent.futures,json
from collect import collect,rpc,P,R
B=P.parent
A='0x427c4b37de0714821b09c4fc655a713abbcfba83'; Z='0x07ae8551be970cb1cca11dd7a11f47ae82e70e67'
rows=json.loads((B/'robinhood_linkage_2026_10_09/transaction_ledger_F0435_F0464.json').read_text())
origins=[r for r in rows if r['record_type']=='origin deposit']
jobs=[rpc('chain_id','eth_chainId',[])]
for label,addr in [('direct',A),('outer',Z)]:
    jobs.append((label+'_history','https://explorer.robinhood.com/api/v2/addresses/'+addr+'/transactions',None))
    jobs.append((label+'_metadata','https://explorer.robinhood.com/api/v2/addresses/'+addr,None))
for r in origins:
    tag=r['ID']; block=r['block_number']; addr=r['sender']
    for side,b in [('pre',block-1),('post',block)]:
        jobs.append(rpc(tag+'_'+side+'_balance','eth_getBalance',[addr,hex(b)]))
        jobs.append(rpc(tag+'_'+side+'_nonce','eth_getTransactionCount',[addr,hex(b)]))
    jobs.append(rpc(tag+'_receipt','eth_getTransactionReceipt',[r['transaction_hash']]))
for label,h in [('first_direct',origins[0]['transaction_hash']),('first_contract',origins[8]['transaction_hash']),('first_cashcat','0x44a5ad893f64a338d607045068dc02e59ddea4e0d6d64ef186b72f0e3e861bc7')]:
    jobs.append(rpc(label+'_trace','debug_traceTransaction',[h,{'tracer':'callTracer'}]))
    jobs.append(rpc(label+'_tx','eth_getTransactionByHash',[h]))
for label,addr in [('direct',A),('outer',Z),('router','0x998d7c178a1f9607b47ea3a8e22426451b3ce707')]:
    jobs.append(rpc(label+'_case_code','eth_getCode',[addr,hex(origins[8]['block_number'])]))
for start in range(81901837,82032268,29999):
    for pos in [1,2]:
        topics=[None]* (pos+1);topics[pos]='0x'+'0'*24+A[2:]
        jobs.append(rpc('direct_logs_'+str(pos)+'_'+str(start),'eth_getLogs',[{'fromBlock':hex(start),'toBlock':hex(min(start+29998,82032267)),'topics':topics}]))
with concurrent.futures.ThreadPoolExecutor(max_workers=6) as e:list(e.map(collect,jobs))
