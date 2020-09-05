#!/usr/bin/env python3

# Day 12: Last Stone Weight
#
# We have a collection of stones, each stone has a positive integer weight.
# Each turn, we choose the two heaviest stones and smash them together.  Suppose the stones have weights x and y with x <= y.  The result of this smash is:
# - If x == y, both stones are totally destroyed;
# - If x != y, the stone of weight x is totally destroyed, and the stone of weight y has new weight y-x.
# At the end, there is at most 1 stone left.  Return the weight of this stone (or 0 if there are no stones left.)

class Solution:
    def lastStoneWeight(self, stones: [int]) -> int:
        while len(stones) > 1:
            sorted_stones = sorted(stones)
            x, y = sorted_stones[-2:]
            if x == y:
                stones = sorted_stones[:-2]
            else:
                stones = sorted_stones[:-2] + [y - x]
            # Smash stones
        if len(stones) == 0:
            return 0
        else:
            return stones[0]


# Tests
assert Solution().lastStoneWeight([2,7,4,1,8,1]) == 1
assert Solution().lastStoneWeight([2,2]) == 0
