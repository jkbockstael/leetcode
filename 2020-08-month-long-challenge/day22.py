#!/usr/bin/env python3

# Day 22: Random Point in Non-overlapping Rectangles
#
# Given a list of non-overlapping axis-aligned rectangles rects, write a
# function pick which randomly and uniformily picks an integer point in the
# space covered by the rectangles.
#
# Note:
# - An integer point is a point that has integer coordinates.
# - A point on the perimeter of a rectangle is included in the space covered by
#   the rectangles. 
# - ith rectangle = rects[i] = [x1,y1,x2,y2], where [x1, y1] are the integer
#   coordinates of the bottom-left corner, and [x2, y2] are the integer
#   coordinates of the top-right corner.
# - length and width of each rectangle does not exceed 2000.
# - 1 <= rects.length <= 100
# - pick return a point as an array of integer coordinates [p_x, p_y]
# - pick is called at most 10000 times.

import random

class Solution:
    def __init__(self, rects: [[int]]):
        def area(rectangle) -> int:
            # In this problem's context, the area of a rectangle is the number
            # of integer points enclosed by the rectangle or on the rectangle's
            # perimeter
            x1, y1, x2, y2 = rectangle
            return (x2 - x1 + 1) * (y2 - y1 + 1)

        # Store the rectangles and their areas, by ascending order of area
        self.rectangles = sorted(rects, key=area)
        self.areas = [area(rectangle) for rectangle in self.rectangles]
        self.total_area = sum(self.areas)

    def pick(self) -> [int]:
        # Pick one of the possible points
        point = random.randint(0, self.total_area)
        # Find the rectangle this point belongs to
        for index, area in enumerate(self.areas):
            point -= area
            if point < 0:
                break;
        # Pick a random point inside this rectangle
        x1, y1, x2, y2 = self.rectangles[index]
        return [random.randint(x1, x2), random.randint(y1, y2)]

# No proper tests for these problems about randomness, I'm lazy
picker = Solution([[-2,-2,-1,-1],[1,0,3,0]])
for _ in range(10):
    print(picker.pick())
