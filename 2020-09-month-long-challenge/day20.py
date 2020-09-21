#!/usr/bin/env python3

# Day 20: Unique Paths III
#
# On a 2-dimensional grid, there are 4 types of squares:
# - 1 represents the starting square.  There is exactly one starting square.
# - 2 represents the ending square.  There is exactly one ending square.
# - 0 represents empty squares we can walk over.
# - -1 represents obstacles that we cannot walk over.
#
# Return the number of 4-directional walks from the starting square to the
# ending square, that walk over every non-obstacle square exactly once.

class Solution:
    def uniquePathsIII(self, grid: [[int]]) -> int:
        paths_count = 0
        walkable_count = 0
        width = len(grid)
        height = len(grid[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        # Map the grid
        for x in range(width):
            for y in range(height):
                if grid[x][y] == 1:
                    start = (x, y)
                if grid[x][y] == 2:
                    end = (x, y)
                if grid[x][y] == 0:
                    walkable_count += 1

        # Recursive depth-first search
        def dfs(cell, path):
            nonlocal paths_count
            cell_x, cell_y = cell
            for dx, dy in directions:
                x = cell_x + dx
                y = cell_y + dy
                if 0 <= x < width \
                and 0 <= y < height \
                and (x, y) not in path \
                and grid[x][y] != -1:
                    if (x, y) == end and len(path) == walkable_count + 1:
                        paths_count += 1
                    else:
                        dfs((x, y), path + [(x, y)])

        dfs(start, [start])
        return paths_count

# Tests
assert Solution().uniquePathsIII([[1,0,0,0],[0,0,0,0],[0,0,2,-1]]) == 2
assert Solution().uniquePathsIII([[1,0,0,0],[0,0,0,0],[0,0,0,2]]) == 4
assert Solution().uniquePathsIII([[0,1],[2,0]]) == 0
