#!/usr/bin/env python3

# Day 3: Prison Cells After N Days
#
# There are 8 prison cells in a row, and each cell is either occupied or
# vacant.
#
# Each day, whether the cell is occupied or vacant changes according to the
# following rules:
# - If a cell has two adjacent neighbors that are both occupied or both vacant,
#   then the cell becomes occupied.
# - Otherwise, it becomes vacant.
#
# We describe the current state of the prison in the following way: cells[i] ==
# 1 if the i-th cell is occupied, else cells[i] == 0.
#
# Given the initial state of the prison, return the state of the prison after N
# days (and N such changes described above.)
#
# Note:
# - cells.length == 8
# - cells[i] is in {0, 1}
# - 1 <= N <= 10^9

class Solution:
    def prisonAfterNDays(self, cells: [int], N: int) -> [int]:
        N = N % 14 # there's a period of 14 days
        N = 14 if N == 0 else N # zero is a nasty value
        for day in range(N):
            next_cells = [0 for _ in cells]
            for cell in range(1, len(cells) - 1): # first and last won't change
                next_cells[cell] = (cells[cell - 1] ^ cells[cell + 1]) ^ 1
            cells = next_cells
        return cells

# Tests
assert Solution().prisonAfterNDays([0,1,0,1,1,0,0,1], 7) == [0,0,1,1,0,0,0,0]
assert Solution().prisonAfterNDays([1,0,0,1,0,0,1,0], 1000000000) == [0,0,1,1,1,1,1,0]
assert Solution().prisonAfterNDays([1,0,0,1,0,0,0,1], 826) == [0,1,1,0,1,1,1,0]
