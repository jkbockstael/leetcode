#!/usr/bin/env python3

# Day 29: Unique Paths
#
# A robot is located at the top-left corner of a m x n grid (marked 'Start' in
# the diagram below).
# The robot can only move either down or right at any point in time. The robot
# is trying to reach the bottom-right corner of the grid.
# How many possible unique paths are there?
#
# Note:
# - 1 <= m, n <= 100
# - It's guaranteed that the answer will be less than or equal to 2 * 10 ^ 9

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = [[None for _ in range(n)] for _ in range(m)]
        def compute(memo, m, n):
            if memo[m][n] is not None:
                return memo[m][n]
            # Base case
            if m == 0 or n == 0:
                memo[m][n] = 1
            # General case
            else:
                memo[m][n] = compute(memo, m - 1, n) + compute(memo, m, n - 1)
            return memo[m][n]
        return compute(memo, m - 1, n - 1)

# Tests
assert Solution().uniquePaths(3, 2) == 3
assert Solution().uniquePaths(7, 3) == 28
