'''https://leetcode.com/problems/word-break/description/
'''
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        mem = {}
        return self.recur(s, wordDict, "", mem)

    def recur(self, s, wordDict, running, mem) :
        if s == "" :
            return running in wordDict
        if s in mem :
            return mem[s]
        running += s[0]
        s = s[1:]
        ans = False
        if running in wordDict :
            ans = self.recur(s, wordDict, "", mem)
        if not ans :
            ans = self.recur(s, wordDict, running, mem)
        mem[s] = ans
        return ans