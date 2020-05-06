#!/usr/bin/env python3

# Day 5: First Unique Character in a String
#
# Given a string, find the first non-repeating character in it and return it's
# index. If it doesn't exist, return -1.
# Note: You may assume the string contain only lowercase letters.

import collections

class Solution:
    def firstUniqChar(self, s: str) -> int:
        # "Your runtime beats 97.25 % of python3 submissions."
        # I fail to see how I could make this even faster, suggestions welcome
        characters = collections.Counter(s)
        # As a generator, as we're not interested in all the values
        uniques = (char for char in characters if characters[char] == 1)
        # collections.Counter retains insertion order, which is convenient here
        try:
            return s.index(next(uniques))
        except StopIteration:
            return -1

# Tests
assert Solution().firstUniqChar("leetcode") == 0
assert Solution().firstUniqChar("loveleetcode") == 2
assert Solution().firstUniqChar("abba") == -1
