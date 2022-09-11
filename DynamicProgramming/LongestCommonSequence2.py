'''
Given 2 different strings, Find Longest common subsequence string / characters
'''

def longestCommonSubsequence(str1, str2):
    if not str1 or not str2 :
        return []
    
    arr = [['' for i in range(len(str2) + 1)] for j in range(len(str1) + 1)]
    #print(len(str1), len(str2))
    #print(len(arr), len(arr[0]))
    for i in range(1, len(str1) +1) :
        for j in range(1, len(str2) +1 ) :
            a = str1[i-1]
            b = str2[j-1]

            if a == b :
                arr[i][j] = arr[i-1][j-1] + a
            else :
                if len(arr[i-1][j]) > len(arr[i][j-1]) :
                    arr[i][j] = arr[i-1][j]
                else :
                    arr[i][j] = arr[i][j-1]
    
    return list(arr[-1][-1])
    