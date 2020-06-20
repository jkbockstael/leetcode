#!/usr/bin/env python3

# Day 19: Longest Duplicate Substring
#
# Given a string S, consider all duplicated substrings: (contiguous) substrings
# of S that occur 2 or more times.  (The occurrences may overlap.)
# Return any duplicated substring that has the longest possible length.  (If S
# does not have a duplicated substring, the answer is "".)
#
# Note:
# - 2 <= S.length <= 10^5
# - S consists of lowercase English letters.

class Solution:
    def longestDupSubstring(self, S: str) -> str:
        # Implementation using the Robin-Karp algorithm, which may not be
        # optimal for this case
        length = len(S)
        chars = [ord(c) - ord('a') for c in S]
        alphabet_size = 26
        prime = 2**63 - 1

        def RabinKarp(middle, prime):
            h = 0
            for i in range(middle):
                h = (h * alphabet_size + chars[i]) % prime
            hashes = {h}
            for position in range(1, length - middle + 1):
                h = (h * alphabet_size - chars[position - 1] * pow(alphabet_size, middle, prime) + chars[position + middle - 1]) % prime
                if h in hashes:
                    return position
                hashes.add(h)
            return None

        left = 1
        right = length
        match_position = -1
        while left <= right:
            middle = (left + right) // 2
            match = RabinKarp(middle, prime)
            if match is not None:
                left = middle + 1
                match_position = match
            else:
                right = middle - 1
        return S[match_position:match_position + left - 1]

# Tests
assert Solution().longestDupSubstring("banana") == "ana"
assert Solution().longestDupSubstring("abcd") == ""
