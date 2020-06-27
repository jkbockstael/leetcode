#!/usr/bin/env python3

# Day 26: Sum Root to Leaf Numbers
#
# Given a binary tree containing digits from 0-9 only, each root-to-leaf path
# could represent a number.
# An example is the root-to-leaf path 1->2->3 which represents the number 123.
# Find the total sum of all root-to-leaf numbers.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        def sumRec(root: TreeNode, acc: int) -> int:
            # Base case
            if root is None:
                return 0
            # Node value
            acc = (acc * 10) + root.val
            # Leaf case
            if root.left is None and root.right is None:
                return acc
            # Node case
            return sumRec(root.left, acc) + sumRec(root.right, acc)

        return sumRec(root, 0)

# Tests
test_tree = TreeNode(1)
test_tree.left = TreeNode(2)
test_tree.right = TreeNode(3)
assert Solution().sumNumbers(test_tree) == 25
test_tree = TreeNode(4)
test_tree.left = TreeNode(9)
test_tree.right = TreeNode(0)
test_tree.left.left = TreeNode(5)
test_tree.left.right = TreeNode(1)
assert Solution().sumNumbers(test_tree) == 1026
