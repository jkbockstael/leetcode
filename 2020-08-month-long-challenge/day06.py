#!/usr/bin/env python3

# Day 6: Find All Duplicates in an Array
#
# Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), some elements
# appear twice and others appear once.
# Find all the elements that appear twice in this array.
# Could you do it without extra space and in O(n) runtime?

class Solution:
    def findDuplicates(self, nums: [int]) -> [int]:
        # We have an array of length N that contains values from 1 to n, n ≤ N
        # We need to keep track of the number we've already seen, for this we
        # would need a list of m elements, m < ≤ n ≤ N
        # This means we can actually use the input array as it is large enough,
        # given that all values are positive we can flip them to negative to
        # encode the seen values
        duplicates = []
        for number in nums:
            value = abs(number) # Maybe this position has been used as a marker
            seen = abs(number) - 1 # indices start at 0, values at 1
            if nums[seen] < 0:
                # We already found this number before
                duplicates.append(value)
            else:
                # Mark the array for this number
                nums[seen] *= -1
        return duplicates

# Test
assert Solution().findDuplicates([4,3,2,7,8,2,3,1]) == [2,3]
