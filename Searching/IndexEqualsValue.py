'''
Given sorted array of distinct integers.
Find index at which value is equal to its index.
Solve it in Olog(n)
'''


def indexEqualsValue(array):
    return indexEqualsValueHelper(array, 0, len(array)-1)

def indexEqualsValueHelper(array, i, j) :
    if j < i :
        return -1
    mid = (i + j) // 2
        
    ans = -1
    if array[mid] >= mid :
        ans = indexEqualsValueHelper(array, i, mid-1)
    if ans == -1 and array[mid] == mid :
        ans = mid
    if ans == -1 :
        ans = indexEqualsValueHelper(array, mid+1, j)
    return ans