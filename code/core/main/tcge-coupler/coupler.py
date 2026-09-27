#!/usr/bin/env python3
import argparse, hashlib, json, pathlib, sys

SCHEMA = 'tcge-coupler/v1'

def sha256_bytes(b): return hashlib.sha256(b).hexdigest()
def canonical(obj): return json.dumps(obj, sort_keys=True, separators=(',', ':'), ensure_ascii=False).encode('utf-8')

def load_manifest(path):
    raw = pathlib.Path(path).read_bytes()
    obj = json.loads(raw.decode('utf-8'))
    return obj, sha256_bytes(raw)

def transform(data, spec):
    kind = spec['kind']
    if kind == 'identity': return data
    if kind == 'utf8_upper': return data.decode('utf-8').upper().encode('utf-8')
    if kind == 'utf8_lower': return data.decode('utf-8').lower().encode('utf-8')
    if kind == 'json_canonical': return canonical(json.loads(data.decode('utf-8')))
    raise ValueError(f'unsupported transformer: {kind}')

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('manifest')
    ap.add_argument('--out', default='coupling-receipt.json')
    a=ap.parse_args()
    m, manifest_hash=load_manifest(a.manifest)
    if m.get('schema') != SCHEMA: raise SystemExit('manifest schema mismatch')
    base=pathlib.Path(a.manifest).resolve().parent
    records=[]; all_r=True; any_i=False; all_e=True
    for item in m.get('inclusions', []):
        p=(base/item['path']).resolve(); data=p.read_bytes(); ih=sha256_bytes(data)
        expected=item.get('sha256'); source_ok=(expected is None or expected==ih)
        current=data; steps=[]
        for tid in item.get('transformers', []):
            spec=next((x for x in m['transformers'] if x['id']==tid), None)
            if spec is None: raise SystemExit(f'unknown transformer {tid}')
            before=sha256_bytes(current); current=transform(current,spec); after=sha256_bytes(current)
            steps.append({'transformer_id':tid,'kind':spec['kind'],'input_sha256':before,'output_sha256':after})
        oh=sha256_bytes(current); any_i = any_i or bool(steps)
        echo=item.get('echo', {})
        echo_ok=bool(echo.get('independent')) and echo.get('sha256')==oh
        all_r = all_r and source_ok
        all_e = all_e and echo_ok
        records.append({'id':item['id'],'path':item['path'],'input_sha256':ih,'source_verified':source_ok,'steps':steps,'output_sha256':oh,'echo_verified':echo_ok})
    R=1 if records and all_r else 0
    I=1 if any_i else 0
    E=1 if records and all_e else 0
    K=1 if R and I and E else 0
    H=1 if I and not K else 0
    status='PASS' if K else 'HOLD'
    receipt={'schema':'tcge-coupling-receipt/v1','manifest_sha256':manifest_hash,'records':records,'tcge':{'R':R,'I':I,'E':E,'K':K,'H':H},'gate':status,'rule':'THROUGH(HOLD)!=PASS'}
    pathlib.Path(a.out).write_bytes(canonical(receipt)+b'\n')
    print(json.dumps(receipt, indent=2))
    return 0 if status=='PASS' else 2
if __name__=='__main__': sys.exit(main())
