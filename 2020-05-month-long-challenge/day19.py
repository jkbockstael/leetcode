#!/usr/bin/env python3

# Day 19: Online Stock Span
#
# Write a class StockSpanner which collects daily price quotes for some stock,
# and returns the span of that stock's price for the current day.
# The span of the stock's price today is defined as the maximum number of
# consecutive days (starting from today and going backwards) for which the
# price of the stock was less than or equal to today's price.
#
# For example, if the price of a stock over the next 7 days were [100, 80, 60,
# 70, 60, 75, 85], then the stock spans would be [1, 1, 1, 2, 1, 4, 6].
#
# Notes:
# - Calls to StockSpanner.next(int price) will have 1 <= price <= 10^5.
# - There will be at most 10000 calls to StockSpanner.next per test case.
# - There will be at most 150000 calls to StockSpanner.next across all test
#   cases.
# - The total time limit for this problem has been reduced by 75% for C++, and
#   50% for all other languages.

class StockSpanner:
    def __init__(self):
        # Stack of (price, span)
        self.spans_stack = []

    def next(self, price: int) -> int:
        span = 1 # Today
        while len(self.spans_stack) > 0 and self.spans_stack[-1][0] <= price:
            span += self.spans_stack.pop()[1]
        self.spans_stack.append((price, span))
        return span

# Tests
S = StockSpanner()
assert S.next(100) == 1
assert S.next(80) == 1
assert S.next(60) == 1
assert S.next(70) == 2
assert S.next(60) == 1
assert S.next(75) == 4
assert S.next(85) == 6
