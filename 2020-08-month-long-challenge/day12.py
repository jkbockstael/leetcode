#!/usr/bin/env python3

# Day 12: Pascal's Triangle II
#
# Given a non-negative index k where k ≤ 33, return the kth index row of the
# Pascal's triangle.
# Note that the row index starts from 0.

class Solution:
    def getRow(self, rowIndex: int) -> [int]:
        # Given the maximum input size a direct approach doesn't give any
        # measurable advantage, so here's the naive iterative approach slightly
        # optimized for space
        row = 0
        numbers = [1]
        while row <= rowIndex:
            row += 1
            next_numbers = [0 for _ in range(row)]
            next_numbers[0] = 1
            for column in range(1, row - 1):
                next_numbers[column] = numbers[column - 1] + numbers[column]
            next_numbers[-1] = 1
            numbers = next_numbers
        return numbers

# Tests
assert Solution().getRow(0) == [1]
assert Solution().getRow(3) == [1,3,3,1]
assert Solution().getRow(7) == [1,7,21,35,35,21,7,1]
assert Solution().getRow(33) == [1,33,528,5456,40920,237336,1107568,4272048,13884156,38567100,92561040,193536720,354817320,573166440,818809200,1037158320,1166803110,1166803110,1037158320,818809200,573166440,354817320,193536720,92561040,38567100,13884156,4272048,1107568,237336,40920,5456,528,33,1]
