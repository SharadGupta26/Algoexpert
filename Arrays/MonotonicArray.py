'''
Given an integer array if it is monotonic.
meaing its elements from left to right are entirely non-increasing only or non-decreasing only.

'''

def isMonotonic(array):
    # Write your code here.
    return checkIncreasing(array) or checkDecreasing(array)
    
def checkIncreasing(array) :
    for i in range(1, len(array)) :
        x,y = array[i], array[i-1]
        if x > y :
            return False
    return True

def checkDecreasing(array) :
    for i in range(1, len(array)) :
        x,y = array[i], array[i-1]
        if x < y :
            return False
    return True

