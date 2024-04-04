'''https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/?source=submission-noac
'''

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        buy = 0
        sell = 1
        while sell < len(prices) :
            if prices[buy] > prices[sell] :
                buy += 1
                #sell += 1
            else :
                profit = max(profit, prices[sell] - prices[buy])
                sell += 1
        return profit
        