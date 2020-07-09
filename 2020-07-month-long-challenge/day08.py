#!/usr/bin/env python3

# Day 8: 3Sum
#
# Given an array nums of n integers, are there elements a, b, c in nums such
# that a + b + c = 0? Find all unique triplets in the array which gives the sum
# of zero.
#
# Note:
# - The solution set must not contain duplicate triplets.

class Solution:
    def threeSum(self, nums: [int]) -> [[int]]:
        nums = sorted(nums)
        triplets = []
        for i in range(len(nums)):
            c = nums[i]
            low = 0
            high = len(nums) - 1
            while low < len(nums) - 1 and high > 0:
                a = nums[low]
                b = nums[high]
                if -c == a + b and i not in [low, high] and low != high:
                    triplet = sorted([a, b, c])
                    if triplet not in triplets:
                        triplets.append(triplet)
                if -c < a + b:
                    high -= 1
                else:
                    low += 1
        return triplets

# Test
assert Solution().threeSum([-1,0,1,2,-1,-4]) == [[-1,-1,2],[-1,0,1]]
assert Solution().threeSum([0,0,0]) == [[0,0,0,]]
