#!/usr/bin/env python3

# Day 21: Count Square Submatrices with All Ones
#
# Given a m * n matrix of ones and zeros, return how many square submatrices
# have all ones.
#
# Constraints:
# - 1 <= arr.length <= 300
# - 1 <= arr[0].length <= 300
# - 0 <= arr[i][j] <= 1

class Solution:
    def countSquares(self, matrix: [[int]]) -> int:
        for row in range(1, len(matrix)):
            for column in range(1, len(matrix[0])):
                matrix[row][column] *= min( \
                    matrix[row - 1][column], \
                    matrix[row][column - 1], \
                    matrix[row - 1][column - 1] \
                    ) + 1
        return sum(map(sum, matrix))

# Tests
test_matrix = [
    [0,1,1,1],
    [1,1,1,1],
    [0,1,1,1]]
assert Solution().countSquares(test_matrix) == 15
test_matrix = [
    [1,0,1],
    [1,1,0],
    [1,1,0]]
assert Solution().countSquares(test_matrix) == 7
