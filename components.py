"""

This module solve two problems.
    - Find the connected graph to one node
    - Find the subset of a graph which sum is close to given number.

I assumed that we start with a list of edges with the relation between two nodes.

This module have three functions:
    - edges_to_adjacency_list.- Take a list of edges (G) and return a dictionary
       with nodes has key and neighbors as values.
        Example:
            G = [(1,2),(2,3),(2,1),(3,2),(3,4),(4,3)]
            result = {1:[2], 2:[1,3], 3:[2,4], 4:[3]}
    - connected_component.- Take a list of edges (G) and a node (i) and return a
       list of connected graph of the given node.
        Example:
            G = {1: [2], 2: [1, 3], 3: [2, 4], 4: [3]}
            i = 2
            result = [1,2,3,4]
    - subset_sum.- Take a list of edges (G), a number of nodes to be
       selected (q) and a maximum absolute error (e) that is a tolerance if
       there is not subset that is exactly equal to q.
       The result is a list of nodes to be selected. The total of nodes in
       this list is close or equal to q.
"""

import collections
import graphs
import subset

def edges_to_adjacency_list(G, n):
    """ Convert list of edges to adjacency list.
    Args:
        G: list of edges. G = [(u0,v0),(u1,v1),...]
        n: total number of nodes in the graph
    Return:
        A dictionary with nodes and their neighbors
    """
    L = {}
    for i in xrange(1,n+1):
        L[i]=set()
    for i in G:
        L[i[0]].add(i[1])
        L[i[1]].add(i[0])
    return L

def connected_component(G, n, i):
    """ Return list of nodes connected to i
    Args:
        G: list of undirected edges
        n: total number of nodes in the graph
        i: node to find connected component
    Return:
        A list of nodes
    """
    adjacency_list = edges_to_adjacency_list(G, n)
    result = graphs.BFS(adjacency_list, i)
    return result

def subset_sum(G, n, q, e):
    """ 
    Args:
        G: list of undirected edges
        n: total number of nodes in the graph
        q: number of nodes to be selected
        e: maximum absolute error to considered if there is not a subset exactly
           equal to q 
    Return:
        A list of nodes to be selected
    """
    adjacency_list = edges_to_adjacency_list(G, n)
    connected_graph = collections.defaultdict(list)
    len_connected_graph = []
    nodes_connected = set()
    for i in adjacency_list:
        if i not in nodes_connected:
            g = graphs.BFS(adjacency_list, i)
            nodes_connected.update(g)
            connected_graph[len(g)].append(g)
            len_connected_graph.append(len(g))

    result = subset.subset(len_connected_graph, q, e)
    if result:
        r = []
        for k in result:
            r.extend(connected_graph[k][-1])
            connected_graph[k].pop()
        return r
