import concurrent.futures,json,pathlib,sys
sys.path.insert(0,str(pathlib.Path(__file__).parent.parent/'robinhood_funding_direct_2026_10_09'));import collect as c
P=pathlib.Path(__file__).parent;A=P/'access';c.R=A;c.RPC='https://arb1.arbitrum.io/rpc';V='0x3e2d81f7a5659e4760ba929ef88eed40ef6640a1';H='0x963c56253dedcfd5ff9f944c91eb9cb9e94d12701d9165f66a40b9aa0b4cfc1f'
jobs=[c.rpc('credit_tx','eth_getTransactionByHash',[H]),c.rpc('credit_receipt','eth_getTransactionReceipt',[H]),('hyperliquid_credit','https://api.hyperliquid.xyz/info',{'type':'userNonFundingLedgerUpdates','user':V,'startTime':1791324000000,'endTime':1791339900000})]
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as e:list(e.map(c.collect,jobs))
t=json.loads((A/'credit_tx.response.txt').read_text())['result'];token='0xaf88d065e77c8cc2239327c5edb3a432268e5831';call={'to':token,'data':'0x70a08231'+'0'*24+V[2:]};bn=int(t['blockNumber'],16)
jobs=[c.rpc('credit_block','eth_getBlockByNumber',[t['blockNumber'],False]),c.rpc('credit_endpoint_code','eth_getCode',['0x2df1c51e09aecf9cacb7bc98cb1742757f163df7',t['blockNumber']]),c.rpc('credit_pre_balance','eth_call',[call,hex(bn-1)]),c.rpc('credit_post_balance','eth_call',[call,t['blockNumber']])]
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as e:list(e.map(c.collect,jobs))
