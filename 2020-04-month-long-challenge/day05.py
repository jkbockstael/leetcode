#!/usr/bin/env python3

# Day 5: Best Time to Buy and Sell Stock II
#
# Say you have an array for which the ith element is the price of a given stock
# on day i.
# Design an algorithm to find the maximum profit. You may complete as many
# transactions as you like (i.e., buy one and sell one share of the stock
# multiple times).
# Note: You may not engage in multiple transactions at the same time (i.e., you
# must sell the stock before you buy again).

class Solution:
    def maxProfit(self, prices: [int]) -> int:
        profit = 0
        for i in range(1, len(prices)):
            profit += max(prices[i] - prices[i - 1], 0)
        return profit

# Tests
assert Solution().maxProfit([]) == 0
assert Solution().maxProfit([7,1,5,3,6,4]) == 7
assert Solution().maxProfit([1,2,3,4,5]) == 4
assert Solution().maxProfit([7,6,4,3,1]) == 0
assert Solution().maxProfit([2,2,2]) == 0
