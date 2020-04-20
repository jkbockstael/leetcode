#!/usr/bin/env python3

# Day 19: Search in Rotated Sorted Array
#
# Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
# (i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).
# You are given a target value to search. If found in the array return its index, otherwise return -1.
# You may assume no duplicate exists in the array.
# Your algorithm's runtime complexity must be in the order of O(log n).

class Solution:
    def search(self, nums: [int], target: int) -> int:
        # Binary search, with a twist
        left = 0
        right = len(nums) - 1
        while left <= right:
            middle = left + ((right - left) // 2)
            if nums[left] == target:
                return left
            if nums[right] == target:
                return right
            if nums[middle] == target:
                return middle
            if nums[left] > nums[middle]:
                if nums[middle] < target <= nums[right]:
                    left = middle + 1
                else:
                    right = middle - 1
            else:
                if nums[middle] > target >= nums[left]:
                    right = middle - 1
                else:
                    left = middle + 1
        return -1

# Tests
assert Solution().search([4,5,6,7,0,1,2], 0) == 4
assert Solution().search([4,5,6,7,0,1,2], 3) == -1
assert Solution().search([1], 1) == 0
assert Solution().search([], 1) == -1
