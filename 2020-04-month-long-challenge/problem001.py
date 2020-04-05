#!/usr/bin/env python3

# Day 1: Single Number
#
# Given a non-empty array of integers, every element appears twice except for one. Find that single one.
# Note: Given a non-empty array of integers, every element appears twice except for one. Find that single one.

class Solution:
    def singleNumber(self, nums: [int]) -> int:
        seen = []
        for num in nums:
            if num in seen:
                seen.remove(num)
            else:
                seen.append(num)
        return seen[0]

assert Solution().singleNumber([2,2,1]) == 1, "[2,2,1] → 1"
assert Solution().singleNumber([4,1,2,1,2]) == 4, "[4,1,2,1,2] → 4"
