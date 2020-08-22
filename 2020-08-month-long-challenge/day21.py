#!/usr/bin/env python3

# Day 21: Sort Array By Parity
#
# Given an array A of non-negative integers, return an array consisting of all
# the even elements of A, followed by all the odd elements of A.
# You may return any answer array that satisfies this condition.
#
# Note:
# - 1 <= A.length <= 5000
# - 0 <= A[i] <= 5000

class Solution:
    def sortArrayByParity(self, A: [int]) -> [int]:
        # One-liner solution
        # return sorted(A, key=lambda x: x % 2)
        
        # Faster solution, as this is a simple partition
        # evens = []
        # odds = []
        # for number in A:
        #     if number % 2 == 0:
        #         evens.append(number)
        #     else:
        #         odds.append(number)
        # return evens + odds

        # Even faster solution, thanks to Python list comprehensions
        # (runtime beats 99% of submissions, memory usage beats 93%)
        return [n for n in A if n % 2 == 0] + [n for n in A if n % 2 != 0]

# Tests
assert Solution().sortArrayByParity([]) == []
assert Solution().sortArrayByParity([1,2]) == [2,1]
assert Solution().sortArrayByParity([3,1,2,4]) in [[2,4,3,1], [4,2,3,1], [2,4,1,3], [4,2,1,3]]
