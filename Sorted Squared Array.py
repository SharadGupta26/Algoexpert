#given an array in sorted order, return squared sorted array.

#approach one
import heapq
def sortedSquaredArray(array):
    # Write your code here.
    data = []
    for i in array :
        heapq.heappush(data, i*i)
    res = []
    for i in range(len(data)) :
        res.append(heapq.heappop(data))
    return res



#approach 2
def sortedSquaredArray(array):
    i = 0
    j = len(array) - 1
    res = [0 for i in range(len(array))]
    for k in reversed(range(len(array))) :
        a = abs(array[i])
        b = abs(array[j])
        
        if a < b :
            res[k] = b * b
            j -= 1
        else :
            res[k] = a * a
            i += 1
    return res