'''https://leetcode.com/problems/spiral-matrix/description/'''
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        vis = [[False for i in range(len(matrix[j]))] for j in range(len(matrix))]

        dir = "right"
        ans = []
        i,j = 0,0
        while len(ans) != (len(matrix) * len(matrix[0])) :
                if i<0 or j<0 or i >= len(matrix) or j >= len(matrix[i]) or vis[i][j] :
                    dir,i,j = self.switchDirection(dir, i,j)
                vis[i][j] = True
                ans.append(matrix[i][j])
                i,j = self.next(dir, i, j)
        
        return ans

    
    def switchDirection(self, dir, i,j) :
        if dir == "right" :
            return ("down", i+1, j-1)
        elif dir == "down" :
            return ("left", i-1, j-1)
        elif dir == "left" :
            return ("up", i-1, j+1)
        else :
            return ("right", i+1, j+1)

    def next(self, dir, i, j) :
        if dir == "right" :
            return (i, j+1)
        elif dir == "down" :
            return (i+1, j)
        elif dir == "left" :
            return (i, j-1)
        else :
            return (i-1, j)