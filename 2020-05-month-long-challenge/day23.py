#!/usr/bin/env python3

# Day 23: Interval List Intersections
#
# Given two lists of closed intervals, each list of intervals is pairwise
# disjoint and in sorted order.
# Return the intersection of these two interval lists.
#
# (Formally, a closed interval [a, b] (with a <= b) denotes the set of real
# numbers x with a <= x <= b.  The intersection of two closed intervals is a
# set of real numbers that is either empty, or can be represented as a closed
# interval.  For example, the intersection of [1, 3] and [2, 4] is [2, 3].)
#
# Notes:
# - 0 <= A.length < 1000
# - 0 <= B.length < 1000
# - 0 <= A[i].start, A[i].end, B[i].start, B[i].end < 10^9

class Solution:
    def intervalIntersection(self, A: [[int]], B: [[int]]) -> [[int]]:
        intersections = []
        a = 0
        b = 0
        while a < len(A) and b < len(B):
            left = max(A[a][0], B[b][0])
            right = min(A[a][1], B[b][1])
            if left <= right:
                intersections.append([left, right])
            if A[a][1] < B[b][1]:
                a += 1
            else:
                b += 1
        return intersections

# Tests
assert Solution().intervalIntersection([[0,2],[5,10],[13,23],[24,25]], B = [[1,5],[8,12],[15,24],[25,26]]) == [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]
