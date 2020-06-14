#!/usr/bin/env python3

# Day 13: Largest Divisible Subset
#
# Given a set of distinct positive integers, find the largest subset such that
# every pair (Si, Sj) of elements in this subset satisfies:
#    Si % Sj = 0 or Sj % Si = 0.

class Solution:
    def largestDivisibleSubset(self, nums: [int]) -> [int]:
        # Pretty sure this is not an optimal solution, but it's readable
        divisible_subsets = {-1: set()} # max() isn't happy with emptiness
        for number in sorted(nums):
            # divisible_subsets[x] is a valid subset with x as the largest
            # value, so we grab the largest subset that divides number and add
            # number itself
            divisible_subsets[number] = {number} | max((
                divisible_subsets[divisor]
                for divisor in divisible_subsets
                if number % divisor == 0), key = len)
        # Return the sorted largest of these subsets
        return sorted(max(divisible_subsets.values(), key=len))

# Tests
assert Solution().largestDivisibleSubset([1,2,3]) in [[1,2], [1,3]]
assert Solution().largestDivisibleSubset([1,2,4,8]) == [1,2,4,8]

