#!/usr/bin/env python3

# Day 2: Delete Node in a Linked List
#
# Write a function to delete a node (except the tail) in a singly linked list,
# given only access to that node.
#
# Note:
# - The linked list will have at least two elements.
# - All of the nodes' values will be unique.
# - The given node will not be the tail and it will always be a valid node of
#   the linked list.
# - Do not return anything from your function.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next

# Tests
test_list = ListNode(4)
test_list.next = ListNode(5)
test_list.next.next = ListNode(1)
test_list.next.next.next = ListNode(9)
test_node = test_list.next # 5
Solution().deleteNode(test_node)
assert test_list.val == 4
assert test_list.next.val == 1
assert test_list.next.next.val == 9
test_list = ListNode(4)
test_list.next = ListNode(5)
test_list.next.next = ListNode(1)
test_list.next.next.next = ListNode(9)
test_node = test_list.next.next # 1
Solution().deleteNode(test_node)
assert test_list.val == 4
assert test_list.next.val == 5
assert test_list.next.next.val == 9
