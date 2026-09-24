from decimal import Decimal, getcontext
import json, hashlib, math
import mpmath as mp

N = 100256
Q = 50128

# A: mpmath library implementation
mp.mp.dps = N + 30
A = str(mp.pi).replace('.', '')[1:N+1]
if len(A) != N:
    raise SystemExit(f'A length {len(A)} != {N}')

# B: independent binary-splitting Chudnovsky implementation
C3_OVER_24 = 10939058860032000

def bs(a,b):
    if b-a == 1:
        if a == 0:
            P = Qv = 1
        else:
            P = (6*a-5)*(2*a-1)*(6*a-1)
            Qv = a*a*a*C3_OVER_24
        T = P*(13591409 + 545140134*a)
        if a & 1:
            T = -T
        return P,Qv,T
    m=(a+b)//2
    P1,Q1,T1=bs(a,m)
    P2,Q2,T2=bs(m,b)
    return P1*P2, Q1*Q2, T1*Q2 + P1*T2

getcontext().prec = N + 40
terms = N//14 + 20
P,Qv,T = bs(0,terms)
pi_b = (Decimal(426880) * Decimal(10005).sqrt() * Decimal(Qv)) / Decimal(T)
B = format(pi_b,'f').replace('.','')[1:N+1]
if len(B) != N:
    raise SystemExit(f'B length {len(B)} != {N}')

first_clean_mismatch = next((i+1 for i,(a,b) in enumerate(zip(A,B)) if a != b), None)
Bprime = list(B)
orig = int(Bprime[Q-1])
Bprime[Q-1] = str((orig+1)%10)
Bprime = ''.join(Bprime)
first_trap_mismatch = next((i+1 for i,(a,b) in enumerate(zip(A,Bprime)) if a != b), None)

result = {
  'experiment':'379999-R2-DYNAMIC',
  'frozen_state':'000',
  'N':N,
  'trap_q':Q,
  'implementation_A':'mpmath pi',
  'implementation_B':'custom binary-splitting Chudnovsky with Decimal',
  'clean_control':{
    'first_mismatch':first_clean_mismatch,
    'status':'COMPLETE' if first_clean_mismatch is None else 'HOLD',
    'last_admitted_position':N if first_clean_mismatch is None else first_clean_mismatch-1
  },
  'injected_error_control':{
    'A_q':A[Q-1],
    'original_B_q':str(orig),
    'mutated_Bprime_q':Bprime[Q-1],
    'first_mismatch':first_trap_mismatch,
    'status':'HOLD' if first_trap_mismatch is not None else 'COMPLETE',
    'last_admitted_position':first_trap_mismatch-1 if first_trap_mismatch is not None else N
  },
  'governance':{
    'physical_validation':False,
    'external_provenance_echo':False,
    'implementation_echo':'two distinct implementations in the same runtime environment',
    'note':'Agreement supports the bounded computational comparison only; it does not establish external provenance or physical validation.'
  }
}

for fn,data in [
 ('first_run_result.json',json.dumps(result,indent=2,sort_keys=True)+'\n'),
 ('first_run_A_digits.txt',A+'\n'),
 ('first_run_B_digits.txt',B+'\n'),
 ('first_run_Bprime_digits.txt',Bprime+'\n')]:
    with open(fn,'w',encoding='utf-8') as f: f.write(data)

for fn in ['runner_379999_r2.py','first_run_result.json','first_run_A_digits.txt','first_run_B_digits.txt','first_run_Bprime_digits.txt']:
    with open(fn,'rb') as f: print(hashlib.sha256(f.read()).hexdigest(), fn)
print(json.dumps(result,indent=2,sort_keys=True))
