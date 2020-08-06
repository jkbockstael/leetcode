#!/usr/bin/env python3

# Day 5: Add and Search Word - Data structure design
#
# Design a data structure that supports the following two operations:
# - void addWord(word)
# - bool search(word)
#
# search(word) can search a literal word or a regular expression string
# containing only letters a-z or .. A . means it can represent any one letter.

class WordDictionary:
    # This is actually a Trie, with a twist
    def __init__(self):
        self.root = {}

    def addWord(self, word: str) -> None:
        node = self.root
        for letter in word:
            if letter not in node:
                node[letter] = {}
            node = node[letter]
        node['#'] = True

    def search(self, word: str) -> bool:
        def search_rec(word, node):
            for i in range(len(word)):
                letter = word[i]
                if letter != '.' and letter not in node:
                    return False
                # Here's the twist: if the current letter is a wildcard
                # character, replace it with every possible character at this
                # node and carry on searching
                if letter == '.':
                    return any([search_rec(wild + word[i+1:], node) \
                        for wild in node if wild != '#'])
                else:
                    node = node[letter]
            return '#' in node
        return search_rec(word, self.root)

# Tests
wd = WordDictionary()
wd.addWord("bad")
wd.addWord("dad")
wd.addWord("mad")
assert wd.search("pad") == False
assert wd.search("bad") == True
assert wd.search(".ad") == True
assert wd.search("b..") == True
