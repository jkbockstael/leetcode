#!/usr/bin/env python3

# Day 3: Repeated Substring Pattern
#
# Given a non-empty string check if it can be constructed by taking a substring
# of it and appending multiple copies of the substring together. You may assume
# the given string consists of lowercase English letters only and its length
# will not exceed 10000.

class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        length = len(s)
        for substring_length in range(1, length // 2 + 1):
            if length % substring_length == 0 \
                and s[:substring_length] * int(length / substring_length) == s:
                    return True
        return False

# Tests
assert Solution().repeatedSubstringPattern("abab") == True
assert Solution().repeatedSubstringPattern("abba") == False
assert Solution().repeatedSubstringPattern("aba") == False
assert Solution().repeatedSubstringPattern("abcabcabcabc") == True
