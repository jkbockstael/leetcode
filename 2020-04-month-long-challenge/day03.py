#!/usr/bin/env python3

# Day 3: Maximum Subarray
#
# Given an integer array nums, find the contiguous subarray (containing at least
# one number) which has the largest sum and return its sum.

class Solution:
    def maxSubArray(self, nums: [int]) -> int:
        total = 0
        best_total = float("-inf")
        for num in nums:
            total = max(total + num, num)
            best_total = max(total, best_total)
        return best_total

# Tests
assert Solution().maxSubArray([-2,1,-3,4,-1,2,1,-5,4]) == 6
assert Solution().maxSubArray([-1]) == -1
