'''https://leetcode.com/problems/rotate-image/description/
https://www.youtube.com/watch?v=fMSJSS7eO1w
'''

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        l,r = 0, len(matrix)-1
        while l < r :
            for i in range(r-l) :
                top = l
                bottom = r

                topLeft = matrix[top][l+i]

                matrix[top][l+i] = matrix[bottom-i][l]

                matrix[bottom-i][l] = matrix[bottom][r-i]

                matrix[bottom][r-i] = matrix[top+i][r]

                matrix[top+i][r] = topLeft
            r -= 1
            l += 1
        
        