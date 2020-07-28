#!/usr/bin/env python3

# Day 27: Construct Binary Tree from Inorder and Postorder Traversal
#
# Given inorder and postorder traversal of a tree, construct the binary tree.
#
# Note:
# - You may assume that duplicates do not exist in the tree.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, inorder: [int], postorder: [int]) -> TreeNode:
        # Terminal case
        if len(inorder) == 0:
            return None  
        # Build the node
        node = TreeNode(postorder[-1])
        # Build its subtrees
        inorder_index = inorder.index(node.val)
        inorder_left = inorder[:inorder_index]
        inorder_right = inorder[inorder_index+1:]
        postorder_left = postorder[:inorder_index]
        postorder_right = postorder[inorder_index:-1]
        node.left = self.buildTree(inorder_left, postorder_left)
        node.right = self.buildTree(inorder_right, postorder_right)
        return node

# Test
test_tree = Solution().buildTree([9,3,15,20,7], [9,15,7,20,3])
assert test_tree is not None
assert test_tree.val == 3
assert test_tree.left is not None
assert test_tree.left.val == 9
assert test_tree.right is not None
assert test_tree.right.val == 20
assert test_tree.left.left is None
assert test_tree.left.right is None
assert test_tree.right.left is not None
assert test_tree.right.left.val == 15
assert test_tree.right.right is not None
assert test_tree.right.right.val == 7
assert test_tree.right.left.left is None
assert test_tree.right.left.right is None
assert test_tree.right.right.left is None
assert test_tree.right.right.right is None
