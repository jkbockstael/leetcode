#!/usr/bin/env python3

# Day 30: Check If a String Is a Valid Sequence from Root to Leaves Path in a
# Binary Tree
#
# Given a binary tree where each path going from the root to any leaf form a
# valid sequence, check if a given string is a valid sequence in such binary
# tree. 
# We get the given string from the concatenation of an array of integers arr
# and the concatenation of all values of the nodes along a path results in a
# sequence in the given binary tree.
#
# Constraints:
# - 1 <= arr.length <= 5000
# - 0 <= arr[i] <= 9
# - Each node's value is between [0 - 9].

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidSequence(self, root: TreeNode, arr: [int]) -> bool:
        # This whole function coule be written as a single boolean expression,
        # but let's split it for the sake of readability
        if root is None:
            return False
        if root.val != arr[0]:
            return False
        if len(arr) == 1:
            return root.left is None and root.right is None
        else:
            return self.isValidSequence(root.left, arr[1:]) \
                or self.isValidSequence(root.right, arr[1:])

# Tests
test_tree = TreeNode(0)
test_tree.right = TreeNode(0)
test_tree.right.left = TreeNode(0)
test_tree.left = TreeNode(1)
test_tree.left.left = TreeNode(0)
test_tree.left.left.right = TreeNode(1)
test_tree.left.right = TreeNode(1)
test_tree.left.right.left = TreeNode(0)
test_tree.left.right.right = TreeNode(0)
assert Solution().isValidSequence(test_tree, [0,1,0,1]) == True
assert Solution().isValidSequence(test_tree, [0,0,1]) == False
assert Solution().isValidSequence(test_tree, [0,1,1]) == False
