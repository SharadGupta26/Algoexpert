'''
Given an string of lower english alphabates, return first non repeating character index
'''

#Time - O(n)
#space - O(1) - dictionary will hold at most 26 keys
def firstNonRepeatingCharacter(string):
    data = {}
    for c in string :
        if c in data :
            data[c] += 1
        else :
            data[c] = 1
    for i in range(len(string)) :
        c = string[i]
        if data[c] == 1 :
            return i
    return -1
