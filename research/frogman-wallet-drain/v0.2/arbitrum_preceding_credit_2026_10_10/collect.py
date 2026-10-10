"""Read-only scope: latest preceding native USDC credits of one funder, before known request."""
import concurrent.futures,importlib.util,pathlib
P=pathlib.Path(__file__).parent;s=importlib.util.spec_from_file_location('hc',P.parent/'hyperliquid_matched_account_2026_10_10/collect.py');c=importlib.util.module_from_spec(s);s.loader.exec_module(c);c.A=P/'access';c.A.mkdir(exist_ok=True)
U='0xae06669dfd3e932476f00ea49fce82e5e63f83bf';T='0xaf88d065e77c8cc2239327c5edb3a432268e5831';B=512342744;RPC='https://arb1.arbitrum.io/rpc'
def rpc(label,method,params):return (label,RPC,{'jsonrpc':'2.0','id':1,'method':method,'params':params})
def balance(label,address,block):return rpc(label,'eth_call',[{'to':T,'data':'0x70a08231'+address[2:].rjust(64,'0')},hex(block)])
if __name__=='__main__':
 jobs=[('usdc_history',f'https://arbitrum.blockscout.com/api?module=account&action=tokentx&address={U}&contractaddress={T}&startblock=0&endblock={B}&sort=desc&page=1&offset=100',None),balance('funder_usdc_before_request',U,B-1),balance('funder_usdc_after_request',U,B),rpc('funder_code','eth_getCode',[U,hex(B)]),('funder_metadata','https://arbitrum.blockscout.com/api/v2/addresses/'+U,None)]
 with concurrent.futures.ThreadPoolExecutor(max_workers=4) as ex:list(ex.map(lambda j:c.get(*j),jobs))
