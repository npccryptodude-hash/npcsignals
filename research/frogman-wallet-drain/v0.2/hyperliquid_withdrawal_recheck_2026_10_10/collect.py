"""Withdrawal-only recheck since prior cutoff; no account/fill continuation."""
import importlib.util,json,pathlib,time
P=pathlib.Path(__file__).parent;s=importlib.util.spec_from_file_location('hc',P.parent/'hyperliquid_matched_account_2026_10_10/collect.py');c=importlib.util.module_from_spec(s);s.loader.exec_module(c);c.A=P/'access';c.A.mkdir(exist_ok=True)
if __name__=='__main__':
 scope={'user':'0x3e2d81f7a5659e4760ba929ef88eed40ef6640a1','previous_cutoff_ms':1791624537690,'startTime':1791624537691,'endTime':int(time.time()*1000)};(P/'withdrawal_recheck_scope.json').write_text(json.dumps(scope,indent=2)+'\n')
 c.get('hyperliquid_new_ledger','https://api.hyperliquid.xyz/info',{'type':'userNonFundingLedgerUpdates','user':scope['user'],'startTime':scope['startTime'],'endTime':scope['endTime']})
