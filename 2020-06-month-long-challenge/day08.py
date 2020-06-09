#!/usr/bin/env python3

# Day 8: Power of Two
#
# Given an integer, write a function to determine if it is a power of two.

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and (n & (n - 1)) == 0

# Tests
assert Solution().isPowerOfTwo(1) == True
assert Solution().isPowerOfTwo(16) == True
assert Solution().isPowerOfTwo(218) == False
assert Solution().isPowerOfTwo(-16) == False
