#!/usr/bin/env python3

# Day 6: Queue Reconstruction by Height
#
# Suppose you have a random list of people standing in a queue. Each person is
# described by a pair of integers (h, k), where h is the height of the person
# and k is the number of people in front of this person who have a height
# greater than or equal to h. Write an algorithm to reconstruct the queue.
#
# Note:
# - The number of people is less than 1,100.

class Solution:
    def reconstructQueue(self, people: [[int]]) -> [[int]]:
        # Convenience functions for clarity
        height = lambda person: person[0]
        taller_in_front = lambda person: person[1]
        # Sort the input by height descending and number of taller persons in
        # front ascending
        sorted_people = sorted(people,
            key = lambda person: (-height(person), taller_in_front(person)))
        # Insert into the queue at the correct position
        queue = []
        for person in sorted_people:
            queue.insert(taller_in_front(person), person)
        return queue

# Test
assert Solution().reconstructQueue([[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]) == [[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]
