"""Exact discovered bridge withdrawal: recipient API, verified metadata, bounded immediate pool logs."""
import concurrent.futures,importlib.util,pathlib
P=pathlib.Path(__file__).parent;s=importlib.util.spec_from_file_location('ac',P/'collect.py');m=importlib.util.module_from_spec(s);s.loader.exec_module(m)
S='0x2df1c51e09aecf9cacb7bc98cb1742757f163df7';B=512342669;TRANSFER='0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef'
if __name__=='__main__':
 jobs=[('funder_hl_ledger','https://api.hyperliquid.xyz/info',{'type':'userNonFundingLedgerUpdates','user':m.U,'startTime':1791312234000,'endTime':1791315855000}),('bridge_verified_source','https://api.routescan.io/v2/network/mainnet/evm/42161/etherscan/api?module=contract&action=getsourcecode&address='+S,None),('bridge_explorer','https://arbiscan.io/address/'+S+'#code',None),m.rpc('sender_incoming_usdc_logs','eth_getLogs',[{'address':m.T,'fromBlock':hex(B-1000),'toBlock':hex(B),'topics':[TRANSFER,None,'0x'+S[2:].rjust(64,'0')]}]),m.rpc('funder_outgoing_usdc_logs','eth_getLogs',[{'address':m.T,'fromBlock':hex(m.B-100000),'toBlock':hex(m.B),'topics':[TRANSFER,'0x'+m.U[2:].rjust(64,'0')]}])]
 with concurrent.futures.ThreadPoolExecutor(max_workers=4) as e:list(e.map(lambda j:m.c.get(*j),jobs))
