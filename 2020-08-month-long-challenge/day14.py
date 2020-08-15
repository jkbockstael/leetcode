#!/usr/bin/env python3

# Day 14: Longest Palindrome
#
# Given a string which consists of lowercase or uppercase letters, find the
# length of the longest palindromes that can be built with those letters.
# This is case sensitive, for example "Aa" is not considered a palindrome here.

import collections

class Solution:
    def longestPalindrome(self, s: str) -> int:
        # Counting frequencies isn't the interesting part here
        frequencies = collections.Counter(s)
        length = 0
        # We want to keep track of how many letters appear in odd numbers
        odd_letters = 0
        for letter in frequencies:
            count = frequencies[letter]
            length += count # Include ALL THE THINGS
            # ... but keep track of the extra letters we should not have
            # included
            if count % 2 == 1:
                odd_letters += 1
        # Now we have to substract the odd ones, except for one that can be put
        # in the middle of our palindrome (that is, if they exist)
        if odd_letters > 0:
            return length - odd_letters + 1
        else:
            return length

# Test
assert Solution().longestPalindrome("") == 0
assert Solution().longestPalindrome("abc") == 1
assert Solution().longestPalindrome("ABba") == 1
assert Solution().longestPalindrome("abba") == 4
assert Solution().longestPalindrome("abccccdd") == 7
