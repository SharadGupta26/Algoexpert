'''
given an array of integers, return the gratest sum that is generated from a strictly-increasing subsequence in the array
as well as the elements in sequesnce.

i/p - [10, 70, 20, 30, 50, 11, 30]

o/p - [110, [10, 20, 30, 50]]
'''

#for generating sequence, 
#pick the element once an dmove to next element. Then don't pick the element and move to next element.
#To keep track of elements in array, keep adding elements in array.

#this solution is not able to handle negatives (all negatives in arr)
def maxSumIncreasingSubsequence(array):
    return traverse(array, 0, [0,[]])

def traverse(array, i, ans) :
    if i >= len(array) :
        return ans
    val, arr = ans[0], ans[1]
    a = ans
    if(len(arr) == 0 or arr[-1] < array[i]) :
        a = traverse(array, i+1, [array[i] + val, arr + [array[i]]])
    b = traverse(array, i+1, [val , arr + []])

    if a[0] > b[0] :
        return a
    else :
        return b