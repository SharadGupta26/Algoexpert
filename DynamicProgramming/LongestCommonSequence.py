'''
Given two different strings, find the longest common subsequence length
'''

def longestCommonSubsequence(text1: str, text2: str) -> int:
        arr = [[0 for i in range(len(text2) + 1)] for j in range(len(text1) + 1)]
        for i in range(1, len(text1) + 1) :
            for j in range(1, len(text2) + 1) :
                a = text1[i-1]
                b = text2[j-1]
                if a == b :
                    arr[i][j] = arr[i-1][j-1] + 1
                else :
                    arr[i][j] = max(arr[i-1][j], arr[i][j-1])
        #print(arr)
        return arr[-1][-1]

longestCommonSubsequence("bsbininm","jmjkbkjkv")