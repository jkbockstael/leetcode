#!/usr/bin/env python3

# Day 13: Iterator for Combination
#
# Design an Iterator class, which has:
# - A constructor that takes a string characters of sorted distinct lowercase
#   English letters and a number combinationLength as arguments.
# - A function next() that returns the next combination of length
#   combinationLength in lexicographical order.
# - A function hasNext() that returns True if and only if there exists a next
#   combination
#
# Constraints:
# - 1 <= combinationLength <= characters.length <= 15
# - There will be at most 10^4 function calls per test.
# - It's guaranteed that all calls of the function next are valid.

class CombinationIterator:
    def __init__(self, characters: str, combinationLength: int):
        # Real-life solution
        # (beats 97.72% of python3 submissions)
        # import itertools
        # self.values = ["".join(c) for c \
        #     in itertools.combinations(characters, combinationLength)]
        # self.index = 0
        
        # Manual solution, for sport
        # (beats 49.66% of python3 submissions (guess what this tells us?))
        combinations = []
        # Left as an exercise for the reader: write the following block as one
        # large unreadable list comprehension
        for n in range(2 ** len(characters)):
            bitmask = bin(n)[2:].zfill(len(characters))
            if bitmask.count("1") == combinationLength:
                combination = ""
                for i in range(len(characters)):
                    if bitmask[i] == "1":
                        combination += characters[i]
                combinations.append(combination)
        # Seriously though, a better exercise for the reader would be to
        # implement this exact method as a generator instead of iterating over
        # a pre-made list, but the problem hints at this method
        self.values = sorted(combinations)
        self.index = 0
    
    def next(self) -> str:
        value = self.values[self.index]
        self.index += 1
        return value
    
    def hasNext(self) -> bool:
        return self.index < len(self.values)

# Test
iterator = CombinationIterator("abc", 2)
assert iterator.hasNext() == True
assert iterator.hasNext() == True
assert iterator.next() == "ab"
assert iterator.hasNext() == True
assert iterator.next() == "ac"
assert iterator.hasNext() == True
assert iterator.next() == "bc"
assert iterator.hasNext() == False
