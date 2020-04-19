#!/usr/bin/env python3

# Day 18: Minimum Path Sum
#
# Given a m x n grid filled with non-negative numbers, find a path from top left
# to bottom right which minimizes the sum of all numbers along its path.
# Note: You can only move either down or right at any point in time.

class Solution:
    def minPathSum(self, grid: [[int]]) -> int:
        height = len(grid)
        if height == 0:
            return 0
        width = len(grid[0])
        costs = [[0 for y in x] for x in grid]
        for row in range(height):
            for col in range(width):
                costs[row][col] += grid[row][col]
                origins = []
                if row > 0:
                    origins.append((row - 1, col))
                if col > 0:
                    origins.append((row, col - 1))
                if len(origins) > 0:
                    costs[row][col] += min(costs[x][y] for x, y in origins)
        return costs[height - 1][width - 1]

# Tests
assert Solution().minPathSum([[1,3,1],[1,5,1],[4,2,1]]) == 7
assert Solution().minPathSum([[1]]) == 1
assert Solution().minPathSum([]) == 0
