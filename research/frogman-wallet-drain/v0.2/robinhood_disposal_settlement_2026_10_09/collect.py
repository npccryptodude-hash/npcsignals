import concurrent.futures,json,pathlib,sys
sys.path.insert(0,str(pathlib.Path(__file__).parent.parent/'robinhood_funding_direct_2026_10_09'));import collect as c
P=pathlib.Path(__file__).parent;A=P/'access';A.mkdir(exist_ok=True);c.R=A;c.RPC='https://eth.drpc.org'
U='0x427c4b37de0714821b09c4fc655a713abbcfba83';F='0xae06669dfd3e932476f00ea49fce82e5e63f83bf';H='0xefa46658dead085751916c1368ed2590d72fa34dce36abf5c6b5a8cbcfc0d624'
jobs=[]
for tag,addr in [('routing',U),('fee_source',F)]:
 for tail in ['','/transactions','/internal-transactions']:jobs.append((tag+'_'+(tail.strip('/') or 'metadata'),'https://eth.blockscout.com/api/v2/addresses/'+addr+tail,None))
jobs.append(('mayan_status','https://explorer-api.mayan.finance/v3/swap/trx/'+H,None))
with concurrent.futures.ThreadPoolExecutor(max_workers=6) as e:list(e.map(c.collect,jobs))
for tag in ['routing_transactions','routing_internal-transactions','fee_source_transactions','fee_source_internal-transactions']:
 d=json.loads((A/(tag+'.response.txt')).read_text());print(tag,len(d.get('items',[])),d.get('next_page_params'),flush=True)
