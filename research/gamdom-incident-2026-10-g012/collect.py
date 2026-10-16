"""Read-only collection of new execution/semantics evidence; frozen source receipts reused."""
import json,pathlib,urllib.request,urllib.error,datetime,sys,concurrent.futures,gzip
R=pathlib.Path(__file__).resolve().parent;E=R/'evidence';E.mkdir(exist_ok=True)
BNB='https://bsc-mainnet.nodereal.io/v1/64a9df0874fb4a93b9d0a3849de012d3'
ETH='https://mainnet.gateway.tenderly.co'
SETTLEMENT='0x9008d19f58aabd9ed0d60971565aa8510560ab41'
B='0xe5686aae44d392aa6a0637fd38393859502f8667'
H=['0xe4eea89ea32d675baa724d2e3926ffd3d4fbbe8d4f73ce381799bf9550a92347','0xcda9343de4eb5ad1e96d210d3e215bdf55cb33fba1c5f3fe3a6456afbe6781d2']
def request(url,label,m=None,p=None):
 f=E/(label+'.json')
 if f.exists():return json.loads(f.read_text())
 o={'url':url,'requested_at_utc':datetime.datetime.now(datetime.timezone.utc).isoformat()}
 data=None
 if m:o['request']={'jsonrpc':'2.0','id':1,'method':m,'params':p};data=json.dumps(o['request']).encode()
 try:
  with urllib.request.urlopen(urllib.request.Request(url,data=data,headers={'Content-Type':'application/json','User-Agent':'NPCsignals-public-evidence-research'}),timeout=25) as h:
   body=h.read().decode();o['http_status']=h.status
   if m:o['response']=json.loads(body)
   else:
    try:o['body']=json.loads(body)
    except ValueError:o['body_text']=body
 except urllib.error.HTTPError as ex:
  o.update(error=str(ex),http_status=ex.code,error_body=ex.read().decode(errors='replace'))
 except Exception as ex:o['error']=str(ex)
 f.write_text(json.dumps(o,indent=2)+'\n');return o
def rpc(url,m,p,label):
 o=request(url,label,m,p)
 if 'result' not in o.get('response',{}):raise RuntimeError(str(o)[:300])
 return o['response']['result']
def tx(h):
 r=rpc(ETH,'eth_getTransactionReceipt',[h],'eth_receipt_'+h)
 t=rpc(ETH,'eth_getTransactionByHash',[h],'eth_tx_'+h)
 b=rpc(ETH,'eth_getBlockByNumber',[r['blockNumber'],False],'eth_block_'+str(int(r['blockNumber'],16)))
 assert t['hash']==r['transactionHash']==h and t['blockHash']==r['blockHash']==b['hash']
 return r,t,b
def old():return json.loads(gzip.decompress((R.parent/'gamdom-incident-2026-10-g011/rpc_archive.json.gz').read_bytes()))
def uids():
 out=[]
 for h in H:
  r=old()['receipt_'+h]['response']['result']
  l=next(l for l in r['logs'] if l['topics'][0].startswith('0xa07a543'))
  d=bytes.fromhex(l['data'][2:]);off=int.from_bytes(d[160:192],'big');size=int.from_bytes(d[off:off+32],'big');out.append('0x'+d[off+32:off+32+size].hex())
 return out
if __name__=='__main__':
 mode=sys.argv[1]
 if mode=='sources':
  urls=[('https://repo.sourcify.dev/contracts/full_match/56/'+SETTLEMENT+'/metadata.json','sourcify_metadata'),('https://sourcify.dev/server/v2/contract/56/'+SETTLEMENT+'?fields=all','sourcify_v2'),('https://raw.githubusercontent.com/cowprotocol/contracts/main/src/contracts/GPv2Settlement.sol','cow_settlement_source'),('https://raw.githubusercontent.com/cowprotocol/contracts/main/src/contracts/libraries/GPv2Trade.sol','cow_trade_source'),('https://raw.githubusercontent.com/cowprotocol/contracts/main/src/contracts/libraries/GPv2Order.sol','cow_order_source'),('https://raw.githubusercontent.com/cowprotocol/contracts/main/src/contracts/mixins/GPv2Signing.sol','cow_signing_source')]
  with concurrent.futures.ThreadPoolExecutor(max_workers=3) as ex:
   for o in ex.map(lambda x:request(*x),urls):print(o['url'],o.get('http_status'),o.get('error','saved'),flush=True)
 elif mode=='orders':
  for uid in uids():
   for network in ['bnb','mainnet']:
    o=request('https://api.cow.fi/'+network+'/api/v1/orders/'+uid,'order_'+network+'_'+uid);print(network,uid,o.get('http_status'),str(o.get('body',o.get('error')))[:300],flush=True)
 elif mode=='eth':
  for h in ['0x6b282435dc06107a499c8b8ef0ed83632a51d32738d81c143dc7e2d53542fd40','0x3afe0536e5a7bc6f33da46ecef12c11a0591c9b13df90cb58f73c6839c99efaf']:
   r,t,b=tx(h);print(h,t['from'],t['to'],t['input'],len(r['logs']),flush=True)
 elif mode=='code':
  for block in [127436960,127437353]:
   c=rpc(BNB,'eth_getCode',[SETTLEMENT,hex(block)],'bnb_settlement_code_'+str(block));print(block,len(c),flush=True)
  for sig,name in [('0xf698da25','domain_separator')]:print(name,rpc(BNB,'eth_call',[{'to':SETTLEMENT,'data':sig},hex(127436960)],'bnb_'+name),flush=True)
 elif mode=='status':
  for address in ['0x16ee1ef93df4657a52f8ea6eebe950b54bc91265','0x66e6a2a0a9d871011b60b2e39902f10a33da4a2c']:
   s=request('https://1click.chaindefuser.com/v0/status?depositAddress='+address,'near_status_'+address)
   for h in s['body']['swapDetails']['nearTxHashes']:
    r=rpc('https://archival-rpc.mainnet.near.org','tx',{'tx_hash':h,'sender_account_id':'intents.near','wait_until':'FINAL'},'near_tx_'+h)
    for bh in {r['transaction_outcome']['block_hash']}:
     request('https://archival-rpc.mainnet.near.org','near_block_'+bh,'block',{'block_id':bh})
 elif mode=='authorization':
  from eth_hash.auto import keccak
  uid=bytes.fromhex(uids()[0][2:]);data='0x'+(keccak(b'preSignature(bytes)')[:4]+(32).to_bytes(32,'big')+len(uid).to_bytes(32,'big')+uid.ljust(64,b'\0')).hex()
  for block in [127436946,127436947,127436960]:
   request(BNB,'presign_state_'+str(block),'eth_call',[{'to':SETTLEMENT,'data':data},hex(block)])
  request(BNB,'presign_call_trace','debug_traceTransaction',['0xf7e40d1d02ef78a0c9c898b31d466cb29918f91532eac712c88bff4c7b2afb2a',{'tracer':'callTracer'}])
