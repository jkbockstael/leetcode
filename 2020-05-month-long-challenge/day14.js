#!/usr/bin/env nodejs

/*
 * Day 14: Implement Trie (Prefix Tree)
 *
 * Implement a trie with insert, search, and startsWith methods.
 *
 * Notes:
 * - You may assume that all inputs are consist of lowercase letters a-z.
 * - All inputs are guaranteed to be non-empty strings.
 */

/**
 * Initialize your data structure here.
 */
var Trie = function() {
    this.root = {};
};

/**
 * Inserts a word into the trie. 
 * @param {string} word
 * @return {void}
 */
Trie.prototype.insert = function(word) {
    node = this.root;
    for (letter of word) {
        if (node[letter] == undefined) {
            node[letter] = {};
        }
        node = node[letter];
    }
    node['#'] = true;
    
};

/**
 * Returns if the word is in the trie. 
 * @param {string} word
 * @return {boolean}
 */
Trie.prototype.search = function(word) {
    node = this.root;
    for (letter of word) {
        if (node[letter] == undefined) {
            return false;
        }
        node = node[letter];
    }
    return node['#'] != undefined;
};

/**
 * Returns if there is any word in the trie that starts with the given prefix. 
 * @param {string} prefix
 * @return {boolean}
 */
Trie.prototype.startsWith = function(prefix) {
    node = this.root;
    for (letter of prefix) {
        if (node[letter] == undefined) {
            return false;
        }
        node = node[letter];
    }
    return true;
};

// Tests
var trie = new Trie();
trie.insert("apple");
console.assert(trie.search("apple") == true);
console.assert(trie.search("app") == false);
console.assert(trie.startsWith("app") == true);
trie.insert("app");   
console.assert(trie.search("app") == true);
