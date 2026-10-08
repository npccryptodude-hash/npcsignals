from resume_evm import get
import pathlib,json,time
P=pathlib.Path(__file__).parent/'raw_sources';rows=[]
for f in P.glob('eth_second_*.response.json'):
 for t in json.loads(f.read_text()).get('items',[]):
  if t['raw_input'].startswith('0x092e8fa4'):
   r=json.loads((P/('eth_getTransactionReceipt_'+t['hash']+'.response.json')).read_text())['result']
   for l in r['logs']:
    if l['address']=='0x4cd00e387622c35bddb9b4c962c136462338bc31':rows.append({'source_tx':t['hash'],'order_id':'0x'+l['data'][-64:],'source_wei':str(int(l['data'][66:130],16)),'depositor':'0x'+l['data'][26:66]})
(P/'relay_order_candidates.json').write_text(json.dumps(rows,indent=2)+'\n')
for i,r in enumerate(rows):
 if r['source_tx']=='0xa7da5d044b2a34fd2105862dfed7b947254bd7ff12d7567e91be48d649f18d3c':continue
 get('relay_order_'+r['order_id'],'https://api.relay.link/requests/v2?orderId='+r['order_id']+'&includeOrderData=true&limit=20')
 time.sleep(31)
