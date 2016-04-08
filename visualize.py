import components
import graphs
import graphviz as gv


def visualize(G, n, q, e):
    """ 
    Args:
        G: list of undirected edges
        n: total number of nodes in the graph
        q: number of nodes to be infected
        e: maximum absolute error to considered if there is not a subset exactly
           equal to q 
    """
    al = components.edges_to_adjacency_list(G, n)
    g = gv.Graph('G', filename='visualization.gv', engine="sfdp")
    for i in al:
        for j in al[i]:
            if i > j:
                g.edge(str(i),str(j))

    result = components.subset_sum(G, n, q, e)
    for i in result:
        g.node(str(i),style='filled', color='lightblue')


    g.body.append(r'label = "\n\Visualization"')
    g.body.append('fontsize=20')
    g.view()


if __name__ == "__main__":
    G = [(1,2), (2,3), (3,4), (3,5), (5,6), (7,8), (8,9), (9, 10), (11,12),
         (12,13), (12,14), (14,15), (14,16)]
    n = 16
    #q = input("Nodes to infect: ")
    q = 9
    e = 1
    visualize(G, n, q, e)
