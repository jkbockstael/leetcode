#!/usr/bin/env python3

# Day 9: Backspace String Compare
#
# Given two strings S and T, return if they are equal when both are typed into empty text editors. # means a backspace character.
# Notes:
# - 1 <= S.length <= 200
# - 1 <= T.length <= 200
# - S and T only contain lowercase letters and '#' characters.

class Solution:
    def apply_backspaces(self, s: str) -> str:
        out = ""
        for c in s:
            if c == "#":
                out = out[:-1]
            else:
                out += c
        return out

    def backspaceCompare(self, S: str, T: str) -> bool:
        return self.apply_backspaces(S) == self.apply_backspaces(T)

# Tests
assert Solution().backspaceCompare("ab#c", "ad#c") == True
assert Solution().backspaceCompare("ab##", "c#d#") == True
assert Solution().backspaceCompare("a##c", "#a#c") == True
assert Solution().backspaceCompare("a#c", "b") == False
