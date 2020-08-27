#!/usr/bin/env nodejs

/* Day 21: Sort Array By Parity
 *
 * Given an array A of non-negative integers, return an array consisting of all
 * the even elements of A, followed by all the odd elements of A.
 * You may return any answer array that satisfies this condition.
 *
 * Note:
 * - 1 <= A.length <= 5000
 * - 0 <= A[i] <= 5000
 */

/**
 * @param {number[]} A
 * @return {number[]}
 */
var sortArrayByParity = function(A) {
    let evens = []
    let odds = []
    for (number of A) {
        if (number % 2 == 0) {
            evens.push(number)
        } else {
            odds.push(number)
        }
    }
    foo = evens.concat(odds)
    console.log(foo)
    return foo
};
