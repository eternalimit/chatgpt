"""Validate the NS-REIK-001 local file hashes and chronological receipt chain.

Usage: python verify_NS_REIK_001.py [directory_containing_manifest]
A PASS establishes only local integrity of files available to this command.
"""
from pathlib import Path
import json,hashlib,sys
base=Path(sys.argv[1]).resolve() if len(sys.argv)>1 else Path(__file__).resolve().parent
m=json.loads((base/'NS_REIK_TCGE_Manifest_001.json').read_text(encoding='utf-8'))

def digest(b):return hashlib.sha256(b).hexdigest()
def canonical(e):return json.dumps(e,sort_keys=True,ensure_ascii=False,separators=(',',':')).encode('utf-8')

for filename,expected in m['local_file_sha256'].items():
    path=base/filename
    assert path.is_file(), f'MISSING FILE: {filename}'
    actual=digest(path.read_bytes())
    assert actual==expected, f'FILE MISMATCH: {filename}: {actual}'
    print('FILE PASS',filename,actual)
prior=bytes(32)
for ix,item in enumerate(m['receipts'],start=1):
    event=item['event']; r=digest(canonical(event)); h=digest(prior+bytes.fromhex(r))
    assert item['index']==ix and item['event_digest_sha256']==r and item['chain_tip_sha256']==h, f'RECEIPT MISMATCH {ix}'
    print('RECEIPT PASS',ix,h)
    prior=bytes.fromhex(h)
assert m['local_receipt_tip_sha256']==prior.hex(), 'TIP MISMATCH'
assert m['verified_external_lineage'] is False,'EXTERNAL LINEAGE MISREPRESENTED'
assert m['universal_navier_stokes_proof']=='HOLD','UNSUPPORTED CLAIM UPGRADE'
print('PASS: locally reproducible integrity checks; external lineage, mathematical proof and independent Echo remain HOLD.')
