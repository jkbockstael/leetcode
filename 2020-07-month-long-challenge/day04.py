#!/usr/bin/env python3

# Day 4: Ugly Number II
#
# Write a program to find the n-th ugly number.
# Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. 
# Note:
# - 1 is typically treated as an ugly number.
# - n does not exceed 1690.

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        uglies = set([1]) # 1 is ugly by convention
        for _ in range(n):
            # Grab the next number in the sequence
            ugly = min(uglies)
            uglies.remove(ugly)
            # Create the next numbers in that sequence
            uglies.add(ugly * 2)
            uglies.add(ugly * 3)
            uglies.add(ugly * 5)
        return ugly

# Tests
assert Solution().nthUglyNumber(10) == 12
assert Solution().nthUglyNumber(1) == 1
assert Solution().nthUglyNumber(10000) == 288325195312500000
