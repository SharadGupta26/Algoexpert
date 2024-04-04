'''https://leetcode.com/problems/longest-repeating-character-replacement/description/
'''

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        data = set(i for i in s)
        ans = 0
        for c in data :
            i = 0
            j = 0
            l = k
            while i <= j and j < len(s):
                if s[j] == c :
                    j += 1
                elif l > 0 :
                    l -= 1
                    j += 1
                elif s[i] == c : 
                    i += 1
                else :
                    i += 1
                    l = min(l + 1, k)
                if i > j :
                    j+=1
                ans = max(ans, j-i)
        return ans


