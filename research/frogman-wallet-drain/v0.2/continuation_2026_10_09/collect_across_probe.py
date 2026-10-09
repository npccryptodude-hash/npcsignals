from collect_followup import get
if __name__=='__main__':
    get('across_indexer_docs','https://docs.across.to/guides/migration/non-evm/indexers')
    get('across_interface_source','https://raw.githubusercontent.com/across-protocol/contracts/master/contracts/interfaces/V3SpokePoolInterface.sol')
    get('base_chain_id','https://mainnet.base.org',{'jsonrpc':'2.0','id':1,'method':'eth_chainId','params':[]})
    # Status is a lookup hint, not source-deposit reproduction.
    get('across_deposit_status_hint','https://app.across.to/api/deposit/status?originChainId=8453&depositId=6301830')
