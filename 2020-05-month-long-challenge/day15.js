#!/usr/bin/env nodejs

/*
 * Day 15: Maximum Sum Circular Subarray
#
 * Given a circular array C of integers represented by A, find the maximum
 * possible sum of a non-empty subarray of C.
 * Here, a circular array means the end of the array connects to the beginning
 * of the array.  (Formally, C[i] = A[i] when 0 <= i < A.length, and
 * C[i+A.length] = C[i] when i >= 0.)
 * Also, a subarray may only include each element of the fixed buffer A at most
 * once.  (Formally, for a subarray C[i], C[i+1], ..., C[j], there does not
 * exist i <= k1, k2 <= j with k1 % A.length = k2 % A.length.)
#
 * Notes:
 * - -30000 <= A[i] <= 30000
 * - 1 <= A.length <= 30000
 */

/**
 * @param {number[]} A
 * @return {number}
 */
var maxSubarraySumCircular = function(A) {
    const maxSubarraySum = function(numbers) {
        let best = Number.NEGATIVE_INFINITY;
        let current = 0;
        for (number of numbers) {
            current += number
            if (best < current) {
                best = current;
            }
            if (current < 0) {
                current = 0;
            }
        }
        return best;
    };
    
    let total = A.reduce((a,b) => a + b);
    let inverted = A.map(a => -a);
    const bestContiguous = maxSubarraySum(A);
    const bestInverted = maxSubarraySum(inverted)
    if (bestInverted == -total) {
        return bestContiguous;
    } else {
        return Math.max(bestContiguous, total + bestInverted);
    }
};

// Tests
console.assert(maxSubarraySumCircular([1,-2,3,-2]) == 3);
console.assert(maxSubarraySumCircular([5,-3,5]) == 10);
console.assert(maxSubarraySumCircular([3,-1,2,-1]) == 4);
console.assert(maxSubarraySumCircular([3,-2,2,-3]) == 3);
console.assert(maxSubarraySumCircular([-2,-3,-1]) == -1);
