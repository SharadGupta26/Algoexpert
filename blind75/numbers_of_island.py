'''https://leetcode.com/problems/number-of-islands/description/
'''

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        vis = [[False for i in range(len(grid[j]))] for j in range(len(grid))]
        ans = 0
        for i in range(len(grid)) :
            for j in range(len(grid[i])) :
                if grid[i][j] == "1" and not vis[i][j]:
                    self.visit(vis, grid, i, j)
                    ans += 1
        return ans

    def visit(self, vis, grid, i ,j) :
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[i]) :
            return
        if vis[i][j] :
            return
        if grid[i][j] == "0" :
            return
        vis[i][j] = True
        self.visit(vis, grid, i+1, j)
        self.visit(vis, grid, i-1, j)
        self.visit(vis, grid, i, j+1)
        self.visit(vis, grid, i, j-1)
