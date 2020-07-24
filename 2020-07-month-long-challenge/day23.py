#!/usr/bin/env python3

# Day 23: Single Number III
#
# Given an array of numbers nums, in which exactly two elements appear only
# once and all the other elements appear exactly twice. Find the two elements
# that appear only once.
#
# Note:
# - The order of the result is not important.
# - Your algorithm should run in linear runtime complexity. Could you implement
#   it using only constant space complexity?

class Solution:
    def singleNumber(self, nums: [int]) -> [int]:
        # Let the two unique numbers be a and b, we have a != b
        # First XOR all the numbers in the list, they will cancel each other
        # out except for a and b, so a XOR of all the numbers will get a XOR b
        a_xor_b = 0
        for number in nums:
            a_xor_b = a_xor_b ^ number
        # Find the lowest bit in a XOR b
        low_bit = a_xor_b & -a_xor_b
        # Now compare every number in the list with that low bit, this will
        # partition the list in two parts: one with numbers that have that bit
        # set to 1, and the other with numbers that have that bit set to 0.
        # XORing all the first part will yield the number a, XORing all the
        # second part will yield the number b (or the other way around, the
        # problem statement doesn't ask for any specific order)
        a = 0
        b = 0
        for number in nums:
            if number & low_bit:
                a = a ^ number
            else:
                b = b ^ number
        return [a,b]

# Test
assert Solution().singleNumber([1,2,1,3,2,5]) in [[3,5],[5,3]]
