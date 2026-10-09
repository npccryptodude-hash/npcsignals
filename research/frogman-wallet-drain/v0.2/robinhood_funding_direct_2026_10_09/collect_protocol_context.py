import concurrent.futures,json
from collect import collect,rpc,P,R
jobs=[rpc('snapshot_block','eth_getBlockByNumber',['latest',False])]
contracts=[('across_origin_settler','0x998d7c178a1f9607b47ea3a8e22426451b3ce707'),('swap_settler','0x40132e775e14ef3a946fa5624468715456fa0be4'),('pool_manager','0x8366a39cc670b4001a1121b8f6a443a643e40951')]
for label,addr in contracts:
    jobs.append((label+'_eth_metadata','https://eth.blockscout.com/api/v2/smart-contracts/'+addr,None))
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as e:list(e.map(collect,jobs))
b=json.loads((R/'snapshot_block.response.txt').read_text())['result']['number'];jobs=[]
for label,addr in contracts+ [('direct','0x427c4b37de0714821b09c4fc655a713abbcfba83'),('outer','0x07ae8551be970cb1cca11dd7a11f47ae82e70e67')]:jobs.append(rpc(label+'_snapshot_code','eth_getCode',[addr,b]))
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as e:list(e.map(collect,jobs))
