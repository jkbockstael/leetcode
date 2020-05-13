#!/usr/bin/env python3

# Day 12: Single Element in a Sorted Array
#
# You are given a sorted array consisting of only integers where every element
# appears exactly twice, except for one element which appears exactly once.
# Find this single element that appears only once.
#
# Note: Your solution should run in O(log n) time and O(1) space.

class Solution:
    def search(self, nums: [int], left: int, right: int) -> int:
        if left == right:
            return nums[left]
        middle = left + (right - left) // 2
        if middle % 2 == 0:
            if nums[middle] == nums[middle + 1]:
                return self.search(nums, middle + 2, right)
            else:
                return self.search(nums, left, middle)
        else:
            if nums[middle] == nums[middle - 1]:
                return self.search(nums, middle + 1, right)
            else:
                return self.search(nums, left, middle - 1)

    def singleNonDuplicate(self, nums: [int]) -> int:
        return self.search(nums, 0, len(nums) - 1)

# Tests
assert Solution().singleNonDuplicate([1,1,2,3,3,4,4,8,8]) == 2
assert Solution().singleNonDuplicate([3,3,7,7,10,11,11]) == 10
