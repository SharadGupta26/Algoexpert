'''
Given an String, find longest palindromic substring
'''

'''
Solution - Idea is that every single character is palindrome in iteslf.
We iterate through the array and check if neighbouring charactors (or fist and last) are equal.
If yes, we check for furtehr string. else we return current substring that is forming palindrome.

There can be two cases, 
One when we append one character on each side. (odd length palindrome)
Another when append one character on either side (even length palindrome)
'''

def longestPalindromicSubstring(string):
    ans = string[0]
    maxlen = 1
    for i in range(1, len(string)) :
        val = checkAndValidate(string, i-1, i+1)
        if len(val) > maxlen :
            maxlen = len(val)
            ans = val
        val = checkAndValidate(string, i-1, i)
        if len(val) > maxlen :
            maxlen = len(val)
            ans = val
    return ans

def checkAndValidate(string, i, j) :
    if i < 0 or j > len(string) :
        return ""
    subString = string[i:j+1] 
    if subString[0] == subString[-1] :
        ans = checkAndValidate(string, i-1, j+1)
        if ans :
            return ans
        else :
            return subString
    else :
        return ""
