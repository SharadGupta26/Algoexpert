'''https://leetcode.com/problems/valid-parentheses/description/
'''


class Solution:
    def isValid(self, s: str) -> bool:
        data = []
        for i in s :
            if i in ('(', '[', '{') :
                data.append(i)
            elif not data :
                return False
            else :
                k = data.pop()
                if not (( i == ')' and k == '(') or (i == ']' and k == '[') or (i == '}' and k == '{')) : 
                    return False
        return False if data else True