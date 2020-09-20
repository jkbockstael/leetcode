#!/usr/bin/env python3

# Day 19: Sequential Digits
#
# An integer has sequential digits if and only if each digit in the number is
# one more than the previous digit.
# Return a sorted list of all the integers in the range [low, high] inclusive
# that have sequential digits.

import itertools

class Solution:
    def sequentialDigits(self, low: int, high: int) -> [int]:
        digits = '123456789'
        numbers = []

        # Slide into these digits to generate all possible numbers
        for i in range(len(digits)):
            for j in range(i + 2, len(digits) + 1):
                number = int(digits[i:j])
                # Keep only the good ones
                if low <= number <= high:
                    numbers.append(number)
        
        return sorted(numbers)

# Tests
assert Solution().sequentialDigits(100, 300) == [123,234]
assert Solution().sequentialDigits(1000, 13000) == [1234,2345,3456,4567,5678,6789,12345]
