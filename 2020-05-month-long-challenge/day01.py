#!/usr/bin/env python3

# Day 1: First Bad Version
#
# You are a product manager and currently leading a team to develop a new
# product. Unfortunately, the latest version of your product fails the quality
# check. Since each version is developed based on the previous version, all the
# versions after a bad version are also bad.
# Suppose you have n versions [1, 2, ..., n] and you want to find out the first
# bad one, which causes all the following ones to be bad.
# You are given an API bool isBadVersion(version) which will return whether
# version is bad. Implement a function to find the first bad version. You
# should minimize the number of calls to the API.
#
# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n:int) -> int:
        # Yup, this is a binary search
        left = 1 # There is no version zero
        right = n
        while left < right:
            middle = left + (right - left) // 2
            if isBadVersion(middle):
                right = middle
            else:
                left = middle + 1
        return left

# Test
def isBadVersion(version: int) -> bool:
    return version >= 4
assert Solution().firstBadVersion(5) == 4
