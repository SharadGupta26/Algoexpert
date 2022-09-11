'''
Given an array of hieghts, return the amount of water trapped between the pillars viewed from the front.
'''

def waterArea(arr):
    water = 0
    i = 0
    while i < len(arr) -1:
        if arr[i] > arr[i+1] :
            left = i
            right = findRight(arr, left)
            if right == -1 :
                break
            water += calculateWater(arr, left, right)
            i = right
        else :
            i+=1
    return water
    
def calculateWater(arr, left, right) :
    value = min(arr[left], arr[right])
    water = 0
    for i in range(left+1, right) :
        water += (value-arr[i])
    return water
    
def findRight(arr, i) :
    maxIndx = -1
    maxVal = 0
    for j in range(i+1, len(arr)) :
        if arr[j] >= arr[i] :
            return j
        if arr[j] > maxVal :
            maxVal = arr[j]
            maxIndx = j
    return maxIndx
