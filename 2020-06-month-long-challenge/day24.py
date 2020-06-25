#!/usr/bin/env python3

# Day 24: Unique Binary Search Trees
#
# Given n, how many structurally unique BST's (binary search trees) that store
# values 1 ... n?

class Solution:
    def numTrees(self, n: int) -> int:
        # No need to generate the actual trees, we only need to know how many
        # there are
        uniques = [1, 1, 2] + [0 for _ in range(3, n + 1)]
        for i in range(3, n + 1):
            for j in range(i):
                uniques[i] = uniques[i] + uniques[j] * uniques[i - j - 1]
        return uniques[n]

# Tests
assert Solution().numTrees(0) == 1
assert Solution().numTrees(1) == 1
assert Solution().numTrees(2) == 2
assert Solution().numTrees(3) == 5
