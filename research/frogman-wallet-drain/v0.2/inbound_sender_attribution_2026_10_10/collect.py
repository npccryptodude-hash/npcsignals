"""Read-only attribution checks for one existing sender; no counterparties fan-out."""
import concurrent.futures,importlib.util,json,pathlib
P=pathlib.Path(__file__).parent;s=importlib.util.spec_from_file_location('hc',P.parent/'hyperliquid_matched_account_2026_10_10/collect.py');c=importlib.util.module_from_spec(s);s.loader.exec_module(c);c.A=P/'access';c.A.mkdir(exist_ok=True)
U='0x18dd3c14e34c1bc379f7538068c59160d9f68e25';RPC='https://eth.drpc.org';START=26135406;END=26135606;H='0x494f960fb252a3bdfb2edb46a0dfe71173f1964f13b26784511f8af8d31e61b2'
def rpc(label,method,params):return (label,RPC,{'jsonrpc':'2.0','id':1,'method':method,'params':params})
if __name__=='__main__':
 jobs=[('ordinary_history',f'https://eth.blockscout.com/api?module=account&action=txlist&address={U}&startblock={START}&endblock={END}&sort=asc&page=1&offset=1000',None),('internal_history',f'https://eth.blockscout.com/api?module=account&action=txlistinternal&address={U}&startblock={START}&endblock={END}&sort=asc&page=1&offset=1000',None),('metadata',f'https://eth.blockscout.com/api/v2/addresses/{U}',None),rpc('case_tx','eth_getTransactionByHash',[H]),rpc('case_receipt','eth_getTransactionReceipt',[H]),rpc('case_block','eth_getBlockByNumber',[hex(26135506),False]),rpc('case_code','eth_getCode',[U,hex(26135506)]),rpc('nonce_before','eth_getTransactionCount',[U,hex(START-1)]),rpc('nonce_after','eth_getTransactionCount',[U,hex(END)]),rpc('snapshot_block','eth_getBlockByNumber',['latest',False])]
 with concurrent.futures.ThreadPoolExecutor(max_workers=5) as ex:list(ex.map(lambda j:c.get(*j),jobs))
 f=c.A/'snapshot_block.response.txt'
 if f.exists():
  b=json.loads(f.read_text()).get('result')
  if b:
   jobs=[rpc('snapshot_code','eth_getCode',[U,b['number']]),rpc('snapshot_nonce','eth_getTransactionCount',[U,b['number']]),rpc('snapshot_balance','eth_getBalance',[U,b['number']])]
   with concurrent.futures.ThreadPoolExecutor(max_workers=3) as ex:list(ex.map(lambda j:c.get(*j),jobs))
