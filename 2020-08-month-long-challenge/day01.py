#!/usr/bin/env python3

# Day 1: Detect Capital
#
# Given a word, you need to judge whether the usage of capitals in it is right
# or not.
# We define the usage of capitals in a word to be right when one of the
# following cases holds:
# - All letters in this word are capitals, like "USA".
# - All letters in this word are not capitals, like "leetcode".
# - Only the first letter in this word is capital, like "Google".

class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if word[0].isupper():
            return all(character.isupper() for character in word[1:]) \
                or all(character.islower() for character in word[1:])
        else:
            return all(character.islower() for character in word[1:])

# Tests
assert Solution().detectCapitalUse("USA") == True
assert Solution().detectCapitalUse("leetcode") == True
assert Solution().detectCapitalUse("Google") == True
assert Solution().detectCapitalUse("FlaG") == False
