#!/usr/bin/env python3

# Day 4: Power of Four
#
# Given an integer (signed 32 bits), write a function to check whether it is a
# power of 4.
#
# Follow up: Could you solve it without loops/recursion?

class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        # 4^x is 2^2x, so we're looking for a single bit followed by an even
        # number of 0
        num_binary = bin(num)
        return num > 0 \
            and len(num_binary) % 2 == 1 \
            and num_binary.count('1') == 1 \

# Tests
assert Solution().isPowerOfFour(16) == True
assert Solution().isPowerOfFour(5) == False
assert Solution().isPowerOfFour(-2147483648) == False
