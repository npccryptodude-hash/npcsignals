"""Read-only first-party exact-order lookup; explorer label secondary."""
import concurrent.futures,importlib.util,pathlib
P=pathlib.Path(__file__).parent;s=importlib.util.spec_from_file_location('sc',P/'collect.py');m=importlib.util.module_from_spec(s);s.loader.exec_module(m)
if __name__=='__main__':
 jobs=[('relay_case_hash','https://api.relay.link/requests/v2?hash='+m.H,None),('relay_case_order','https://api.relay.link/requests/v2?orderId=0xc1599f96e04748f16542c86be2172c77f468d4ae1bb98979ab1d76f5fa27d05f',None),('relay_api_documentation','https://docs.relay.link/references/api/get-requests-v2.md',None),('explorer_label','https://etherscan.io/address/'+m.U,None)]
 with concurrent.futures.ThreadPoolExecutor(max_workers=4) as e:list(e.map(lambda j:m.c.get(*j),jobs))
