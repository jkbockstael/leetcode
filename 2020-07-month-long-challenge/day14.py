#!/usr/bin/env python3

# Day 14: Angle Between Hands of a Clock
#
# Given two numbers, hour and minutes. Return the smaller angle (in degrees)
# formed between the hour and the minute hand.
#
# Constraints:
# - 1 <= hour <= 12
# - 0 <= minutes <= 59
# - Answers within 10^-5 of the actual value will be accepted as correct.

class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        angle = abs(30.0 * hour - 5.5 * minutes)
        return min(angle, 360.0 - angle)

# Tests
assert abs(Solution().angleClock(12,30) - 165) < 0.00001
assert abs(Solution().angleClock(3,30) - 75) < 0.00001
assert abs(Solution().angleClock(3,15) - 7.5) < 0.00001
assert abs(Solution().angleClock(4,50) - 155) < 0.00001
assert abs(Solution().angleClock(12,0) - 0) < 0.00001
