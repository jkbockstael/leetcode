#!/usr/bin/env python3

# Day 8: Path Sum III
#
# You are given a binary tree in which each node contains an integer value.
# Find the number of paths that sum to a given value.
#
# The path does not need to start or end at the root or a leaf, but it must go
# downwards (traveling only from parent nodes to child nodes).
# The tree has no more than 1,000 nodes and the values are in the range
# -1,000,000 to 1,000,000. 

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        # Termination condition
        if root is None:
            return 0
        
        # Get the number of valid paths for a given total starting at a given
        # node
        def dfs(node, total): 
            if node is None:
                return 0
            else:
                return (1 if node.val == total else 0) \
                    + dfs(node.left, total - node.val) \
                    + dfs(node.right, total - node.val)

        # Search for path starting at the root, and paths starting at each child
        return dfs(root, sum) \
            + self.pathSum(root.left, sum) \
            + self.pathSum(root.right, sum)

# Test
test_tree = TreeNode(10)
test_tree.left = TreeNode(5)
test_tree.right = TreeNode(-3)
test_tree.left.left = TreeNode(3)
test_tree.left.right = TreeNode(2)
test_tree.right.right = TreeNode(11)
test_tree.left.left.left = TreeNode(3)
test_tree.left.left.right = TreeNode(-2)
test_tree.left.right.right = TreeNode(1)
assert Solution().pathSum(test_tree, 8) == 3
