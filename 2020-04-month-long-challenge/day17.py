#!/usr/bin/env python3

# Day 17: Number of Islands
#
# Given a 2d grid map of '1's (land) and '0's (water), count the number of
# islands. An island is surrounded by water and is formed by connecting adjacent
# lands horizontally or vertically. You may assume all four edges of the grid
# are all surrounded by water.

class Solution:
    def neighbors(self, x: int, y: int, width: int, height: int) -> [(int,int)]:
        coords = []
        for offset in [-1, 1]:
            coords.append((x + offset, y))
            coords.append((x, y + offset))
        return [(x, y) for x, y in coords if 0 <= x < height and 0 <= y < width]

    def walk_island(self, x: int, y: int) -> None:
        self.grid[x][y] = None
        for x, y in self.neighbors(x, y, len(self.grid[0]), len(self.grid)):
            if self.grid[x][y] == '1':
                self.walk_island(x, y)

    def numIslands(self, grid: [[str]]) -> int:
        if len(grid) == 0:
            return 0
        self.grid = grid
        island_count = 0
        for x, line in enumerate(grid):
            for y, cell in enumerate(line):
                if cell == '1':
                    island_count += 1
                    self.walk_island(x, y)
        return island_count

# Tests
def parse_test_grid(grid: str) -> [[str]]:
    return [[char for char in line] for line in grid.split("\n")]
test_grid = """11110
11010
11000
00000"""
assert Solution().numIslands(parse_test_grid(test_grid)) == 1
test_grid = """11000
11000
00100
00011"""
assert Solution().numIslands(parse_test_grid(test_grid)) == 3
test_grid = ""
assert Solution().numIslands(parse_test_grid(test_grid)) == 0
test_grid = """111
010
111"""
assert Solution().numIslands(parse_test_grid(test_grid)) == 1
test_grid = """10111
10101
11101"""
assert Solution().numIslands(parse_test_grid(test_grid)) == 1
