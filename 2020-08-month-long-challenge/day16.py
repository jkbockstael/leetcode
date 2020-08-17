#!/usr/bin/env python3

# Day 16: Best Time to Buy and Sell Stock III
#
# Say you have an array for which the ith element is the price of a given stock
# on day i.
# Design an algorithm to find the maximum profit. You may complete at most two
# transactions.
# Note: You may not engage in multiple transactions at the same time (i.e., you
# must sell the stock before you buy again).

class Solution:
    def maxProfit(self, prices: [int]) -> int:
        if len(prices) == 0:
            return 0

        profits = [0 for _ in range(len(prices))]
        lowest_price = prices[0]
        for day in range(1, len(prices)):
            profits[day] = max(profits[day - 1], prices[day] - lowest_price)
            lowest_price = min(lowest_price, prices[day])
        
        best_profit = profits[-1]
        highest_price = prices[-1]
        for day in range(len(prices) - 2, 0, -1):
            best_profit = max(best_profit, highest_price - prices[day] \
                + profits[day - 1])
            highest_price = max(highest_price, prices[day])

        return best_profit

# Tests
assert Solution().maxProfit([3,3,5,0,0,3,1,4]) == 6
assert Solution().maxProfit([1,2,3,4,5]) == 4
assert Solution().maxProfit([7,6,4,3,1]) == 0
