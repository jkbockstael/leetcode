#!/usr/bin/env python3

# Day 7: Vertical Order Traversal of a Binary Tree
#
# Given a binary tree, return the vertical order traversal of its nodes values.
#
# For each node at position (X, Y), its left and right children respectively
# will be at positions (X-1, Y-1) and (X+1, Y-1).
# Running a vertical line from X = -infinity to X = +infinity, whenever the
# vertical line touches some nodes, we report the values of the nodes in order
# from top to bottom (decreasing Y coordinates).
# If two nodes have the same position, then the value of the node that is
# reported first is the value that is smaller.
#
# Return an list of non-empty reports in order of X coordinate.  Every report
# will have a list of values of nodes.
#
# Note:
# - The tree will have between 1 and 1000 nodes.
# - Each node's value will be between 0 and 1000.

from collections import defaultdict

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def verticalTraversal(self, root: TreeNode) -> [[int]]:
        nodes = defaultdict(list)
        self.layers_min = float("inf")
        self.layers_max = float("-inf")

        def dfs(root, horizontal, vertical):
            self.layers_min = min(horizontal, self.layers_min)
            self.layers_max = max(horizontal, self.layers_max)
            nodes[horizontal].append((vertical, root.val))
            if root.left:
                dfs(root.left,  horizontal - 1, vertical + 1)
            if root.right:
                dfs(root.right, horizontal + 1, vertical + 1)
        
        dfs(root, 0, 0)
        traversal = []
        for layer in range(self.layers_min, self.layers_max + 1):
            traversal += [[node for layer, node in sorted(nodes[layer])]]
        return traversal

# Tests
test_tree = TreeNode(3)
test_tree.left = TreeNode(9)
test_tree.right = TreeNode(20)
test_tree.right.left = TreeNode(15)
test_tree.right.right = TreeNode(7)
assert Solution().verticalTraversal(test_tree) == [[9],[3,15],[20],[7]]
test_tree = TreeNode(1)
test_tree.left = TreeNode(2)
test_tree.right = TreeNode(3)
test_tree.left.left = TreeNode(4)
test_tree.left.right = TreeNode(5)
test_tree.right.left = TreeNode(6)
test_tree.right.right = TreeNode(7)
assert Solution().verticalTraversal(test_tree) == [[4],[2],[1,5,6],[3],[7]]
