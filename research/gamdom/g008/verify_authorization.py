#!/usr/bin/env python3
"""Decode saved signed bytes, recover both keys and decode the execute batch. No RPC."""
import json,pathlib
import rlp
from eth_hash.auto import keccak
from eth_keys import keys
ROOT=pathlib.Path(__file__).resolve().parent
EXPECTED='0xf1d9478bfcccf3dcc7ea5211fd7924230226be0bee7a5b96d767cc9f7167e9a2'
B='0xe5686AaE44d392aa6A0637FD38393859502F8667'
def h(b):return '0x'+b.hex()
def n(b):return int.from_bytes(b,'big')
def recover(digest,v,r,s):
 sig=keys.Signature(vrs=(n(v),n(r),n(s)))
 pub=sig.recover_public_key_from_msg_hash(digest)
 assert sig.verify_msg_hash(digest,pub)
 return pub.to_checksum_address()
def calculate():
 raw=bytes.fromhex((ROOT/'evidence/authorization_raw.hex').read_text().strip()[2:])
 assert raw[0]==4 and h(keccak(raw))==EXPECTED
 v=rlp.decode(raw[1:],strict=True);assert len(v)==13 and rlp.encode(v)==raw[1:]
 assert len(v[9])==1
 a=v[9][0];assert len(a)==6
 ah=keccak(b'\x05'+rlp.encode(a[:3]));th=keccak(b'\x04'+rlp.encode(v[:-3]))
 authority=recover(ah,*a[3:]);sender=recover(th,*v[-3:])
 assert authority==sender==B
 assert n(v[0])==n(a[0])==1 and n(v[1])==0 and n(a[2])==1
 assert a[1].hex()=='63c0c19a282a1b52b07dd5a65b58948a07dae32b'
 assert 0<n(a[5])<=0x7fffffffffffffffffffffffffffffff5d576e7357a4501ddfe92f46681b20a0
 data=v[7];assert data[:4]==keccak(b'execute(bytes32,bytes)')[:4]
 p=data[4:];mode=p[:32];offset=n(p[32:64]);size=n(p[offset:offset+32]);payload=p[offset+32:offset+32+size]
 arraystart=n(payload[:32]);count=n(payload[arraystart:arraystart+32]);head=arraystart+32
 calls=[]
 for j in range(count):
  base=head+n(payload[head+32*j:head+32*(j+1)])
  target=h(payload[base+12:base+32]);value=n(payload[base+32:base+64]);d=base+n(payload[base+64:base+96]);length=n(payload[d:d+32]);calldata=payload[d+32:d+32+length]
  calls.append({'target':target,'value_wei':value,'calldata':h(calldata)})
 assert count==2 and mode==b'\x01'+b'\x00'*31
 approve=bytes.fromhex(calls[0]['calldata'][2:]);pre=bytes.fromhex(calls[1]['calldata'][2:])
 assert calls[0]['target']=='0xdac17f958d2ee523a2206206994597c13d831ec7'
 assert approve[:4]==keccak(b'approve(address,uint256)')[:4]
 spender=h(approve[16:36]);allowance=n(approve[36:68])
 assert spender=='0xc92e8bdf79f0507f65a392b0ab4667716bfe0110' and allowance==2**256-1
 assert calls[1]['target']=='0x9008d19f58aabd9ed0d60971565aa8510560ab41'
 assert pre[:4]==keccak(b'setPreSignature(bytes,bool)')[:4]
 q=pre[4:];o=n(q[:32]);uid=q[o+32:o+32+n(q[o:o+32])];signed=n(q[32:64])
 assert len(uid)==56 and uid[32:52].hex()==B[2:].lower() and signed==1
 return {'transaction_hash':EXPECTED,'raw_length_bytes':len(raw),'outer_chain_id':n(v[0]),'outer_nonce':n(v[1]),'outer_to':h(v[5]),'outer_value_wei':n(v[6]),'outer_signing_digest':h(th),'outer_y_parity':n(v[-3]),'outer_r':h(v[-2]),'outer_s':h(v[-1]),'recovered_transaction_sender':sender,'authorization_count':1,'authorization':{'chain_id':n(a[0]),'implementation':h(a[1]),'nonce':n(a[2]),'y_parity':n(a[3]),'r':h(a[4]),'s':h(a[5]),'signing_digest':h(ah),'recovered_authority':authority},'expected_delegation_indicator_if_applied':'0xef0100'+a[1].hex(),'historical_eth_getCode_verified':False,'execution_selector':h(data[:4]),'mode':h(mode),'calls':calls,'decoded_approval':{'spender':spender,'allowance_raw':str(allowance)},'decoded_pre_signature':{'order_uid':h(uid),'signed':bool(signed)},'verification_scope':'Signed bytes and recovered keys independently verified offline; inclusion, success, logs and traces observed on Etherscan; no independent RPC state proof.'}
if __name__=='__main__':print(json.dumps(calculate(),indent=2,sort_keys=True))
