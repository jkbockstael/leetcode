#!/usr/bin/env python3

# Day 25: Find the Duplicate Number
#
# Given an array nums containing n + 1 integers where each integer is between 1
# and n (inclusive), prove that at least one duplicate number must exist.
# Assume that there is only one duplicate number, find the duplicate one.
#
# Note:
# - You must not modify the array (assume the array is read only).
# - You must use only constant, O(1) extra space.
# - Your runtime complexity should be less than O(n^2).
# - There is only one duplicate number in the array, but it could be repeated
# more than once.

class Solution:
    def findDuplicate(self, nums: [int]) -> int:
        # This is equivalent to finding a cycle in a graph
        # Hello, Floyd
        # First synchronise two pointers at an intersection point by having
        # them walk the graph at different speeds until they meet
        hare = nums[0]
        tortoise = nums[0]
        while True:
            # The hare takes two steps each time the tortoise takes one
            hare = nums[nums[hare]]
            tortoise = nums[tortoise]
            # ... until they meet
            if hare == tortoise:
                break
        # Then take the tortoise out of the cycle and make it walk the graph
        # from the root, it will meet the hare at the first node in the cycle
        tortoise = nums[0]
        while tortoise != hare:
            hare = nums[hare]
            tortoise = nums[tortoise]
        return tortoise

# Tests
assert Solution().findDuplicate([1,3,4,2,2]) == 2
assert Solution().findDuplicate([3,1,3,4,2]) == 3
