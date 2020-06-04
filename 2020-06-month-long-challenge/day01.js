#!/usr/bin/env nodejs

/*
 * Day 1: Invert Binary Tree
 *
 * Invert a binary tree.
 */

// Definition for a binary tree node.
function TreeNode(val, left, right) {
    this.val = (val===undefined ? 0 : val)
    this.left = (left===undefined ? null : left)
    this.right = (right===undefined ? null : right)
}
/**
 * @param {TreeNode} root
 * @return {TreeNode}
 */
const invertTree = root =>
    (root == undefined)
    ? null
    : new TreeNode(root.val, invertTree(root.right), invertTree(root.left))

// Tests

let test_tree = new TreeNode(4)
test_tree.left = new TreeNode(2)
test_tree.right = new TreeNode(7)
test_tree.left.left = new TreeNode(1)
test_tree.left.right = new TreeNode(3)
test_tree.right.left = new TreeNode(6)
test_tree.right.right = new TreeNode(9)
let inverted_tree = invertTree(test_tree)
console.assert(inverted_tree.val == 4);
console.assert(inverted_tree.left.val == 7);
console.assert(inverted_tree.right.val == 2);
console.assert(inverted_tree.left.left.val == 9);
console.assert(inverted_tree.left.right.val == 6);
console.assert(inverted_tree.right.left.val == 3);
console.assert(inverted_tree.right.right.val == 1);
