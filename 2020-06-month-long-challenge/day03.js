#!/usr/bin/env nodejs

/*
 * Day 3: Two City Scheduling
 *
 * There are 2N people a company is planning to interview. The cost of flying
 * the i-th person to city A is costs[i][0], and the cost of flying the i-th
 * person to city B is costs[i][1].
 * Return the minimum cost to fly every person to a city such that exactly N
 * people arrive in each city.
 *
 * Note:
 * - 1 <= costs.length <= 100
 * - It is guaranteed that costs.length is even.
 * - 1 <= costs[i][0], costs[i][1] <= 1000
 */

/**
 * @param {number[][]} costs
 * @return {number}
 */
var twoCitySchedCost = function(costs) {
    const N = costs.length / 2
    costs.sort((a,b) => (a[0] - a[1]) - (b[0] - b[1]))
    total = 0
    for (let i = 0; i < costs.length; i++) {
        if (i < N) {
            total += costs[i][0]
        } else {
            total += costs[i][1]
        }
    }
    return total
};

// Tests
console.assert(twoCitySchedCost([[10,20],[30,200],[400,50],[30,20]]) == 110)
console.assert(twoCitySchedCost([[259,770],[448,54],[926,667],[184,139],[840,118],[577,469]]) == 1859)
