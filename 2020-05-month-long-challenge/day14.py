#!/usr/bin/env python3

# Day 14: Implement Trie (Prefix Tree)
#
# Implement a trie with insert, search, and startsWith methods.
#
# Notes:
# - You may assume that all inputs are consist of lowercase letters a-z.
# - All inputs are guaranteed to be non-empty strings.

class Trie:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = {} # basic types for the win
        

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        node = self.root
        for letter in word:
            if letter not in node:
                node[letter] = {}
            node = node[letter]
        node['#'] = True
        

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        node = self.root
        for letter in word:
            if letter not in node:
                return False
            node = node[letter]
        return '#' in node
        

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        node = self.root
        for letter in prefix:
            if letter not in node:
                return False
            node = node[letter]
        return True


# Tests
trie = Trie()
trie.insert("apple")
assert trie.search("apple") == True
assert trie.search("app") == False
assert trie.startsWith("app") == True
trie.insert("app");   
assert trie.search("app") == True
