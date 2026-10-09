import concurrent.futures,json,pathlib,sys
sys.path.insert(0,str(pathlib.Path(__file__).parent.parent/'robinhood_funding_direct_2026_10_09'));import collect as c
P=pathlib.Path(__file__).parent;A=P/'access';c.R=A;c.RPC='https://arbitrum.drpc.org';V='0x3e2d81f7a5659e4760ba929ef88eed40ef6640a1';t=json.loads((A/'credit_tx.response.txt').read_text())['result'];bn=int(t['blockNumber'],16);call={'to':'0xaf88d065e77c8cc2239327c5edb3a432268e5831','data':'0x70a08231'+'0'*24+V[2:]}
jobs=[c.rpc('credit_pre_balance_drpc','eth_call',[call,hex(bn-1)]),c.rpc('credit_post_balance_drpc','eth_call',[call,hex(bn)])]
with concurrent.futures.ThreadPoolExecutor(max_workers=2) as e:list(e.map(c.collect,jobs))
