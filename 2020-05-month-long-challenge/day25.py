#!/usr/bin/env python3

# Day 25: Uncrossed Lines
#
# We write the integers of A and B (in the order they are given) on two
# separate horizontal lines.
#
# Now, we may draw connecting lines: a straight line connecting two numbers
# A[i] and B[j] such that:
# - A[i] == B[j];
# - The line we draw does not intersect any other connecting (non-horizontal)
#   line.
#
# Note that a connecting lines cannot intersect even at the endpoints: each
# number can only belong to one connecting line.
# Return the maximum number of connecting lines we can draw in this way.
#
# Note:
# - 1 <= A.length <= 500
# - 1 <= B.length <= 500
# - 1 <= A[i], B[i] <= 2000

class Solution:
    def __init__(self):
        self.memo = {}
        
    def maxUncrossedLinesRec(self, A: [int], B: [int], i: int, j: int):
        # Base case
        if i == len(A) or j == len(B):
            return 0
        # Memoized case
        if (i, j) in self.memo:
            return self.memo[i, j]
        # General case
        if A[i] == B[j]:
            # A line can be drawn, count it and move both cursors
            count = 1 + self.maxUncrossedLinesRec(A, B, i + 1, j + 1)
        else:
            # No line can be drawn and there are two ways to move the cursors
            # We're interested only in the best one
            count = max(self.maxUncrossedLinesRec(A, B, i + 1, j), \
                self.maxUncrossedLinesRec(A, B, i, j + 1))
        self.memo[i, j] = count
        return count

    def maxUncrossedLines(self, A: [int], B: [int]) -> int:
        return self.maxUncrossedLinesRec(A, B, 0, 0)

# Tests
assert Solution().maxUncrossedLines([1,4,2], [1,2,4]) == 2
assert Solution().maxUncrossedLines([2,5,1,2,5], [10,5,2,1,5,2]) == 3
assert Solution().maxUncrossedLines([1,3,7,1,7,5], [1,9,2,5,1]) == 2
