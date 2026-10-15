#!/usr/bin/env python3
"""Fetch missing boundary state, selected receipts, headers and independent RPC checks."""
from continue_collection import cached, receipt, balance
from collect_evidence import ROOT, rpc, TOKEN, D
import concurrent.futures, json

def bounded_logs():
    values=[]
    for pos in [1,2]:
        values += json.loads((ROOT/'evidence'/f'bounded_logs_93000000_95434113_{pos}.json').read_text())['response']['result']
    return values

if __name__=='__main__':
    events=bounded_logs()
    incoming=[x for x in events if x['topics'][2][-40:]==D[2:]]
    largest=sorted(incoming,key=lambda x:int(x['data'],16),reverse=True)[:3]
    hashes=[x['transactionHash'] for x in largest]
    for e in largest: print('largest',e['transactionHash'],int(e['data'],16),e['topics'][1][-40:],flush=True)
    print('opening balance raw',int(balance(92999999),16),flush=True)
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as pool:
        for h,(_,t) in zip(hashes,pool.map(receipt,hashes)): print('receipt',h,t['from'],flush=True)
    receipt_files=list((ROOT/'evidence').glob('receipt_*.json'))
    blocks={int(json.loads(p.read_text())['response']['result']['blockNumber'],16) for p in receipt_files}
    blocks.add(92999999)
    def getheader(b):return cached('eth_getBlockByNumber',[hex(b),False],'block_'+str(b))
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:list(pool.map(getheader,sorted(blocks)))
    endpoints=['https://polygon-mainnet.public.blastapi.io','https://polygon.api.onfinality.io/public','https://polygon-mainnet.gateway.tatum.io']
    def check(pair):
        i,u=pair
        try:return rpc('eth_call',[{'to':TOKEN,'data':'0x70a08231'+'0'*24+D[2:]},hex(95434112)],'second_rpc_'+str(i),endpoint=u)
        except RuntimeError:return 'unavailable; response saved'
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as pool:
        for u,v in zip(endpoints,pool.map(check,enumerate(endpoints))):print('second provider',u,v,flush=True)
