'''
Given an array, return lenght of longest peak in the array.
Peak is defined as adjacent integers in the array are stricty increasing until they reach to hieghest.
after the peak they strictly decrase.
At least three integers are required to form a peak.
'''

def longestPeak(array):
    left = 0
    right = 0
    maxHeight = 0
    while right < len(array) :
        while right < len(array)-1 and array[right] < array[right + 1] :
            right += 1
        peak = right
        while right < len(array)-1 and array[right] > array[right + 1] :
            right += 1
        
        #print(left, right)
        if isPeak(left, right, peak, array) :
            height = right - left + 1
            maxHeight = max(maxHeight, height)
        
        left = peak+1
        right = peak+1
    return maxHeight
        
        

def isPeak(left, right, peak, array) :
    if right - left +1>= 3 and peak < len(array)-1 and array[peak] > array[peak + 1] and peak > 0 and array[peak] > array[peak-1]:
        return True
    else :
        return False