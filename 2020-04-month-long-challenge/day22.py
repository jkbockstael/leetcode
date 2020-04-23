#!/usr/bin/env python3

# Day 22: Subarray Sum Equals K
#
# Given an array of integers and an integer k, you need to find the total
# number of continuous subarrays whose sum equals to k.

class Solution:
    def subarraySum(self, nums: [int], k: int) -> int:
        count = 0
        ways_to_sum = {}
        current_sum = 0
        for number in nums:
            current_sum += number
            if current_sum == k:
                count += 1
            if current_sum - k in ways_to_sum:
                count += ways_to_sum[current_sum - k]
            if current_sum not in ways_to_sum:
                ways_to_sum[current_sum] = 1
            else:
                ways_to_sum[current_sum] += 1
        return count

# Tests
assert Solution().subarraySum([1,1,1], 2) == 2
assert Solution().subarraySum([1,1], 2) == 1
assert Solution().subarraySum([1,1], 2) == 1
assert Solution().subarraySum([1], 2) == 0
assert Solution().subarraySum([1,2,3], 3) == 2
assert Solution().subarraySum([1,2,3,4,5], 3) == 2
assert Solution().subarraySum([1], 0) == 0
assert Solution().subarraySum([-1,-1,1], 0) == 1
