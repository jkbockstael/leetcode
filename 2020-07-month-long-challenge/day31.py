#!/usr/bin/env python3

# Day 31: Climbing Stairs
#
# You are climbing a stair case. It takes n steps to reach to the top.
# Each time you can either climb 1 or 2 steps. In how many distinct ways can
# you climb to the top?

import math

class Solution:
    def climbStairs(self, n: int) -> int:
        # Hello Fibonnaci
        a, b = 1, 1
        for _ in range(n):
            a, b = b, a + b
        return a

# Tests
assert Solution().climbStairs(0) == 1
assert Solution().climbStairs(1) == 1
assert Solution().climbStairs(2) == 2
assert Solution().climbStairs(3) == 3
assert Solution().climbStairs(4) == 5
