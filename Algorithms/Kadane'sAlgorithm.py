

#when given input array consist at least one positive integer.
#Case not handeled when all elements are negetive.

import math
def kadanesAlgorithm(array):
    ans = 0
    runningSum = 0
    for i in array :
        runningSum += i
        ans = max(runningSum, ans)
        runningSum = max(0, runningSum)
    return ans


def kadanesAlgorithm_2(array):
    ans = array[0]
    runningSum = array[0]
    for i in range(1, len(array)) :
        val = array[i]
        runningSum  = max(val, runningSum + val)
        ans = max(runningSum, ans)
       
        
    return ans
