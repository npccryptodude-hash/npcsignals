from collect_collector import rpc,ADDRESS,TOKEN
if __name__=='__main__':
    start=hex(512421999)
    rpc('collector_opening_usdc_balance','eth_call',[{'to':TOKEN,'data':'0x70a08231'+ADDRESS[2:].rjust(64,'0')},start])
    rpc('collector_code','eth_getCode',[ADDRESS,'0x1e91f292'])
    rpc('opening_block','eth_getBlockByNumber',[start,False])
