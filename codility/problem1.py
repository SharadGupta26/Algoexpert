# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

from collections import deque
def solution(A, S):
    if(len(A) == 0) :
        return 0
    count = 0
    data = deque()
    #data.append((A[0], 1))
    for i in range(0, len(A)) :
        val = A[i]
        n = len(data)
        data.append((val, 1))
        while n>0 :
            n -= 1
            prev, size = data.popleft()
            if(prev / size == S) :
                count += 1
                #print(prev, size)
            data.append((prev + val, size + 1))

    while data :
        prev, size = data.popleft()
        if(prev / size == S) :
            count += 1
            #print(prev, size)

    return count