import concurrent.futures,json,pathlib,sys
sys.path.insert(0,str(pathlib.Path(__file__).parent.parent/'robinhood_funding_direct_2026_10_09'));import collect as c
P=pathlib.Path(__file__).parent;A=P/'access';c.R=A;U='0x427c4b37de0714821b09c4fc655a713abbcfba83';c.RPC='https://eth.drpc.org'
items=[]
for f in A.glob('routing_transactions*.response.txt'):items+=json.loads(f.read_text())['items']
out=[x for x in items if x['from']['hash'].lower()==U and '2026-10-06T20:00'<x['timestamp']<'2026-10-07T02:19']
jobs=[]
for x in out:
 h=x['hash'];jobs.extend([c.rpc(h+'_tx','eth_getTransactionByHash',[h]),c.rpc(h+'_receipt','eth_getTransactionReceipt',[h]),c.rpc('block_'+hex(x['block_number']),'eth_getBlockByNumber',[hex(x['block_number']),False]),c.rpc(h+'_pre_balance','eth_getBalance',[U,hex(x['block_number']-1)]),c.rpc(h+'_post_balance','eth_getBalance',[U,hex(x['block_number'])]),c.rpc(h+'_recipient_code','eth_getCode',[x['to']['hash'],hex(x['block_number'])])])
fee=json.loads((P.parent/'robinhood_disposal_2026_10_09/access/supplement_tx.response.txt').read_text())['result'];jobs.append(c.rpc('fee_source_case_code','eth_getCode',[fee['from'],fee['blockNumber']]))
with concurrent.futures.ThreadPoolExecutor(max_workers=8) as e:list(e.map(c.collect,jobs))
c.RPC='https://arb1.arbitrum.io/rpc';d=json.loads((A/'mayan_status.response.txt').read_text());t=json.loads((A/'destination_tx.response.txt').read_text())['result'];bn=int(t['blockNumber'],16);end=bn+9999;token=d['toTokenAddress'];V=d['destAddress'];topic='0x'+'0'*24+V[2:];transfer='0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef'
jobs=[c.rpc('destination_outgoing_USDC_logs','eth_getLogs',[{'address':token,'fromBlock':hex(bn),'toBlock':hex(end),'topics':[transfer,topic]}]),c.rpc('destination_incoming_USDC_logs','eth_getLogs',[{'address':token,'fromBlock':hex(bn),'toBlock':hex(end),'topics':[transfer,None,topic]}]),c.rpc('destination_window_end','eth_getBlockByNumber',[hex(end),False]),c.rpc('destination_window_USDC_balance','eth_call',[{'to':token,'data':'0x70a08231'+topic[2:]},hex(end)])]
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as e:list(e.map(c.collect,jobs))
