import concurrent.futures
from collect import collect
host='https://robinhoodchain.blockscout.com'
jobs=[('network_docs','https://docs.robinhood.com/chain/connecting/',None)]
for label,addr in [('direct','0x427c4b37de0714821b09c4fc655a713abbcfba83'),('outer','0x07ae8551be970cb1cca11dd7a11f47ae82e70e67'),('router','0x998d7c178a1f9607b47ea3a8e22426451b3ce707')]:
    for tail in ['','/transactions','/internal-transactions']:
        jobs.append((label+'_canonical_'+(tail.strip('/') or 'metadata'),host+'/api/v2/addresses/'+addr+tail,None))
    jobs.append((label+'_canonical_contract',host+'/api/v2/smart-contracts/'+addr,None))
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as e:list(e.map(collect,jobs))
