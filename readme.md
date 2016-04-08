# Graph algorithms

## What's in this package?

This problem has two subtasks:
    
* Connected components: given a set of edges and a value (i), determine the connected
component of the graph that contains i.
        Solution:
            This problem can be solved using a DFS or BFS algorithms.
            
* Subset sum: given a set of edges and a number (q) that represents the
    number of nodes to select, determine the nodes to be selected given the
    condition that all of nodes in a connected subgraph have to be selected.
        Solution:
            This problem is NP-complete, so there is no known polynomial time
            solution. So, here I'm solving it in Pseudo-polynomial time using
            Dynamic programming.
        Notes:
            I suppose the following rules:
                - To use this code you have a list of unidirected edges.
                - It is not always possible to find a exact solution, so you have
                to provide a value (e) such that any solution between (q-e, q+e)
                is acceptable.
        

## Features

* Written in Python 2.7


## How to use this code

The main file of this project is `components.py`. The module has two functions:
    
- `connected_component(G, n, s)`

        G: list of undirected edges
        n: total number of nodes in the graph
        i: node to find connected component

        This function will return a list of nodes that are connected to i.  
        
- `subset_sum(G, n, q, e)`

        G: list of undirected edges
        n: total number of nodes in the graph
        q: number of nodes to be selected
        e: maximum absolute error to considered if there is not a subset exactly
           equal to q 

        This function will return a list of nodes to be selected. This list could
        have any value in (q-e, q+e) nodes. If there is not a subset that fulfils
        this requirements the return value is None.


Finally, if you want to visualize the node selection, you can use the file
`visualize.py`. To use it you need to have
[graphviz](http://graphviz.readthedocs.org/en/latest/index.html) installed. 



             
             
