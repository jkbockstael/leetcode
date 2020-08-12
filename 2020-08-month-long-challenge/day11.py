#!/usr/bin/env python3

# Day 11: H-Index II
#
# Given an array of citations sorted in ascending order (each citation is a
# non-negative integer) of a researcher, write a function to compute the
# researcher's h-index.
# According to the definition of h-index on Wikipedia: "A scientist has index h
# if h of his/her N papers have at least h citations each, and the other N − h
# papers have no more than h citations each."
#
# Notes:
# - If there are several possible values for h, the maximum one is taken as the
#   h-index.
# - Expected runtime complexity is in O(log n) and the input is sorted.

class Solution:
    def hIndex(self, citations: [int]) -> int:
        # This problem appeared during the June Challenge, but back then the
        # input was sorted
        citations = sorted(citations)
        count = len(citations)
        if count == 0:
            return 0
        # Binary search
        left = 0
        right = count - 1
        while left <= right:
            middle = (left + right) // 2
            if citations[middle] + middle < count:
                left = middle + 1
            else:
                right = middle - 1
        return count - left

# Test
assert Solution().hIndex([3,0,6,1,5]) == 3
