#!/usr/bin/env python3

# Day 21: Leftmost Column with at Least a One
#
# (This problem is an interactive problem.)
# A binary matrix means that all elements are 0 or 1. For each individual row
# of the matrix, this row is sorted in non-decreasing order.
# Given a row-sorted binary matrix binaryMatrix, return leftmost column
# index(0-indexed) with at least a 1 in it. If such index doesn't exist, return
# -1.
#
# You can't access the Binary Matrix directly.  You may only access the matrix
# using a BinaryMatrix interface:
# - BinaryMatrix.get(x, y) returns the element of the matrix at index (x, y)
#   (0-indexed).
# - BinaryMatrix.dimensions() returns a list of 2 elements [n, m], which means
#   the matrix is n * m.
#
# Submissions making more than 1000 calls to BinaryMatrix.get will be judged
# Wrong Answer.  Also, any solutions that attempt to circumvent the judge will
# result in disqualification.
#
# Constraints:
# - 1 <= mat.length, mat[i].length <= 100
# - mat[i][j] is either 0 or 1.
# - mat[i] is sorted in a non-decreasing way.

# Implemented for testing purpose
class BinaryMatrix(object):
    def __init__(self, values: [[int]]):
        self.vals = values

    def get(self, x: int, y: int) -> int:
        return self.vals[x][y]

    def dimensions(self) -> [int]:
        return [len(self.vals), len(self.vals[0])]

class Solution():
    def leftMostColumnWithOne(self, binaryMatrix: BinaryMatrix) -> int:
        rows, columns = binaryMatrix.dimensions()
        # We're looking for the leftmost value so let's scan from right to left
        row, column = 0, columns - 1
        leftmost = None
        while row < rows and column >= 0:
            value = binaryMatrix.get(row, column)
            if value == 0:
                row += 1
            if value == 1:
                leftmost = column
                column -= 1
        return leftmost if leftmost is not None else -1

# Tests
assert Solution().leftMostColumnWithOne(BinaryMatrix([[0,0],[1,1]])) == 0
assert Solution().leftMostColumnWithOne(BinaryMatrix([[0,0],[0,1]])) == 1
assert Solution().leftMostColumnWithOne(BinaryMatrix([[0,0],[0,0]])) == -1
assert Solution().leftMostColumnWithOne(BinaryMatrix([[0,0,0,1],[0,0,1,1],[0,1,1,1]])) == 1
assert Solution().leftMostColumnWithOne(BinaryMatrix([[1]])) == 0
assert Solution().leftMostColumnWithOne(BinaryMatrix([[0]])) == -1
