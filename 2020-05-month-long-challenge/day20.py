#!/usr/bin/env python3

# Day 20: Kth Smallest Element in a BST
#
# Given a binary search tree, write a function kthSmallest to find the kth
# smallest element in it.
#
# Note:
# - You may assume k is always valid, 1 ≤ k ≤ BST's total elements.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def traverse(self, root: TreeNode) -> [int]:
        if root is None:
            return []
        else:
            return self.traverse(root.left) + [root.val] \
                + self.traverse(root.right)

    def kthSmallest(self, root: TreeNode, k: int) -> int:
        # "Your runtime beats 67.36 % of python3 submissions."
        # So yeah
        return sorted(self.traverse(root))[k - 1]

# Tests
test_tree = TreeNode(3)
test_tree.left = TreeNode(1)
test_tree.right = TreeNode(4)
test_tree.left.right = TreeNode(2)
assert Solution().kthSmallest(test_tree, 1) == 1
test_tree = TreeNode(5)
test_tree.left = TreeNode(3)
test_tree.right = TreeNode(6)
test_tree.left.left = TreeNode(2)
test_tree.left.right = TreeNode(4)
test_tree.left.left.left = TreeNode(1)
assert Solution().kthSmallest(test_tree, 3) == 3
