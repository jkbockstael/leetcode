#!/usr/bin/env nodejs

/*
 * Day 2: Delete Node in a Linked List
 *
 * Write a function to delete a node (except the tail) in a singly linked list,
 * given only access to that node.
 * 
 * Note:
 * - The linked list will have at least two elements.
 * - All of the nodes' values will be unique.
 * - The given node will not be the tail and it will always be a valid node of
 *   the linked list.
 * - Do not return anything from your function.
 */

// Definition for singly-linked list.
function ListNode(val) {
    this.val = val;
    this.next = null;
}

/**
 * @param {ListNode} node
 * @return {void} Do not return anything, modify node in-place instead.
 */
var deleteNode = function(node) {
    node.val = node.next.val
    node.next = node.next.next
};

// Tests
let test_list = new ListNode(4)
test_list.next = new ListNode(5)
test_list.next.next = new ListNode(1)
test_list.next.next.next = new ListNode(9)
let test_node = test_list.next // 5
deleteNode(test_node)
console.assert(test_list.val == 4)
console.assert(test_list.next.val == 1)
console.assert(test_list.next.next.val == 9)
test_list = new ListNode(4)
test_list.next = new ListNode(5)
test_list.next.next = new ListNode(1)
test_list.next.next.next = new ListNode(9)
test_node = test_list.next.next // 1
deleteNode(test_node)
console.assert(test_list.val == 4)
console.assert(test_list.next.val == 5)
console.assert(test_list.next.next.val == 9)
