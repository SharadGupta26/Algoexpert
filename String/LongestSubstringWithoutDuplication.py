'''
Given an string, return longest substring without duplicated characters
'''

#my solution, sliding window
def longestSubstringWithoutDuplication(string):
    unique = set()
    
    i = 0
    j = 0
    longest = ''
    temp = ''
    while j < len(string) :
        char = string[j]
        
        if char in unique :
            val = string[i]
            i+=1
            unique.remove(val)
            temp = string[i:j]
        else :
            temp += char
            unique.add(char)
            j+=1
        print(temp)
        if len(temp) > len(longest) :
            longest = temp
    return longest


#algo expert solution, same sliding window, but a lil better time 
def longestSubstringWithoutDuplication(string):
    data = {}
    i = 0
    j = 0
    longest = ''
    temp = ''
    while j < len(string) :
        char = string[j]
        if char in data :
            i = max(i, data[char])            
        j += 1
        data[char] = j
        temp = string[i:j]
        #print(temp)
        if len(temp) > len(longest) :
            longest = temp
    return longest
