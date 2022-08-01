def checkWordBreak(s, words) :
    return checkWordBreakHelper(s, words, 1)

def checkWordBreakHelper(s, words, i) :
    if s == '' :
        return True
    if i > len(s) :
        return False 
    a = s[0:i]
    b = s[i : len(s)]
    if a in words and checkWordBreakHelper(b,words, 1) :
        return True
    else :
        return checkWordBreakHelper(s, words, i+1)


def test() :
    words = { 'i', 'like', 'sam', 'sung', 'samsung', 'mobile', 'ice', 'and', 'cream', 'icecream', 'man', 'go', 'mango'}
    print(checkWordBreak('ilikesamsungmobile', words))

test()