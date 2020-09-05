#!/usr/bin/env python3

# Day 7: Counting Elements
#
# Given an integer array arr, count element x such that x + 1 is also in arr.
# If there're duplicates in arr, count them seperately.

class Solution:
    def countElements(self, arr: [int]) -> int:
        return sum(1 for x in arr if x + 1 in arr)

# Tests
assert Solution().countElements([1,2,3]) == 2
assert Solution().countElements([1,1,3,3,5,5,7,7]) == 0
assert Solution().countElements([1,3,2,3,5,0]) == 3
assert Solution().countElements([1,1,2,2]) == 2
