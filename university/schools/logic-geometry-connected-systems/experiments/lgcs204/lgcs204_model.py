"""LGCS-204: defined mathematical models, not extracted image geometry.

Pure Python standard library. Original REIK/TCGE kernel is not imported or modified.
A vertex/edge graph never by itself verifies a physical process or knowledge claim.
"""
from collections import deque
from fractions import Fraction
from itertools import combinations, product
from math import ceil, log2

HEX = ((2,0),(1,1),(-1,1),(-2,0),(-1,-1),(1,-1))
DOMAINS = ("A", "B", "C", "D")
HUB = "H"


def decode(bits):
    if len(bits) != 3 or set(bits) - {"0","1"}:
        raise ValueError("requires exactly three binary characters")
    return sum(int(bit)*weight for bit,weight in zip(bits,(4,2,1)))


def port_count(bits):
    return decode(bits) + 1   # selected encoding convention, NOT a physical law


def all_pairs(nodes):
    return frozenset(frozenset(pair) for pair in combinations(nodes,2))


def star_edges():
    return frozenset(frozenset((HUB, domain)) for domain in DOMAINS)


def domain_clique():
    return all_pairs(DOMAINS)


def combined_edges():
    return star_edges() | domain_clique()


def neighbors(nodes, edges):
    nodes=set(nodes)
    return {n: {next(iter(e-{n})) for e in edges if n in e and e <= nodes} for n in nodes}


def components(nodes,edges):
    nodes=set(nodes)
    adj=neighbors(nodes,edges)
    found=[]
    while nodes:
        start=nodes.pop();seen={start};todo=[start]
        while todo:
            for nxt in adj[todo.pop()]:
                if nxt not in seen:
                    seen.add(nxt);todo.append(nxt)
        found.append(frozenset(seen));nodes-=seen
    return found


def triangles(nodes,edges):
    return sum(1 for triple in combinations(nodes,3) if all(frozenset(e) in edges for e in combinations(triple,2)))


def diameter(nodes,edges):
    adj=neighbors(nodes,edges)
    longest=0
    for v in nodes:
        seen={v};queue=deque([(v,0)])
        while queue:
            here,d=queue.popleft();longest=max(longest,d)
            for dest in adj[here]:
                if dest not in seen:
                    seen.add(dest);queue.append((dest,d+1))
        if len(seen)!=len(nodes):
            return None
    return longest


def nodes13():
    # Euclidean coordinate for encoded (x2,y2) is (x2/2, sqrt(3)*y2/2).
    # This *defined* idealized layout is not claimed to be extracted from a JPEG.
    nodes={"O":(0,0)}
    for prefix,r in (("I",1),("J",2)):
        for i,(x,y) in enumerate(HEX):
            nodes[f"{prefix}{i}"]=(r*x,r*y)
    return nodes


def model13_edges():
    es=set()
    for k in range(6):
        nxt=(k+1)%6
        for a,b in (("O",f"I{k}"),(f"I{k}",f"I{nxt}"),(f"J{k}",f"J{nxt}"),(f"I{k}",f"J{k}")):
            es.add(frozenset((a,b)))
    return frozenset(es)


def squared_length(p,q):
    dx=p[0]-q[0];dy=p[1]-q[1]
    return Fraction(dx*dx+3*dy*dy,4)


def rotate_label(node,steps):
    if node=="O":return "O"
    return node[0]+str((int(node[1:])+steps)%6)


def reflect_label(node):
    if node=="O":return "O"
    return node[0]+str((-int(node[1:]))%6)


def transform_edges(edges,transform):
    return frozenset(frozenset(map(transform,e)) for e in edges)


def volume6(a,b,c,d):
    p=[tuple(b[k]-a[k] for k in range(3)),tuple(c[k]-a[k] for k in range(3)),tuple(d[k]-a[k] for k in range(3))]
    (u,v,w),(x,y,z),(j,k,l)=p
    return abs(u*(y*l-z*k)-v*(x*l-z*j)+w*(x*k-y*j))


def star_tetra_edges():
    cube=list(product((-1,1),repeat=3))
    parity={n:sum(x==-1 for x in xyz)%2 for n,xyz in enumerate(cube)}
    e=frozenset(frozenset((a,b)) for a,b in combinations(range(8),2) if parity[a]==parity[b])
    return cube,parity,e
