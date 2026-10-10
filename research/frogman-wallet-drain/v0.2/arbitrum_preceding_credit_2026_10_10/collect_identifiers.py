"""Reproduce discovered exact withdrawal identifiers, not unrelated accounts."""
import concurrent.futures,importlib.util,json,pathlib,sys
P=pathlib.Path(__file__).parent;s=importlib.util.spec_from_file_location('ac',P/'collect.py');m=importlib.util.module_from_spec(s);s.loader.exec_module(m);sys.path.insert(0,str(P.parent/'mayan_verification_2026_10_09'));from keccak_utils import keccak
S='0x2df1c51e09aecf9cacb7bc98cb1742757f163df7';W='0xd116117e42279dea647d45dd012c67e31e7d1a63';B=512342669
if __name__=='__main__':
 jobs=[('withdrawal_user_ledger','https://api.hyperliquid.xyz/info',{'type':'userNonFundingLedgerUpdates','user':W,'startTime':1791312234000,'endTime':1791315855000}),('withdrawal_user_preceding_ledger','https://api.hyperliquid.xyz/info',{'type':'userNonFundingLedgerUpdates','user':W,'startTime':1791244800000,'endTime':1791315607707}),('bridge_official_source','https://raw.githubusercontent.com/hyperliquid-dex/contracts/master/Bridge2.sol',None),m.rpc('funder_incoming_usdc_logs','eth_getLogs',[{'address':m.T,'fromBlock':hex(m.B-100000),'toBlock':hex(m.B),'topics':['0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef',None,'0x'+m.U[2:].rjust(64,'0')]}]),m.rpc('withdrawal_requested_logs','eth_getLogs',[{'address':S,'fromBlock':hex(B-4000),'toBlock':hex(B),'topics':['0x'+keccak(b'RequestedWithdrawal(address,address,uint64,uint64,bytes32,uint64)'),'0x'+W[2:].rjust(64,'0')]}])]
 with concurrent.futures.ThreadPoolExecutor(max_workers=4) as ex:list(ex.map(lambda j:m.c.get(*j),jobs))
 # Exact previously discovered request transaction, no event fan-out.
 H='0x1494cd99d97619fed4b08d5a551e4162a2623aaecea5ac98c404c9f8b9cfbf12';RB=512341880
 jobs=[m.rpc('withdrawal_request_tx','eth_getTransactionByHash',[H]),m.rpc('withdrawal_request_receipt','eth_getTransactionReceipt',[H]),m.rpc('withdrawal_request_block','eth_getBlockByNumber',[hex(RB),False])]
 with concurrent.futures.ThreadPoolExecutor(max_workers=3) as ex:list(ex.map(lambda j:m.c.get(*j),jobs))
