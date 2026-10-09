import concurrent.futures,json
from collect import collect,rpc,R
jobs=[('metamask_deployments','https://raw.githubusercontent.com/MetaMask/delegation-framework/v1.3.0/documents/Deployments.md',None),('eip7702_spec','https://eips.ethereum.org/EIPS/eip-7702',None),rpc('first_cashcat_receipt','eth_getTransactionReceipt',['0x44a5ad893f64a338d607045068dc02e59ddea4e0d6d64ef186b72f0e3e861bc7']),('gateway_implementation','https://eth.blockscout.com/api/v2/smart-contracts/0xd9e79b648e42b660d9943a2861aa5d0e4d5cdd3e',None)]
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as e:list(e.map(collect,jobs))
t=json.loads((R/'first_cashcat_tx.response.txt').read_text())['result'];collect(rpc('first_cashcat_block','eth_getBlockByNumber',[t['blockNumber'],False]))
