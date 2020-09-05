#!/usr/bin/env python3

# Day 14: Perform String Shifts
#
# You are given a string s containing lowercase English letters, and a matrix
# shift, where shift[i] = [direction, amount]:
# - direction can be 0 (for left shift) or 1 (for right shift).
# - amount is the amount by which string s is to be shifted.
# - A left shift by 1 means remove the first character of s and append it to
#   the end.
# - Similarly, a right shift by 1 means remove the last character of s and add
#   it to the beginning.
# Return the final string after all operations.
#
# Constraints:
# - 1 <= s.length <= 100
# - s only contains lower case English letters.
# - 1 <= shift.length <= 100
# - shift[i].length == 2
# - 0 <= shift[i][0] <= 1
# - 0 <= shift[i][1] <= 100

class Solution:
    def stringShift(self, s: str, shift: [[int]]) -> str:
        total_shift = sum(distance * (-1 if direction == 1 else 1)
            for direction, distance in shift) % len(s)
        return s[total_shift:] + s[:total_shift]

# Tests
assert Solution().stringShift("abc", [[0,1],[1,2]]) == "cab"
assert Solution().stringShift("abcdefg", [[1,1],[1,1],[0,2],[1,3]]) == "efgabcd"
assert Solution().stringShift("xqgwkiqpif", [[1,4],[0,7],[0,8],[0,7],[0,6],[1,3],[0,1],[1,7],[0,5],[0,6]]) == "qpifxqgwki"
