#!/usr/bin/env python3

# Day 28: First Unique Number
#
# You have a queue of integers, you need to retrieve the first unique integer
# in the queue.
# Implement the FirstUnique class:
# - FirstUnique(int[] nums) Initializes the object with the numbers in the
#   queue.
# - int showFirstUnique() returns the value of the first unique integer of the
#   queue, and returns -1 if there is no such integer.
# - void add(int value) insert value to the queue.
# Constraints:
# - 1 <= nums.length <= 10^5
# - 1 <= nums[i] <= 10^8
# - 1 <= value <= 10^8
# - At most 50000 calls will be made to showFirstUnique and add.

import collections

class FirstUnique:
    def __init__(self, nums: [int]):
        # The actual queue
        self.queue = collections.deque()
        # A map of the number of occurences of each number in the queue
        self.map = {}
        for num in nums:
            self.add(num)

    def showFirstUnique(self) -> int:
        while len(self.queue) > 0 and self.map[self.queue[0]] > 1:
            self.queue.popleft()
        if len(self.queue) == 0:
            return -1
        else:
            return self.queue[0]

    def add(self, value: int) -> None:
        if value in self.map:
            self.map[value] += 1
        else:
            self.map[value] = 1
            self.queue.append(value)

# Tests
test = FirstUnique([2,3,5])
assert test.showFirstUnique() == 2
test.add(5)
assert test.showFirstUnique() == 2
test.add(2)
assert test.showFirstUnique() == 3
test.add(3)
assert test.showFirstUnique() == -1
