import urllib.request,json,pathlib,concurrent.futures,datetime
P=pathlib.Path(__file__).parent/'raw_sources'
jobs=[('mint_zes','https://api.mainnet-beta.solana.com','getAccountInfo',['ZesMGYmokFiEuDvNzWeMhB7jxF6eUW8c512vwSKSTNK',{'encoding':'jsonParsed','commitment':'finalized'}]),('usdc_account','https://api.mainnet-beta.solana.com','getAccountInfo',['HMnB7bHSFLfo2k4GdGQ2c6inb6eLt3Wpx8SbXgzwnaU2',{'encoding':'jsonParsed','commitment':'finalized'}]),('conversion_program','https://api.mainnet-beta.solana.com','getAccountInfo',['61DFfeTKM7trxYcPQCM78bJ794ddZprZpAwAnLiwTpYH',{'encoding':'jsonParsed','commitment':'finalized'}]),('grr_history','https://api.mainnet-beta.solana.com','getSignaturesForAddress',['Grr9WnZdcetQywtFXog81UhqmnJyvFhb4AT3ipw44mZP',{'limit':1000,'commitment':'finalized'}])]
for key,u in [('eth_llama','https://eth.llamarpc.com'),('eth_publicnode','https://ethereum-rpc.publicnode.com'),('eth_cloudflare','https://cloudflare-eth.com'),('rh_rpc','https://rpc.mainnet.chain.robinhood.com'),('bsc_rpc','https://bsc-dataseed.binance.org'),('arb_rpc','https://arb1.arbitrum.io/rpc')]:jobs.append((key,u,'eth_getTransactionCount',['0x427C4b37de0714821B09C4FC655a713AbbCfbA83','latest']))
def fetch(job):
 key,url,method,params=job;req={'jsonrpc':'2.0','id':1,'method':method,'params':params};rec={'requested_at_UTC':datetime.datetime.now(datetime.timezone.utc).isoformat(),'url':url,'request':req}
 try:
  r=urllib.request.urlopen(urllib.request.Request(url,data=json.dumps(req).encode(),headers={'Content-Type':'application/json'}),timeout=12);raw=r.read();(P/(key+'.response.json')).write_bytes(raw);rec['status']=r.status;rec['response_file']=key+'.response.json';print(key,raw[:350].decode())
 except Exception as e:rec['error']=str(e);print(key,str(e))
 (P/(key+'.request.json')).write_text(json.dumps(rec,indent=2)+'\n')
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as ex:list(ex.map(fetch,jobs))
