import pathlib,sys
sys.path.insert(0,str(pathlib.Path(__file__).parent.parent/'robinhood_funding_direct_2026_10_09'));import collect as c
c.R=pathlib.Path(__file__).parent/'access'
c.collect(('lifi_primary_docs','https://docs.li.fi/agents/reference/endpoint-specs',None))
c.collect(('router_lifi_status','https://li.quest/v1/status?txHash=0xefa46658dead085751916c1368ed2590d72fa34dce36abf5c6b5a8cbcfc0d624&fromChain=1',None))
