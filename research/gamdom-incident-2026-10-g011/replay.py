"""Replay one preserved read-only request into a new output directory."""
import argparse,pathlib,json
from analyse import records
import collect
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--record',required=True);p.add_argument('--output',required=True);a=p.parse_args()
 o=records()[a.record];q=o['request']
 assert q['method'] in ['eth_chainId','eth_call','eth_getLogs','eth_getTransactionCount','eth_getCode','eth_getTransactionByHash','eth_getTransactionReceipt','eth_getBlockByNumber']
 collect.E=pathlib.Path(a.output);collect.E.mkdir(parents=True,exist_ok=True)
 print(json.dumps(collect.rpc(o['endpoint'],q['method'],q['params'],a.record),indent=2))
