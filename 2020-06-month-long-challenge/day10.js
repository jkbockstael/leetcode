#!/usr/bin/env nodejs

/*
 * Day 10: Search Insert Position
 *
 * Given a sorted array and a target value, return the index if the target is
 * found. If not, return the index where it would be if it were inserted in
 * order.
 * You may assume no duplicates in the array.
 */

/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var searchInsert = function(nums, target) {
    // 30% slower than the exact same algorithm in Python, yay JavaScript!
    for (let i = 0; i < nums.length; i++) {
        if (nums[i] >= target) {
            return i
        }
    }
    return nums.length
};

// Tests
console.assert(searchInsert([1,3,5,6], 5) == 2)
console.assert(searchInsert([1,3,5,6], 2) == 1)
console.assert(searchInsert([1,3,5,6], 7) == 4)
console.assert(searchInsert([1,3,5,6], 0) == 0)
