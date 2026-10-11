"""LGCS-203: finite combinatorial and geometric invariants, Python standard library."""
from itertools import combinations, product
from fractions import Fraction
import unittest


def decode(bits):
    assert len(bits) == 3 and set(bits) <= {'0','1'}
    return sum(int(x) * weight for x, weight in zip(bits, (4,2,1)))


def edges(nodes):
    return frozenset(combinations(nodes, 2))


def determinant3(r1, r2, r3):
    a,b,c = r1; d,e,f = r2; g,h,i = r3
    return a*(e*i-f*h) - b*(d*i-f*g) + c*(d*h-e*g)


def volume6(A, B, C, D):
    subtract = lambda p: tuple(p[k] - A[k] for k in range(3))
    return abs(determinant3(subtract(B), subtract(C), subtract(D)))


class TestLGCS203(unittest.TestCase):
    def test_01_all_eight_states_decode(self):
        self.assertEqual([decode(format(n, '03b')) for n in range(8)], list(range(8)))

    def test_02_eight_port_counts(self):
        self.assertEqual([decode(format(n,'03b'))+1 for n in range(8)],list(range(1,9)))

    def test_03_pair_counts(self):
        self.assertEqual([len(edges(range(n+1))) for n in range(8)], [0,1,3,6,10,15,21,28])

    def test_04_formula_all_states(self):
        for n in range(8):
            P=n+1
            self.assertEqual(len(edges(range(P))), P*(P-1)//2)

    def test_05_011_maps_to_four(self):
        self.assertEqual(decode('011')+1,4)

    def test_06_six_unique_pairs(self):
        self.assertEqual(edges('ABCD'), frozenset({('A','B'),('A','C'),('A','D'),('B','C'),('B','D'),('C','D')}))

    def test_07_coplanar_k4_zero_volume(self):
        A,B,C,D=(0,0,0),(1,0,0),(0,1,0),(1,1,0)
        self.assertEqual(len(edges('ABCD')),6)
        self.assertEqual(volume6(A,B,C,D),0)

    def test_08_noncoplanar_k4_nonzero_volume(self):
        A,B,C,D=(0,0,0),(1,0,0),(0,1,0),(0,0,1)
        self.assertEqual(len(edges('ABCD')),6)
        self.assertEqual(volume6(A,B,C,D),1)

    def test_09_same_graph_different_geometry(self):
        A,B,C=(0,0,0),(1,0,0),(0,1,0)
        self.assertNotEqual(volume6(A,B,C,(1,1,0)),volume6(A,B,C,(0,0,1)))

    def test_10_star_tetra_two_k4_edges(self):
        cube=list(product((-1,1), repeat=3))
        groups=[tuple(pt for pt in cube if (sum(v==-1 for v in pt)%2)==parity) for parity in (0,1)]
        self.assertEqual([len(group) for group in groups],[4,4])
        e0=edges(range(4))
        e1=edges(range(4,8))
        self.assertEqual(len(e0 | e1),12)
        self.assertEqual(len(edges(range(8))),28)
        self.assertEqual(len(edges(range(8))-(e0|e1)),16)
        for group in groups:
            self.assertNotEqual(volume6(*group),0)

    def test_11_simplex_dimension_definition(self):
        # 5 affinely independent points in R^4: zero vector and 4 basis vectors.
        points=[(0,0,0,0)] + [tuple(1 if i==j else 0 for i in range(4)) for j in range(4)]
        self.assertEqual(len(points),5)
        self.assertEqual([tuple(p[k]-points[0][k] for k in range(4)) for p in points[1:]],points[1:])
        self.assertEqual(len(edges(range(5))),10)

    def test_12_three_bits_are_not_and(self):
        self.assertEqual(decode('011'),3)
        self.assertEqual(0 & 1 & 1,0)

    def test_13_cross_is_star_not_k4_by_default(self):
        cross=frozenset({('H','A'),('H','B'),('H','C'),('H','D')})
        self.assertEqual(len(cross),4)
        self.assertEqual(len(edges('ABCD')),6)
        self.assertNotEqual(cross,edges('ABCD'))

    def test_14_bit_boolean_tetrahedron_boolean_volume(self):
        for a,b,c in product((0,1),repeat=3):
            sixV=volume6((0,0,0),(a,0,0),(0,b,0),(0,0,c))
            self.assertEqual(sixV,a*b*c)
            self.assertEqual(bool(sixV), bool(a and b and c))


if __name__ == '__main__':
    unittest.main(verbosity=2)
