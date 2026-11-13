import json,urllib.request,datetime,hashlib
from collect import P,call
u='https://mainnet.gateway.tenderly.co';src='0x4521ef4df51a7689d4db5d8fc598685cb226ff58';dst='0xbbae94f15c551920f45ad9a099e2a6b821822e3e';block=26282041
for name,method,params in [('eth_source_before','eth_getBalance',[src,hex(block-1)]),('eth_source_after','eth_getBalance',[src,hex(block)]),('eth_dest_before','eth_getBalance',[dst,hex(block-1)]),('eth_dest_after','eth_getBalance',[dst,hex(block)]),('eth_dest_current','eth_getBalance',[dst,'latest']),('eth_dest_nonce','eth_getTransactionCount',[dst,'latest']),('eth_dest_code','eth_getCode',[dst,hex(block)])]:
 try:call(name,u,{'jsonrpc':'2.0','id':1,'method':method,'params':params})
 except Exception as e:print(name,str(e),flush=True)
for label,a in [('eth_source_history',src),('eth_dest_history',dst)]:
 url='https://eth.blockscout.com/api?module=account&action=txlist&address='+a+'&startblock=26100000&endblock=99999999&page=1&offset=1000&sort=asc'
 try:
  with urllib.request.urlopen(url,timeout=20) as r:b=r.read()
  (P/'raw'/(label+'.json')).write_bytes(b);(P/'raw'/(label+'.meta.json')).write_text(json.dumps({'url':url,'retrieved_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'sha256':hashlib.sha256(b).hexdigest()},indent=2)+'\n')
 except Exception as e:(P/'raw'/(label+'.error.json')).write_text(json.dumps({'url':url,'checked_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'error':str(e)},indent=2)+'\n');print(label,str(e),flush=True)
