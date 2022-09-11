import heapq


        
def mergeSortedArrays(arrays):
    class info :
        def __init__(self, val, arr, idx) :
            self.val = val
            self.arr = arr
            self.idx = idx
        def __lt__(self, other) :
            return self.val < other.val
        def __gt__(self, other) :
            return self.val > other.val
            
    data = []
    ans = []
    for i in range(len(arrays)) :
        heapq.heappush(data, info(arrays[i][0], i, 0))
    while data :
        obj = heapq.heappop(data)
        ans.append(obj.val)
        if obj.idx < len(arrays[obj.arr]) - 1 :
            heapq.heappush(data, info(arrays[obj.arr][obj.idx+1], obj.arr, obj.idx+1))
    return ans
