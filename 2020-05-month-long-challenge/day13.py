#!/usr/bin/env python3

# Day 13: Remove K Digits
#
# Given a non-negative integer num represented as a string, remove k digits
# from the number so that the new number is the smallest possible. 
#
# Notes:
# - The length of num is less than 10002 and will be ≥ k.
# - The given num does not contain any leading zero.

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        for digit in num:
            while k > 0 and len(stack) > 0 and stack[-1] > int(digit):
                stack.pop()
                k = k - 1
            stack.append(int(digit))
        while k > 0:
            stack.pop()
            k = k - 1
        while len(stack) > 0 and stack[0] == 0:
            stack = stack[1:]
        if len(stack) == 0:
            return "0"
        else:
            return "".join(map(str, stack))

# Tests
assert Solution().removeKdigits("1432219", 3) == "1219"
assert Solution().removeKdigits("10200", 1) == "200"
assert Solution().removeKdigits("10", 2) == "0"
