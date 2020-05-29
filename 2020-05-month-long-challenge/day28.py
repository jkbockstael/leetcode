#!/usr/bin/env python3

# Day 28: Counting Bits
#
# Given a non negative integer number num. For every numbers i in the range 0 ≤
# i ≤ num calculate the number of 1's in their binary representation and return
# them as an array.

class Solution:
    def countBits(self, num: int) -> [int]:
        return [len(bin(x)[2:].replace('0','')) for x in range(0, num + 1)]

assert Solution().countBits(2) == [0,1,1]
assert Solution().countBits(5) == [0,1,1,2,1,2]
