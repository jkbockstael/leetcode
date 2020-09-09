#!/usr/bin/env python3

# Day 2: Design HashSet
#
# Design a HashSet without using any built-in hash table libraries.
# 
# To be specific, your design should include these functions:
# - add(value): Insert a value into the HashSet.
# - contains(value) : Return whether the value exists in the HashSet or not.
# - remove(value): Remove a value in the HashSet. If the value does not exist
#   in the HashSet, do nothing.
#
# Note:
# - All values will be in the range of [0, 1000000]
# - The number of operations will be in the range of [1, 10000]
# - Please do not use the built-in HashSet library.

class MyHashSet:
    def __init__(self, memory=16):
        self.values = [[] for _ in range(2**memory)]
        self.memory = memory

    def add(self, key: int) -> None:
        hashed = self.hash(key)
        if key not in self.values[hashed]:
            self.values[hashed].append(key)

    def remove(self, key: int) -> None:
        hashed = self.hash(key)
        if key in self.values[hashed]:
            self.values[hashed].remove(key)

    def contains(self, key: int) -> bool:
        hashed = self.hash(key)
        return key in self.values[hashed]

    def hash(self, key) -> int:
        # Multiplicative hash, for simplicity
        a = 27644437 #prime
        w = 64 # word size
        m = self.memory # size of output set
        return (a * key) >> (w - m)

# Tests
hash_set = MyHashSet()
hash_set.add(1)
hash_set.add(2)
assert hash_set.contains(1) == True
assert hash_set.contains(3) == False
hash_set.add(2)
assert hash_set.contains(2) == True
hash_set.remove(2)
assert hash_set.contains(2) == False
