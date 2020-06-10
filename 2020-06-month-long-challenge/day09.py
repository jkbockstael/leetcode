#!/usr/bin/env python3

# Day 9: Is Subsequence
#
# Given a string s and a string t, check if s is subsequence of t.
# A subsequence of a string is a new string which is formed from the original
# string by deleting some (can be none) of the characters without disturbing
# the relative positions of the remaining characters. (ie, "ace" is a
# subsequence of "abcde" while "aec" is not).
#
# Constraints:
# - 0 <= s.length <= 100
# - 0 <= t.length <= 10^4
# - Both strings consists only of lowercase characters.

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0:
            return True
        if len(t) == 0:
            return False
        else:
            return s[0] in t \
                and self.isSubsequence(s[1:], t[t.index(s[0]) + 1:])

# Tests
assert Solution().isSubsequence("abc", "ahbgdc") == True
assert Solution().isSubsequence("axc", "ahbgdc") == False
