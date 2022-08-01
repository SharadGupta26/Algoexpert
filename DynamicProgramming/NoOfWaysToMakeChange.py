'''
Given an array of denomenator coins and an amount.
Find no of ways oyu can make value equal to amount using given denoms.

You have unlimited supply of each denom coin
'''

def numberOfWaysToMakeChange(n, denoms):
    amounts = [0 for i in range(n+1)]
    amounts[0] = 1
    for i in denoms :
        for amount in range(1, n+1) :
            if amount >= i :
                amounts[amount] += amounts[amount - i]
    return amounts[-1]