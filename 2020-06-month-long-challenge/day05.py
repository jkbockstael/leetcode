#!/usr/bin/env python3

# Day 5: Random Pick with Weight
#
# Given an array w of positive integers, where w[i] describes the weight of
# index i, write a function pickIndex which randomly picks an index in
# proportion to its weight.
#
# Note:
# - 1 <= w.length <= 10000
# - 1 <= w[i] <= 10^5
# - pickIndex will be called at most 10000 times.

import random

class Solution:
    def __init__(self, w: [int]):
        # Compute a list of cumulative weights
        cumulative = 0
        self.cumulatives = []
        for weight in w:
            cumulative += weight
            self.cumulatives.append(cumulative)

    def pickIndex(self) -> int:
        # Pick a random integer in the larger range of cumulative weights
        number = random.randint(1, self.cumulatives[-1])
        # Basic binary search for the index of that value
        left = 0
        right = len(self.cumulatives) - 1
        while left <= right:
            middle = (left + right) // 2
            if number <= self.cumulatives[middle]:
                right = middle - 1
            else:
                left = middle + 1
        return left

# No test, feel free to contribute one
