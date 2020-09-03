#!/usr/bin/env python3

# Day 2: Contains Duplicate III
#
# Given an array of integers, find out whether there are two distinct indices i
# and j in the array such that the absolute difference between nums[i] and
# nums[j] is at most t and the absolute difference between i and j is at most
# k.

class Solution:
    def containsNearbyAlmostDuplicate(self, nums: [int], k: int, t: int) -> bool:
        # Edge case
        if t == 0 and len(nums) == len(set(nums)):
            return False

        # General case, quite brutal but it gets thejob done
        for i, value in enumerate(nums):
            for j in range(i + 1, min(i + k + 1, len(nums))):
                if abs(value - nums[j]) <= t:
                    return True

        return False

# Tests
assert Solution().containsNearbyAlmostDuplicate([1,2,3,1], 3, 0) == True
assert Solution().containsNearbyAlmostDuplicate([1,0,1,1], 1, 2) == True
assert Solution().containsNearbyAlmostDuplicate([1,5,9,1,5,9], 2, 3) == False
