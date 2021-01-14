from api.DiGraph import DiGraph
from api.GraphAlgo import GraphAlgo

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
        return self.g

    def test_1(self):
        self.g = self.build_graph()
        self.ga = GraphAlgo(self.g)
        self.ga.plot_graph()
        print(self.ga.shortest_path(0,4))
        self.assertEqual(self.ga.shortest_path(0,4), (10,[0,1,4]))
        '''self.ga.gr.remove_edge(1,4)
        print(self.ga.shortest_path(0, 4))
        self.assertEqual(self.ga.shortest_path(0, 4), (15, [0, 2, 3, 4]))'''

    def test_2(self):
        self.g = self.build_graph()
        self.ga = GraphAlgo(self.g)
        self.ga.plot_graph()
        print(self.ga.connected_component(1))
        self.assertEqual(self.ga.connected_component(1), [0, 1, 2, 4, 3])

    def test_3(self):
        self.g = self.build_graph()
        self.ga = GraphAlgo(self.g)
        self.ga.plot_graph()
        print(self.ga.connected_components())
        self.assertEqual(self.ga.connected_components(), [[0, 1, 2, 4, 3]])
