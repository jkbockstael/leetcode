#!/usr/bin/env python3

# Day 17: Surrounded Regions
#
# Given a 2D board containing 'X' and 'O' (the letter O), capture all regions
# surrounded by 'X'.
# A region is captured by flipping all 'O's into 'X's in that surrounded
# region.

class Solution:
    def solve(self, board: [[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = len(board)
        if rows == 0:
            return []
        columns = len(board[0])

        # recursively search for an unsurrounded region
        def color_unsurrounded(row, column):
            # don't do anything outside the board
            if row < 0 or row >= rows or column < 0 or column >= columns:
                return
            if board[row][column] == 'O':
                # we start on the border, so that's an unsurrounded region,
                # color it recursively, ignoring diagonals
                board[row][column] = '_'
                for r in [row - 1, row + 1]:
                    color_unsurrounded(r, column)
                for c in [column - 1, column + 1]:
                    color_unsurrounded(row, c)

        # start that search with the borders of the board, as they can't be
        # surrounded
        for row in range(rows):
            for column in [0, columns - 1]:
                color_unsurrounded(row, column)
        for column in range(columns):
            for row in [0, rows - 1]:
                color_unsurrounded(row, column)

        # now color O the unsurrounded regions, everything else turns to X or
        # stays X
        for row in range(rows):
            for column in range(columns):
                board[row][column] = 'O' if board[row][column] == '_' else 'X'

        # no return is weird, man

# Test
test_board = [
    ['X', 'X', 'X', 'X'],
    ['X', 'O', 'O', 'X'],
    ['X', 'X', 'O', 'X'],
    ['X', 'O', 'X', 'X']]
Solution().solve(test_board)
assert test_board == [
    ['X', 'X', 'X', 'X'],
    ['X', 'X', 'X', 'X'],
    ['X', 'X', 'X', 'X'],
    ['X', 'O', 'X', 'X']]
