'''
Give a string of '('  ')'.
Remove MINIMUM parantheses to make string balanced.
'''

'''
This can be solved using DFS too but in DFS we can't keep track of minimum characters removed to get result.

In BFS, we traverse level wise, so we try removing one character from all positions. then two and so on.
As soon as we find a valid string, we don't go to next level (check 1). This way we find a valid string after min removal.

https://www.geeksforgeeks.org/remove-invalid-parentheses/

'''
from collections import deque
def removeInvalidParanthasisBFS(s) :
    data = deque()
    data.append(s)
    visit = set()
    lengthAfterMinRemoval = -1
    while data :
        s = data.popleft()
        if isValid(s) :
            print(s)
            lengthAfterMinRemoval = len(s)
        if lengthAfterMinRemoval == -1 : #------ check 1
            for i in range(len(s)) :
                if s[i] not in ['(', ')'] : # if any other character than ( )
                    continue
                x = s[0:i] + s[i+1:len(s)]
                if x not in visit :
                    visit.add(x)
                    data.append(x)

        
def isValid(s) :
    cnt = 0
    for i in s :
        if i == '(' :
            cnt += 1
        elif i == ')' :
            cnt -= 1
        if cnt < 0 :
            return False
    return cnt == 0

def test() :
    removeInvalidParanthasisBFS('()())()')

test()

