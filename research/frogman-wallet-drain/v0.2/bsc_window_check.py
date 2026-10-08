import json,concurrent.futures
from resume_evm import get,A
# Timestamp-bracketed blocks established by preserved binary-search block responses.
from pathlib import Path
P=Path(__file__).parent/'raw_sources'
blocks=[]
for label in ['bsc_start_26','bsc_end_26']:
 j=json.loads((P/(label+'.response.json')).read_text())['result'];blocks.append(j['number']);print(label,int(j['number'],16),int(j['timestamp'],16),flush=True)
jobs=[]
for i,a in enumerate(A):
 for b in blocks:jobs.append((f'bsc_window_nonce_{i}_{int(b,16)}','https://bsc-dataseed.binance.org',{'jsonrpc':'2.0','id':1,'method':'eth_getTransactionCount','params':[a,b]}))
 for b in blocks[:1]:jobs.append((f'bsc_small_logs_{i}','https://bsc-dataseed.binance.org',{'jsonrpc':'2.0','id':1,'method':'eth_getLogs','params':[{'fromBlock':b,'toBlock':hex(int(b,16)+999),'topics':['0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef','0x'+'0'*24+a[2:].lower()]}]}))
with concurrent.futures.ThreadPoolExecutor(max_workers=6) as e:list(e.map(lambda j:get(*j),jobs))
