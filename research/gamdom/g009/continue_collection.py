#!/usr/bin/env python3
"""Continue bounded collection; use cached response files so completed requests are not repeated."""
from collect_evidence import rpc,logs,ROOT,D,TOKEN
import pathlib,json,concurrent.futures,datetime

def cached(method,params,label):
 p=ROOT/'evidence'/f'{label}.json'
 if p.exists():
  o=json.loads(p.read_text())
  if 'result' in o.get('response',{}):return o['response']['result']
 return rpc(method,params,label)
def receipt(h):
 return cached('eth_getTransactionReceipt',[h],'receipt_'+h),cached('eth_getTransactionByHash',[h],'tx_'+h)
def balance(b):return cached('eth_call',[{'to':TOKEN,'data':'0x70a08231'+'0'*24+D[2:]},hex(b)],'balance_'+str(b))
if __name__=='__main__':
 blocks=[95400000,95434112,95434113,93000000,94700000]
 def readblock(b):
  x=cached('eth_getBlockByNumber',[hex(b),False],'block_'+str(b));print(b,datetime.datetime.fromtimestamp(int(x['timestamp'],16),datetime.timezone.utc).isoformat(),flush=True)
 with concurrent.futures.ThreadPoolExecutor(max_workers=3) as pool:list(pool.map(readblock,blocks))
 for b in [95399999,95434112,95434113]:print('balance',b,int(balance(b),16),flush=True)
 files=['recent_logs_test_1.json','recent_logs_test_2.json']
 arr=[]
 for f in files:arr+=json.loads((ROOT/'evidence'/f).read_text())['response']['result']
 hashes=sorted({x['transactionHash'] for x in arr}|{'0x06f5eeef95dcabfcb68f7241990594977f23d4a19e1c89d01a2bf4321313ead5','0x0cd2ddf10b66c7762a5b8027531b0e99c57f24e3eb7c672660e6f81c9718969d','0x563cba0b72c43d5d66ddd3a217eea56719f483a1e342132ce256b215031c5daa'})
 with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
  for h,(r,t) in zip(hashes,pool.map(receipt,hashes)):
   print(h,'status',r['status'],'from',t['from'],'block',int(t['blockNumber'],16),flush=True)
