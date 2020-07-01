#!/usr/bin/env python3

# Day 30: Word Search II
#
# Given a 2D board and a list of words from the dictionary, find all words in
# the board.
# Each word must be constructed from letters of sequentially adjacent cell,
# where "adjacent" cells are those horizontally or vertically neighboring. The
# same letter cell may not be used more than once in a word.
#
# Note:
# - All inputs are consist of lowercase letters a-z.
# - The values of words are distinct.

# Trie implementation from May 14, slightly modified
class Trie:
    def __init__(self):
        self.root = {}
        self.root['_'] = ""
        
    def insert(self, word: str) -> None:
        node = self.root
        prefix = ""
        for letter in word:
            prefix += letter
            if letter not in node:
                node[letter] = {}
            node = node[letter]
            node['_'] = prefix
        node['#'] = True
        
    def search(self, word: str) -> bool:
        node = self.root
        for letter in word:
            if letter not in node:
                return False
            node = node[letter]
        return '#' in node

class Solution:
    def findWords(self, board: [[str]], words: [str]) -> [str]:
        # Edge cases
        if len(words) == 0 or len(board) == 0 or len(board[0]) == 0:
            return []

        # Read the input dictionary into a Trie
        trie = Trie()
        for word in words:
            trie.insert(word)

        # Go through the board and do a DFS starting at each cell
        rows = len(board)
        columns = len(board[0])
        visited = [[False for column in range(columns)] for row in range(rows)]
        def dfs(node, row, column):
            if trie.search(node['_']):
                matches.add(node['_'])
            if row < 0 or column < 0 \
                or row >= len(board) or column >= len(board[0]) \
                or visited[row][column] \
                or board[row][column] not in node:
                return None
            visited[row][column] = True
            next_node = node[board[row][column]]
            for x, y in [(row - 1, column), (row + 1, column), \
                (row, column - 1), (row, column + 1)]:
                dfs(next_node, x, y)
            visited[row][column] = False
            
        matches = set()
        for row in range(len(board)):
            for column in range(len(board[0])):
                dfs(trie.root, row, column)
        return list(matches)

# Tests
test_board = [['a', 'b']]
test_words = ['a', 'b']
assert Solution().findWords(test_board, test_words) == ['a', 'b']
test_board = [
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']]
test_words = ["oath","pea","eat","rain"]
assert Solution().findWords(test_board, test_words) == ["eat", "oath"]
