#!/usr/bin/env python3

# Day 31: Edit Distance
#
# Given two words word1 and word2, find the minimum number of operations
# required to convert word1 to word2.
# You have the following 3 operations permitted on a word:
# - Insert a character
# - Delete a character
# - Replace a character

class Solution:
    def __init__(self):
        # Levenshtein is more readable as a recursion, but it's quite
        # inefficient so let's memoize to speed it up
        self.memo = {}

    def minDistance(self, word1: str, word2: str) -> int:
        distance = None
        if (word1, word2) in self.memo:
            return self.memo[word1, word2]
        if word1 == "":
            distance = len(word2)
        if word2 == "":
            distance = len(word1)
        if word1 != "" and word2 != "":
            if word1[-1] == word2[-1]:
                cost = 0
            else:
                cost = 1
        if distance is None:
            distance = min(
                self.minDistance(word1[:-1], word2) + 1,
                self.minDistance(word1, word2[:-1]) + 1,
                self.minDistance(word1[:-1], word2[:-1]) + cost)
        self.memo[word1, word2] = distance
        return distance

# Tests
assert Solution().minDistance("horse", "ros") == 3
assert Solution().minDistance("intention", "execution") == 5
assert Solution().minDistance("dinitrophenylhydrazine", "acetylphenylhydrazine") == 6
