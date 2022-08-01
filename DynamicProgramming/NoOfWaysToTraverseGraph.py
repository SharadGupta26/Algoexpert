'''
Given two integers representing width and height of a grid.
return no of ways to reach bottom right corner (w-1, h-1) of the graph when starting from top left (0,0) corner.

You can only go either down or right direction. 
'''

def numberOfWaysToTraverseGraph(width, height):
    mem = [[-1 for i in range(width)] for j in range(height)]
    return waysToTraverse(width,height, 0, 0, mem)

def waysToTraverse(w, h, i,j, mem) :
    if i >= h or j >= w :
        return 0
    if i == h-1 and j == w -1 :
        return 1
    if mem[i][j] != -1 :
        return mem[i][j]
    a = waysToTraverse(w,h, i+1, j, mem)
    b = waysToTraverse(w,h, i, j+1, mem)
    mem[i][j] = a + b
    return mem[i][j]
    


#algoexpert sol, O(W+h) time, O(1) space
def numberOfWaysToTraverseGraph(width, height):
    xdistance = width-1
    ydistance = height - 1

    #no of permutation of right and down movements are the no of ways to reach bottom right corner
    num = factorial(xdistance + ydistance)
    den = factorial(xdistance) * factorial(ydistance)
    return num // den

def factorial(n) :
    res = 1
    for n in range(2, n + 1) :
        res *= n
    return res
