from resume_evm import get,A
import pathlib,json,urllib.parse,concurrent.futures
P=pathlib.Path(__file__).parent/'raw_sources';j=json.loads((P/'eth_transactions_1.response.json').read_text());alltx=j['items'];n=1
while j.get('next_page_params') and n<6:
 label=f'eth_transactions_1_page{n}';url='https://eth.blockscout.com/api/v2/addresses/'+A[1]+'/transactions?'+urllib.parse.urlencode(j['next_page_params']);get(label,url)
 f=P/(label+'.response.json')
 if not f.exists():break
 j=json.loads(f.read_text());alltx+=j.get('items',[]);n+=1
(P/'eth_history_combined.json').write_text(json.dumps({'items':alltx,'next_page_params':j.get('next_page_params')},indent=2)+'\n')
outs=[t for t in alltx if t['from']['hash'].lower()==A[1].lower()]
print('history',len(alltx),'outgoing',len(outs),'next',j.get('next_page_params'),flush=True)
jobs=[]
for t in outs:
 h=t['hash'];jobs.append(('relay_hash_'+h,'https://api.relay.link/requests/v2?hash='+h+'&limit=50',None))
 for meth in ['eth_getTransactionByHash','eth_getTransactionReceipt']:jobs.append((meth+'_'+h,'https://ethereum-rpc.publicnode.com',{'jsonrpc':'2.0','id':1,'method':meth,'params':[h]}))
for b in sorted(set(t['block_number'] for t in alltx)):
 if any(t['block_number']==b for t in outs):jobs.append(('eth_block_'+str(b),'https://ethereum-rpc.publicnode.com',{'jsonrpc':'2.0','id':1,'method':'eth_getBlockByNumber','params':[hex(b),False]}))
for meth in ['eth_getBalance','eth_chainId']:jobs.append(('eth_current_'+meth,'https://ethereum-rpc.publicnode.com',{'jsonrpc':'2.0','id':1,'method':meth,'params':[A[1],'latest'] if meth=='eth_getBalance' else []}))
with concurrent.futures.ThreadPoolExecutor(max_workers=8) as e:list(e.map(lambda x:get(*x),jobs))
