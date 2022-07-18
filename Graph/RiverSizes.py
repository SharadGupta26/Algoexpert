'''
Given an array of ones and zeros.
One represnt array and zero represnt land.
count the size of all rivers and return in array
'''

def riverSizes(matrix):
    vis = [[False for j in range(len(matrix[i]))] for i in range(len(matrix))]
    ans = []
    for i in range(len(matrix)) :
        for j in range(len(matrix[i])) :
            val = traverse(matrix, i, j, vis)
            if val > 0 :
                ans.append(val)
    return ans

def traverse(matrix, i, j, vis) :
    if i < 0 or i >= len(matrix) or j < 0 or j >= len(matrix[i]) :
        return 0
    if vis[i][j] or matrix[i][j] == 0:
        return 0
    vis[i][j] = True
    return 1 + traverse(matrix, i+1, j, vis) + traverse(matrix, i-1, j, vis) + traverse(matrix, i, j+1, vis) + traverse(matrix, i, j-1, vis)
            



