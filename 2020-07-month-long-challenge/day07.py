#!/usr/bin/env python3

# Day 7: Island Perimeter
#
# You are given a map in form of a two-dimensional integer grid where 1
# represents land and 0 represents water.
# Grid cells are connected horizontally/vertically (not diagonally). The grid
# is completely surrounded by water, and there is exactly one island (i.e., one
# or more connected land cells).
# The island doesn't have "lakes" (water inside that isn't connected to the
# water around the island). One cell is a square with side length 1. The grid
# is rectangular, width and height don't exceed 100. Determine the perimeter of
# the island.

class Solution:
    def islandPerimeter(self, grid: [[int]]) -> int:
        # This is not the most subtle approach, but it gets the job done fast
        # enough and without extra memory
        def neighbors(row, col):
            count = 0
            if row > 0:
                count += grid[row - 1][col]
            if row < len(grid) - 1:
                count += grid[row + 1][col]
            if col > 0:
                count += grid[row][col - 1]
            if col < len(grid[0]) - 1:
                count += grid[row][col + 1]
            return count
        perimeter = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    perimeter += 4 - neighbors(row, col)
        return perimeter

# Test
test_grid = [[0,1,0,0],
    [1,1,1,0],
    [0,1,0,0],
    [1,1,0,0]]
assert Solution().islandPerimeter(test_grid) == 16
