#!/usr/bin/env python3

# Day 5: Hamming Distance
#
# The Hamming distance between two integers is the number of positions at which the corresponding bits are different.
# Given two integers x and y, calculate the Hamming distance.

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        diff = x ^ y
        bits = 0
        while diff > 0:
            bits += diff & 1
            diff >>= 1
        return bits

# Test
assert Solution().hammingDistance(1, 4) == 2
