""" Searching graph algorithms

    (BFS).- Breadth-First Search

    (DFS).- Depth-First Search
    
"""

def BFS(G, s):
    """ Returns a list of the nodes connected with s.
    Args:
        s: node of which we want to find the connections.
        G: dictionary with nodes and their neighbours.
    Returns:
        A list of all nodes connected to s
    """

    discovered = {s}
    L = []
    L.append([s])
    i = 0
    while (len(L[i]) != 0 ):
        L.append([])
        for u in L[i]:
            if u in G:
                for v in G[u]:
                    if v not in discovered:
                        discovered.add(v)
                        L[i+1].append(v)
        i = i + 1
    return discovered 


def DFS(G, s):
    """ Returns a list of the nodes connected with s.
    Args:
        s: node of which we want to find the connections.
    Returns:
        A list of all nodes connected to s
    """

    S = [s]
    Explored = set()
    while S:
        s = S.pop()
        if s not in Explored:
            Explored.add(s)
            for i in G[s]:
                S.append(i)
    return Explored
                    
                    
            
    
