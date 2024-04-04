'''https://leetcode.com/problems/set-matrix-zeroes/description/

'''
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        firstCol = False
        for i in range(len(matrix)) :
            for j in range(len(matrix[i])) :
                if matrix[i][j] == 0 :
                    if j == 0 :
                        firstCol = True
                        continue
                    matrix[0][j] = 0
                    matrix[i][0] = 0

        for i in range(1,len(matrix)) :
            for j in range(1,len(matrix[i])) :
                if matrix[0][j] == 0 or matrix[i][0] == 0: 
                    matrix[i][j] = 0
        
        for j in range(len(matrix[0])) :
            if matrix[0][0] == 0 :
                matrix[0][j] = 0

        for i in range(len(matrix)) :
            if firstCol :
                matrix[i][0] = 0

        
        