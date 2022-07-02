'''
Given an integer array and an integer, move all elements of given integer in array to end.
perform it in place.
'''
def moveElementToEnd(array, toMove):
    i = 0
    j = len(array) - 1
    while i < j :
        val = array[i]
        if val == toMove :
            array[i], array[j] = array[j], array[i]
            j -= 1
        else :
            i += 1
    return array
    
            