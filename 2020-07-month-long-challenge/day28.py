#!/usr/bin/env python3

# Day 28: Task Scheduler
#
# You are given a char array representing tasks CPU need to do. It contains
# capital letters A to Z where each letter represents a different task. Tasks
# could be done without the original order of the array. Each task is done in
# one unit of time. For each unit of time, the CPU could complete either one
# task or just be idle.
# However, there is a non-negative integer n that represents the cooldown
# period between two same tasks (the same letter in the array), that is that
# there must be at least n units of time between any two same tasks.
#
# You need to return the least number of units of times that the CPU will take
# to finish all the given tasks.
#
# Note:
# - The number of tasks is in the range [1, 10000].
# - The integer n is in the range [0, 100].

import collections

class Solution:
    def leastInterval(self, tasks: [str], n: int) -> int:
        frequencies = list(collections.Counter(tasks).values())
        most_common_count = max(frequencies)
        same_count = frequencies.count(most_common_count)
        return max(len(tasks), same_count + (most_common_count - 1) * (n + 1))

# Tests
assert Solution().leastInterval(["A","A","A","B","B","B"], 2) == 8
assert Solution().leastInterval(["A","A","A","B","B","B"], 0) == 6
assert Solution().leastInterval(["A","A","A","A","A","A","B","C","D","E","F","G"], 2) == 16
