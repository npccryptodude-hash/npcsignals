import concurrent.futures,json,pathlib,sys
sys.path.insert(0,str(pathlib.Path(__file__).parent.parent/'robinhood_funding_direct_2026_10_09'));import collect as c
P=pathlib.Path(__file__).parent;B=P.parent;c.R=P/'access';c.R.mkdir(exist_ok=True);c.RPC='https://eth.drpc.org';A=c.R
edges=json.loads((B/'robinhood_linkage_2026_10_09/cross_chain_edges.json').read_text());jobs=[c.rpc('eth_chain_id','eth_chainId',[])]
for i,e in enumerate(edges):
    tag=e['origin_record_ID'];h=e['destination_transaction'];jobs.extend([c.rpc(tag+'_fill_tx','eth_getTransactionByHash',[h]),c.rpc(tag+'_fill_receipt','eth_getTransactionReceipt',[h]),c.rpc(tag+'_fill_block','eth_getBlockByNumber',[hex(e['destination_block']),False])])
    if i>=8:jobs.append(c.rpc(tag+'_callback_trace','debug_traceTransaction',[h,{'tracer':'callTracer'}]))
h='0x204c2bf7375b0d44cc648f630a09a9c32e93fe8cedc416f6587012c2afa7cc99';jobs.extend([c.rpc('terminal_tx','eth_getTransactionByHash',[h]),c.rpc('terminal_receipt','eth_getTransactionReceipt',[h])])
addr='0xec96957de4ececf24abd382090026e9b5c647405'
for tail in ['','/transactions','/internal-transactions']:jobs.append(('terminal_'+(tail.strip('/') or 'metadata'),'https://eth.blockscout.com/api/v2/addresses/'+addr+tail,None))
with concurrent.futures.ThreadPoolExecutor(max_workers=6) as e:list(e.map(c.collect,jobs))
t=json.loads((A/'terminal_tx.response.txt').read_text())['result'];jobs=[c.rpc('terminal_block','eth_getBlockByNumber',[t['blockNumber'],False]),c.rpc('terminal_case_code','eth_getCode',[addr,t['blockNumber']]),c.rpc('routing_wallet_pre_first_fill_balance','eth_getBalance',['0x427c4b37de0714821b09c4fc655a713abbcfba83',hex(edges[0]['destination_block']-1)]),c.rpc('routing_wallet_pre_terminal_balance','eth_getBalance',['0x427c4b37de0714821b09c4fc655a713abbcfba83',hex(int(t['blockNumber'],16)-1)])]
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as e:list(e.map(c.collect,jobs))
d=json.loads((A/'terminal_transactions.response.txt').read_text());print('terminal pagination',d.get('next_page_params'));print([(x['hash'],x['from']['hash'],x['to']['hash'] if x['to'] else None,x['value'],x['timestamp']) for x in d['items']])
