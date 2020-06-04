#!/usr/bin/env python3

# Day 3: Two City Scheduling
#
# There are 2N people a company is planning to interview. The cost of flying
# the i-th person to city A is costs[i][0], and the cost of flying the i-th
# person to city B is costs[i][1].
# Return the minimum cost to fly every person to a city such that exactly N
# people arrive in each city.
#
# Note:
# - 1 <= costs.length <= 100
# - It is guaranteed that costs.length is even.
# - 1 <= costs[i][0], costs[i][1] <= 1000

class Solution:
    def twoCitySchedCost(self, costs: [[int]]) -> int:
        N = len(costs) // 2
        # Greedy!
        sorted_costs = sorted(costs, key=lambda cost: cost[0] - cost[1])
        return sum(cost[0] for cost in sorted_costs[:N]) \
            + sum(cost[1] for cost in sorted_costs[N:])

# Test
assert Solution().twoCitySchedCost([[10,20],[30,200],[400,50],[30,20]]) == 110
assert Solution().twoCitySchedCost([[259,770],[448,54],[926,667],[184,139],[840,118],[577,469]]) == 1859
