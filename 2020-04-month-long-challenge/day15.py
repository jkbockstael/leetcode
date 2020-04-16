#!/usr/bin/env python3

# Day 15: Product of Array Except Self
#
# Given an array nums of n integers where n > 1,  return an array output such
# that output[i] is equal to the product of all the elements of nums except
# nums[i].
# Constraint: It's guaranteed that the product of the elements of any prefix or
# suffix of the array (including the whole array) fits in a 32 bit integer.
# Note: Please solve it without division and in O(n).
# Follow up:
# - Could you solve it with constant space complexity? (The output array does
# not count as extra space for the purpose of space complexity analysis.)

class Solution:
    def productExceptSelf(self, nums: [int]) -> [int]:
        output = [1] + [0 for _ in nums[1:]]
        # left to right
        for i in range(1, len(nums)):
            output[i] = output[i - 1] * nums[i - 1]
        # right to left
        product_on_right = 1
        for i in range(len(nums)-1, -1, -1):
            output[i] *= product_on_right
            product_on_right *= nums[i]
        return output

# Test
assert Solution().productExceptSelf([1,2,3,4]) == [24,12,8,6]
