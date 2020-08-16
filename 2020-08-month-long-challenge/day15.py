#!/usr/bin/env python3

# Day 15: Non-overlapping Intervals
#
# Given a collection of intervals, find the minimum number of intervals you
# need to remove to make the rest of the intervals non-overlapping.
#
# Note:
# - You may assume the interval's end point is always bigger than its start
#   point.
# - Intervals like [1,2] and [2,3] have borders "touching" but they don't
#   overlap each other.

class Solution:
    def eraseOverlapIntervals(self, intervals: [[int]]) -> int:
        # Edge case
        if len(intervals) == 0:
            return 0

        # Convenience functions for code clarity
        start = lambda interval: interval[0]
        end = lambda interval: interval[1]

        # Sort intervals by their end
        intervals = sorted(intervals, key = end)

        # Greedy!
        intervals_to_remove = 0
        previous_start = start(intervals[0])
        previous_end = end(intervals[0])
        for interval in intervals[1:]:
            if start(interval) < previous_end:
                intervals_to_remove += 1
            else:
                previous_start = start(interval)
                previous_end = end(interval)

        return intervals_to_remove

# Tests
assert Solution().eraseOverlapIntervals([[1,2],[2,3],[3,4],[1,3]]) == 1
assert Solution().eraseOverlapIntervals([[1,2],[1,2],[1,2]]) == 2
assert Solution().eraseOverlapIntervals([[1,2],[2,3]]) == 0
