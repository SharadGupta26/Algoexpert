'''
https://leetcode.com/problems/decode-ways/description/
'''

class Solution:
    def numDecodings(self, s: str) -> int:
        mem = {}
        return self.ways(s, mem)
        
        
    def ways(self, s, mem) :
        if s == "" :
            return 1
        
        if s in mem :
            return mem[s]

        ans = 0
        d1 = s[0:1]
        if d1 == '0' :
            return 0
        ans +=  self.ways(s[1:], mem)

        if len(s) > 1 :
            d2 = s[0:2]
            if int(d2) < 27 :
                ans += self.ways(s[2:], mem)
        mem[s] = ans
        return ans
        