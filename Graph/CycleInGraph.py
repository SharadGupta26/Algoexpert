'''
Given an adjacency list of graph.
Check if graph contains cycle or not.

Cycle means, any no of virtices, inculding one, connected in chain
'''

def cycleInGraph(edges):
    vis = [False for i in edges]
    
    for i in range(len(edges)) :
        val = checkCycle(i, edges, vis)
        if val :
            return val
    return False

def checkCycle(node, edges, vis) :
    
    neighbours = edges[node]
    for neighbour in neighbours :
        if vis[node] :
            return True
        vis[node] = True
        val = checkCycle(neighbour, edges, vis)
        vis[node] = False
        if val :
            return val
    return False
        
        