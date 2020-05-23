#!/usr/bin/env python3

# Day 22: Sort Characters By Frequency
#
# Given a string, sort it in decreasing order based on the frequency of
# characters.

import collections

class Solution:
    def frequencySort(self, s: str) -> str:
        return "".join(map(
            lambda t: t[0] * t[1],
            collections.Counter(s).most_common(len(s))))

# Tests
assert Solution().frequencySort("tree") in ["eert", "eetr"]
assert Solution().frequencySort("cccaaa") in ["cccaaa", "aaaccc"]
assert Solution().frequencySort("Aabb") in ["bbAa", "bbaA"]
