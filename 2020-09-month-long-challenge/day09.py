#!/usr/bin/env python3

# Day 9: Compare Version Numbers
#
# Compare two version numbers version1 and version2.
# If version1 > version2 return 1; if version1 < version2 return -1;otherwise
# return 0.
# You may assume that the version strings are non-empty and contain only digits
# and the . character.
# The . character does not represent a decimal point and is used to separate
# number sequences.
# For instance, 2.5 is not "two and a half" or "half way to version three", it
# is the fifth second-level revision of the second first-level revision.
# You may assume the default revision number for each level of a version number
# to be 0. For example, version number 3.4 has a revision number of 3 and 4 for
# its first and second level revision number. Its third and fourth level
# revision number are both 0.
#
# Note:
# - Version strings are composed of numeric strings separated by dots . and
#   this numeric strings may have leading zeroes. 
# - Version strings do not start or end with dots, and they will not be two
#   consecutive dots.

class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        parse = lambda s: list(map(int, s.split('.')))
        v1 = parse(version1)
        v2 = parse(version2)
        # It's way easier if the two version sequences have the same length
        normalise = lambda n: lambda xs: xs + [0] * n
        if len(v1) < len(v2):
            v1 = normalise(len(v2) - len(v1))(v1)
        else:
            v2 = normalise(len(v1) - len(v2))(v2)
        # Now we can safely traverse both at once
        for position in range(len(v1)):
            if v1[position] > v2[position]:
                return 1
            if v1[position] < v2[position]:
                return -1
        return 0

# Tests
assert Solution().compareVersion("0.1", "1.1") == -1
assert Solution().compareVersion("1.0.1", "1") == 1
assert Solution().compareVersion("7.5.2.4", "7.5.3") == -1
assert Solution().compareVersion("1.01", "1.001") == 0
assert Solution().compareVersion("1.0", "1.0.0") == 0
