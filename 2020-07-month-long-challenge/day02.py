#!/usr/bin/env python3

# Day 2: Binary Tree Level Order Traversal II
#
# Given a binary tree, return the bottom-up level order traversal of its nodes'
# values. (ie, from left to right, level by level from leaf to root).

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> [[int]]:
        if root is None:
            return []
        result = [[root.val]]
        queue = [root]
        while len(queue) > 0:
            children = []
            for node in queue:
                if node.left is not None:
                    children.append(node.left)
                if node.right is not None:
                    children.append(node.right)
            queue = children
            if len(children) > 0:
                result.append([node.val for node in queue])
        return result[::-1]

# Test
test_tree = TreeNode(3)
test_tree.left = TreeNode(9)
test_tree.right = TreeNode(20)
test_tree.right.left = TreeNode(15)
test_tree.right.right = TreeNode(7)
assert Solution().levelOrderBottom(test_tree) == [[15,7],[9,20],[3]]
