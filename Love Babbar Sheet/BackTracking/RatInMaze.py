

def ratInMaze(n, matrix) :
    vis = [[False for i in range(n)] for j in range(n)]
    solveRatInMaze(matrix, vis, 0 ,0 , '')

def solveRatInMaze(matrix, vis, i, j, ans) :
    #print(ans)
    n = len(matrix)
    if i == n - 1 and j == n - 1 : 
        print(ans)
        return
    if i < 0 or j < 0 or i >= n or j >= n :
        return
    
    if matrix[i][j] == 0 or vis[i][j]: 
        return
    #do
    vis[i][j] = True
    #recur
    solveRatInMaze(matrix, vis, i+1, j, ans + 'D')
    solveRatInMaze(matrix, vis, i, j-1, ans + 'L')
    solveRatInMaze(matrix, vis, i, j+1, ans + 'R')
    solveRatInMaze(matrix, vis, i-1, j, ans + 'U')
    #undo
    vis[i][j] = False


def test() :
    matrix = [
         [ 1, 0, 0, 0, 0 ],
        [ 1, 1, 1, 1, 1 ],
        [ 1, 1, 1, 0, 1 ],
        [ 0, 0, 0, 0, 1 ],
        [ 0, 0, 0, 0, 1 ]
     ]
    ratInMaze(len(matrix), matrix)

test()




