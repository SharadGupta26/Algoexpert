'''https://leetcode.com/problems/longest-common-prefix/description/'''


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        i = 0 
        while i < len(strs[0]) :
            temp = strs[0][i]
            for s in strs :
                if i >= len(s) or s[i] != temp :
                    return res
            res = res + temp
            i += 1
        return res