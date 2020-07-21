#!/usr/bin/env python3

# Day 20: Remove Linked List Elements
#
# Remove all elements from a linked list of integers that have value val.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        dummy = ListNode(-1)
        dummy.next = head
        current = dummy
        while current.next is not None:
            if current.next.val == val:
                current.next = current.next.next
            else:
                current = current.next
        return dummy.next

# Test
def list2linked(numbers: [int]) -> ListNode:
    if len(numbers) == 0:
        return None
    head = ListNode()
    node = head
    while len(numbers) > 1:
        node.val = numbers[0]
        node.next = ListNode()
        node = node.next
        numbers = numbers[1:]
    if len(numbers) > 0:
        node.val = numbers[0]
    return head

def compare_linked(a: ListNode, b: ListNode) -> ListNode:
    if a is None:
        return b is None
    else:
        return a.val == b.val and compare_linked(a.next, b.next)

test_list = list2linked([1,2,6,3,4,5,6])
expected = list2linked([1,2,3,4,5])
assert compare_linked(Solution().removeElements(test_list, 6), expected)
