#!/usr/bin/env python3

# Day 27: Maximal Square
#
# Given a 2D binary matrix filled with 0's and 1's, find the largest square
# containing only 1's and return its area.

class Solution:
    def maximalSquare(self, matrix: [[str]]) -> int:
        # Uber Brute Force
        # still "Your runtime beats 18.29 % of python3 submissions."
        rows = len(matrix)
        if rows == 0:
            return 0
        columns = len(matrix[0])
        largest_size = 0
        size = 0
        for row in range(rows):
            for column in range(columns):
                if matrix[row][column] == '1':
                    size = 1
                    in_square = True
                    while in_square and row + size < rows \
                        and column + size < columns:
                        for x in range(row, row + size + 1):
                            if matrix[x][column + size] == '0':
                                in_square = False
                                break
                        for y in range(column, column + size + 1):
                            if matrix[row + size][y] == '0':
                                in_square = False
                                break
                        if in_square:
                            size += 1
                    if size > largest_size:
                        largest_size = size
        return largest_size ** 2

# Test
test_matrix = [["1","0","1","0","0"],["1","0","1","1","1"],
    ["1","1","1","1","1"],["1","0","0","1","0"]]
assert Solution().maximalSquare(test_matrix) == 4
