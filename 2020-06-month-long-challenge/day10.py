#!/usr/bin/env python3

# Day 10: Search Insert Position
#
# Given a sorted array and a target value, return the index if the target is
# found. If not, return the index where it would be if it were inserted in
# order.
# You may assume no duplicates in the array.

class Solution:
    def searchInsert(self, nums: [int], target: int) -> int:
        # Real-life solution:
        #    return bisect.bisect_left(nums, target)
        # LeetCode lazy but readable solution:
        for index, number in enumerate(nums):
            if number >= target:
                return index
        return len(nums)

# Tests
assert Solution().searchInsert([1,3,5,6], 5) == 2
assert Solution().searchInsert([1,3,5,6], 2) == 1
assert Solution().searchInsert([1,3,5,6], 7) == 4
assert Solution().searchInsert([1,3,5,6], 0) == 0
