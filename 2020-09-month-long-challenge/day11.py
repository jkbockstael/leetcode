#!/usr/bin/env python3

# Day 11: Maximum Product Subarray
#
# Given an integer array nums, find the contiguous subarray within an array
# (containing at least one number) which has the largest product.

import functools

class Solution:
    def maxProduct(self, nums: [int]) -> int:
        # This naive approach is beautiful, but it's too slow
        # product = lambda xs: functools.reduce(lambda x,y: x*y, xs)
        # return max(product(nums[i:j+1])
        #     for i in range(0, len(nums))
        #     for j in range(i, len(nums)))

        # A dynamic approach is faster
        max_pos = [0 for _ in nums]
        max_neg = [0 for _ in nums]
        max_pos[0] = nums[0]
        max_neg[0] = nums[0]

        for i in range(1, len(nums)):
            n = nums[i]
            max_pos[i] = max(n, n * max_pos[i - 1], n * max_neg[i - 1])
            max_neg[i] = min(n, n * max_pos[i - 1], n * max_neg[i - 1])

        return max(max_pos)

# Tests
assert Solution().maxProduct([0,2]) == 2
assert Solution().maxProduct([2,3,-2,4]) == 6
assert Solution().maxProduct([-2,0,-1]) == 0
assert Solution().maxProduct([-2]) == -2
assert Solution().maxProduct([-4, -3]) == 12
