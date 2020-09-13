#!/usr/bin/env python3

# Day 12: Combination Sum III
#
# Find all possible combinations of k numbers that add up to a number n, given
# that only numbers from 1 to 9 can be used and each combination should be a
# unique set of numbers.
#
# Note:
# - All numbers will be positive integers.
# - The solution set must not contain duplicate combinations.

import itertools

class Solution:
    def combinationSum3(self, k: int, n: int) -> [[int]]:
        # Sometimes you just want to one-line the shit out of a problem
        return [list(combination)
            for combination in itertools.combinations(range(1, 10), k)
            if sum(combination) == n]

# Tests
assert Solution().combinationSum3(3, 7) == [[1,2,4]]
assert Solution().combinationSum3(3, 9) == [[1,2,6], [1,3,5], [2,3,4]]
