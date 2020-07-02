#!/usr/bin/env python3

# Day 1: Arranging Coins
#
# You have a total of n coins that you want to form in a staircase shape, where
# every k-th row must have exactly k coins.
# Given n, find the total number of full staircase rows that can be formed.
# n is a non-negative integer and fits within the range of a 32-bit signed integer.

import math

class Solution:
    def arrangeCoins(self, n: int) -> int:
        # Direct formula
        return int(math.sqrt(2 * n + 0.25) - 0.5)
        # Iterative approach
        # a = 0
        # triangular = 0
        # while triangular <= n:
        #     a += 1
        #     triangular += a
        # if n < triangular:
        #     a = a - 1
        # return a

# Tests
assert Solution().arrangeCoins(5) == 2
assert Solution().arrangeCoins(8) == 3
assert Solution().arrangeCoins(0) == 0
assert Solution().arrangeCoins(35) == 7
assert Solution().arrangeCoins(36) == 8
