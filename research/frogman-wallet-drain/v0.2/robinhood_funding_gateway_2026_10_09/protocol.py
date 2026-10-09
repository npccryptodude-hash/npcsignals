"""Pure ABI/Merkle checks against saved Gateway inputs; no signature ownership inference."""
import pathlib,sys
sys.path.insert(0,str(pathlib.Path(__file__).parent.parent/'unlabeled_a3ca_verification_2026_10_09'))
from keccak import keccak
def gateway_path(tx,event):
    data=bytes.fromhex(tx['input'][10:])
    def word(at):return data[at:at+32]
    def num(at):return int.from_bytes(word(at),'big')
    assert tx['input'][:10]=='0x'+keccak(b'execute(bytes32,((uint256,bytes32,bytes32,bytes),bytes32[],bytes),(uint256,bytes)[])')[:8]
    assert '0x'+word(0).hex()==event['topics'][1]
    s=num(32); path=s+num(s); chain=num(path);salt=word(path+32);executor=word(path+64);message=path+num(path+96);size=num(message);msg=data[message+32:message+32+size]
    assert len(msg)==size and chain==4663
    leaf=bytes.fromhex(keccak(word(path)+salt+executor+bytes.fromhex(keccak(msg))))
    assert '0x'+leaf.hex()==event['topics'][2]
    at=s+num(s+32);length=num(at);proof=[word(at+32+32*i) for i in range(length)];root=leaf
    for sibling in proof:root=bytes.fromhex(keccak(min(root,sibling)+max(root,sibling)))
    assert root==word(0)
    return {'step_id':event['topics'][1],'path_id':event['topics'][2],'chain_id':chain,'executor':'0x'+executor[-20:].hex(),'path_message_hex':'0x'+msg.hex(),'path_proof':['0x'+x.hex() for x in proof],'independent_merkle_check':'PASS'}
