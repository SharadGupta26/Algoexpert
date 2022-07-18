'''
Given list of string. Return list by grouping anagrams together.

'''

#Time - O(W * n * log(n)) - W, length of given array ; n, length of longest string
#Space - (W*n)
def groupAnagrams(words):
    data = {}
    for word in words :
        s = word
        s = "".join(sorted(s))
        if s in data :
            data[s].append(word)
        else :
            data[s] = [word]
    return list(data.values())