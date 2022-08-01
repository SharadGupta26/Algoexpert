'''
Given a string, fina all permutations

'''

def permutations(s) :
    print(permutations_rec(list(s), 0))

#solution usign #backtracking
def permutations_rec(s, i) :
    ans = []
    if i == len(s):
        return ["".join(s)]
   
    for k in range(i,len(s)) :
        s[i], s[k] = s[k], s[i] #swap
        ans.extend(permutations_rec(s, i+1))
        s[i], s[k] = s[k], s[i] #swap it back to get original string
    return ans


def test() :
    permutations('abc')
    permutations('abcd')

test()