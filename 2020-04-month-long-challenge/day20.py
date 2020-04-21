#!/usr/bin/env python3

# Day 20: Construct Binary Search Tree from Preorder Traversal
#
# Return the root node of a binary search tree that matches the given preorder
# traversal.
# (Recall that a binary search tree is a binary tree where for every node, any
# descendant of node.left has a value < node.val, and any descendant of
# node.right has a value > node.val.  Also recall that a preorder traversal
# displays the value of the node first, then traverses node.left, then traverses
# node.right.)

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def bstFromPreorder(self, preorder: [int]) -> TreeNode:
        # Minimal cases
        if len(preorder) == 0:
            return None
        if len(preorder) == 1:
            return TreeNode(preorder[0])
        # The first item in a preorder traversal is the root
        root = TreeNode(preorder[0])
        # The next values that are smaller than the root are in the left subtree
        preorder_left = [x for x in preorder[1:] if x < root.val]
        # The rest is in the right subtree
        preorder_right = preorder[len(preorder_left) + 1:]
        # Build the subtrees
        root.left = self.bstFromPreorder(preorder_left)
        root.right = self.bstFromPreorder(preorder_right)
        # Done
        return root

# Tests
test_tree = Solution().bstFromPreorder([8,5,1,7,10,12])
assert test_tree.val == 8
assert test_tree.left.val == 5
assert test_tree.left.left.val == 1
assert test_tree.left.right.val == 7
assert test_tree.right.val == 10
assert test_tree.right.left == None
assert test_tree.right.right.val == 12
test_tree = Solution().bstFromPreorder([1])
assert test_tree.val == 1
test_tree = Solution().bstFromPreorder([])
assert test_tree == None
