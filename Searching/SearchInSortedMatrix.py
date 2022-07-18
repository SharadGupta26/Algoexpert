'''
Given a sorted 2d matrix. In matrix all rows are sorted in ASC order and all columns are sorted in ASC order.
Given an integer, check if given integer is present in array or not.

matrix = [
    [1, 4, 7, 12, 15, 1000]
    [2, 5, 19, 31, 32, 1001]
    [3, 8, 24, 33, 35, 1003]
    [40, 41 , 42, 44, 45, 1004]
    ]
target = 24
'''

#using extra space to keep track of 
def searchInSortedMatrix(matrix, target):
    vis = [[False for j in range(len(matrix[i]))] for i in range(len(matrix))]
    return search(matrix, target, 0,0, vis)

def search(matrix, target, i, j, vis) :
    if i<0 or j < 0 or i >= len(matrix) or j >= len(matrix[i]) :
        return [-1, -1]
    
    if vis[i][j] :
        return[-1,-1]

    vis[i][j] = True
    if matrix[i][j] == target :        
        return [i,j]
    if target < matrix[i][j] :
        res = search(matrix, target, i, j-1, vis)
        if res[0] == -1 :
            return search(matrix, target, i-1, j, vis)
        else :
            return res
    else :
        res = search(matrix, target, i+1, j, vis)
        if res[0] == -1 :
            return search(matrix, target, i, j+1, vis)
        else :
            return res


#without using any extra space 
def searchInSortedMatrix(matrix, target):
    i = 0
    j = len(matrix[i]) - 1
    while i < len(matrix) and j >= 0 :
        if matrix[i][j] == target :
            return [i,j]
        elif target < matrix[i][j] :
            j -= 1
        else :
            i += 1
    return [-1, -1]
