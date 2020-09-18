#!/usr/bin/env python3

# Day 17: Robot Bounded In Circle
#
# On an infinite plane, a robot initially stands at (0, 0) and faces north.
# The robot can receive one of three instructions:
# - "G": go straight 1 unit;
# - "L": turn 90 degrees to the left;
# - "R": turn 90 degress to the right.
#
# The robot performs the instructions given in order, and repeats them forever.
# Return true if and only if there exists a circle in the plane such that the
# robot never leaves the circle.

class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        # The robot can only face one of the cardinal directions, this means
        # that in at most four cycles it must be back at its starting point
        instructions *= 4
        turns = [(0, 1), (-1,0), (0, -1), (1, 0)]
        direction = 0 # 0 = North, 1 = West, 2 = South, 3 = East
        x, y = 0, 0

        # Run for four cycles
        for instruction in instructions:
            if instruction == "L":
                direction += 1
            elif instruction == "R":
                direction -= 1
            else: # instruction == "G"
                movement_x, movement_y = turns[direction % 4]
                x += movement_x
                y += movement_y

        # Are we back at the start?
        return x == 0 and y == 0

# Tests
assert Solution().isRobotBounded("GGLLGG") == True
assert Solution().isRobotBounded("GG") == False
assert Solution().isRobotBounded("GL") == True
