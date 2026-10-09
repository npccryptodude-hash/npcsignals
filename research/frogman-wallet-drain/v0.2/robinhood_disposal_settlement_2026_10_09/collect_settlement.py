import concurrent.futures,json,pathlib,sys,urllib.parse
sys.path.insert(0,str(pathlib.Path(__file__).parent.parent/'robinhood_funding_direct_2026_10_09'));import collect as c
P=pathlib.Path(__file__).parent;A=P/'access';c.R=A;c.RPC='https://arb1.arbitrum.io/rpc'
d=json.loads((A/'mayan_status.response.txt').read_text());H=d['fulfillTxHash'];V=d['destAddress'];jobs=[c.rpc('destination_tx','eth_getTransactionByHash',[H]),c.rpc('destination_receipt','eth_getTransactionReceipt',[H]),c.rpc('arb_chain','eth_chainId',[])]
for tail in ['/transactions','/token-transfers']:
 jobs.append(('destination_'+tail.strip('/'),'https://arbitrum.blockscout.com/api/v2/addresses/'+V+tail,None))
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as e:list(e.map(c.collect,jobs))
t=json.loads((A/'destination_tx.response.txt').read_text())['result'];jobs=[c.rpc('destination_block','eth_getBlockByNumber',[t['blockNumber'],False]),c.rpc('destination_code','eth_getCode',[V,t['blockNumber']]),c.rpc('destination_pre_balance','eth_call',[{'to':d['toTokenAddress'],'data':'0x70a08231'+'0'*24+V[2:]},hex(int(t['blockNumber'],16)-1)]),c.rpc('destination_post_balance','eth_call',[{'to':d['toTokenAddress'],'data':'0x70a08231'+'0'*24+V[2:]},t['blockNumber']])]
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as e:list(e.map(c.collect,jobs))
# Bounded routing-account pagination: reach first case funding, never fan out to recipients.
base='https://eth.blockscout.com/api/v2/addresses/0x427c4b37de0714821b09c4fc655a713abbcfba83/transactions';prev='routing_transactions'
for i in range(1,9):
 data=json.loads((A/(prev+'.response.txt')).read_text());params=data.get('next_page_params')
 if not params or min(x['timestamp'] for x in data['items'])<'2026-10-06T20:00':break
 tag='routing_transactions_page_'+str(i);c.collect((tag,base+'?'+urllib.parse.urlencode(params),None));prev=tag
