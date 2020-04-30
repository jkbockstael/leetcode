#!/usr/bin/env python3

# Day 29: Binary Tree Maximum Path Sum
#
# Given a non-empty binary tree, find the maximum path sum.
# For this problem, a path is defined as any sequence of nodes from some
# starting node to any node in the tree along the parent-child connections. The
# path must contain at least one node and does not need to go through the root.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxPathSumRec(self, root: TreeNode) -> int:
        if root is None:
            return 0
        node = root.val
        left = self.maxPathSumRec(root.left)
        right = self.maxPathSumRec(root.right)
        candidates = [node]
        if root.left is not None:
            candidates.append(node + left)
        if root.right is not None:
            candidates.append(node + right)
        if root.left is not None and root.right is not None:
            self.best = max(node + left + right, self.best)
        best = max(candidates)
        self.best = max(best, self.best)
        return best

    def maxPathSum(self, root: TreeNode) -> int: 
        self.best = root.val
        self.maxPathSumRec(root)
        return self.best



# Test
test_tree = TreeNode(1)
test_tree.left = TreeNode(2)
test_tree.right = TreeNode(3)
assert Solution().maxPathSum(test_tree) == 6
test_tree = TreeNode(-10)
test_tree.left = TreeNode(9)
test_tree.right = TreeNode(20)
test_tree.right.left = TreeNode(15)
test_tree.right.right = TreeNode(7)
assert Solution().maxPathSum(test_tree) == 42
test_tree = TreeNode(-3)
assert Solution().maxPathSum(test_tree) == -3
test_tree = TreeNode(-2)
test_tree.left = TreeNode(-1)
assert Solution().maxPathSum(test_tree) == -1
test_tree = TreeNode(1)
test_tree.left = TreeNode(-2)
test_tree.right = TreeNode(-3)
test_tree.left.left = TreeNode(1)
test_tree.left.right = TreeNode(3)
test_tree.left.left.left = TreeNode(-1)
test_tree.right.left = TreeNode(-2)
assert Solution().maxPathSum(test_tree) == 3
test_tree = TreeNode(1)
test_tree.left = TreeNode(-2)
test_tree.right = TreeNode(3)
assert Solution().maxPathSum(test_tree) == 4
test_tree = TreeNode(-1)
test_tree.left = TreeNode(5)
test_tree.left.left = TreeNode(4)
test_tree.left.left.right = TreeNode(2)
test_tree.left.left.right.left = TreeNode(-4)
assert Solution().maxPathSum(test_tree) == 11
test_tree = TreeNode(5)
test_tree.left = TreeNode(4)
test_tree.left.left = TreeNode(11)
test_tree.left.left.left = TreeNode(7)
test_tree.left.left.right = TreeNode(2)
test_tree.right = TreeNode(8)
test_tree.right.left = TreeNode(13)
test_tree.right.right = TreeNode(4)
test_tree.right.right.right = TreeNode(1)
assert Solution().maxPathSum(test_tree) == 48
