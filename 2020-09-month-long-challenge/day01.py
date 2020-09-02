#!/usr/bin/env python3

# Day 1: Largest Time for Given Digits
#
# Given an array of 4 digits, return the largest 24 hour time that can be made.
# The smallest 24 hour time is 00:00, and the largest is 23:59. Starting from
# 00:00, a time is larger if more time has elapsed since midnight.
# Return the answer as a string of length 5.  If no valid time can be made,
# return an empty string.

import itertools

class Solution:
    def largestTimeFromDigits(self, A: [int]) -> str:
        # Glory to the snake
        return max(("%d%d:%d%d" % permutation
            for permutation in itertools.permutations(A)
            if permutation[:2] < (2, 4) and permutation[2] < 6), default = "")

# Tests
assert Solution().largestTimeFromDigits([1,2,3,4]) == "23:41"
assert Solution().largestTimeFromDigits([5,5,5,5]) == ""
