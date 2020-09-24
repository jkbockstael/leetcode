#!/usr/bin/env python3

# Day 22: Majority Element II
#
# Given an integer array of size n, find all elements that appear more than ⌊
# n/3 ⌋ times.

class Solution:
    def majorityElement(self, nums: [int]) -> [int]:
        # Good enough
        return [number for number in set(nums) \
            if nums.count(number) > len(nums) // 3]

# Tests
assert Solution().majorityElement([3,2,3]) == [3]
assert Solution().majorityElement([1,1,1,3,3,2,2,2]) == [1,2]
