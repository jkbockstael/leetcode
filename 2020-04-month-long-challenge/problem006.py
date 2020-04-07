#!/usr/bin/env python3

# Day 6: Group Anagrams
#
# Given an array of strings, group anagrams together.

class Solution:
    def groupAnagrams(self, strs: [str]) -> [[str]]:
        groups = []
        lookup = {}
        for word in strs:
            key = ''.join(sorted(word))
            if key in lookup:
                groups[lookup[key]].append(word)
            else:
                lookup[key] = len(groups)
                groups.append([word])
        sorted_groups = [sorted(group) for group in groups]
        return sorted_groups

assert Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]) ==\
    [["ate","eat","tea"],["nat","tan"],["bat"]]
