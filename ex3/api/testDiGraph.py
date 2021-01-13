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
        self.assertEqual(len(self.g.edges), 12)

    def test_2_1(self):
        self.g = DiGraph()
        for x in range(1000000):
            self.g.add_node(x)
        for y in range(500000):
            self.g.add_edge(y, y+2, y*3)
        self.assertEqual(len(self.g.vertices), 1000000)

    '''def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)'''


if __name__ == '__main__':
    unittest.main()










