import heapq
def laptopRentals(times):
    times.sort(key= lambda x : x[0])
    if not times :
        return 0
    count = 1
    data = []
    heapq.heappush(data, times[0][1])
    for i in range(1, len(times)) :
        s,e = times[i][0], times[i][1]
        if s < data[0] :
            count += 1
        else :
            heapq.heappop(data)
        heapq.heappush(data, e)
    return count