import concurrent.futures,json,pathlib,sys
sys.path.insert(0,str(pathlib.Path(__file__).parent.parent/'robinhood_funding_direct_2026_10_09'));import collect as c
P=pathlib.Path(__file__).parent;c.R=P/'access';c.RPC='https://eth.drpc.org';A=c.R
h='0x33590b022e2f09bc824f0d6c94a6586941096faca9c21f497004ee20f4c61f62';addr='0x3e2d81f7a5659e4760ba929ef88eed40ef6640a1';u='0xec96957de4ececf24abd382090026e9b5c647405'
jobs=[c.rpc('onward_tx','eth_getTransactionByHash',[h]),c.rpc('onward_receipt','eth_getTransactionReceipt',[h])]
for tail in ['','/transactions','/internal-transactions']:jobs.append(('onward_'+(tail.strip('/') or 'metadata'),'https://eth.blockscout.com/api/v2/addresses/'+addr+tail,None))
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as e:list(e.map(c.collect,jobs))
t=json.loads((A/'onward_tx.response.txt').read_text())['result'];incoming=json.loads((A/'terminal_tx.response.txt').read_text())['result'];bn=t['blockNumber']
jobs=[c.rpc('onward_block','eth_getBlockByNumber',[bn,False]),c.rpc('onward_case_code','eth_getCode',[addr,bn]),c.rpc('forwarder_pre_incoming_balance','eth_getBalance',[u,hex(int(incoming['blockNumber'],16)-1)]),c.rpc('forwarder_pre_onward_balance','eth_getBalance',[u,hex(int(bn,16)-1)]),c.rpc('onward_recipient_pre_balance','eth_getBalance',[addr,hex(int(bn,16)-1)])]
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as e:list(e.map(c.collect,jobs))
