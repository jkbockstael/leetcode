#!/usr/bin/env python3

# Day 8: Check If It Is a Straight Line
#
# You are given an array coordinates, coordinates[i] = [x, y], where [x, y]
# represents the coordinate of a point. Check if these points make a straight
# line in the XY plane.
# Constraints:
# - 2 <= coordinates.length <= 1000
# - coordinates[i].length == 2
# - -10^4 <= coordinates[i][0], coordinates[i][1] <= 10^4
# - coordinates contains no duplicate point.

class Solution:
    def checkStraightLine(self, coordinates: [[int]]) -> bool:
        if len(coordinates) == 2:
            return True
        else:
            for i in range(2, len(coordinates)):
                x1, y1 = coordinates[i - 2]
                x2, y2 = coordinates[i - 1]
                x3, y3 = coordinates[i]
                vector_product = (x2 - x1)*(y3 - y1) - (y2 - y1)*(x3 - x1)
                if vector_product != 0:
                    return False
            return True

# Tests
assert Solution().checkStraightLine([[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]) == True
assert Solution().checkStraightLine([[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]) == False
