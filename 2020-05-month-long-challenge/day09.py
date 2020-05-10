#!/usr/bin/env python3

# Day 9: Valid Perfect Square
#
# Given a positive integer num, write a function which returns True if num is a
# perfect square else False.
# Note: Do not use any built-in library function such as sqrt.

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        # Zero and one are squares of themselves
        if num == 0 or num == 1:
            return True
        # Squares can't have any last digit, this allows ruling out almost half
        # the candidates
        if num % 10 not in [0, 1, 4, 5, 6, 9]:
            return False
        # Even numbers produce even squares, odd numbers produce odd squares
        if num % 2 == 0:
            start = 2
        else:
            start = 1
        # Straightforward linear search as it is fast enough for the input size
        for candidate in range(start, num // 2 + 1, 2):
            if candidate ** 2 == num:
                return True
        return False

# Tests
assert Solution().isPerfectSquare(16) == True
assert Solution().isPerfectSquare(14) == False
assert Solution().isPerfectSquare(0) == True
assert Solution().isPerfectSquare(1) == True
assert Solution().isPerfectSquare(4) == True
assert Solution().isPerfectSquare(3481) == True
assert Solution().isPerfectSquare(2147483647) == False
