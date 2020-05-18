#!/usr/bin/env python3

# Day 17: Find All Anagrams in a String
#
# Given a string s and a non-empty string p, find all the start indices of p's
# anagrams in s.
# Strings consists of lowercase English letters only and the length of both
# strings s and p will not be larger than 20,100.
# The order of output does not matter.

class Solution:
    def findAnagrams(self, s: str, p: str) -> [int]:
        if len(s) < len(p) or p == "":
            return []
        ALPHABET_SIZE = 26
        # Character to index
        c2i = lambda c: ord(c) - ord('a')
        frequencies_s = [0 for _ in range(ALPHABET_SIZE)]
        frequencies_p = [0 for _ in range(ALPHABET_SIZE)]
        positions = []
        # First window
        for i in range(len(p)):
            frequencies_p[c2i(p[i])] += 1
            frequencies_s[c2i(s[i])] += 1
        # Next windows
        for i in range(len(p), len(s)):
            if frequencies_s == frequencies_p:
                positions.append(i-len(p))
            frequencies_s[c2i(s[i])] += 1
            frequencies_s[c2i(s[i-len(p)])] -= 1
        # Last window
        if frequencies_s == frequencies_p:
            positions.append(len(s)-len(p))
        return positions

# Tests
assert Solution().findAnagrams("cbaebabacd", "abc") == [0, 6]
assert Solution().findAnagrams("abab", "ab") == [0, 1, 2]
assert Solution().findAnagrams("", "a") == []
