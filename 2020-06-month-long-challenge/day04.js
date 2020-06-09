#!/usr/bin/env nodejs

/*
 * Day 4: Reverse String
 *
 * Write a function that reverses a string. The input string is given as an
 * array of characters char[].
 * Do not allocate extra space for another array, you must do this by modifying
 * the input array in-place with O(1) extra memory.
 * You may assume all the characters consist of printable ascii characters.
 */

/**
 * @param {character[]} s
 * @return {void} Do not return anything, modify s in-place instead.
 */
var reverseString = function(s) {
    // Manually for the sake of it
    for (let i = 0; i < s.length / 2; i++) {
        let tmp = s[i]
        s[i] = s[s.length - i - 1]
        s[s.length - i - 1] = tmp
    }
};

// Tests
let test_string = ["h","e","l","l","o"]
reverseString(test_string)
// [1,2,3] == [1,2,3] is false in JavaScript, because it is a beautiful and
// thoughfully designed langage
console.assert(test_string.join('') == 'olleh')
test_string = ["H","a","n","n","a","h"]
reverseString(test_string)
console.assert(test_string.join('') == 'hannaH')
