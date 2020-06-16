#!/usr/bin/env python3

# Day 15: Search in a Binary Search Tree
#
# Given the root node of a binary search tree (BST) and a value. You need to
# find the node in the BST that the node's value equals the given value. Return
# the subtree rooted with that node. If such node doesn't exist, you should
# return NULL.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        # This is why binary search trees are so cool
        if root is None:
            return None
        if root.val == val:
            return root
        if root.val > val:
            return self.searchBST(root.left, val)
        if root.val < val:
            return self.searchBST(root.right, val)

# Tests
test_tree = TreeNode(4)
test_tree.left = TreeNode(2)
test_tree.right = TreeNode(7)
test_tree.left.left = TreeNode(1)
test_tree.left.right = TreeNode(3)
assert Solution().searchBST(test_tree, 5) == None
subtree = Solution().searchBST(test_tree, 2)
assert subtree is not None
assert subtree.val == 2
assert subtree.left is not None
assert subtree.left.val == 1
assert subtree.right is not None
assert subtree.right.val == 3
