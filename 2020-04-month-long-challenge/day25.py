#!/usr/bin/env python3

# Day 25: Jump Game
#
# Given an array of non-negative integers, you are initially positioned at the
# first index of the array.
# Each element in the array represents your maximum jump length at that
# position.
# Determine if you are able to reach the last index.

class Solution:
    def canJump(self, nums: [int]) -> bool:
        leftmost = len(nums) - 1
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] + i >= leftmost:
                leftmost = i
        return leftmost == 0

# Tests
assert Solution().canJump([2,3,1,1,4]) == True
assert Solution().canJump([3,2,1,0,4]) == False
