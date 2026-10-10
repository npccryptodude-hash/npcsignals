"""Offline review of evidence correspondence, not RPC HTTP success assumptions."""
import hashlib,json,pathlib,sys
P=pathlib.Path(__file__).parent;A=P/'access';sys.path.insert(0,str(P.parent/'mayan_verification_2026_10_09'));from keccak_utils import keccak
U='0xae06669dfd3e932476f00ea49fce82e5e63f83bf';S='0x2df1c51e09aecf9cacb7bc98cb1742757f163df7';W='0xd116117e42279dea647d45dd012c67e31e7d1a63';T='0xaf88d065e77c8cc2239327c5edb3a432268e5831'
def raw(n):return json.loads((A/(n+'.response.txt')).read_text())
def r(n):return raw(n)['result']
def topic(s):return '0x'+keccak(s.encode())
def words(l):d=l['data'][2:];return [d[i:i+64] for i in range(0,len(d),64)]
prior=P.parent/'hyperliquid_withdrawal_recheck_2026_10_10/master_timeline_F0001_F0603.json';assert hashlib.sha256(prior.read_bytes()).hexdigest()=='ba7c22a38e7fb57fe1cb9824afa8707a8f2e919507b4a8c688113d0be0b54378';old=json.loads(prior.read_text())['rows'];new=json.loads((P/'master_timeline_F0001_F0605.json').read_text())['rows'];assert len(old)==603 and new[:603]==old and sorted(x['ID'] for x in new)==[f'F{i:04}' for i in range(1,606)]
for n in ['credit','withdrawal_request']:
 t,q,b=r(n+'_tx'),r(n+'_receipt'),r(n+'_block');assert q['status']=='0x1' and t['hash']==q['transactionHash'] and t['blockHash']==q['blockHash']==b['hash'] and t['blockNumber']==q['blockNumber']==b['number'] and t['hash'] in b['transactions'] and int(t['chainId'],16)==42161 and t['to']==S
q=r('credit_receipt');tl,fl=q['logs'];assert tl['address']==T and tl['topics'][0]==topic('Transfer(address,address,uint256)') and '0x'+tl['topics'][1][-40:]==S and '0x'+tl['topics'][2][-40:]==U and int(tl['data'],16)==1002300000;assert int(r('credit_block')['number'],16)==512342669 and int(r('credit_block')['timestamp'],16)==1791315834
incoming=r('funder_incoming_usdc_logs');assert len(incoming)==1;assert incoming[0]['transactionHash']==q['transactionHash'] and incoming[0]['data']==tl['data'] and incoming[0]['blockHash']==tl['blockHash']
assert fl['address']==S and fl['topics'][0]==topic('FinalizedWithdrawal(address,address,uint64,uint64,bytes32)') and '0x'+fl['topics'][1][-40:]==W;fw=words(fl);assert '0x'+fw[0][-40:]==U and int(fw[1],16)==1002300000 and int(fw[2],16)==1791315607929000
logs=r('withdrawal_requested_logs');assert len(logs)==1;rl=logs[0];assert rl['topics'][0]==topic('RequestedWithdrawal(address,address,uint64,uint64,bytes32,uint64)') and rl['topics'][1]==fl['topics'][1];rw=words(rl);assert rw[:4]==fw and int(rw[4],16)==int(r('withdrawal_request_block')['timestamp'],16);assert any(x['topics']==rl['topics'] and x['data']==rl['data'] and x['logIndex']==rl['logIndex'] for x in r('withdrawal_request_receipt')['logs'])
t=r('credit_tx');assert t['input'][:10]==topic('batchedFinalizeWithdrawals(bytes32[])')[:10] and t['input'][10:74]==format(32,'064x') and t['input'][74:138]==format(1,'064x') and t['input'][138:202]==fw[3]
api=raw('withdrawal_user_ledger');assert len(api)==2;wd=next(x for x in api if x['delta']['type']=='withdraw');it=next(x for x in api if x['delta']['type']=='accountClassTransfer');assert wd['hash']==t['hash'] and wd['delta']['usdc']=='1002.3' and wd['delta']['nonce']==int(fw[2],16) and wd['delta']['fee']=='1.0';assert it['delta']=={'type':'accountClassTransfer','usdc':'1003.3','toPerp':True};assert it['time']<wd['time'];m=json.loads((A/'withdrawal_user_ledger.json').read_text());assert m['HTTP_status']==200 and m['request']['user']==W and m['request']['type']=='userNonFundingLedgerUpdates'
source=(A/'bridge_official_source.response.txt').read_bytes();blob=hashlib.sha1(b'blob '+str(len(source)).encode()+b'\x00'+source).hexdigest();assert blob=='2f2e98e3be5e6eccc3a24e5a8317105e220e7ccb';assert len(r('sender_latest_code'))>2;assert 'error' in raw('sender_case_code') and 'error' in raw('sender_usdc_before_credit') and 'error' in raw('sender_usdc_after_credit') and 'error' in raw('funder_usdc_before_request');assert raw('relay_credit_hash')['requests']==[]
for x in new[603:]:
 for f in x['evidence_files']:assert (P/f).exists()
if (P/'master_timeline_F0001_F0607.json').exists():
 final=json.loads((P/'master_timeline_F0001_F0607.json').read_text())['rows'];assert final[:605]==new and sorted(x['ID'] for x in final)==[f'F{i:04}' for i in range(1,608)];assert final[-1]['classification']=='UNRESOLVED'
for f,h in json.loads((P/'SHA256SUMS.json').read_text()).items():assert hashlib.sha256((P/f).read_bytes()).hexdigest()==h
print('PASS: public-pinned 603 prior records preserved; credit/request receipt and block inclusion; exact Transfer and official ABI topics; withdrawal account/hash/nonce/amount/message; code-state errors retained; checksums')
