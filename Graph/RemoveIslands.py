'''
Given a matrix of 0 and 1, remove islands by replacing 1 with 0.

Any island touching border (row 0, row n, col 0, col n) is not considered as island
'''

def removeIslands(matrix):
    markNonIslands(matrix)
    updateIslands(matrix, 1, 0)
    updateIslands(matrix, -1, 1)
    return matrix

def updateIslands(matrix, oldValue, newValue) :
    for i in range(len(matrix)) :
        for j in range(len(matrix[i])) :
            if matrix[i][j] == oldValue :
                matrix[i][j] = newValue
        
def markNonIslands(matrix) :
   for i in range(len(matrix)) :
       for j in range(len(matrix[i])) :
           if isBorder(i, j, matrix) :
               traverse(i, j, matrix)

def traverse(i, j, matrix) :
    try :
        if matrix[i][j] == 1 :
            matrix[i][j] = -1 
            traverse(i+1 ,j , matrix)
            traverse(i-1, j, matrix)
            traverse(i, j+1, matrix)
            traverse(i, j-1, matrix)
    except :
        pass
    
def isBorder(i, j, matrix) :
    return i == 0 or j == 0 or i == len(matrix) - 1 or j == len(matrix[i]) - 1 