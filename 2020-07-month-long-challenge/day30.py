#!/usr/bin/env python3

# Day 30: Word Break II
#
# Given a non-empty string s and a dictionary wordDict containing a list of
# non-empty words, add spaces in s to construct a sentence where each word is a
# valid dictionary word. Return all such possible sentences.
#
# Note:
# - The same word in the dictionary may be reused multiple times in the
#   segmentation.
# - You may assume the dictionary does not contain duplicate words.

from functools import lru_cache

class Solution:
    def wordBreak(self, s: str, wordDict: [str]) -> [str]:
        @lru_cache(None)
        def sentencesStartingAt(position):
            if position == len(s):
                return [[]]
            sentences = []
            word = ""
            while position < len(s):
                word += s[position]
                if word in wordDict:
                    for sub_sentences in sentencesStartingAt(position + 1):
                        sentences.append([word] + sub_sentences)
                position += 1
            return sentences
        return [" ".join(sentence) for sentence in sentencesStartingAt(0)]

# Tests
assert Solution().wordBreak("catsanddog", ["cat", "cats", "and", "sand", "dog"]) == ["cat sand dog", "cats and dog"]
assert Solution().wordBreak("pineapplepenapple", ["apple", "pen", "applepen", "pine", "pineapple"]) == ["pine apple pen apple", "pine applepen apple", "pineapple pen apple"]
assert Solution().wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"]) == []
