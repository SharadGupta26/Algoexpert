'''
Given an array representing coins denominations and a target amount.
Find minimum no of coins required to make target amount.

Consider infinite supply of each coin
'''
import math
def minNumberOfCoinsForChange(n, denoms):
    amounts = [math.inf for i in range(n+1)]
    amounts[0] = 0
    for i in denoms :
        for amount in range(1, n+1) :
            if amount == i :
                amounts[amount] = 1
            elif amount >= i :
                amounts[amount] = min(amounts[i] + amounts[amount - i], amounts[amount])
    return -1 if amounts[-1] == math.inf else amounts[-1]
