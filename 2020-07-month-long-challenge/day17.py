#!/usr/bin/env python3

# Day 17: Top K Frequent Elements
#
# Given a non-empty array of integers, return the k most frequent elements.

import collections

class Solution:
    def topKFrequent(self, nums: [int], k: int) -> [int]:
        value = lambda couple: couple[0]
        return list(map(value, collections.Counter(nums).most_common(k)))

# Tests
assert Solution().topKFrequent([1,1,1,2,2,3], 2) == [1,2]
assert Solution().topKFrequent([1], 1) == [1]
