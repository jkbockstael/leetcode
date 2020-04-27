#!/usr/bin/env python3

# Day 26: Longest Common Subsequence
#
# Given two strings text1 and text2, return the length of their longest common
# subsequence.
# A subsequence of a string is a new string generated from the original string
# with some characters(can be none) deleted without changing the relative order
# of the remaining characters. (eg, "ace" is a subsequence of "abcde" while
# "aec" is not). A common subsequence of two strings is a subsequence that is
# common to both strings.
# If there is no common subsequence, return 0.
#
# Constraints:
# - 1 <= text1.length <= 1000
# - 1 <= text2.length <= 1000
# - The input strings consist of lowercase English characters only.

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        common_length = [[None for _ in range(len(text2) + 1)]
            for _ in range(len(text1) + 1)]
        for i in range(len(text1) + 1):
            for j in range(len(text2) + 1):
                if i == 0 or j == 0:
                    common_length[i][j] = 0
                elif text1[i - 1] == text2[j - 1]:
                    common_length[i][j] = common_length[i - 1][j - 1] + 1
                else:
                    common_length[i][j] = max(common_length[i - 1][j],
                        common_length[i][j - 1])
        return common_length[len(text1)][len(text2)]

# Tests
assert Solution().longestCommonSubsequence("abcde", "ace") == 3
assert Solution().longestCommonSubsequence("abc", "abc") == 3
assert Solution().longestCommonSubsequence("abc", "def") == 0
