#!/usr/bin/env python3

# Day 18: Numbers With Same Consecutive Differences
#
# Return all non-negative integers of length N such that the absolute
# difference between every two consecutive digits is K.
# Note that every number in the answer must not have leading zeros except for
# the number 0 itself. For example, 01 has one leading zero and is invalid, but
# 0 is valid.
# You may return the answer in any order.
#
# Note:
# 1 <= N <= 9
# 0 <= K <= 9

class Solution:
    def numsSameConsecDiff(self, N: int, K: int) -> [int]:
        # Edge case
        if N == 1:
            return list(range(10))

        numbers = []

        # Recursively search possible numbers
        def buildNumbers(N, number):
            if N == 0:
                numbers.append(number)
            else:
                last_digit = number % 10
                if K == 0:
                    next_digits = [last_digit]
                else:
                    next_digits = []
                    if last_digit - K >= 0:
                        next_digits.append(last_digit - K)
                    if last_digit + K < 10:
                        next_digits.append(last_digit + K)
                for next_digit in next_digits:
                    buildNumbers(N - 1, number * 10 + next_digit)

        for first_digit in range(1, 10):
            buildNumbers(N - 1, first_digit)
        
        return numbers

# Tests
numbers = Solution().numsSameConsecDiff(3, 7)
expected = [181,292,707,818,929]
assert len(numbers) == len(expected) and set(numbers) == set(expected)
numbers = Solution().numsSameConsecDiff(2, 1)
expected = [10,12,21,23,32,34,43,45,54,56,65,67,76,78,87,89,98]
assert len(numbers) == len(expected) and set(numbers) == set(expected)
numbers = Solution().numsSameConsecDiff(1, 9)
expected = [0,1,2,3,4,5,6,7,8,9]
assert len(numbers) == len(expected) and set(numbers) == set(expected)
