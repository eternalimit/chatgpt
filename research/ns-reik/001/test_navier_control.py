"""Reproducible symbolic Navier--Stokes control; not a global regularity proof."""
import json
import sympy as sp

x,y,z,t = sp.symbols('x y z t', real=True)
nu = sp.symbols('nu', positive=True)
coords=(x,y,z)

def residual(u):
    div=sp.simplify(sum(sp.diff(u[j],coords[j]) for j in range(3)))
    delta=[sp.simplify(sum(sp.diff(ui, c, 2) for c in coords)) for ui in u]
    adv=[sp.simplify(sum(u[j]*sp.diff(ui,coords[j]) for j in range(3))) for ui in u]
    lhs=[sp.simplify(sp.diff(ui,t)+adv[i]-nu*delta[i]) for i,ui in enumerate(u)]
    return str(div),[str(q) for q in lhs], all(q==0 for q in sp.Matrix(lhs))

u_correct=(sp.exp(-nu*t)*sp.sin(y),sp.Integer(0),sp.Integer(0))
u_bad=(sp.sin(y),sp.Integer(0),sp.Integer(0))
correct_div,correct_res,correct_pass=residual(u_correct)
bad_div,bad_res,bad_pass=residual(u_bad)
output={
 'test_id':'NS-REIK-CONTROL-001', 'sympy_version':sp.__version__,
 'domain':'periodic 3D torus (2*pi periodic coordinates); viscosity nu > 0; p=0; f=0',
 'correct_solution':'(exp(-nu*t)*sin(y), 0, 0)',
 'correct_divergence':correct_div,'correct_residual':correct_res,
 'correct_pass':bool(correct_pass and correct_div=='0'),
 'negative_control':'(sin(y), 0, 0)',
 'negative_divergence':bad_div,'negative_residual':bad_res,
 'negative_control_detected':bool((not bad_pass) and bad_div=='0'),
 'scope':'single exact special solution and single deliberately incorrect candidate; not a universal theorem'
}
with open('/mnt/data/navier_tcge_20261009/output/ns_symbolic_test.json','w',encoding='utf-8') as f:
    json.dump(output,f,indent=2,sort_keys=True,ensure_ascii=False);f.write('\n')
print(json.dumps(output,indent=2))
assert output['correct_pass'] and output['negative_control_detected']
