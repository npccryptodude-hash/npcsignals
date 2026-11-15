#!/usr/bin/env python3
"""Canonical-token events for a fixed interval covering September and October; no current balances."""
from collect_evidence import rpc,ROOT,TOKEN,D,TRANSFER
import concurrent.futures,json
LO=93000000
HI=95434113

def collect(pos):
 label=f'bounded_logs_{LO}_{HI}_{pos}';p=ROOT/'evidence'/f'{label}.json'
 if p.exists() and 'result' in json.loads(p.read_text()).get('response',{}):return json.loads(p.read_text())['response']['result']
 topics=[TRANSFER,None,None];topics[pos]='0x'+'0'*24+D[2:]
 return rpc('eth_getLogs',[{'address':TOKEN,'fromBlock':hex(LO),'toBlock':hex(HI),'topics':topics}],label)
if __name__=='__main__':
 with concurrent.futures.ThreadPoolExecutor(max_workers=2) as pool:
  for pos,arr in zip([1,2],pool.map(collect,[1,2])):print('position',pos,'logs',len(arr),flush=True)
