'''https://leetcode.com/problems/pacific-atlantic-water-flow/description/'''


'''partially working and long solution
approach  - DFS in matrix once to identify all cells fro pacific. Then same for atlantic.
And then check if cell exist in both
'''

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pecificMem = {}
        atlanticMem = {}
        vis = [[False for i in range(len(heights[j]))] for j in range(len(heights))]
        ans = []

        for i in range(len(heights)) :
            for j in range(len(heights[i])) :
                self.oceanPacific(heights, vis, pecificMem, i,j, heights[i][j])

        vis = [[False for i in range(len(heights[j]))] for j in range(len(heights))]

        for i in range(len(heights)) :
            for j in range(len(heights[i])) :
                self.oceanAtlantic(heights, vis, atlanticMem, i,j, heights[i][j])

        for i in range(len(heights)) :
            for j in range(len(heights[i])) :
                #print(i,j,pecificMem[(i,j)],atlanticMem[(i,j)])
                if pecificMem[(i,j)] and atlanticMem[(i,j)]:
                    ans.append([i,j])

        return ans

    def oceanPacific(self, heights, vis, mem, i, j , prev) :
        if i<0 or j < 0 or i >= len(heights) or j >= len(heights[i]) :
            return False

        if heights[i][j] > prev :
            return False
        
        if vis[i][j] :
            return False

        if (i,j) in mem :
            return mem[(i,j)]

        if i==0 or j == 0 :
            mem[(i,j)] = True
            return True
        vis[i][j] = True
        ans = False
        ans = ans or self.oceanPacific(heights, vis, mem, i-1, j, heights[i][j])
        ans = ans or self.oceanPacific(heights, vis, mem, i, j-1, heights[i][j])
        ans = ans or self.oceanPacific(heights, vis, mem, i+1, j, heights[i][j])
        ans = ans or self.oceanPacific(heights, vis, mem, i, j+1, heights[i][j])
        mem[(i,j)] = ans
        vis[i][j] = False
        return ans
        

    def oceanAtlantic(self, heights, vis, mem, i, j , prev) :
            if i<0 or j < 0 or i >= len(heights) or j >= len(heights[i]) :
                return False

            if heights[i][j] > prev :
                return False
            
            if vis[i][j] :
                return False

            #atlantic
            if i==len(heights) - 1 or j == len(heights[i]) - 1  :
                mem[(i,j)] = True
                return True
            vis[i][j] = True
            ans = False
            ans = ans or self.oceanAtlantic(heights, vis, mem, i-1, j, heights[i][j])
            ans = ans or self.oceanAtlantic(heights, vis, mem, i, j-1, heights[i][j])
        
            ans = ans or self.oceanAtlantic(heights, vis, mem, i+1, j, heights[i][j])
            ans = ans or self.oceanAtlantic(heights, vis, mem, i, j+1, heights[i][j])
            mem[(i,j)] = ans
            vis[i][j] = False
            return ans


'''Perfectly working solution
We start from known and dfs to all cells.
iterate all rows. Keep track of all cells that are rechable from first column for pacifc.
Celss that are rechable from last column for atlantic

Same for all columns.
Keep track of all cells reachable from first row for pacific
all cells reachable from last row for atlantic

And then traverse matrix and check if cell exist in both data
'''
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pac = set()
        atl = set()
        rows = len(heights)
        cols = len(heights[0])
        
        ans = []

        def dfs(i,j,prev, vis) :
            if i < 0 or j < 0 or i >= len(heights) or j >= len(heights[i]) or (i,j) in vis or prev > heights[i][j] :
                return
            vis.add((i,j))
            dfs(i+1,j,heights[i][j], vis)
            dfs(i-1,j,heights[i][j], vis)
            dfs(i,j+1,heights[i][j], vis)
            dfs(i,j-1,heights[i][j], vis)

        for r in range(rows) :
            dfs(r,0,heights[r][0], pac)
            dfs(r,cols-1,heights[r][cols-1], atl)

        for c in range(cols) :
            dfs(0,c,heights[0][c], pac)
            dfs(rows-1,c,heights[rows-1][c], atl)
        
        for i in range(len(heights)) :
            for j in range(len(heights[i])) :
                if (i,j) in pac and (i,j) in atl:
                    ans.append([i,j])

        return ans



        