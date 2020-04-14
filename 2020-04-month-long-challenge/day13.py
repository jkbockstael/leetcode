#!/usr/bin/env python3

# Day 13: Contiguous Array
#
# Given a binary array, find the maximum length of a contiguous subarray with equal number of 0 and 1.

class Solution:
    def findMaxLength(self, nums: [int]) -> int:
        counts = {0: -1}
        longest = 0
        count = 0
        for i in range(len(nums)):
            count += -1 if nums[i] == 0 else 1
            if count not in counts:
                counts[count] = i
            else:
                longest = max(longest, i - counts[count])
        return longest

# Test
assert Solution().findMaxLength([0,1]) == 2
assert Solution().findMaxLength([0,1,0]) == 2
assert Solution().findMaxLength([0,0,0]) == 0
assert Solution().findMaxLength([0,0,0,1,0,1,1]) == 6
