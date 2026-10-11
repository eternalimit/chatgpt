"""Exhaustive and adversarial finite checks for LGCS-204 mathematical models."""
import unittest
from itertools import product
from math import comb
from lgcs204_model import *

class LGCS204Tests(unittest.TestCase):
    def test_01_decode_all(self):self.assertEqual([decode(f'{n:03b}') for n in range(8)],list(range(8)))
    def test_02_port_map(self):self.assertEqual([port_count(f'{n:03b}') for n in range(8)],list(range(1,9)))
    def test_03_graph_edge_counts_all(self):self.assertEqual([len(all_pairs(range(p))) for p in range(1,9)],[0,1,3,6,10,15,21,28])
    def test_04_bad_binary_rejected(self):
        for s in ('','1','01','012','aaa','1011'):
            with self.assertRaises(ValueError):decode(s)
    def test_05_011_four_points(self):self.assertEqual(port_count('011'),4)
    def test_06_k4_six_pairs(self):self.assertEqual(len(domain_clique()),6)
    def test_07_four_spoke_star_edges(self):self.assertEqual(len(star_edges()),4)
    def test_08_union_ten_edges(self):self.assertEqual(len(combined_edges()),10)
    def test_09_star_degrees(self):self.assertEqual({k:len(v) for k,v in neighbors(DOMAINS+(HUB,),star_edges()).items()},{'A':1,'B':1,'C':1,'D':1,'H':4})
    def test_10_clique_degrees(self):self.assertEqual({k:len(v) for k,v in neighbors(DOMAINS,domain_clique()).items()},{'A':3,'B':3,'C':3,'D':3})
    def test_11_star_hub_cut_vertex(self):self.assertEqual(len(components(DOMAINS,star_edges())),4)
    def test_12_clique_survives_hub_loss(self):self.assertEqual(len(components(DOMAINS,combined_edges())),1)
    def test_13_star_triangle_zero(self):self.assertEqual(triangles(DOMAINS+(HUB,),star_edges()),0)
    def test_14_clique_triangle_four(self):self.assertEqual(triangles(DOMAINS,domain_clique()),4)
    def test_15_combined_graph_ten_triangles(self):self.assertEqual(triangles(DOMAINS+(HUB,),combined_edges()),10)
    def test_16_diameter_star_two(self):self.assertEqual(diameter(DOMAINS+(HUB,),star_edges()),2)
    def test_17_diameter_k4_one(self):self.assertEqual(diameter(DOMAINS,domain_clique()),1)
    def test_18_diameter_union_one(self):self.assertEqual(diameter(DOMAINS+(HUB,),combined_edges()),1)
    def test_19_e_witness_not_implied(self):self.assertNotIn('E',set().union(*combined_edges()))
    def test_20_k4_planar_volume_zero(self):self.assertEqual(volume6((0,0,0),(1,0,0),(0,1,0),(1,1,0)),0)
    def test_21_k4_tetra_volume_nonzero(self):self.assertEqual(volume6((0,0,0),(1,0,0),(0,1,0),(0,0,1)),1)
    def test_22_13_distinct_nodes(self):self.assertEqual(len(set(nodes13().values())),13)
    def test_23_13_radii(self):
        n=nodes13()
        self.assertEqual([squared_length(n['O'],n[f'I{k}']) for k in range(6)],[1]*6)
        self.assertEqual([squared_length(n['O'],n[f'J{k}']) for k in range(6)],[4]*6)
    def test_24_13_ring_edges(self):self.assertEqual(len(model13_edges()),24)
    def test_25_13_degree_distribution(self):
        n=neighbors(nodes13(),model13_edges())
        self.assertEqual(len(n['O']),6)
        self.assertEqual([len(n[f'I{k}']) for k in range(6)],[4]*6)
        self.assertEqual([len(n[f'J{k}']) for k in range(6)],[3]*6)
    def test_26_handshake_13(self):self.assertEqual(sum(len(v) for v in neighbors(nodes13(),model13_edges()).values()),48)
    def test_27_13_connected(self):self.assertEqual(len(components(nodes13(),model13_edges())),1)
    def test_28_13_ring_survives_origin_removal(self):
        remain=set(nodes13())-{'O'}
        e=frozenset(x for x in model13_edges() if 'O' not in x)
        self.assertEqual(len(components(remain,e)),1)
    def test_29_13_six_rotation_automorphisms(self):
        edges=model13_edges()
        for r in range(6):self.assertEqual(transform_edges(edges,lambda p:rotate_label(p,r)),edges)
    def test_30_13_six_reflected_automorphisms(self):
        edges=model13_edges()
        for r in range(6):self.assertEqual(transform_edges(edges,lambda p:rotate_label(reflect_label(p),r)),edges)
    def test_31_13_distance_rotation(self):
        nodes=nodes13()
        for r in range(6):
            for a,b in [('I0','J3'),('I1','I4'),('O','J2'),('J0','J1')]:
                self.assertEqual(squared_length(nodes[a],nodes[b]),squared_length(nodes[rotate_label(a,r)],nodes[rotate_label(b,r)]))
    def test_32_13_clique_seventy_eight(self):self.assertEqual(len(all_pairs(nodes13())),78)
    def test_33_13_ring_triangle_count(self):self.assertEqual(triangles(nodes13(),model13_edges()),6)
    def test_34_four_bits_address_thirteen(self):self.assertEqual(next(k for k in range(1,10) if (1<<k)>=13),4)
    def test_35_star_tetra_twelve_edges(self):self.assertEqual(len(star_tetra_edges()[2]),12)
    def test_36_k8_twenty_eight_edges(self):self.assertEqual(len(all_pairs(range(8))),28)
    def test_37_cross_tetra_sixteen(self):self.assertEqual(len(all_pairs(range(8))-star_tetra_edges()[2]),16)
    def test_38_star_tetra_volumes_nonzero(self):
        xyz,group,_=star_tetra_edges()
        for p in (0,1):self.assertNotEqual(volume6(*[xyz[i] for i in range(8) if group[i]==p]),0)
    def test_39_rotation_negative_control(self):
        edges=model13_edges()-{frozenset(('I0','I1'))}
        self.assertNotEqual(transform_edges(edges,lambda p:rotate_label(p,1)),edges)
    def test_40_hub_fragility_negative_control(self):
        self.assertNotEqual(len(components(DOMAINS,star_edges())),len(components(DOMAINS,combined_edges())))
    def test_41_edge_conservation_false_inference(self):
        self.assertEqual(len(domain_clique()),6)
        # Edge number by itself carries no fluid rate, mass or pressure samples.
        self.assertFalse(any(isinstance(e,dict) and 'flow' in e for e in domain_clique()))
    def test_42_subset_of_13_pair_graph(self):self.assertTrue(model13_edges().issubset(all_pairs(nodes13())))

if __name__=='__main__': unittest.main(verbosity=2)
