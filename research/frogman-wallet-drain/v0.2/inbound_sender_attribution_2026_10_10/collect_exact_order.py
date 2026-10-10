"""Bounded follow-up: exact Relay order origin, one nearby replenishment, withdrawal-only recheck."""
import importlib.util,pathlib,json,concurrent.futures,time
P=pathlib.Path(__file__).parent;s=importlib.util.spec_from_file_location('sc',P/'collect.py');m=importlib.util.module_from_spec(s);s.loader.exec_module(m)
H='0x23e2c2bdaa4e38dfa93b656042179ff96ad39f51cf867dd3a213281fdc381b2d';I='0xa4afb63f1a0cb8f13cbe7fa7981f23e0b73a35d9b6b2782e7365a42124678a46';AR='https://arb1.arbitrum.io/rpc'
def ar(label,method,params):return(label,AR,{'jsonrpc':'2.0','id':1,'method':method,'params':params})
if __name__=='__main__':
 jobs=[ar('origin_tx','eth_getTransactionByHash',[H]),ar('origin_receipt','eth_getTransactionReceipt',[H]),ar('origin_block','eth_getBlockByNumber',[hex(512342744),False]),m.rpc('replenishment_tx','eth_getTransactionByHash',[I]),m.rpc('replenishment_receipt','eth_getTransactionReceipt',[I]),m.rpc('replenishment_block','eth_getBlockByNumber',[hex(26135540),False])]
 with concurrent.futures.ThreadPoolExecutor(max_workers=4) as e:list(e.map(lambda j:m.c.get(*j),jobs))
