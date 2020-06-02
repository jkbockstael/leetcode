#!/usr/bin/env python3

# Day 1: Invert Binary Tree
#
# Invert a binary tree.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root is None:
            return None
        # Immutability is good
        node = TreeNode(root.val)
        node.left = self.invertTree(root.right)
        node.right = self.invertTree(root.left)
        return node

# Test
test_tree = TreeNode(4)
test_tree.left = TreeNode(2)
test_tree.right = TreeNode(7)
test_tree.left.left = TreeNode(1)
test_tree.left.right = TreeNode(3)
test_tree.right.left = TreeNode(6)
test_tree.right.right = TreeNode(9)
inverted_tree = Solution().invertTree(test_tree)
assert inverted_tree.val == 4
assert inverted_tree.left.val == 7
assert inverted_tree.right.val == 2
assert inverted_tree.left.left.val == 9
assert inverted_tree.left.right.val == 6
assert inverted_tree.right.left.val == 3
assert inverted_tree.right.right.val == 1
