from collect_followup import get
if __name__=='__main__':
    for label,url in [('wagyu_native_bridge','https://docs.wagyu.xyz/native-bridge'),('wagyu_authentication','https://docs.wagyu.xyz/authentication'),('wagyu_money','https://docs.wagyu.xyz/money-and-settlement'),('wagyu_monero','https://wagyu.xyz/monero')]:get(label,url)
    get('wagyu_openapi','https://api-beta.wagyu.xyz/v2/docs')
    get('wagyu_bridge_terms','https://api-beta.wagyu.xyz/v2/bridges/terms')
