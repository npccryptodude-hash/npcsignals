import concurrent.futures,json,pathlib,sys
sys.path.insert(0,str(pathlib.Path(__file__).parent.parent/'robinhood_funding_direct_2026_10_09'))
from collect import collect as _collect,rpc
import collect as c
P=pathlib.Path(__file__).parent; B=P.parent; A=P/'access'; A.mkdir(exist_ok=True);c.P=P;c.R=A
origins=[x for x in json.loads((B/'robinhood_linkage_2026_10_09/transaction_ledger_F0435_F0464.json').read_text()) if x['record_type']=='origin deposit'][8:]
steps=[];jobs=[]
for o in origins:
    q=json.loads((B/'robinhood_linkage_2026_10_09/access'/('eth_getTransactionReceipt_'+o['transaction_hash']+'.response.txt')).read_text())['result']
    l=next(x for x in q['logs'] if x['address']=='0x998d7c178a1f9607b47ea3a8e22426451b3ce707');steps.append(l['topics'][1])
    jobs.extend([rpc(o['ID']+'_tx','eth_getTransactionByHash',[o['transaction_hash']]),rpc(o['ID']+'_receipt','eth_getTransactionReceipt',[o['transaction_hash']]),rpc(o['ID']+'_block','eth_getBlockByNumber',[hex(o['block_number']),False])])
for start in range(81901837,82035592,29999):
    jobs.append(rpc('escrow_step_logs_'+str(start),'eth_getLogs',[{'address':'0x794dbdbdbfd3f8a3b887f4513bf5ff29edd04a94','fromBlock':hex(start),'toBlock':hex(min(start+29998,82035591)),'topics':[None,steps]}]))
jobs.append(('escrow_eth_metadata','https://eth.blockscout.com/api/v2/smart-contracts/0x794dbdbdbfd3f8a3b887f4513bf5ff29edd04a94',None))
with concurrent.futures.ThreadPoolExecutor(max_workers=6) as e:list(e.map(_collect,jobs))
logs=[]
for f in A.glob('escrow_step_logs_*.response.txt'):logs.extend(json.loads(f.read_text()).get('result',[]))
hs=sorted({x['transactionHash'] for x in logs});jobs=[]
for h in hs:jobs.extend([rpc(h+'_tx','eth_getTransactionByHash',[h]),rpc(h+'_receipt','eth_getTransactionReceipt',[h])])
with concurrent.futures.ThreadPoolExecutor(max_workers=6) as e:list(e.map(_collect,jobs))
jobs=[]
for h in hs:
    t=json.loads((A/(h+'_tx.response.txt')).read_text())['result'];jobs.append(rpc('block_'+t['blockNumber'],'eth_getBlockByNumber',[t['blockNumber'],False]))
with concurrent.futures.ThreadPoolExecutor(max_workers=6) as e:list(e.map(_collect,jobs))
print('matching step logs',[(x['transactionHash'],x['topics'],x['data'][:180]) for x in logs],flush=True)
