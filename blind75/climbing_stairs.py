'''
https://leetcode.com/problems/climbing-stairs/
'''

class Solution:
    def climbStairs(self, n: int) -> int:
        mem = {}
        return self.recur(0, n, mem)
    def recur(self, i, n, mem) :
        if i > n : 
            return 0
        if i == n :
            return 1
        if i in mem : 
            return mem[i]
        ways = 0
        ways += self.recur(i+1, n, mem)
        ways += self.recur(i+2, n, mem)
        mem[i] = ways
        return ways