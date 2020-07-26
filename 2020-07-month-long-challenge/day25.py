#!/usr/bin/env python3

# Day 25: Find Minimum in Rotated Sorted Array II
#
# Suppose an array sorted in ascending order is rotated at some pivot unknown
# to you beforehand.
# (i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).
# Find the minimum element.
# The array may contain duplicates.

class Solution:
    def findMin(self, nums: [int]) -> int:
        # It's a binary search, with a twist (of lemon)
        left = 0
        right = len(nums) - 1
        while (left < right):
            middle = left + (right - left) // 2
            if nums[middle] == nums[right]:
                right = right - 1
            elif nums[middle] > nums[right]:
                left = middle + 1
            else:
                right = middle
        return nums[right]
# Tests
assert Solution().findMin([1,3,5]) == 1
assert Solution().findMin([2,2,2,0,1]) == 0
