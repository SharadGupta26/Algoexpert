'''
Given an array, find maximum sum of non adjecent elements in array.
'''

#my solution
def maxSubsetSumNoAdjacent(array):
    if not array :
        return 0
    mem = [-1 for i in array]
    val1 = maxSubsetSumNoAdjacentHelper(array,0,0, mem)
    return val1

def maxSubsetSumNoAdjacentHelper(array, i, sum, mem) :
    if i >= len(array) :
        return sum
    if i == len(array) - 1 :
        return sum + array[i]
    ans = sum
    for j in range(i, i+2) :
        val = maxSubsetSumNoAdjacentHelper(array, j+2, sum + array[j], mem)
        ans = max(ans, val)
    return ans


#algo expert solution
def maxSubsetSumNoAdjecent_2(array) :
    if not array :
        return 0
    if len(array) == 1 :
        return array[0]
    sums = [i for i in array]
    sums[1] = max(array[0], array[1])
    for i in range(2, len(array)) :
        sums[i] = max(sums[i-1], sums[i-2] + array[i])
    return sums[-1]

