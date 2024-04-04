'''
https://leetcode.com/problems/unique-paths/description/
'''

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        return self.recur(m,n, 0,0, {})
        
    def recur(self, m, n, i, j, mem) :
        if i >= m or j >= n :
            return 0
        if i == m-1 and j == n-1 :
            return 1
        if (i,j) in mem :
            return mem[(i,j)]

        ways = 0
        ways += self.recur(m,n, i+1, j, mem)
        ways += self.recur(m,n, i, j+1, mem)
        mem[(i,j)] = ways
        return ways

