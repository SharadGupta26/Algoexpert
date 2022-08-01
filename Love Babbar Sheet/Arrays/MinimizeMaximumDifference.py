'''
import math
def minimize(arr, k) :
    arr.sort()
    ans = arr[-1] - arr[0]
    tempMin = arr[0]
    tempMax = arr[-1]

    xxxxxx``x
    for i in range(len(arr)) :
        tempMin = min(tempMin, getValue(arr[i] + k, math.inf), getValue(arr[i] - k, math.inf))
        tempMax = max(tempMax, getValue(arr[i] + k, -math.inf), getValue(arr[i] - k, -math.inf))
        ans = min(ans, tempMax - tempMin)

    return ans


def getValue(val, default) :
    return val if val >= 0 else default
def test() :
    print(minimize([1,15,10], 6))

test()
'''