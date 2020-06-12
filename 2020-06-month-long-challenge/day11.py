#!/usr/bin/env python3

# Day 11: Sort Colors
#
# Given an array with n objects colored red, white or blue, sort them in-place
# so that objects of the same color are adjacent, with the colors in the order
# red, white and blue.
# Here, we will use the integers 0, 1, and 2 to represent the color red, white,
# and blue respectively.
#
# Note:
# - You are not suppose to use the library's sort function for this problem.
#
# Follow up:
# - A rather straight forward solution is a two-pass algorithm using counting
#   sort. First, iterate the array counting number of 0's, 1's, and 2's, then
#   overwrite array with total number of 0's, then 1's and followed by 2's.
# - Could you come up with a one-pass algorithm using only constant space?

class Solution:
    def sortColors(self, nums: [int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def swap(a, b):
            nums[a], nums[b] = nums[b], nums[a]
        
        sorted_left = -1
        sorted_right = len(nums)
        current = 0
        while current < sorted_right:
            if nums[current] == 0:
                sorted_left += 1
                swap(current, sorted_left)
                current += 1
            elif nums[current] == 1:
                current += 1
            elif nums[current] == 2:
                sorted_right -= 1
                swap(current, sorted_right)

# Tests
test_array = [2,0,2,1,1,0]
Solution().sortColors(test_array)
assert test_array == [0,0,1,1,2,2]
test_array = [2,0,1]
Solution().sortColors(test_array)
assert test_array == [0,1,2]
