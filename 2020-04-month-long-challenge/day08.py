#!/usr/bin/env python3

# Day 8: Middle of the Linked List
#
# Given a non-empty, singly linked list with head node head, return a middle node of linked list.
# If there are two middle nodes, return the second middle node.
# Note: The number of nodes in the given list will be between 1 and 100.

# Definition for singly-linked list.
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        list_length = 1
        node = head
        while node.next is not None:
            node = node.next
            list_length += 1
        counter = 0
        node = head
        while counter < list_length // 2:
            counter += 1
            node = node.next
        return node

# Testing support function
def linked(items: [int]) -> ListNode:
    head = ListNode(items[0])
    node = head
    for item in items[1:]:
        node.next = ListNode(item)
        node = node.next
    return head

# Tests
case_1 = linked([1,2,3,4,5])
expected_1 = case_1.next.next
assert Solution().middleNode(case_1) == expected_1, "[1,2,3,4,5] → [3,4,5]"
case_2 = linked([1,2,3,4,5,6])
expected_2 = case_2.next.next.next
assert Solution().middleNode(case_2) == expected_2, "[1,2,3,4,5,6] → [4,5,6]"
