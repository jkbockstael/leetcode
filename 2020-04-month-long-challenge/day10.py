#!/usr/bin/env python3

# Day 10: Min Stack
#
# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
# - push(x) -- Push element x onto stack.
# - pop() -- Removes the element on top of the stack.
# - top() -- Get the top element.
# - getMin() -- Retrieve the minimum element in the stack.

class MinStack:
    def __init__(self):
        self.values = []
        self.mins = []

    def push(self, x: int) -> None:
        self.values.append(x)
        if len(self.mins) == 0 or x <= self.mins[-1]:
            self.mins.append(x)

    def pop(self) -> None:
        if self.values[-1] <= self.mins[-1]:
            self.mins = self.mins[:-1]
        self.values = self.values[:-1]

    def top(self) -> int:
        return self.values[-1]

    def getMin(self) -> int:
        return self.mins[-1]

# Tests
min_stack = MinStack()
min_stack.push(-2)
min_stack.push(0)
min_stack.push(-3)
min_item = min_stack.getMin()
assert min_item == -3
min_stack.pop()
top_item = min_stack.top()
assert top_item == 0
min_item = min_stack.getMin()
assert min_item == -2
