#!/usr/bin/env python3

# Day 10: Excel Sheet Column Number
#
# Given a column title as appear in an Excel sheet, return its corresponding
# column number.
# A = 1
# B = 2
# C = 3
# ...
# Z = 26
# AA = 27
# AB = 28
# ...

class Solution:
    def titleToNumber(self, s: str) -> int:
        # In other words, convert from base 26 to base 10, plus 1 as we
        # don't start at zero
        decimal = 0
        for digit in s:
            decimal *= 26
            decimal += ord(digit) - ord("A") + 1
        return decimal

# Tests
assert Solution().titleToNumber("A") == 1
assert Solution().titleToNumber("AB") == 28
assert Solution().titleToNumber("ZY") == 701
