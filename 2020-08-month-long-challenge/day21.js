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
    return evens.concat(odds)
};

// Let's build a list comparison function since [a,b,c] == [d,e,f] doesn't work
// in JavaScript
const eq = x => y => x == y
const range = n => [...Array(n).keys()]
const map = fn => xs => xs.map(fn)
const zipwith = fn => xs => ys =>
    map(i => fn(xs[i])(ys[i]))(range(Math.min(xs.length, ys.length)))
const all = xs => xs.every(x => x == true)
const list_equal = xs => ys => eq(xs.length)(ys.length)
    && all(zipwith(eq)(xs)(ys))

// Tests
console.assert(list_equal(sortArrayByParity([]))([]))
console.assert(list_equal(sortArrayByParity([1,2]))([2,1]))
console.assert(list_equal(sortArrayByParity([3,1,2,4]))([2,4,3,1]))
