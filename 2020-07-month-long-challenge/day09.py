#!/usr/bin/env python3

# Day 9: Maximum Width of Binary Tree
#
# Given a binary tree, write a function to get the maximum width of the given
# tree. The width of a tree is the maximum width among all levels. The binary
# tree has the same structure as a full binary tree, but some nodes are null.
# The width of one level is defined as the length between the end-nodes (the
# leftmost and right most non-null nodes in the level, where the null nodes
# between the end-nodes are also counted into the length calculation.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        def height(root: TreeNode) -> int:
            if root is None:
                return 0
            else:
                return 1 + max(height(root.left), height(root.right))

        def traverse(root: TreeNode) -> dict:
            # This tree is a monstruosity where empty nodes sometimes count
            values = {}
            queue = []
            queue.append([root, 0, 0])
            while queue:
                node, level, position = queue.pop(0)
                if level not in values:
                    values[level] = [position]
                else:
                    values[level].append(position)
                if node.left is not None:
                    queue.append([node.left, level + 1, 2 * position + 1])
                if node.right is not None:
                    queue.append([node.right, level + 1, 2 * position + 2])
            return values

        values = traverse(root)
        return max(max(values[level]) - min(values[level]) + 1 \
            for level in range(height(root)))

# Tests
test_tree = TreeNode(1)
test_tree.left = TreeNode(3)
test_tree.right = TreeNode(2)
test_tree.left.left = TreeNode(5)
test_tree.left.right = TreeNode(3)
test_tree.right.right = TreeNode(9)
assert Solution().widthOfBinaryTree(test_tree) == 4
test_tree = TreeNode(1)
test_tree.left = TreeNode(3)
test_tree.left.left = TreeNode(5)
test_tree.left.right = TreeNode(3)
assert Solution().widthOfBinaryTree(test_tree) == 2
test_tree = TreeNode(1)
test_tree.left = TreeNode(3)
test_tree.right = TreeNode(2)
test_tree.left.left = TreeNode(5)
assert Solution().widthOfBinaryTree(test_tree) == 2
test_tree = TreeNode(1)
test_tree.left = TreeNode(3)
test_tree.right = TreeNode(2)
test_tree.left.left = TreeNode(5)
test_tree.right.right = TreeNode(9)
test_tree.left.left.left = TreeNode(6)
test_tree.right.right.right = TreeNode(7)
assert Solution().widthOfBinaryTree(test_tree) == 8
