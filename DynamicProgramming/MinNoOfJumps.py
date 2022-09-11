'''
Given an not empty array of positive integers where each value represent max no of steps you can take.
For example, if value at index 1 is 3. Then you can jump to index 2, index 3, index 4.
For each jump from i to i+x, it counts to one jump.

Count min no of jumps required to reach at last index.
'''

def minNumberOfJumps(array):
    mem = [-1 for i in range(len(array))]
    return traverse(array, 0, mem)

def traverse(array, i, mem) :
    if i >= len(array) :
        return 0
    if i == len(array) - 1 :
        return 0
    if mem[i] != -1 :
        return mem[i]
    jumps = array[i]
    minVal = float('inf')
    for k in range(1,jumps+1) :
        val = traverse(array, i+k, mem)+1
        minVal = min(val, minVal)
    mem[i] = minVal
    return minVal
        
        