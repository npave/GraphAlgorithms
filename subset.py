""" Subset sum problem with tolerance

Given a set of integers, a value s and a value e. Determine if there is a subset
of given set with sum equal to s(+-)e. 

This is a NP-Complete problem. This is a solution using Dynamic programming.

"""
import numpy as np

def subset(G, s, e):
    """ 
    Args:
        G: list of numbers
        s: desaired sum
        e: maximun absoulte error       
    Return: subset of numbers of G which sum is equal or close to s or nothing
    if this subset does not exist.   
    """
    ns = s + e
    n = len(G)
    d = np.zeros((n+1, ns+1))
    
    for i in xrange(n+1):
        d[i][0] = True

    for i in xrange(1,n+1):
        for j in xrange(1,ns+1):
            if (j - G[i-1]) >= 0:
                d[i][j] = d[i-1][j] or d[i-1][j-G[i-1]]
            else:
                 d[i][j] = d[i-1][j]

    # After the DP table is built, we have to find if we can have a subset
    # which sum is equal or close to s with a tolerance of e. If there is not
    # a subset that sum exact s, then we start looking at s+1 and s-1,
    # then s+2 and s-2, and so on until we get to s+e.
    
    for j in xrange(e+1):            
        if d[n][s+j]:
            return select_subset(G, d, s+j)
        if d[n][s-j]:
            return select_subset(G, d, s-j)

def select_subset(G,d,s):
    """
    Args:
        G: list of numbers
        d: DP table
        s: desired sum
    Return: subset of numbers of G
    """
    n = len(G)
    result = []
    i = s
    while i > 0:
        if d[n][i] != d[n-1][i]:
            result.append(G[n-1])
            i -= G[n-1]
        n -= 1
    return result


