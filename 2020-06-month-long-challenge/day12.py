#!/usr/bin/env python3

# Day 12: Insert Delete GetRandom O(1)
#
# Design a data structure that supports all following operations in average
# O(1) time.
# 1. insert(val): Inserts an item val to the set if not already present.
# 2. remove(val): Removes an item val from the set if present.
# 3. getRandom: Returns a random element from current set of elements. Each
#    element must have the same probability of being returned.

import random

class RandomizedSet:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.set = {}
        self.values = []
        
    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already
        contain the specified element.
        """
        new = val not in self.set
        if new:
            self.set[val] = val
            self.values.append(val)
        return new
        
    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the
        specified element.
        """
        exists = val in self.set
        if exists:
            self.set.pop(val)
            self.values.remove(val)
        return exists
        
    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return random.choice(self.values)

# Tests
test = RandomizedSet()
assert test.insert(1) == True
assert test.remove(2) == False
assert test.insert(2) == True
assert test.getRandom() in [1,2]
assert test.remove(1) == True
assert test.insert(2) == False
assert test.getRandom() == 2
