import pathlib,sys
sys.path.insert(0,str(pathlib.Path(__file__).parent.parent/'robinhood_funding_direct_2026_10_09'));import collect as c
c.R=pathlib.Path(__file__).parent/'access';c.RPC='https://eth.drpc.org'
c.collect(c.rpc('routing_pre_initial_balance','eth_getBalance',['0x427c4b37de0714821b09c4fc655a713abbcfba83',hex(26135681)]))
