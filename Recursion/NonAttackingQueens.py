'''
Gievn an no n
Find out no of ways you can place n queens on n*n chess board such that no queen can attack any other queen.

In chess board, any queen can attack any other queen in horizonaraly, vertically and dioganal direction.

#backtracking
'''

def nonAttackingQueens(n):
    matrix = [[0 for i in range(n)] for j in range(n)]
    return countPlacements(matrix, 0, 0,0)


'''
Appraoch is to check if is it safe to place queen on given col.
If safe, we place queen on col and move on to next row and try for remaining queens.
If not safe, we move to next col and check same.

At any point if we have crossed boundries and could not place queen anywher in same row, we return false (0 solution for this config).
else if all queens have been placed then we return true (1 solution for this config)

We always place any queen only one row and place next queen always in next row.

Using backtracking, we try placing each queen in each column, and count all possible configurations that satisfy constraint.

'''

#queens= queens placed so far
def countPlacements(matrix, queens, i, j) :
    n = len(matrix)
    if j == n :
        return 0
    if queens ==  len(matrix) :
        return 1 
    ans = 0
    
    if safeToPlace(matrix, i, j) :
        print('here')
        matrix[i][j] = 1 #do
        #once we have placed a queen in any column, just move to next row
        #because we never can place another queen in same row
        ans += countPlacements(matrix, queens + 1, i +1, 0) #recur
        matrix[i][j] = 0 #undo
    ans += countPlacements(matrix, queens, i, j+1)
    return ans

def safeToPlace(matrix, i, j) :
    r = i
    c = j
    while r >= 0 :
        if matrix[r][c] == 1 :
            return False
        r -= 1
    # no need to check left columns on same row    
    #r = i
    #c = j
    #while c >= 0 :
     #   if matrix[r][c] == 1 :
      #      return False
       # c -= 1

    r = i
    c = j
    while c >= 0 and r >= 0:
        if matrix[r][c] == 1 :
            return False
        c -= 1
        r -= 1

    r = i
    c = j
    while c < len(matrix) and r >= 0 :
        if matrix[r][c] == 1 :
            return False
        c += 1
        r -= 1
    return True

    
    
