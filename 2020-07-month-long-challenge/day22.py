#!/usr/bin/env python3

# Day 22: Binary Tree Zigzag Level Order Traversal
#
# Given a binary tree, return the zigzag level order traversal of its nodes'
# values. (ie, from left to right, then right to left for the next level and
# alternate between).

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> [[int]]:
        # First get a regular level order traversal
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
        # Then flip the odd levels
        for level in range(len(result)):
            if level % 2 == 1:
                result[level] = result[level][::-1]
        return result

# Test
test_tree = TreeNode(3)
test_tree.left = TreeNode(9)
test_tree.right = TreeNode(20)
test_tree.right.left = TreeNode(15)
test_tree.right.right = TreeNode(7)
assert Solution().zigzagLevelOrder(test_tree) == [[3],[20,9],[15,7]]
