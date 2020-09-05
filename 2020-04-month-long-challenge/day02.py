#!/usr/bin/env python3

# Day 2: Happy Number
#
# Write an algorithm to determine if a number is "happy".
# A happy number is a number defined by the following process: Starting with
# any positive integer, replace the number by the sum of the squares of its
# digits, and repeat the process until the number equals 1 (where it will stay),
# or it loops endlessly in a cycle which does not include 1. Those numbers for
# which this process ends in 1 are happy numbers.

class Solution:
    def perfect_digital_invariant(self, n: int) -> int:
        total = 0
        while n > 0:
            total = total + pow(n % 10, 2)
            n = int(n / 10)
        return total

    def isHappy(self, n: int) -> bool:
        visited = []
        while n > 1 and n not in visited:
            visited.append(n)
            n = self.perfect_digital_invariant(n)
        return n == 1

# Tests
assert Solution().isHappy(19) == True
assert Solution().isHappy(20) == False
