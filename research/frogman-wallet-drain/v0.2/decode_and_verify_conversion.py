"""Decode Solana wire signers and verify Ed25519 signatures with OpenSSL."""
import pathlib,json,base64,subprocess,tempfile
P=pathlib.Path(__file__).parent/'raw_sources'
j=json.loads((P/'conversion_base64.response.json').read_text())['result'];wire=base64.b64decode(j['transaction'][0]);pos=0
ALPHABET='123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'
def shortvec():
 global pos
 n=shift=0
 while True:
  b=wire[pos];pos+=1;n|=(b&127)<<shift
  if b<128:return n
  shift+=7
  if shift>28:raise ValueError('Invalid shortvec')
def base58(v):
 n=int.from_bytes(v,'big');s=''
 while n:n,r=divmod(n,58);s=ALPHABET[r]+s
 return '1'*(len(v)-len(v.lstrip(b'\0')))+s
count=shortvec();signatures=[wire[pos+64*i:pos+64*(i+1)] for i in range(count)];pos+=64*count;message=wire[pos:]
if wire[pos]&128:pos+=1
header=list(wire[pos:pos+3]);pos+=3;keycount=shortvec();keys=[wire[pos+32*i:pos+32*(i+1)] for i in range(keycount)];pos+=32*keycount
assert header[0]==count
results=[]
with tempfile.TemporaryDirectory() as d:
 d=pathlib.Path(d);(d/'message').write_bytes(message)
 for i in range(count):
  (d/'key.der').write_bytes(bytes.fromhex('302a300506032b6570032100')+keys[i]);(d/'signature').write_bytes(signatures[i])
  r=subprocess.run(['openssl','pkeyutl','-verify','-rawin','-pubin','-keyform','DER','-inkey',str(d/'key.der'),'-sigfile',str(d/'signature'),'-in',str(d/'message')],capture_output=True,text=True)
  results.append({'signer':base58(keys[i]),'verified':r.returncode==0,'output':r.stdout.strip(),'error':r.stderr.strip()})
(P/'conversion_wire_decoded.json').write_text(json.dumps({'wire_signature_count':count,'wire_header':header,'static_account_count':keycount,'wire_signers':[base58(x) for x in keys[:count]],'wire_static_keys':[base58(x) for x in keys]},indent=2)+'\n')
(P/'conversion_signature_verification.json').write_text(json.dumps(results,indent=2)+'\n')
assert all(x['verified'] for x in results)
print(json.dumps(results,indent=2))
