#!/usr/bin/env python3

# Day 21: Word Search
#
# Given a 2D board and a word, find if the word exists in the grid.
# The word can be constructed from letters of sequentially adjacent cell, where
# "adjacent" cells are those horizontally or vertically neighboring. The same
# letter cell may not be used more than once.
#
# Note:
# - board and word consists only of lowercase and uppercase English letters.
# - 1 <= board.length <= 200
# - 1 <= board[i].length <= 200
# - 1 <= word.length <= 10^3

class Solution:
    def exist(self, board: [[str]], word: str) -> bool:
        rows = len(board)
        columns = len(board[0])

        # Recursive search function
        def search(row, column, seq, visited):
            # Base case
            if seq == "":
                return True
            # Out of bounds
            if row < 0 or row >= rows or column < 0 or column >= columns:
                return False
            # Wrong character
            if board[row][column] != seq[0]:
                return False
            # Recursively search for the rest of the word nearby
            neighbors = [(row - 1, column), (row + 1, column), \
                (row, column - 1), (row, column + 1)]
            for neighbor in neighbors:
                if neighbor in visited:
                    continue
                n_row = neighbor[0]
                n_col = neighbor[1]
                if search(n_row, n_col, seq[1:], visited + [(row, column)]):
                    return True
            # No possible path
            return False
    
        # Look for the word starting at all possible positions
        for row in range(rows):
            for column in range(columns):
                if search(row, column, word, []):
                    return True

        # Word couldn't be found anywhere
        return False

# Tests
test_board = [['A','B','C','E'],['S','F','C','S'],['A','D','E','E']]
assert Solution().exist(test_board, "ABCCED") == True
assert Solution().exist(test_board, "SEE") == True
assert Solution().exist(test_board, "ABCB") == False
