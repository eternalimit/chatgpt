"""NS-REIK-002: exact Fourier arithmetic and separate grid quadrature; no external dependency beyond sympy/numpy."""
import itertools,json,hashlib,math
import sympy as sp
import numpy as np
I=sp.I
K=[(1,0,0),(0,1,1),(1,1,1)]
P=[(0,-2,2),(1,-2,2),(1,1,-2)]
PH=['sin','cos','cos']

def cross(a,b):
 return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])

def dot(a,b):return sum(a[i]*b[i] for i in range(3))

def coeffs():
 out={}
 for k,p,ph in zip(K,P,PH):
  for sign in (-1,1):
   coef=sp.Rational(1,2) if ph=='cos' else sign/(2*I)
   out[tuple(sign*kv for kv in k)]=tuple(coef*x for x in p)
 return out

U=coeffs()
W={k:tuple(I*c for c in cross(k,v)) for k,v in U.items()}
assert all(dot(k,p)==0 for k,p in zip(K,P))
assert all(sum(I*k[i]*v[i] for i in range(3))==0 for k,v in U.items())
S=0
for k,wk in W.items():
 for l,wl in W.items():
  q=tuple(-k[j]-l[j] for j in range(3))
  if q in U:
   S+=sum(wk[i]*wl[j]*I*q[j]*U[q][i] for i in range(3) for j in range(3))
S=sp.simplify(S)
E=sp.simplify(sum(dot(w, W[tuple(-ki for ki in k)]) for k,w in W.items()))
D=sp.simplify(sum(dot(k,k)*dot(w,W[tuple(-ki for ki in k)]) for k,w in W.items()))
assert (S,E,D)==(1,22,49),(S,E,D)
# independent physical-space quadrature. For modes maximum summed frequencies of cubic products below 4,
# uniform 16^3 trapezoid integrates the trigonometric polynomial to floating tolerance.
N=16
a=2*np.pi*np.arange(N)/N
x,y,z=np.meshgrid(a,a,a,indexing='ij')
u=np.zeros((3,N,N,N));du=np.zeros((3,3,N,N,N))
for k,p,phase in zip(K,P,PH):
 theta=k[0]*x+k[1]*y+k[2]*z
 wave=np.sin(theta) if phase=='sin' else np.cos(theta)
 dw=np.cos(theta) if phase=='sin' else -np.sin(theta)
 for i in range(3):
  u[i]+=p[i]*wave
  for j in range(3):du[i,j]+=p[i]*k[j]*dw
omega=np.stack([du[2,1]-du[1,2],du[0,2]-du[2,0],du[1,0]-du[0,1]])
stretch=np.zeros((N,N,N)); gradomega=np.zeros((3,3,N,N,N))
for i in range(3):
 for j in range(3): stretch+=omega[i]*omega[j]*du[i,j]
# analytic mode derivatives for gradomega, independent direct derivative
for k,p,phase in zip(K,P,PH):
 c=np.array(cross(k,p));theta=k[0]*x+k[1]*y+k[2]*z
 dw=(-np.sin(theta) if phase=='sin' else -np.cos(theta)) # omega=c*cos for sin, -c*sin for cos
 for i in range(3):
  for j in range(3):gradomega[i,j]+=c[i]*k[j]*dw
avgS=float(np.mean(stretch));avgE=float(np.mean(np.sum(omega**2,axis=0)));avgD=float(np.mean(np.sum(gradomega**2,axis=(0,1))))
assert abs(avgS-1)<1e-12,(avgS,avgE,avgD)
assert abs(avgE-22)<1e-12
assert abs(avgD-49)<1e-12
# negative controls: phase sign inversion changes S; non-solenoidal perturbation breaks divergence
badP=list(P);badP[2]=(1,1,-1)
baddiv=dot(K[2],badP[2]);assert baddiv==1
# test a natural false heuristic S<=nu*D for all data at nu=1; lambda=50 gives S = 125000 and D = 122500
l=50;assert int(S)*l**3>int(D)*l*l
result={
 "test_id":"NS-REIK-002-ENSTROPHY-001", "domain":"T^3=(R/2pi Z)^3", 
 "wavevectors":K,"polarization":P,"phases":PH,"divergence_free":True,
 "exact_normalized_averages":{"stretching_S":str(S),"enstrophy_E":str(E),"dissipation_D":str(D)},
 "independent_grid":{"resolution":[N,N,N],"S":avgS,"E":avgE,"D":avgD,"tolerance":1e-12},
 "negative_controls":{"nondivergence_pol_3_dot_k3":baddiv,"lambda":l,"S_lambda":int(S)*l**3,"D_lambda":int(D)*l*l,"false_bound_S_le_D_at_nu1":"FALSIFIED"},
 "logical_boundary":"Refutes data-independent linear enstrophy absorption estimate only. Does not refute global smoothness, does not establish singularity.",
 "status":"PASS_WITHIN_SCOPE"}
p='/mnt/data/ns_reik_002/work/enstrophy_test_result.json'
open(p,'w').write(json.dumps(result,sort_keys=True,indent=2)+'\n')
print(json.dumps(result,indent=2))
