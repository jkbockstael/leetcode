#!/usr/bin/env python3

# Day 26: Add Digits
#
# Given a non-negative integer num, repeatedly add all its digits until the
# result has only one digit.
# Could you do it without any loop/recursion in O(1) runtime?

class Solution:
    def addDigits(self, num: int) -> int:
        if num == 0:
            return 0
        elif num % 9 == 0:
            return 9
        else:
            return num % 9

# Tests
assert Solution().addDigits(38) == 2
assert Solution().addDigits(0) == 0
