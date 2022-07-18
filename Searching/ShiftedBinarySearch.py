'''
Given an sorted array and an integer, check if integer is present in arary.
Here caveat is that 
'''

#this is using recusrion so space is being used as stack memory.
#for constant space, run throgh while loop (while i < j) and search
def shiftedBinarySearch(array, target):
    pivot = len(array)-1
    for i in range(len(array)-1) :
        if array[i] > array[i+1] :
            pivot = i
            break
    print(pivot)
    ans = search(array, 0, pivot, target)
    if ans == -1 and pivot < len(array)-1:
        return search(array, pivot + 1, len(array)-1, target)
    else :
        return ans

def search(array, i, j, target) :
    mid = (i + j) // 2
    val = array[mid]
    if target == val :
        return mid
    if i >= j :
        return -1
        
    if target < val : 
        return search(array, i, mid-1, target)
    else :
        return search(array, mid+1, j, target)