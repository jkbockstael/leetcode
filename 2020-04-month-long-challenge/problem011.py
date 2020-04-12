#!/usr/bin/env python3

# Day 11: Diameter of Binary Tree
#
# Given a binary tree, you need to compute the length of the diameter of the tree. The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root. 
# Note: The length of path between two nodes is represented by the number of edges between them. 

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def height(self, root: TreeNode) -> int:
        if root is None:
            return 0
        else:
            return 1 + max(self.height(root.left), self.height(root.right))
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        if root is None:
            return 0
        else:
            return max(self.height(root.left) + self.height(root.right),
                self.diameterOfBinaryTree(root.left),
                self.diameterOfBinaryTree(root.right))
        

# Test
test_tree = TreeNode(1)
test_tree.left = TreeNode(2)
test_tree.right = TreeNode(3)
test_tree.left.left = TreeNode(4)
test_tree.left.right = TreeNode(5)
assert Solution().diameterOfBinaryTree(test_tree) == 3
