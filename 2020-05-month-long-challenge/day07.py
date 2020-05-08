#!/usr/bin/env python3

# Day 7: Cousins in Binary Tree
#
# In a binary tree, the root node is at depth 0, and children of each depth k
# node are at depth k+1.
# Two nodes of a binary tree are cousins if they have the same depth, but have
# different parents.
# We are given the root of a binary tree with unique values, and the values x
# and y of two different nodes in the tree.
# Return true if and only if the nodes corresponding to the values x and y are
# cousins.
# Notes:
# - The number of nodes in the tree will be between 2 and 100.
# - Each node has a unique integer value from 1 to 100.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def enumerate(self, root: TreeNode, depth=0, parent=None) -> dict:
        if root is None:
            return {}
        else:
            elems = {root.val: (depth, parent)}
            elems.update(self.enumerate(root.left, depth + 1, root.val))
            elems.update(self.enumerate(root.right, depth + 1, root.val))
            return elems

    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        elems = self.enumerate(root)
        return elems[x][0] == elems[y][0] and elems[x][1] != elems[y][1]

# Tests
test_tree = TreeNode(1)
test_tree.left = TreeNode(2)
test_tree.right = TreeNode(3)
test_tree.left.left = TreeNode(4)
assert Solution().isCousins(test_tree, 4, 3) == False
test_tree = TreeNode(1)
test_tree.left = TreeNode(2)
test_tree.right = TreeNode(3)
test_tree.left.right = TreeNode(4)
test_tree.right.right = TreeNode(5)
assert Solution().isCousins(test_tree, 5, 4) == True
test_tree = TreeNode(1)
test_tree.left = TreeNode(2)
test_tree.right = TreeNode(3)
test_tree.left.right = TreeNode(4)
assert Solution().isCousins(test_tree, 2, 3) == False
