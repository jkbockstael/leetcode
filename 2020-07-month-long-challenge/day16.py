#!/usr/bin/env python3

# Day 16: Pow(x, n)
#
# Implement pow(x, n), which calculates x raised to the power n (xn).
#
# Note:
# - -100.0 < x < 100.0
# - n is a 32-bit signed integer, within the range [−231, 231 − 1]

class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 0:
            return 0
        if x == 1:
            return 1
        if n == 0:
            return 1
        if n < 0:
            return self.myPow(1 / x, -n)
        if n % 2 == 0:
            return self.myPow(x * x, n // 2)
        return x * self.myPow(x, n - 1)

# Tests
assert abs(Solution().myPow(2.0, 10) - 1024.0) < 0.00001
assert abs(Solution().myPow(2.1, 3) - 9.261) < 0.00001
assert abs(Solution().myPow(2.0, -2) - 0.25) < 0.00001
assert abs(Solution().myPow(0.00001, 2147483647) - 0.0) < 0.00001
