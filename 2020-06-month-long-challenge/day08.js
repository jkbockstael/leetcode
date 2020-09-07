#!/usr/bin/env nodejs

/*
 * Day 8: Power of Two
 *
 * Given an integer, write a function to determine if it is a power of two.
 */

/**
 * @param {number} n
 * @return {boolean}
 */
var isPowerOfTwo = function(n) {
    // In JavaScript this is faster than return n > 0 && (n & (n - 1)) == 0
    return n > 0 && n.toString(2).split('1').length == 2
};

// Tests
console.assert(isPowerOfTwo(1) == true)
console.assert(isPowerOfTwo(16) == true)
console.assert(isPowerOfTwo(218) == false)
console.assert(isPowerOfTwo(-16) == false)
