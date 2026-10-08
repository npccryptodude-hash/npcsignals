"""Preserve narrowly scoped primary RPC evidence; never overwrite responses."""
import concurrent.futures, datetime, json, pathlib, urllib.request
P = pathlib.Path(__file__).parent
RAW = P / 'raw'
RAW.mkdir(exist_ok=True)
RPC = 'https://arb1.arbitrum.io/rpc'
ADDRESS = '0x2df1c51e09aecf9cacb7bc98cb1742757f163df7'
TOKEN = '0xaf88d065e77c8cc2239327c5edb3a432268e5831'
TRANSFER = '0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef'
TOPIC = '0x' + ADDRESS[2:].rjust(64, '0')
def rpc(label, method, params):
    target = RAW / (label + '.response.json')
    if target.exists():
        return json.loads(target.read_bytes()).get('result')
    request = {'jsonrpc':'2.0','id':1,'method':method,'params':params}
    metadata = {'url':RPC,'requested_at_UTC':datetime.datetime.now(datetime.timezone.utc).isoformat(),'method':'POST','request':request}
    try:
        req = urllib.request.Request(RPC, data=json.dumps(request).encode(), headers={'Content-Type':'application/json','User-Agent':'NPCsignals research'})
        with urllib.request.urlopen(req,timeout=25) as response:
            body=response.read(); metadata['HTTP_status']=response.status
        target.write_bytes(body)
        metadata['response_file']=target.name
        parsed=json.loads(body)
        if 'error' in parsed: print(label,parsed['error'],flush=True)
        return parsed.get('result')
    except Exception as error:
        metadata['error']=str(error); print(label,str(error),flush=True)
    finally:
        (RAW / (label+'.request.json')).write_text(json.dumps(metadata,indent=2)+'\n')
def main():
    latest=rpc('arb_latest','eth_blockNumber',[])
    if latest is None: return
    end=int(latest,16)
    rpc('arb_chain','eth_chainId',[])
    rpc('collector_usdc_balance','eth_call',[{'to':TOKEN,'data':'0x70a08231'+ADDRESS[2:].rjust(64,'0')},latest])
    rpc('collector_native_balance','eth_getBalance',[ADDRESS,latest])
    rpc('collector_nonce','eth_getTransactionCount',[ADDRESS,latest])
    jobs=[]
    for start in range(512422000,end+1,100000):
        stop=min(start+99999,end)
        for direction,topics in [('out',[TRANSFER,TOPIC]),('in',[TRANSFER,None,TOPIC])]:
            jobs.append((f'collector_{direction}_{start}_{stop}','eth_getLogs',[{'address':TOKEN,'fromBlock':hex(start),'toBlock':hex(stop),'topics':topics}]))
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
        lists=list(executor.map(lambda job:rpc(*job),jobs))
    logs={ (x['transactionHash'],x['logIndex']):x for result in lists if isinstance(result,list) for x in result }
    print('examined blocks',512422000,end,'unique USDC events',len(logs),flush=True)
    # High-traffic wallets require a scoped sample, not thousands of receipt calls.
    # Reproduce the earliest non-case positive inflow and earliest positive outflow.
    ordered=sorted(logs.values(),key=lambda x:(int(x['blockNumber'],16),int(x['transactionIndex'],16),int(x['logIndex'],16)))
    known={'0xd7efd720adf271b7173dd01a9b81668892bee6b1','0x68d6e20a28f9d50ebf798ccf9fae9e3d5e4f1ac4','0x888795f84f5f81352a7639f1254662ae5897e223','0x4079067aa1bdff060c6c45155966d81c79e754e9','0x68b3a77db46418905c7eaf63324d4adcce06a680','0xd9249de6224382ce7791600d1d1f9e5fdf633abb'}
    incoming=[x for x in ordered if '0x'+x['topics'][2][-40:]==ADDRESS and '0x'+x['topics'][1][-40:] not in known and int(x['data'],16)>0]
    outgoing=[x for x in ordered if '0x'+x['topics'][1][-40:]==ADDRESS and int(x['data'],16)>0]
    selected=incoming[:1]+outgoing[:1]
    detail=[]
    for tx in sorted({x['transactionHash'] for x in selected}):
        detail.extend([(tx+'_tx','eth_getTransactionByHash',[tx]),(tx+'_receipt','eth_getTransactionReceipt',[tx])])
    for block in sorted({x['blockNumber'] for x in selected} | {latest}):
        detail.append(('block_'+block,'eth_getBlockByNumber',[block,False]))
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
        list(executor.map(lambda job:rpc(*job),detail))
if __name__=='__main__': main()
