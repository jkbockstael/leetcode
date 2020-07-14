#!/usr/bin/env python3

# Day 13: Same Tree
#
# Given two binary trees, write a function to check if they are the same or
# not.
# Two binary trees are considered the same if they are structurally identical
# and the nodes have the same value.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if p is None:
            return q is None
        if q is None:
            return p is None
        if p.val != q.val:
            return False
        else:
            return self.isSameTree(p.left, q.left) \
                and self.isSameTree(p.right, q.right)

# Tests
test_tree_a = TreeNode(1)
test_tree_a.left = TreeNode(2)
test_tree_a.right = TreeNode(3)
test_tree_b = TreeNode(1)
test_tree_b.left = TreeNode(2)
test_tree_b.right = TreeNode(3)
assert Solution().isSameTree(test_tree_a, test_tree_b) == True
test_tree_a = TreeNode(1)
test_tree_a.left = TreeNode(2)
test_tree_b = TreeNode(1)
test_tree_b.right = TreeNode(2)
assert Solution().isSameTree(test_tree_a, test_tree_b) == False
test_tree_a = TreeNode(1)
test_tree_a.left = TreeNode(2)
test_tree_a.right = TreeNode(1)
test_tree_b = TreeNode(1)
test_tree_b.left = TreeNode(1)
test_tree_b.right = TreeNode(2)
assert Solution().isSameTree(test_tree_a, test_tree_b) == False
