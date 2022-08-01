'''
Given an integer, generate all possible combinations of valid <div> tags.
A valid tag is <div></div>
'''

def generateDivTags(n):
    ans = []
    generate('', n, n, ans)
    return ans

def generate(s, o, c, ans) :
    if o==0 and c == 0 :
        ans.append(s)
        return
    if c < o :
        return

    if o > 0 :
        generate(s + '<div>', o-1, c,ans)
    if c > 0 :
        generate(s + '</div>', o, c-1, ans)
    
