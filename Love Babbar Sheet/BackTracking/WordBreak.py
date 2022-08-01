'''
Given a stringwithout spaces and a words array.
Find all combinations of string by breaking into words such that each word is present in given words array.
#backtracking
https://www.geeksforgeeks.org/word-break-problem-using-backtracking/
'''

def wordBreak(s, words) :
    ans = []
    wordBreakHelper(s, words, 1, [], ans)
    return ans

def wordBreakHelper(s, words, i, curr, ans) :
    if s == '' :
        ans.append(list(curr))
        return
    if i > len(s) :
        return
        
    a = s[0:i]
    b = s[i : len(s)]
    #print(a,b)
    if a in words :
        curr.append(a) #do
        wordBreakHelper(b, words, 1, curr, ans) #recur
        curr.pop() #undo
    
    wordBreakHelper(s, words, i+1, curr, ans)



def test() :
    words = { 'i', 'like', 'sam', 'sung', 'samsung', 'mobile', 'ice', 'and', 'cream', 'icecream', 'man', 'go', 'mango'}
    print(wordBreak('ilikesamsungmobile', words))
    print()
    print(wordBreak('ilikeicecreamandmango', words))

test()