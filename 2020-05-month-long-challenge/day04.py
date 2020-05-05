#!/usr/bin/env python3

# Day 4: Number Complement
#
# Given a positive integer, output its complement number. The complement
# strategy is to flip the bits of its binary representation.

class Solution:
    def findComplement(self, num: int) -> int:
        return (1 << len(bin(num)) - 2) - 1 - num

# Tests
assert Solution().findComplement(5) == 2
assert Solution().findComplement(1) == 0
