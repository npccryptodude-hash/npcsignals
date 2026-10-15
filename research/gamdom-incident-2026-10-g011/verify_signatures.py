"""Rebuild canonical signed envelopes from preserved RPC fields; recover EOA signers."""
import pathlib,json,gzip
import rlp
from eth_hash.auto import keccak
from eth_keys import keys
R=pathlib.Path(__file__).resolve().parent
def load():
 if (R/'rpc_archive.json.gz').exists():return json.loads(gzip.decompress((R/'rpc_archive.json.gz').read_bytes()))
 return {p.stem:json.loads(p.read_text()) for p in (R/'evidence').glob('*.json')}
def raw(s):return bytes.fromhex(s[2:])
def n(s):return int(s,16)
def recover(t):
 typ=n(t['type']);v=n(t['v']);r=n(t['r']);s=n(t['s'])
 authorities=[]
 if typ in [2,4]:
  chain=n(t['chainId']);parity=n(t.get('yParity',t['v']))
  access=[[raw(x['address']),[raw(k) for k in x['storageKeys']]] for x in t['accessList']]
  unsigned=[chain,n(t['nonce']),n(t['maxPriorityFeePerGas']),n(t['maxFeePerGas']),n(t['gas']),raw(t['to']),n(t['value']),raw(t['input']),access]
  if typ==4:
   authorization=[]
   for a in t['authorizationList']:
    arr=[n(a['chainId']),raw(a['address']),n(a['nonce']),n(a['yParity']),n(a['r']),n(a['s'])];authorization.append(arr)
    assert 0<arr[5]<=0x7fffffffffffffffffffffffffffffff5d576e7357a4501ddfe92f46681b20a0
    ah=keccak(b'\x05'+rlp.encode(arr[:3]));sig=keys.Signature(vrs=tuple(arr[3:]));pub=sig.recover_public_key_from_msg_hash(ah)
    assert sig.verify_msg_hash(ah,pub)
    authorities.append({'chain_id':arr[0],'implementation':a['address'],'nonce':arr[2],'y_parity':arr[3],'r':a['r'],'s':a['s'],'signing_digest':'0x'+ah.hex(),'recovered_authority':pub.to_checksum_address(),'recovered_public_key':'0x'+pub.to_bytes().hex()})
   unsigned.append(authorization)
  prefix=bytes([typ]);digest=keccak(prefix+rlp.encode(unsigned));envelope=prefix+rlp.encode(unsigned+[parity,r,s])
 elif typ==0:
  assert v>=35
  chain=(v-35)//2;parity=(v-35)%2
  unsigned=[n(t['nonce']),n(t['gasPrice']),n(t['gas']),raw(t['to']),n(t['value']),raw(t['input'])]
  digest=keccak(rlp.encode(unsigned+[chain,0,0]));envelope=rlp.encode(unsigned+[v,r,s])
 else:raise ValueError('Unsupported transaction type')
 assert '0x'+keccak(envelope).hex()==t['hash']
 assert 0<s<=0x7fffffffffffffffffffffffffffffff5d576e7357a4501ddfe92f46681b20a0
 signature=keys.Signature(vrs=(parity,r,s));pub=signature.recover_public_key_from_msg_hash(digest)
 assert signature.verify_msg_hash(digest,pub)
 addr=pub.to_checksum_address();assert addr.lower()==t['from']
 return {'transaction_hash':t['hash'],'chain_id':chain,'transaction_type':typ,'nonce':n(t['nonce']),'signing_digest':'0x'+digest.hex(),'y_parity':parity,'r':hex(r),'s':hex(s),'recovered_signer':addr,'recovered_public_key':'0x'+pub.to_bytes().hex(),'reconstructed_signed_envelope':'0x'+envelope.hex(),'hash_matches_requested':True,'signature_verified':True,'authorizations':authorities,'limits':'Proves valid key signature for the saved transaction bytes, not human identity, legitimate consent or chain inclusion by itself.'}
def calculate():
 e=load();out=[]
 for name,o in sorted(e.items()):
  if not name.startswith('tx_'):continue
  t=o['response']['result']
  out.append(recover(t))
 old=json.loads(gzip.decompress((R.parent/'gamdom-incident-2026-10-g010/rpc_archive.json.gz').read_bytes()))
 for h in ['0xa3753b1e3f2cd12a159b6b5f2753a7a4047ed25c2a3bf7b6add89e05d348d7d3','0xb2cca150592b3ba9344ff17a6f39888a40a855fc1619e8946b8b87e17217578f']:
  row=recover(old['tx_'+h]['response']['result']);row['previously_verified_transaction_new_signature_comparison']=True;out.append(row)
 for addr in ['0x0067cc2416f792cf0ec5629f5506324ac508f859','0xd5fbda4c79f38920159fe5f22df9655fde292d47']:
  rows=[x for x in out if x['recovered_signer'].lower()==addr]
  assert {x['chain_id'] for x in rows}=={1,56} and len({x['recovered_public_key'] for x in rows})==1
 return out
if __name__=='__main__':print(json.dumps(calculate(),indent=2))
