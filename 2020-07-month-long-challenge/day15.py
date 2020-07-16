#!/usr/bin/env python3

# Day 15: Reverse Words in a String
#
# Given an input string, reverse the string word by word.
#
# Note:
# - A word is defined as a sequence of non-space characters.
# - Input string may contain leading or trailing spaces. However, your reversed
#   string should not contain leading or trailing spaces.
# - You need to reduce multiple spaces between two words to a single space in
#   the reversed string.

class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(reversed(s.split()))

# Tests
assert Solution().reverseWords("the sky is blue") == "blue is sky the"
assert Solution().reverseWords("  hello world!  ") == "world! hello"
assert Solution().reverseWords("a good   example") == "example good a"
