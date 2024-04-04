'''
Given n queens and n*n matrix.
place all queens in matrix in such a way that no queen can attack any other queen.

Any queen can attack any other queen in all 8 directions. (same row, same col, same diagonal)
'''

'''
Soluttion

solution is to place one queen at a index.
Move to next index in matrix and check if it is safe to place another queen at this index.
if it is safe, then we place one more queen at this index and check next index for remaining queens untill all queens are placed.

If it is not safe, we move to next index.

Once a queen is placed and we have checked all possibilities, we come back, remove queen from current place and then check for next all possiblities

https://www.youtube.com/watch?v=PC0lSbDN2gY

'''
def NQueens(n) :
    arr = [[False for i in range(n)] for j in range(n)]
    NQeensSolver(arr, n, 0, 0, 0, '')

def NQeensSolver(arr, n, i, j, placedQueens, ans) :
    if placedQueens == n :
        print(ans)
        return
    if j == n : # out of cols
        i += 1 #moving to next row
        j = 0 #resetting col to 0
    
    if i == n : # out of rows 
        return 
    safe = safeToPlace(arr, i, j)
    if safe :
        arr[i][j] = True
        #ans = ans + ' ' + str([i,j])
        NQeensSolver(arr, n, i, j + 1, placedQueens + 1, ans + ' ' + str([i,j]))
        arr[i][j] = False

    NQeensSolver(arr, n, i, j + 1, placedQueens, ans)


# we just need to check if any queen is already present in any cell in same row, same col, or dioganally.
# no need to check cells after given positions
def safeToPlace(arr, i, j) :
    r= i-1
    c = j
    #checking all rows in same col
    while r >= 0 :
        if arr[r][c] :
            return False
        r -= 1

    r= i
    c = j-1
    #checking all cols in same row
    while c >= 0 :
        if arr[r][c] :
            return False
        c -= 1

    r= i-1
    c = j-1
    #checking all rows and cols in dioganally left up
    while r >= 0 and c >= 0:
        if arr[r][c] :
            return False
        r -= 1
        c -= 1

    r= i-1
    c = j+1
    #checking all rows and cols in dioganally right up
    while r >= 0 and c < len(arr[0]):
        if arr[r][c] :
            return False
        r -= 1
        c += 1

    
    return True


def test() :
    NQueens(4)

test()