'''
given an array from 1 to n of size n.
find first integer that is duplicating.
solve in O(1) space.
'''

def firstDuplicateValue(array):
   i = 0
   while i < len(array)  :
       print(array)
       val = abs(array[i])
       if array[val-1] < 0 :
           return val
       array[val-1] = -1 * array[val-1]
       i += 1
   return -1