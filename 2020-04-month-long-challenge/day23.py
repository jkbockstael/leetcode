#!/usr/bin/env python3

# Day 23: Bitwise AND of Numbers Range
#
# Given a range [m, n] where 0 <= m <= n <= 2147483647, return the bitwise AND
# of all numbers in this range, inclusive.

class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        power = 0
        # The problem states that n <= 2**31 - 1
        while power < 31:
            low = 2**power
            high = 2**(power + 1)
            if m >= low and n < high:
                return low + self.rangeBitwiseAnd(m - low, n - low)
            power += 1
        return 0

# Tests
assert Solution().rangeBitwiseAnd(5, 7) == 4
assert Solution().rangeBitwiseAnd(0, 1) == 0
assert Solution().rangeBitwiseAnd(3, 3) == 3
assert Solution().rangeBitwiseAnd(6, 7) == 6
assert Solution().rangeBitwiseAnd(1, 2) == 0
assert Solution().rangeBitwiseAnd(12, 14) == 12
assert Solution().rangeBitwiseAnd(10, 12) == 8
