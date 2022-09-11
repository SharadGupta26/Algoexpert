'''
Given two strings, return minimum no of edit operations that needs to be performed on fist string to obtain the second string.

There are three edit operations, insertion of character, deletion of character and substituion of character.

i/p - 
str1 - abc
str2 - yabd

o/p - 2
//insert y, substitute c with d
'''

def levenshteinDistance(str1, str2):
    arr = [[0 for i in range(len(str1) + 1)] for j in range(len(str2) + 1)]
    for i in range(len(arr)) :
        for j in range(len(arr[i])) :
            if i == 0 :
                arr[i][j] = j
                continue
            if j == 0 :
                arr[i][j] = i
                continue
            a = str1[j-1]
            b = str2[i-1]

            if a == b :
                arr[i][j] = arr[i-1][j-1]
            else :
                arr[i][j] = 1 + min(arr[i-1][j], arr[i][j-1], arr[i-1][j-1])
    return arr[-1][-1]