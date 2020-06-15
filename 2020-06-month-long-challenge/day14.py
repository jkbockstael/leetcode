#!/usr/bin/env python3

# Day 14: Cheapest Flights Within K Stops
#
# There are n cities connected by m flights. Each flight starts from city u and
# arrives at v with a price w.
# Now given all the cities and flights, together with starting city src and the
# destination dst, your task is to find the cheapest price from src to dst with
# up to k stops. If there is no such route, output -1.
#
# Constraints:
# - The number of nodes n will be in range [1, 100], with nodes labeled from 0
#   to n - 1.
# - The size of flights will be in range [0, n * (n - 1) / 2].
# - The format of each flight will be (src, dst, price).
# - The price of each flight will be in the range [1, 10000].
# - k is in the range of [0, n - 1].
# - There will not be any duplicated flights or self cycles.

import math

class Solution:
    def findCheapestPrice(self, n: int, flights: [[int]], src: int, dst: int, K: int) -> int:
        # Hello Bellman-Ford
        # distances[x] is the shortest distance from src to x
        distances = [math.inf for _ in range(n)]
        distances[src] = 0 # obviously
        for _ in range(K + 1): # we consider at max K total nodes in the path
            tmp = distances[:] # safeguard the previous iteration's outcome
            for origin, destination, cost in flights:
                tentative_distance = tmp[origin] + cost
                if tentative_distance < distances[destination]:
                    distances[destination] = tentative_distance
        return distances[dst] if distances[dst] < math.inf else -1

# Tests
assert Solution().findCheapestPrice(3, [[0,1,100],[1,2,100],[0,2,500]], 0, 2, 1) == 200
assert Solution().findCheapestPrice(3, [[0,1,100],[1,2,100],[0,2,500]], 0, 2, 0) == 500
