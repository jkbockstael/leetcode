#!/usr/bin/env python3

# Day 20: Permutation Sequence
#
# The set [1,2,3,...,n] contains a total of n! unique permutations.
# By listing and labeling all of the permutations in order, we get the
# following sequence for n = 3:
# 1 - "123"
# 2 - "132"
# 3 - "213"
# 4 - "231"
# 5 - "312"
# 6 - "321"
#
# Given n and k, return the kth permutation sequence.
#
# Note:
# - Given n will be between 1 and 9 inclusive.
# - Given k will be between 1 and n! inclusive.

import math

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        digits = [str(x) for x in range(1, n + 1)]
        permutation = ""
        k = k - 1
        perms = math.factorial(n)
        while digits != []:
            perms = perms // len(digits)
            digit = k // perms
            k = k % perms
            permutation += digits.pop(digit)
        return permutation

# Tests
assert Solution().getPermutation(3, 3) == "213"
assert Solution().getPermutation(4, 9) == "2314"
