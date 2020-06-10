#!/usr/bin/env nodejs

/*
 * Day 9: Is Subsequence
 *
 * Given a string s and a string t, check if s is subsequence of t.
 * A subsequence of a string is a new string which is formed from the original
 * string by deleting some (can be none) of the characters without disturbing
 * the relative positions of the remaining characters. (ie, "ace" is a
 * subsequence of "abcde" while "aec" is not).
 *
 * Constraints:
 * - 0 <= s.length <= 100
 * - 0 <= t.length <= 10^4
 * - Both strings consists only of lowercase characters.
 */

/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isSubsequence = function(s, t) {
    if (s.length == 0) {
        return true
    }
    if (t.length == 0) {
        return false
    }
    return t.indexOf(s[0]) != -1
        && isSubsequence(s.substring(1), t.substring(t.indexOf(s[0]) + 1 ))
};

// Tests
console.assert(isSubsequence("abc", "ahbgdc") == true)
console.assert(isSubsequence("axc", "ahbgdc") == false)
