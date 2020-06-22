#!/usr/bin/env python3

# Day 21: Dungeon Game
#
# The demons had captured the princess (P) and imprisoned her in the
# bottom-right corner of a dungeon. The dungeon consists of M x N rooms laid
# out in a 2D grid. Our valiant knight (K) was initially positioned in the
# top-left room and must fight his way through the dungeon to rescue the
# princess.
# The knight has an initial health point represented by a positive integer. If
# at any point his health point drops to 0 or below, he dies immediately.
# Some of the rooms are guarded by demons, so the knight loses health (negative
# integers) upon entering these rooms; other rooms are either empty (0's) or
# contain magic orbs that increase the knight's health (positive integers).
# In order to reach the princess as quickly as possible, the knight decides to
# move only rightward or downward in each step.
#
# Write a function to determine the knight's minimum initial health so that he
# is able to rescue the princess.
#
# Note:
# - The knight's health has no upper bound.
# - Any room can contain threats or power-ups, even the first room the knight
#   enters and the bottom-right room where the princess is imprisoned.

class Solution:
    def calculateMinimumHP(self, dungeon: [[int]]) -> int:
        # This problem reminds me of Day 18 of the April Challenge
        height = len(dungeon)
        width = len(dungeon[0])
        required = [[0 for y in x] for x in dungeon]
        # Start at the end and DP to the start
        for row in range(height - 1, -1, -1):
            for column in range(width - 1, -1, -1):
                # Bottom-right room
                if row == height - 1 and column == width - 1:
                    required[row][column] = max(1, 1 - dungeon[row][column])
                # Bottom row
                elif row == height - 1:
                    required[row][column] = max(1, \
                        required[row][column + 1] - dungeon[row][column])
                # Rightmost column
                elif column == width - 1:
                    required[row][column] = max(1, \
                        required[row + 1][column] - dungeon[row][column])
                # General case
                else:
                    required[row][column] = max(1, \
                        min(required[row][column + 1], \
                            required[row + 1][column]) \
                        - dungeon[row][column])
        return required[0][0]

# Test
assert Solution().calculateMinimumHP([[-2, -3, 3], [-5, -10, 1], [10, 30, -5]]) == 7
