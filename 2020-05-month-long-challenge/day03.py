#!/usr/bin/env python3

# Day 3: Ransom Note
#
# Given an arbitrary ransom note string and another string containing letters
# from all the magazines, write a function that will return true if the ransom
# note can be constructed from the magazines ; otherwise, it will return false. 
# Each letter in the magazine string can only be used once in your ransom note. 
# You may assume that both strings contain only lowercase letters. 

import collections

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # This could be a one-liner, but it would be slightly less obvious
        # I could implement my own counter, but it would be way less obvious
        needed = collections.Counter(ransomNote)
        available = collections.Counter(magazine)
        available.subtract(needed)
        return all(map(lambda x: x >= 0, available.values()))

assert Solution().canConstruct("a", "b") == False
assert Solution().canConstruct("aa", "ab") == False
assert Solution().canConstruct("aa", "aab") == True
