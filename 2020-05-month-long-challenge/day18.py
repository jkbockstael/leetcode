#!/usr/bin/env python3

# Day 18: Permutation in String
#
# Given two strings s1 and s2, write a function to return true if s2 contains
# the permutation of s1. In other words, one of the first string's permutations
# is the substring of the second string.
#
# Notes:
# - The input strings only contain lower case letters.
# - The length of both given strings is in range [1, 10,000].

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # This is almost the same code as Day 17, with early returns
        if len(s2) < len(s1) or s1 == "":
            return False
        ALPHABET_SIZE = 26
        # Character to index
        c2i = lambda c: ord(c) - ord('a')
        frequencies_s2 = [0 for _ in range(ALPHABET_SIZE)]
        frequencies_s1 = [0 for _ in range(ALPHABET_SIZE)]
        positions = []
        # First window
        for i in range(len(s1)):
            frequencies_s1[c2i(s1[i])] += 1
            frequencies_s2[c2i(s2[i])] += 1
        # Next windows
        for i in range(len(s1), len(s2)):
            if frequencies_s2 == frequencies_s1:
                return True
                positions.append(i-len(s1))
            frequencies_s2[c2i(s2[i])] += 1
            frequencies_s2[c2i(s2[i-len(s1)])] -= 1
        # Last window
        if frequencies_s2 == frequencies_s1:
            return True
            positions.append(len(s2)-len(s1))
        return False

# Tests
assert Solution().checkInclusion("ab", "eidbaooo") == True
assert Solution().checkInclusion("ab", "eidboaoo") == False
