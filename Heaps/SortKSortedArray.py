'''
Given an array and integer k.
Where array is K sorted meaning, It is partailly sorted array in which all elements are at most K positions away
from their sorted position.

Sort the input array in less than nlog(n) time

eg. i/p - [3, 2, 1, 5, 4, 7, 6, 5]
k = 3

o/p -[1, 2, 3, 4, 5, 5, 6, 7]
'''
import heapq
def sortKSortedArray(arr, k):
    data = []
    j = 0
    k = min(k, len(arr)-1)
    for i in range(k+1) :
        heapq.heappush(data, arr[i])
    for i in range(k+1, len(arr)) :
        val = heapq.heappop(data)
        arr[j] = val
        j+=1
        heapq.heappush(data, arr[i])
    for i in range(k+1) :
        val = heapq.heappop(data)
        arr[j] = val
        j+=1
    return arr
