#!/usr/bin/env python3

# Day 4: Move Zeroes
#
# Given an array nums, write a function to move all 0's to the end of it while
# maintaining the relative order of the non-zero elements.
# Notes:
# - You must do this in-place without making a copy of the array.
# - Minimize the total number of operations.

class Solution:
    def moveZeroes(self, nums: [int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # hail the snake
        for i in range(nums.count(0)):
            nums.remove(0)
            nums.append(0)

# modifying input is a heresy
test_input = [0,1,0,3,12]
Solution().moveZeroes(test_input)
assert test_input == [1,3,12,0,0], "[0,1,0,3,12] → [1,3,12,0,0]"
