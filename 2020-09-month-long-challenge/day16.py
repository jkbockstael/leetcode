#!/usr/bin/env python3

# Day 16: Maximum XOR of Two Numbers in an Array
#
# Given an integer array nums, return the maximum result of nums[i] XOR
# nums[j], where 0 ≤ i ≤ j < n.
#
# Follow up: Could you do this in O(n) runtime?
#
# Constraints:
# - 1 <= nums.length <= 2 * 10^4
# - 0 <= nums[i] <= 2^31 - 1

class Solution:
    def findMaximumXOR(self, nums: [int]) -> int:
        # This is beautiful, but too slow for LeetCode
        # return max(a ^ b for a in nums for b in nums)

        # An iterative approach is harder to read but faster
        best = 0
        mask = 0
        prefixes = set()

        # Input numbers are guaranteed to be < 2^31
        for i in range(30, -1, -1):
            mask |= (1 << i)
            current_best = best | (1 << i)
            
            for number in nums:
                prefixes.add(number & mask)

            for prefix in prefixes:
                if (current_best ^ prefix) in prefixes:
                    best = current_best
                    break

            prefixes.clear()

        return best

# Tests
assert Solution().findMaximumXOR([3,10,5,25,2,8]) == 28
assert Solution().findMaximumXOR([0]) == 0
assert Solution().findMaximumXOR([2,4]) == 6
assert Solution().findMaximumXOR([8,10,2]) == 10
assert Solution().findMaximumXOR([14,70,53,83,49,91,36,80,92,51,66,70]) == 127
