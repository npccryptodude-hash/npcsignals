"""Exact preceding token-credit transaction and immediate sender context only."""
import concurrent.futures,importlib.util,json,pathlib
P=pathlib.Path(__file__).parent;s=importlib.util.spec_from_file_location('ac',P/'collect.py');m=importlib.util.module_from_spec(s);s.loader.exec_module(m)
H='0x9614b76aa2d529da3f22eab40ec412c0602e9cede74937754d4402035ff9b2d1';S='0x2df1c51e09aecf9cacb7bc98cb1742757f163df7';B=int('1e89ba8d',16)
if __name__=='__main__':
 jobs=[m.rpc('credit_tx','eth_getTransactionByHash',[H]),m.rpc('credit_receipt','eth_getTransactionReceipt',[H]),m.rpc('credit_block','eth_getBlockByNumber',[hex(B),False]),m.rpc('sender_case_code','eth_getCode',[S,hex(B)]),m.rpc('sender_latest_code','eth_getCode',[S,'latest']),m.balance('sender_usdc_before_credit',S,B-1),m.balance('sender_usdc_after_credit',S,B),m.balance('funder_usdc_before_credit',m.U,B-1),('relay_credit_hash','https://api.relay.link/requests/v2?hash='+H,None)]
 with concurrent.futures.ThreadPoolExecutor(max_workers=4) as e:list(e.map(lambda j:m.c.get(*j),jobs))
