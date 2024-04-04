'''https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
'''

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        data = set()
        i = 0
        j = 0
        ans = 0
        while i<=j and j < len(s) :
            if s[j] not in data :
                data.add(s[j])
                ans = max(ans, j-i +1)
                j+=1
            else :
                data.remove(s[i])
                i += 1
        return ans
        