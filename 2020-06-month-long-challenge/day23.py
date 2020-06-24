#!/usr/bin/env python3

# Day 23: Count Complete Tree Nodes
#
# Given a complete binary tree, count the number of nodes.
#
# In a complete binary tree every level, except possibly the last, is
# completely filled, and all nodes in the last level are as far left as
# possible. It can have between 1 and 2h nodes inclusive at the last level h.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def countNodes(self, root: TreeNode) -> int:
        # This naive solution is still fast enough to be accepted, even though
        # it doesn't take advantage of the completeness of the tree:
        #if root is None:
        #    return 0
        #else:
        #    return 1 + self.countNodes(root.left) + self.countNodes(root.right)
        #
        # But because this is a complete binary tree, we can use the fact that
        # it's filled from the left to have a more efficient solution (even
        # though LeetCode rarely provides test inputs that are large enough for
        # this difference to be noticeable.
        #
        # A truly complete tree of height H has 2^H - 1 nodes, any complete
        # tree is made of complete subtrees. We can use that property to avoid
        # counting every single node.
        #
        # The base case stays the same: an empty subtree has zero node
        if root is None:
            return 0
        # Measure the leftmost and the rightmost heights
        leftmost_height = 1 # this node
        node = root
        while node.left is not None:
            leftmost_height += 1
            node = node.left
        rightmost_height = 1
        node = root
        while node.right is not None:
            rightmost_height += 1
            node = node.right
        # If both are equal, this is a truly complete tree
        if leftmost_height == rightmost_height:
            return 2 ** (leftmost_height) - 1
        # Otherwise we calculate it recursively, some of these recursive calls
        # will be truly complete subtrees
        else:
            return 1 + self.countNodes(root.left) + self.countNodes(root.right)

# Test
test_tree = TreeNode(1)
test_tree.left = TreeNode(2)
test_tree.right = TreeNode(3)
test_tree.left.left = TreeNode(4)
test_tree.left.right = TreeNode(5)
test_tree.right.left = TreeNode(6)
assert Solution().countNodes(test_tree) == 6
