'''https://leetcode.com/problems/palindromic-substrings/description/'''


class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        for i in range(len(s)) :
            #for odd length strings
            l,r = i,i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
                count += 1
            # for even length strings
            l,r = i,i+1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
                count += 1
        return count