# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A, k, l):
    val1 = helper(A, k, l)
    val2 = helper(A, l, k)
    return max(val1, val2)

def helper(A, l, k) :
    n = len(A)
    if(n < k + l) :
        return -1
    arr = [0 for i in range(200)] 
    arr[0] = A[0]
    for i in range(1, n) :
        arr[i] = arr[i-1] + A[i]
    maxVal = -1
    val1 = 0
    val2 = 0
    for i in range(0, n-l+1) :
        if i == 0 :
            val1 = arr[i+l-1]
        else :
            val1 = arr[i+l-1] - arr[i-1]
        for j in range(i+l, n-k+1) :
            if j == 0 :
                val2 = arr[j+k-1]
            else :
                val2 = arr[j+k-1] - arr[j-1] 
        maxVal = max(maxVal, val1 + val2)
    return maxVal      

