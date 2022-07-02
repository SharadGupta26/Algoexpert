'''
Given an array of positive integers representing the values of coins.
write a function that returns the minimum amount of change that you can not create.

coins = [1,2,5]
ans = 4

we can create [1,2,3,5,6,7]

'''

def nonConstructibleChange(coins):
    ans = 0
    coins.sort()
    for i in coins :
        if i > ans + 1 :
            return ans + 1
        else :
            ans =  i + ans
    return ans + 1

