#!/usr/bin/env python3

# Day 18: Best Time to Buy and Sell Stock
#
# Say you have an array for which the ith element is the price of a given stock
# on day i.
# If you were only permitted to complete at most one transaction (i.e., buy one
# and sell one share of the stock), design an algorithm to find the maximum
# profit.
# Note that you cannot sell a stock before you buy one.

class Solution:
    def maxProfit(self, prices: [int]) -> int:
        best_profit = 0
        profit = 0
        for day in range(1, len(prices)):
            profit = max(0, profit + prices[day] - prices[day - 1])
            if profit > best_profit:
                best_profit = profit

        return best_profit

# Tests
assert Solution().maxProfit([7,1,5,3,6,4]) == 5
assert Solution().maxProfit([7,6,4,3,1]) == 0
