""" Test infection problem """

import components
import unittest

class TestConnectedComponents(unittest.TestCase):
    def test_two_node_graph(self):
        G = []
        n = 1
        s = 1
        E = {1}
        self.assertItemsEqual(components.connected_component(G, n, s), E)

class TestSubsetSum(unittest.TestCase):
    def test_one_connected_graph(self):
        G = [(1,2), (2,3), (2,1), (3,2), (3,4), (4,3)]
        n = 4
        q = 5
        e = 1
        E = [1,2,3,4]
        self.assertItemsEqual(components.subset_sum(G, n, q, e), E)

    def test_two_subgraph(self):
        G = [(1,2), (2,1), (3,4), (4,3)]
        n = 4
        q = 2
        e = 1
        E = [3,4]
        self.assertItemsEqual(components.subset_sum(G, n, q, e), E)
        G = [(1,2), (2,1), (3,4), (4,3)]
        n = 4
        q = 3
        e = 1
        E = [1,2,3,4]
        self.assertItemsEqual(components.subset_sum(G, n, q, e), E)
        G = [(1,2), (2,1), (3,4), (4,3)]
        n = 4
        q = 1
        e = 1
        E = [3,4]
        self.assertItemsEqual(components.subset_sum(G, n, q, e), E)

    def test_three_subgraph(self):
        G = [(1,2), (2,3), (3,4), (3,5), (5,6), (7,8), (8,9), (9, 10), (11,12),
             (12,13), (12,14), (14,15), (14,16)]
        n = 16
        q = 4
        e = 1
        E = [8,9,10,7]
        self.assertItemsEqual(components.subset_sum(G, n, q, e), E)
        
if __name__ == '__main__':
    unittest.main()
