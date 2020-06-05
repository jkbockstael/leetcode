#!/usr/bin/env python3

# Day 4: Reverse String
#
# Write a function that reverses a string. The input string is given as an
# array of characters char[].
# Do not allocate extra space for another array, you must do this by modifying
# the input array in-place with O(1) extra memory.
# You may assume all the characters consist of printable ascii characters.

class Solution:
    def reverseString(self, s: [str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """ 
        # Real-life implementation:
        #   s.reverse()
        # or:
        #   s[::] = s[::-1]
        # But let's do it manually, even if it's slower:
        for i in range(0, len(s) // 2):
            s[i], s[len(s) - i - 1] = s[len(s) - i - 1], s[i]

# Tests
test_string = ["h","e","l","l","o"]
Solution().reverseString(test_string)
assert test_string == ["o","l","l","e","h"]
test_string = ["H","a","n","n","a","h"]
Solution().reverseString(test_string)
assert test_string == ["h","a","n","n","a","H"]
