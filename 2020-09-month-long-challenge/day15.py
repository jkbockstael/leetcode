#!/usr/bin/env python3

# Day 15: Length of Last Word
#
# Given a string s consists of upper/lower-case alphabets and empty space
# characters ' ', return the length of last word (last word means the last
# appearing word if we loop from left to right) in the string.
# If the last word does not exist, return 0.

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.strip().split(' ')[-1])

# Tests
assert Solution().lengthOfLastWord("Hello World") == 5
assert Solution().lengthOfLastWord("a ") == 1
