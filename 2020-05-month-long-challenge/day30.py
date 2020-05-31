#!/usr/bin/env python3

# Day 30: K Closest Points to Origin
#
# We have a list of points on the plane.  Find the K closest points to the
# origin (0, 0).
# (Here, the distance between two points on a plane is the Euclidean distance.)
# You may return the answer in any order.  The answer is guaranteed to be
# unique (except for the order that it is in.)
#
# Note:
# - 1 <= K <= points.length <= 10000
# - -10000 < points[i][0] < 10000
# - -10000 < points[i][1] < 10000

import math

class Solution:
    def kClosest(self, points: [[int]], K: int) -> [[int]]:
        # This could be written as a one-liner but I'd rather break it down
        # Distance function
        euclidian_distance = lambda x, y: math.sqrt(x**2 + y**2)
        # Map the input points list to (distance, point) couples
        distances = map(lambda p: (euclidian_distance(p[0], p[1]), p), points)
        # Convenience functions to access the parts of these couples
        distance = lambda a: a[0]
        point = lambda a: a[1]
        # Sort based on distance in ascending order
        sorted_distances = sorted(distances, key=distance)
        # Return the point component of the first K items
        return list(map(point, sorted_distances[:K]))

# Tests
assert Solution().kClosest([[1,3],[-2,2]], 1) == [[-2,2]]
assert Solution().kClosest([[3,3],[5,-1],[-2,4]], 2) == [[3,3],[-2,4]]
