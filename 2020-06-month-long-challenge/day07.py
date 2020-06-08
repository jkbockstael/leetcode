#!/usr/bin/env python3

# Day 7: Coin Change 2
#
# You are given coins of different denominations and a total amount of money.
# Write a function to compute the number of combinations that make up that
# amount. You may assume that you have infinite number of each kind of coin.
#
# Note:
# - 0 <= amount <= 5000
# - 1 <= coin <= 5000
# - the number of coins is less than 500
# - the answer is guaranteed to fit into signed 32-bit integer

class Solution:
    def change(self, amount: int, coins: [int]) -> int:
        # combinations[amount] := number of ways to get `amount` using `coins`
        combinations = [0 for _ in range(0, amount + 1)]
        combinations[0] = 1
        for coin in coins:
            for value in range(1, amount + 1):
                if value >= coin:
                    combinations[value] += combinations[value - coin]
        return combinations[amount]

# Tests
assert Solution().change(5, [1,2,5]) == 4
assert Solution().change(3, [2]) == 0
assert Solution().change(10, [10]) == 1
