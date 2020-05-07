#!/usr/bin/env python3

# Day 6: Majority Element
#
# Given an array of size n, find the majority element. The majority element is
# the element that appears more than ⌊ n/2 ⌋ times.
# You may assume that the array is non-empty and the majority element always
# exist in the array.

import collections

class Solution:
    def majorityElement(self, nums: [int]) -> int:
        return collections.Counter(nums).most_common(1)[0][0]

# Tests
assert Solution().majorityElement([3,2,3]) == 3
assert Solution().majorityElement([2,2,1,1,1,2,2]) == 2
