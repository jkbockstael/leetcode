#!/usr/bin/env python3

# Day 22: Single Number II
#
# Given a non-empty array of integers, every element appears three times except
# for one, which appears exactly once. Find that single one.
#
# Note:
# - Your algorithm should have a linear runtime complexity. Could you implement
#   it without using extra memory?

class Solution:
    def singleNumber(self, nums: [int]) -> int:
        # Yes this is pretty naive, but it beats 83.79% of python3 submissions
        counts = {}
        for number in nums:
            if number not in counts:
                counts[number] = 1
            else:
                counts[number] += 1
        for number in counts:
            if counts[number] == 1:
                return number

# Tests
assert Solution().singleNumber([2,2,3,2]) == 3
assert Solution().singleNumber([0,1,0,1,0,1,99]) == 99
