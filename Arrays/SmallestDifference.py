'''
given two no empty arrays,
find a pair from each array whose absolute difference is closest to zero. (smallest difference)
'''

def smallestDifference(a, b):
    minDistance = 999999999
    res = []
    p1, p2 = 0,0
    a.sort()
    b.sort()
    while p1 < len(a) and p2 < len(b) :
        val = getDist(a[p1], b[p2])
        if val < minDistance :
            minDistance = val
            res = [a[p1], b[p2]]
        if a[p1] < b[p2] :
            p1 += 1
        else :
            p2 += 1
    return res
    

def getDist(i, j) :
    return max(i, j) - min(i, j)
