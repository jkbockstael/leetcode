#!/usr/bin/env nodejs

/*
 * Day 5: Random Pick with Weight
 *
 * Given an array w of positive integers, where w[i] describes the weight of
 * index i, write a function pickIndex which randomly picks an index in
 * proportion to its weight.
 *
 * Note:
 * - 1 <= w.length <= 10000
 * - 1 <= w[i] <= 10^5
 * - pickIndex will be called at most 10000 times.
 */

/**
 * @param {number[]} w
 */
var Solution = function(w) {
    // Compute a list of cumulative weights
    let cumulative = 0
    this.cumulatives = []
    for (weight of w) {
        cumulative += weight
        this.cumulatives.push(cumulative)
    }
};

/**
 * @return {number}
 */
Solution.prototype.pickIndex = function() {
    // Pick a random integer in the larger range of cumulative weights
    let min = 1
    let max = this.cumulatives[this.cumulatives.length - 1]
    let number = Math.floor(Math.random() * (max - min)) + min
    // Basic binary search for the index of that value
    let left = 0
    let right = this.cumulatives.length - 1
    let middle = undefined
    while (left < right) {
        middle = Math.floor((left + right) / 2)
        if (number <= this.cumulatives[middle]) {
            right = middle - 1
        } else {
            left = middle + 1
        }
    }
    return left
};

/** 
 * Your Solution object will be instantiated and called as such:
 * var obj = new Solution(w)
 * var param_1 = obj.pickIndex()
 */
