"""G014 offline historical export, metadata and Ethereum signing-scope audit."""
import pathlib,json,gzip,base64,hashlib,tarfile,io
import rlp
from eth_hash.auto import keccak
from eth_keys import keys
R=pathlib.Path(__file__).resolve().parent;P=R.parent/'gamdom-incident-2026-10-g013';BASE='543c6435dbd0bf18e3049cf0cefcb868e7d37092'
def records():
 f=R/'acquisition_archive.json.gz'
 return json.loads(gzip.decompress(f.read_bytes())) if f.exists() else {p.stem:json.loads(p.read_text()) for p in (R/'evidence').glob('*.json')}
def res(e,k):return e[k]['response']['result']
def hx(b):return '0x'+b.hex()
def n(v):return int(v,16)
def b58(s):
 abc='123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz';v=0
 for c in s:v=v*58+abc.index(c)
 return b'\0'*(len(s)-len(s.lstrip('1')))+v.to_bytes((v.bit_length()+7)//8,'big')
def leb(d,p):
 n=0;shift=0
 while True:
  v=d[p];p+=1;n|=(v&127)<<shift
  if v<128:return n,p
  shift+=7;assert shift<64
def exports(d):
 assert d[:8]==b'\0asm\1\0\0\0';p=8;out=[]
 while p<len(d):
  section=d[p];size,q=leb(d,p+1);end=q+size
  if section==7:
   count,q=leb(d,q)
   for _ in range(count):
    size,q=leb(d,q);name=d[q:q+size].decode();q+=size;kind=d[q];q+=1;index,q=leb(d,q);out.append({'name':name,'kind':kind,'index':index})
   assert q==end
  p=end
 assert p==len(d);return out
def derive():
 e=records();old=json.loads(gzip.decompress((P/'acquisition_archive.json.gz').read_bytes()));eth=json.loads(gzip.decompress((P.parent/'gamdom-incident-2026-10-g012/acquisition_archive.json.gz').read_bytes()))
 factory=base64.b64decode(res(e,'historical_factory_view_code')['code_base64']);state=res(e,'historical_factory_view_account');state2=res(e,'historical_factory_account_route2')
 assert hashlib.sha256(factory).digest()==b58(state['code_hash']) and state2['code_hash']==state['code_hash']
 token=base64.b64decode(res(old,'fastnear_view_code_eth-0x6b175474e89094c44da98b954eedeac495271d0f.omft.near')['code_base64'])
 tokenstate=res(old,'fastnear_view_account_eth-0x6b175474e89094c44da98b954eedeac495271d0f.omft.near');assert hashlib.sha256(token).digest()==b58(tokenstate['code_hash'])
 fx,tx=exports(factory),exports(token);fn={x['name'] for x in fx if x['kind']==0};tn={x['name'] for x in tx if x['kind']==0}
 assert {'get_withdrawal','record_withdrawal','update_withdrawal'}.isdisjoint(fn)
 assert {'ft_transfer','contract_source_metadata','owner_get'}<=tn
 metadata=json.loads(bytes(res(e,'omft_historical_source_metadata')['result']));assert metadata['link']=='https://github.com/near/intents' and metadata['build_info'] is None
 assert json.dumps(metadata,separators=(',',':')).encode() in token
 for i in [1,2]:assert 'MethodResolveError(MethodNotFound)' in res(e,'historical_get_withdrawal_route'+str(i))['error']
 source=base64.b64decode(e['source_contracts_poa_factory_src_contract.rs']['body']['content']).decode();assert all('fn '+m in source for m in ['get_withdrawal','record_withdrawal','update_withdrawal'])
 architecture={'historical_factory_account':'omft.near','factory_code_hash':state['code_hash'],'factory_wasm_sha256':hashlib.sha256(factory).hexdigest(),'historical_blocks':[state['block_height'],state2['block_height']],'factory_exports':fx,'token_exports':tx,'token_code_hash':tokenstate['code_hash'],'token_source_metadata':metadata,'current_registry_methods_absent_historically':['get_withdrawal','record_withdrawal','update_withdrawal'],'receipt_probe_results':['MethodNotFound','MethodNotFound'],'historical_factory_embeds_identical_token_wasm':factory.find(token)>=0,'source_to_wasm_equivalence':'NOT ASSESSED; metadata lacks build commit','scope':'Exact historical method availability, not proof no off-chain registry exists.'}
 sigs=[];instructions=[];ids=json.loads((P/'message_identifier_register.json').read_text())
 assert ids[1]['withdrawal_action_receipt_id']=='96ktG3EwUqmz24aeen7ptcQLJfKrFdox8rsUF1kqHEwq'
 for row in ids:
  h=row['ethereum_transaction_hash'];t=res(eth,'eth_tx_'+h);r=res(eth,'eth_receipt_'+h);assert n(t['type'])==2 and n(t['chainId'])==1 and t['accessList']==[]
  body=[n(t['chainId']),n(t['nonce']),n(t['maxPriorityFeePerGas']),n(t['maxFeePerGas']),n(t['gas']),bytes.fromhex(t['to'][2:]),n(t['value']),bytes.fromhex(t['input'][2:]),[]]
  parity=n(t['v']);digest=keccak(b'\2'+rlp.encode(body));signature=keys.Signature(vrs=(parity,n(t['r']),n(t['s'])));pub=signature.recover_public_key_from_msg_hash(digest)
  raw=b'\2'+rlp.encode(body+[parity,n(t['r']),n(t['s'])]);assert hx(keccak(raw))==h and pub.to_address()==t['from'] and signature.verify_msg_hash(digest,pub)
  d=bytes.fromhex(t['input'][2:]);assert len(d)==68 and d[:4]==keccak(b'transfer(address,uint256)')[:4] and t['to']=='0x6b175474e89094c44da98b954eedeac495271d0f'
  receiver=hx(d[16:36]);amount=int.from_bytes(d[36:68],'big');assert receiver=='0xe5686aae44d392aa6a0637fd38393859502f8667' and n(t['value'])==0 and len(r['logs'])==1
  log=r['logs'][0];assert log['address']==t['to'] and n(log['data'])==amount and '0x'+log['topics'][1][-40:]==t['from'] and '0x'+log['topics'][2][-40:]==receiver
  sigs.append({'route':row['route'],'ethereum_transaction':h,'valid_EIP1559_transaction_signature':True,'chain_id':1,'nonce':n(t['nonce']),'signing_digest':hx(digest),'r':t['r'],'s':t['s'],'y_parity':parity,'recovered_signer':pub.to_address(),'recovered_public_key':pub.to_hex(),'signed_envelope':hx(raw),'calldata':t['input'],'recipient':receiver,'dai_raw':str(amount),'calldata_fully_decoded':True,'separate_protocol_identifier_bytes':0,'signed_source_referenced_OMFT_instruction':None,'historical_OMFT_payout_authority':'UNRESOLVED','limit':'Valid Ethereum transfer authorization only. No NEAR withdrawal reference is encoded in this transaction.'})
  instructions.append({'route':row['route'],'near_execution':row['near_intent_transaction_hash'],'withdrawal_action_receipt_id':row['withdrawal_action_receipt_id'],'ethereum_payout':h,'authenticated_payout_instruction':None,'onchain_factory_registry_available_at_both_incident_snapshots':False,'protocol_API_mapping':'SUPPORTED; reuse G013, no fresh status query needed','api_backend_independence':'UNRESOLVED','final_edge':'SUPPORTED','full_route':'SUPPORTED','alternative_withdrawal_or_pool_netting_excluded':False,'single_transaction_multi_recipient_batch':False,'negative_scope':'Each selected Ethereum transaction contains one canonical DAI transfer, not a multi-recipient batch. Economic pooling/netting or alternative source requests remain possible.'})
 assert len({x['recovered_public_key'] for x in sigs})==1
 interfaces=[]
 for name in ['historical_internal_utils_release','historical_bridge_sdk_release']:
  v=e[name+'_archive'];raw=base64.b64decode(v['body_base64']);assert v['declared_integrity']=='sha512-'+base64.b64encode(hashlib.sha512(raw).digest()).decode()
  tf=tarfile.open(fileobj=io.BytesIO(raw),mode='r:gz');files={p.name:tf.extractfile(p).read().decode() for p in tf.getmembers() if p.isfile() and p.name.endswith(('.js','.d.ts'))}
  matched={name:text for name,text in files.items() if 'withdrawal_status' in text}
  schemas=[]
  for path,text in matched.items():
   if path.endswith('.d.ts'):
    start=text.index('type WithdrawalStatusRequest');end=text.index('type HotOmniWithdrawRequest',start);schema=text[start:end];assert 'withdrawal_hash: string' in schema and 'transfer_tx_hash: string | null' in schema
    assert not any(x in schema.lower() for x in ['signature','attestation','public_key']);schemas.append({'path':path,'schema':schema,'sha256':hashlib.sha256(schema.encode()).hexdigest()})
  interfaces.append({'package':e[name]['body']['name'],'version':e[name]['body']['version'],'archive_sha256':hashlib.sha256(raw).hexdigest(),'registry_integrity_matches':True,'matching_withdrawal_status_files':list(matched),'typed_schema_findings':schemas,'limit':'Static published client interface, not proof of production service completeness or backend independence; package integrity is not payout-signature authentication.'})
 return {'historical_architecture_verification':architecture,'payout_signature_verification':sigs,'payout_instruction_register':instructions,'public_interface_audit':interfaces}
if __name__=='__main__':
 for name,value in derive().items():(R/(name+'.json')).write_text(json.dumps(value,indent=2)+'\n')
