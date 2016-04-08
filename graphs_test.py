import unittest
import graphs

class TestBFS(unittest.TestCase):
    
    def test_one_node_graph(self):
        """ Test BFS with one node graph. """
        G = {1:[]}
        s = 1
        E = [1]
        self.assertItemsEqual(graphs.BFS(G,s), E)

    def test_linear_graph(self):
        """ Test BFS with a linear graph. """
        G = {1:[2], 2:[1,3], 3:[2,4], 4:[3]}
        s = 2
        E = [1, 2, 3, 4]
        self.assertItemsEqual(graphs.BFS(G,s), E)
        s = 1
        E = [1, 2, 3, 4]
        self.assertItemsEqual(graphs.BFS(G,s), E)

    def test_general_graph(self):
        """ Test BFS with general graph. """
        G = {1:[2], 2:[1,3,4], 3:[2,4], 4:[2,3,5,6]}
        s = 2
        E = [1, 2, 3, 4, 5, 6]
        self.assertItemsEqual(graphs.BFS(G,s), E)


class TestDFS(unittest.TestCase):

    def test_one_graph(self):
        """ Test DFS with one node graph. """
        G = {1:[]}
        s = 1
        E = [1]
        self.assertItemsEqual(graphs.DFS(G,s), E)

    def test_linear_graph(self):
        """ Test DFS with a linear graph. """
        G = {1:[2], 2:[1,3], 3:[2,4], 4:[3]}
        s = 2
        E = [2,1, 3, 4]
        self.assertItemsEqual(graphs.DFS(G,s), E)
        s = 1
        E = [1,2,3,4]
        self.assertItemsEqual(graphs.DFS(G,s), E)

if __name__ == '__main__':
    unittest.main()
    
