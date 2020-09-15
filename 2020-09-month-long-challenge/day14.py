#!/usr/bin/env python3

# Day 14: House Robber
#
# You are a professional robber planning to rob houses along a street. Each
# house has a certain amount of money stashed, the only constraint stopping you
# from robbing each of them is that adjacent houses have security system
# connected and it will automatically contact the police if two adjacent houses
# were broken into on the same night.
#
# Given a list of non-negative integers representing the amount of money of
# each house, determine the maximum amount of money you can rob tonight without
# alerting the police.

class Solution:
    def rob(self, nums: [int]) -> int:
        # Edge cases
        if len(nums) == 0:
            return 0
        if len(nums) < 3:
            return max(nums)
        
        loot = [0 for _ in nums]
        loot[0] = nums[0]
        loot[1] = max(nums[0:2])

        for i in range(2, len(nums)):
            loot[i] = max(loot[i - 1], loot[i - 2] + nums[i])

        return loot[-1]

# Tests
assert Solution().rob([1,2,3,1]) == 4
assert Solution().rob([2,7,9,3,1]) == 12
