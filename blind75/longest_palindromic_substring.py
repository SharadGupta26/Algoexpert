'''https://leetcode.com/problems/longest-palindromic-substring/description/
for each character, consider it is middle of string. 
To check palindromes, move in both direction by one distance.and check if end characters are same.
'''


class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans = ''
        maxVal = 0
        for i in range(len(s)) :
            l,r = i,i
            #for odd len string
            while l >= 0 and r < len(s) and s[l] == s[r]: 
                if (r-l+1) > maxVal :
                    ans = s[l:r+1]
                    maxVal = r-l+1
                l -= 1
                r += 1
            #for even len strings
            l,r = i,i+1
            while l >= 0 and r < len(s) and s[l] == s[r]: 
                if (r-l+1) > maxVal :
                    ans = s[l:r+1]
                    maxVal = r-l+1
                l -= 1
                r += 1
        return ans