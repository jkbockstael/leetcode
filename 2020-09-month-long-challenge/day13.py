#!/usr/bin/env python3

# Day 13: Insert Interval
#
# Given a set of non-overlapping intervals, insert a new interval into the
# intervals (merge if necessary).
# You may assume that the intervals were initially sorted according to their
# start times.

class Solution:
    def insert(self, intervals: [[int]], newInterval: [int]) -> [[int]]:
        before = []
        after = []
        left = lambda interval: interval[0]
        right = lambda interval: interval[1]

        for interval in intervals:
            # Distincly smaller
            if right(interval) < left(newInterval):
                before += [interval]
            # Distinctly larger
            elif left(interval) > right(newInterval):
                after += [interval]
            # Merge
            else:
                newInterval = [min(left(interval), left(newInterval)), \
                    max(right(interval), right(newInterval))]

        return before + [newInterval] + after

# Tests
assert Solution().insert([[1,3],[6,9]], [2,5]) == [[1,5],[6,9]]
assert Solution().insert([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8]) == [[1,2],[3,10],[12,16]]
