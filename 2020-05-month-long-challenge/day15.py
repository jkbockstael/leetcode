#!/usr/bin/env python3

# Day 15: Maximum Sum Circular Subarray
#
# Given a circular array C of integers represented by A, find the maximum
# possible sum of a non-empty subarray of C.
# Here, a circular array means the end of the array connects to the beginning
# of the array.  (Formally, C[i] = A[i] when 0 <= i < A.length, and
# C[i+A.length] = C[i] when i >= 0.)
# Also, a subarray may only include each element of the fixed buffer A at most
# once.  (Formally, for a subarray C[i], C[i+1], ..., C[j], there does not
# exist i <= k1, k2 <= j with k1 % A.length = k2 % A.length.)
#
# Notes:
# - -30000 <= A[i] <= 30000
# - 1 <= A.length <= 30000

class Solution:
    def maxSubarraySum(self, numbers: [int]) -> int:
        best = float("-inf")
        current = 0
        for number in numbers:
            current += number
            if best < current:
                best = current
            if current < 0:
                current = 0
        return best

    def maxSubarraySumCircular(self, A: [int]) -> int:
        total = sum(A)
        inverted = [-number for number in A]
        best_contiguous = self.maxSubarraySum(A)
        best_inverted = self.maxSubarraySum(inverted)
        if best_inverted == -total:
            return best_contiguous
        else:
            return max(best_contiguous, total + best_inverted)

# Tests
assert Solution().maxSubarraySumCircular([1,-2,3,-2]) == 3
assert Solution().maxSubarraySumCircular([5,-3,5]) == 10
assert Solution().maxSubarraySumCircular([3,-1,2,-1]) == 4
assert Solution().maxSubarraySumCircular([3,-2,2,-3]) == 3
assert Solution().maxSubarraySumCircular([-2,-3,-1]) == -1
