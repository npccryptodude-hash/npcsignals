from collect import *
import concurrent.futures
HASHES=['0x19711cef0ce78f5743fececf0ef0c141aca256b212e593b330314f416a461b80','0x90d15c162609522d1229818adfe352d48270db57050e7179a0c0d779a6c1fc0e','0xe1552e4f3b520a25b7ff28ed89217385b2d8ee6578dda952da50197905d2bd7c','0x3793d029d0e319546fcd685e0ffae566b09fe5956c779831470bb616cd1a0791','0xc3d89645282862feb0d71628146a4d07aa52b8c98343f25451f32580da22cfa4','0xa5a9034013bae44c7975a4457adec4fc709192c51b1dc92712e9a3a50a442f1a','0xd7bdc7b4a407d6b49e12c1b911f3f63e90702893b454901334822eca7fe00068','0x03169b589e724c00e958e059800fe1201e4e88bf11c2edcd8c0fdda971ca457f','0x6b5d703fa55f105b6c169bdd18349ba47664425c8be6e19e8d4fb2c4850ff909','0x178957dc5339430fef6c8e460f54722968b59d06dcc899d1ca1cfdf5bedd19ae']
if __name__=='__main__':
 with concurrent.futures.ThreadPoolExecutor(max_workers=2) as ex:
  for r,t,b in ex.map(tx,HASHES):print(t['hash'],t['from'],t['to'],int(t['value'],16),flush=True)
 for a,n in [('0x4b304741599c125a244e498d14562487d7109ab8','E1'),(B,'B')]:
  for block in [26184449,26185250]:
   print(n,block,rpc('eth_getBalance',[a,hex(block)],f'native_{n}_{block}'),flush=True)
