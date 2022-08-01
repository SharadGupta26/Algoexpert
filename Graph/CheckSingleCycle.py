'''
Given an array of integer where each integer represent its jump value.
Postive jump value meaning right jump. Negative jump value meaning left jump.
Return if it forms single cycle. Means if starting at any index, and following the jumps, 
every element in the array is visited exactly once before landing back on starting index.

ip - [2, 3, 1, -4, -4, 2]
op - True
'''

def hasSingleCycle(array):
    vis = [False for i in array]
    vis[0] = True
    return checkCycle(array, vis, getNextIndex(array, 0))

def getNextIndex(array, i) :
    val = array[i] + i
    n = len(array)
    val = val % n
    if val < 0 :
        val + n
    return val

def checkAllVisited(vis) :
    for i in vis :
        if not i :
            return False
    return True
    
def checkCycle(nodes, vis, i) :
    if i == 0 :
        return  checkAllVisited(vis)
    if vis[i] :
        return False
    vis[i] = True
    return checkCycle(nodes,vis, getNextIndex(nodes, i))
    
