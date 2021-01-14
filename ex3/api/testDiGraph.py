from random import random

from api.DiGraph import DiGraph

import unittest


class TestDiGraph (unittest.TestCase):

    def build_graph(self):
        self.g = DiGraph()
        for x in range(5):
            self.g.add_node(x)
        self.g.add_edge(0, 1, 5)
        self.g.add_edge(1, 0, 8)
        self.g.add_edge(0, 2, 2)
        self.g.add_edge(2, 0, 1)
        self.g.add_edge(2, 3, 1)
        self.g.add_edge(3, 2, 0.5)
        self.g.add_edge(3, 4, 12)
        self.g.add_edge(4, 3, 1)
        self.g.add_edge(0, 4, 20)
        self.g.add_edge(4, 0, 20)
        self.g.add_edge(4, 1, 5)
        self.g.add_edge(1, 4, 5)

    def test_1_1(self):
        self.build_graph()
        self.assertEqual(self.g.nodeCounter, 5)

    def test_1_2(self):
        self.build_graph()
        self.g.remove_node(2)
        self.assertEqual(self.g.nodeCounter, 4)

    def test_1_3(self):
        self.build_graph()
        self.g.remove_node(2)
        self.assertEqual(len(self.g.vertices), 4)

    def test_1_4(self):
        self.build_graph()
        self.assertEqual(self.g.edgeCounter, 12)

    def test_1_5(self):
        self.build_graph()
        self.g.add_node(5)
        self.assertEqual(len(self.g.vertices), 6)

    def test_1_6(self):
        self.build_graph()
        self.assertEqual(len(self.g.edges), 12)
        self.g.remove_edge(0, 4)
        self.assertEqual(len(self.g.edges), 11)


    def test_1_7(self):
        self.build_graph()
        self.assertEqual(self.g.get_all_v().keys(), {0,1,2,3,4})

    def test_1_8(self):
        self.build_graph()
        self.assertEqual(str(self.g.get_edge(0,4)), '0:4,20')

    def test_1_9(self):
        self.build_graph()
        self.assertEqual(str(self.g.get_node(4)), '4:0.0')

    def test_1_10(self):
        self.build_graph()
        self.assertEqual(self.g.v_size(), 5)

    def test_1_11(self):
        self.build_graph()
        self.assertEqual(self.g.e_size(), 12)

    def test_1_12(self):
        self.build_graph()
        self.g.add_node(6)
        self.assertEqual(str(self.g.get_node1(6)), '6:0.0')

    def test_1_13(self):
        self.build_graph()
        self.assertEqual(str(self.g.all_in_edges_of_node(1)), '{0:0.0: 8, 4:0.0: 5}')

    def test_1_14(self):
        self.build_graph()
        self.assertEqual(str(self.g.all_out_edges_of_node(2)), '{0:0.0: 1, 3:0.0: 1}')

    def test_1_15(self):
        self.build_graph()
        self.assertEqual(self.g.get_mc(), 17)

    def test_1_16(self):
        self.build_graph()
        self.assertTrue(self.g.has_edge(0, 4))
        self.g.remove_edge(0, 4)
        self.assertFalse(self.g.has_edge(0, 4))
        self.assertFalse(self.g.has_edge(0, 8))
        self.assertTrue(self.g.has_edge(4, 0))


    def test_2_1(self):
        self.g = DiGraph()
        for x in range(1000000):
            self.g.add_node(x)
        '''for y in range(1,500000):
            self.g.add_edge(y, y+1, y)
            #self.g.add_edge(random.randrange(0,100)/100000000,random.randrange(0,100)/100000000, random.randrange(0,200)/100000000)'''
        self.assertEqual(len(self.g.vertices), 1000000)




if __name__ == '__main__':
    unittest.main()










