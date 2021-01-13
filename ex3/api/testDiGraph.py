from api.DiGraph import DiGraph

import unittest


class TestDiGraph (unittest.TestCase):

    def __init__(self):
        self.g = DiGraph()

    def build_graph(self):
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

    def test_1(self):
        self.build_graph()
        self.assertEqual(self.g.nodeCounter, 5)

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










