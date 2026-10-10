"""Bounded read-only check of the existing common funding source; no recipient fan-out."""
import concurrent.futures,importlib.util,pathlib,json
P=pathlib.Path(__file__).parent
s=importlib.util.spec_from_file_location('hc',P.parent/'hyperliquid_matched_account_2026_10_10/collect.py');c=importlib.util.module_from_spec(s);s.loader.exec_module(c);c.A=P/'access';c.A.mkdir(exist_ok=True)
U='0xae06669dfd3e932476f00ea49fce82e5e63f83bf';START=26130000;END=26137480
if __name__=='__main__':
 jobs=[('ordinary_history',f'https://eth.blockscout.com/api?module=account&action=txlist&address={U}&startblock={START}&endblock={END}&sort=asc&page=1&offset=1000',None),('internal_history',f'https://eth.blockscout.com/api?module=account&action=txlistinternal&address={U}&startblock={START}&endblock={END}&sort=asc&page=1&offset=1000',None),('metadata',f'https://eth.blockscout.com/api/v2/addresses/{U}',None)]
 with concurrent.futures.ThreadPoolExecutor(max_workers=3) as ex:list(ex.map(lambda j:c.get(*j),jobs))
