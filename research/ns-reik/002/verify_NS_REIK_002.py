#!/usr/bin/env python3
"""Independent local replay for NS-REIK-002. Does not assert global mathematical truth."""
from pathlib import Path
import sys,json,hashlib,zipfile
BASE=Path(__file__).resolve().parent

def canonical(x):return json.dumps(x,sort_keys=True,ensure_ascii=False,separators=(',',':')).encode('utf-8')
def dig(b):return hashlib.sha256(b).hexdigest()

def check():
    m=json.loads((BASE/'NS_REIK_TCGE_Manifest_002.json').read_bytes())
    assert m['schema']=='NS-REIK-002-MANIFEST-v1'
    for name,h in m['local_file_sha256'].items():
        p=BASE/name;assert p.is_file(),f'MISSING {name}'
        actual=dig(p.read_bytes());assert actual==h,f'HASH MISMATCH {name} {actual}'
        print('FILE PASS',name,actual)
    parent=BASE/m['parent']['zip_filename']
    assert dig(parent.read_bytes())==m['parent']['zip_sha256']
    with zipfile.ZipFile(parent) as z:
        pm_bytes=z.read('NS_REIK_TCGE_Manifest_001.json');pm=json.loads(pm_bytes)
        assert dig(pm_bytes)==m['parent']['manifest_sha256']
        for name,expected in pm['local_file_sha256'].items():
            assert dig(z.read(name))==expected,name
        prior=bytes.fromhex(pm['local_genesis_sha256'])
        for row in pm['receipts']:
            rh=dig(canonical(row['event']))
            assert rh==row['event_digest_sha256']
            prior=hashlib.sha256(prior+bytes.fromhex(rh)).digest()
            assert prior.hex()==row['chain_tip_sha256']
        assert prior.hex()==pm['local_receipt_tip_sha256']==m['parent']['receipt_tip_sha256']
        assert len(pm['receipts'])==3
    print('PARENT PASS: five files, three receipts, chronological tip')
    prev=prior
    for offset,row in enumerate(m['receipts'],start=4):
        assert row['index']==offset
        hh=dig(canonical(row['event']))
        assert hh==row['event_digest_sha256'],f'EVENT {offset}'
        prev=hashlib.sha256(prev+bytes.fromhex(hh)).digest()
        assert prev.hex()==row['chain_tip_sha256'],f'LINK {offset}'
        print('RECEIPT PASS',offset,prev.hex())
    assert prev.hex()==m['local_receipt_tip_sha256']
    test=json.loads((BASE/'enstrophy_test_result.json').read_bytes())
    assert test['exact_normalized_averages']=={'stretching_S':'1','enstrophy_E':'22','dissipation_D':'49'}
    assert test['negative_controls']['false_bound_S_le_D_at_nu1']=='FALSIFIED'
    assert m['proof_gate']=='HOLD'
    assert m['source_pdf_exact_sha256']=='NOT_ACQUIRED'
    print('PASS within local scope; independent Lean build and manuscript PDF hashing remain HOLD')
    return 0
if __name__=='__main__':
    try:sys.exit(check())
    except Exception as e:print('FAIL',repr(e),file=sys.stderr);sys.exit(1)
