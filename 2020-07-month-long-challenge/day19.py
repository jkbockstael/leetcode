#!/usr/bin/env python3

# Day 19: Add Binary
#
# Given two binary strings, return their sum (also a binary string).
# The input strings are both non-empty and contains only characters 1 or 0.
#
# Note:
# - Each string consists only of '0' or '1' characters.
# - 1 <= a.length, b.length <= 10^4
# - Each string is either "0" or doesn't contain any leading zero.

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # In real life that's what I would do:
        #     return bin(int(a, 2) + int(b, 2))[2:]
        # But this is LeetCode so let's do things by hand, even if it's way
        # slower than using the standard library
        a_digits = list(map(int, a))
        b_digits = list(map(int, b))
        sum_digits = list()
        carry = 0
        while len(a_digits) > 0 or len(b_digits) > 0:
            if len(a_digits) > 0:
                a_digit = a_digits.pop()
            else:
                a_digit = 0
            if len(b_digits) > 0:
                b_digit = b_digits.pop()
            else:
                b_digit = 0
            sum_digit = a_digit + b_digit + carry
            if sum_digit > 1:
                carry = 1
                sum_digit = sum_digit % 2
            else:
                carry = 0
            sum_digits.insert(0, sum_digit)
        if carry != 0:
            sum_digits.insert(0, carry)
        return "".join(map(str, sum_digits))


# Tests
assert Solution().addBinary("11", "1") == "100"
assert Solution().addBinary("1010", "1011") == "10101"
