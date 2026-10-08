from resume_evm import get
import pathlib,json,concurrent.futures
P=pathlib.Path(__file__).parent/'raw_sources';U='https://arb1.arbitrum.io/rpc'
rows=json.loads((P/'relay_fill_candidates.json').read_text());wallets=sorted({r['recipient'].lower() for r in rows})
jobs=[]
for i,a in enumerate(wallets):jobs.append(('arb_USDC_balance_'+a,U,{'jsonrpc':'2.0','id':1,'method':'eth_call','params':[{'to':'0xaf88d065e77c8cc2239327c5edb3a432268e5831','data':'0x70a08231'+'0'*24+a[2:]},'latest']}))
jobs.append(('arb_USDC_downstream_logs',U,{'jsonrpc':'2.0','id':1,'method':'eth_getLogs','params':[{'fromBlock':hex(512422000),'toBlock':'latest','address':'0xaf88d065e77c8cc2239327c5edb3a432268e5831','topics':['0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef',['0x'+'0'*24+a[2:] for a in wallets]]}]}))
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as e:list(e.map(lambda j:get(*j),jobs))
