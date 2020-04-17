#!/usr/bin/env python3

# Day 16: Valid Parenthesis String
#
# Given a string containing only three types of characters: '(', ')' and '*', write a function to check whether this string is valid. We define the validity of a string by these rules:
# - Any left parenthesis '(' must have a corresponding right parenthesis ')'.
# - Any right parenthesis ')' must have a corresponding left parenthesis '('.
# - Left parenthesis '(' must go before the corresponding right parenthesis ')'.
# - '*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string.
# - An empty string is also valid.
#
# Note:
# - The string size will be in the range [1, 100].

class Solution:
    def checkValidString(self, s: str) -> bool:
        balance_min = 0
        balance_max = 0
        for char in s:
            if char == '(':
                balance_min += 1
                balance_max += 1
            if char == ')':
                balance_min -= 1
                balance_max -= 1
            if char == '*':
                balance_min -= 1
                balance_max += 1
            if balance_min < 0:
                balance_min = 0
            if balance_max < 0:
                return False
        return balance_min == 0

# Tests
assert Solution().checkValidString("()") == True
assert Solution().checkValidString("(*)") == True
assert Solution().checkValidString("(*))") == True
assert Solution().checkValidString("") == True
assert Solution().checkValidString("(()") == False
assert Solution().checkValidString("(()))") == False
assert Solution().checkValidString("(((*)") == False
assert Solution().checkValidString("()(())") == True
assert Solution().checkValidString("()(()") == False
assert Solution().checkValidString(")))(((") == False
