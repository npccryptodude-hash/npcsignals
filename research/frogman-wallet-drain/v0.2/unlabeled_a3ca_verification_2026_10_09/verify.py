import json,pathlib,hashlib
from keccak import keccak
p=pathlib.Path(__file__).parent
old=json.loads((p.parent/'unlabeled_4521_verification_2026_10_09/master_timeline_F0001_F0497.json').read_text())['rows'];new=json.loads((p/'master_timeline_F0001_F0504.json').read_text())['rows']
assert new[:497]==old and sorted(x['ID'] for x in new)==[f'F{i:04}' for i in range(1,505)]
def raw(s):return json.loads((p/'access'/(s+'.response.txt')).read_text())
def r(s):return raw(s)['result']
def w(log):return [log['data'][2+i*64:2+(i+1)*64] for i in range(len(log['data'][2:])//64)]
for l in ['inbound','router','fill','onward']:
 t=r(l+'_tx');q=r(l+'_receipt');b=r(l+'_block');assert q['status']=='0x1' and t['hash']==q['transactionHash'] and t['blockHash']==b['hash'] and q['blockNumber']==b['number'];assert t['hash'] in b['transactions']
assert r('chain_id')=='0x1' and r('arb_chain_id')=='0xa4b1'
assert r('destination_code')==r('arb_recipient_snapshot_code')=='0x' and len(r('router_code'))>2
D='FundsDeposited(bytes32,bytes32,uint256,uint256,uint256,uint256,uint32,uint32,uint32,bytes32,bytes32,bytes32,bytes)'
F='FilledRelay(bytes32,bytes32,uint256,uint256,uint256,uint256,uint256,uint32,uint32,bytes32,bytes32,bytes32,bytes32,bytes32,(bytes32,bytes32,uint256,uint8))'
interface=(p/'access/across_interface.response.txt').read_text();assert 'event FundsDeposited' in interface and 'event FilledRelay' in interface
abi=raw('spoke_implementation')['abi'];assert all(any(x.get('name')==n and x.get('type')=='event' for x in abi) for n in ['FundsDeposited','FilledRelay'])
d=next(x for x in r('router_receipt')['logs'] if x['topics'][0]=='0x'+keccak(D.encode()));f=next(x for x in r('fill_receipt')['logs'] if x['topics'][0]=='0x'+keccak(F.encode()));dw=w(d);fw=w(f)
assert not d['removed'] and not f['removed']
assert int(d['topics'][1],16)==42161 and int(f['topics'][1],16)==1
assert int(d['topics'][2],16)==int(f['topics'][2],16)==4737420
assert d['topics'][3][2:]==fw[8]
for di,fi in [(0,0),(1,1),(2,2),(3,3),(5,5),(6,6),(7,9),(8,7)]:assert dw[di]==fw[fi]
assert int(dw[9],16)==320 and int(dw[10],16)==0
assert int(fw[10],16)==int(fw[12],16)==int(fw[14],16)==0 and fw[11]==fw[9] and fw[13]==fw[3]
assert '0x'+fw[9][-40:]==r('router_tx')['from']==r('inbound_tx')['to']==r('onward_tx')['from']
assert int(r('router_tx')['value'],16)==35*10**18
assert int(dw[2],16)==91241354058 and int(fw[3],16)==91232216513
T='0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef'
a='0xaf88d065e77c8cc2239327c5edb3a432268e5831';u='0xa3ca6199d8692ec40d0287e615b48d0e8cde9abe';bridge='0x2df1c51e09aecf9cacb7bc98cb1742757f163df7'
transfer=next(x for x in r('fill_receipt')['logs'] if x['address']==a and x['topics'][0]==T);assert int(transfer['data'],16)==91232216513 and '0x'+transfer['topics'][2][-40:]==u
out=next(x for x in r('onward_receipt')['logs'] if x['address']==a and x['topics'][0]==T);assert int(out['data'],16)==91232216513 and '0x'+out['topics'][1][-40:]==u and '0x'+out['topics'][2][-40:]==bridge
credit=next(x for x in raw('hyperliquid_deposit_credit') if x['hash']==r('onward_tx')['hash']);assert credit['delta']=={'type':'deposit','usdc':'91232.216513'}
assert bridge in (p/'access/hl_bridge_docs.response.txt').read_text().lower()
status=raw('across_status');assert status['status']=='filled' and status['depositTxHash']==r('router_tx')['hash'] and status['fillTx']==r('fill_tx')['hash'] and int(status['depositId'])==4737420
lifi=raw('lifi_status');assert lifi['sending']['txHash']==r('router_tx')['hash'] and lifi['receiving']['txHash']==r('fill_tx')['hash'] and lifi['receiving']['amount']=='91232216513'
assert raw('router_metadata')['is_verified'] and raw('router_metadata')['name']=='LiFiDiamond';assert raw('swap_router_metadata')['is_verified'] and raw('swap_router_metadata')['name']=='MetaAggregationRouterV2'
for rel,h in json.loads((p/'SHA256SUMS.json').read_text()).items():assert hashlib.sha256((p/rel).read_bytes()).hexdigest()==h
print('PASS: 497 prior objects unchanged; exact receipts/blocks, full Across event correspondence, API records, USDC outflow and HL deposit credit, hashes')
