#!/usr/bin/env python3

# Day 27: Perfect Squares
#
# Given a positive integer n, find the least number of perfect square numbers
# (for example, 1, 4, 9, 16, ...) which sum to n.

class Solution:
    def numSquares(self, n: int) -> int:
        # This approach may seem a bit brute-force, but it still beats 85% of
        # submissions, it's good enough.
        # Get all squares that are smaller than or equal to n
        squares = [x ** 2 for x in range(1, n + 1) if x ** 2 <= n]
        # Is n a perfect square?
        if n in squares:
            return 1
        # Is n the sum of two squares?
        for a in squares:
            if n - a in squares:
                return 2
        # Is n the sum of three squares?
        for a in squares:
            for b in squares:
                if n - a - b in squares:
                    return 3
        # Then Number Theory tells us it's the sum of four squares
        return 4

# Tests
assert Solution().numSquares(12) == 3
assert Solution().numSquares(13) == 2
assert Solution().numSquares(14) == 3
assert Solution().numSquares(15) == 4
assert Solution().numSquares(16) == 1
