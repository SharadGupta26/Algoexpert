'''
Given a list of words, find unique characters required to build all the words.
Output can be in any order
input :
["this", "that", "did", "deed", "them!", "a"]

Output : 
["!", "a", "d", "d", "e", "e", "h", "i", "m", "s", "t", "t"]

'''

def minimumCharactersForWords(words):
    data = {}
    for word in words :
        temp = getCounts(word)
        for key, value in temp.items() :
            if key not in data or data[key] < value : 
                data[key] = value
    ans = []
    for key, value in data.items() :
        for i in range(value) :
            ans.append(key)

    return ans

def getCounts(s) :
    data = {}
    for i in s :
        if i in data :
            data[i] += 1
        else :
            data[i] = 1
    return data
