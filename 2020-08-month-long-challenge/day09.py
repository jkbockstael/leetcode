#!/usr/bin/env python3

# Day 9: Rotting Oranges
#
# In a given grid, each cell can have one of three values:
# - the value 0 representing an empty cell;
# - the value 1 representing a fresh orange;
# - the value 2 representing a rotten orange.
#
# Every minute, any fresh orange that is adjacent (4-directionally) to a rotten
# orange becomes rotten.
# Return the minimum number of minutes that must elapse until no cell has a
# fresh orange.  If this is impossible, return -1 instead.
#
# Note:
# - 1 <= grid.length <= 10
# - 1 <= grid[0].length <= 10
# - grid[i][j] is only 0, 1, or 2

class Solution:
    def orangesRotting(self, grid: [[int]]) -> int:
        def copy(grid):
            return [[cell for cell in row] for row in grid]
        
        def fresh(grid):
            return sum(row.count(1) for row in grid)

        if fresh(grid) == 0:
            return 0

        turn = 0
        while True:
            turn += 1
            # Copy grid to next grid
            next_grid = copy(grid)
            # Spread the pestilence (is that a death metal band name?)
            for row in range(len(grid)):
                for column in range(len(grid[0])):
                    if grid[row][column] == 2:
                        neighbors = []
                        if row > 0:
                            neighbors.append((row - 1, column))
                        if row < len(grid) - 1:
                            neighbors.append((row + 1, column))
                        if column > 0:
                            neighbors.append((row, column - 1))
                        if column < len(grid[0]) - 1:
                            neighbors.append((row, column + 1))
                        for r, c in neighbors:
                            if grid[r][c] == 1:
                                next_grid[r][c] = 2
            # Is everything rotten now ?
            if fresh(next_grid) == 0:
                return turn
            # Is the situation stalled ?
            if fresh(next_grid) == fresh(grid):
                return - 1
            # Commit the changes for the next turn
            grid = copy(next_grid)

# Tests
assert Solution().orangesRotting([[2,1,1],[1,1,0],[0,1,1]]) == 4
assert Solution().orangesRotting([[2,1,1],[0,1,1],[1,0,1]]) == -1
