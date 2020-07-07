#!/usr/bin/env python3

# Day 6: Plus One
#
# Given a non-empty array of digits representing a non-negative integer, plus
# one to the integer.
# The digits are stored such that the most significant digit is at the head of
# the list, and each element in the array contain a single digit.
# You may assume the integer does not contain any leading zero, except the
# number 0 itself.

class Solution:
    def plusOne(self, digits: [int]) -> [int]:
        # "Your runtime beats 70.54 % of python3 submissions."
        # "Your memory usage beats 82.55 % of python3 submissions."
        # Online test cases include very long numbers that would choke integer
        # sizes in other languages, but the glorious snake can handle anything
        return list(map(int, list(str(int("".join(map(str, digits)))+ 1))))

# Tests
assert Solution().plusOne([1,2,3]) == [1,2,4]
assert Solution().plusOne([4,3,2,1]) == [4,3,2,2]
