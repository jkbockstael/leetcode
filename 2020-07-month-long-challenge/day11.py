#!/usr/bin/env python3

# Day 11: Subsets
#
# Given a set of distinct integers, nums, return all possible subsets (the
# power set).
# Note: The solution set must not contain duplicate subsets.

class Solution:
    def subsets(self, nums: [int]) -> [[int]]:
        def powerset_rec(nums):
            if len(nums) < 2:
                yield nums
                yield []
            else:
                for subset in powerset_rec(nums[1:]):
                    yield [nums[0]] + subset
                    yield subset

        return list(powerset_rec(nums))

# Test
assert Solution().subsets([1,2,3]) == [[1,2,3],[2,3],[1,3],[3],[1,2],[2],[1],[]]
