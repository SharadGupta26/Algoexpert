'''
Given integer array, find three largest elements in array and returm them in sorted order
'''

#using heap
import heapq
def findThreeLargestNumbers(array):
    data = []
    heapq.heappush(data, array[0])
    heapq.heappush(data, array[1])
    heapq.heappush(data, array[2])
    for i in range(3, len(array)) :
        val = array[i]
        if val > data[0] :
            heapq.heappop(data)
            heapq.heappush(data, val)
    data.sort()
    return data


