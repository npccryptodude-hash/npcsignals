import collect_collector as c
if __name__=='__main__':
    c.RPC='https://rpc.mainnet.chain.robinhood.com'
    h='0x44a5ad893f64a338d607045068dc02e59ddea4e0d6d64ef186b72f0e3e861bc7'
    c.rpc('rh_first_cashcat_trace','trace_transaction',[h])
    c.rpc('rh_first_cashcat_debug','debug_traceTransaction',[h,{'tracer':'callTracer'}])
