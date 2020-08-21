#!/usr/bin/env python3

# Day 20: Reorder List
#
# Given a singly linked list L: L0→L1→…→Ln-1→Ln,
# reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…
# You may not modify the values in the list's nodes, only nodes itself may be
# changed.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: ListNode) -> None:
        # Edge case
        if head is None:
            return None
        
        # Build a list of pointers
        nodes = []
        node = head
        while node is not None:
            nodes.append(node)
            node = node.next

        # Traverse that list to alter the nodes
        length = len(nodes)
        for index in range(length // 2):
            nodes[index].next = nodes[length - index - 1]
            nodes[length - index - 1].next = nodes[index + 1]
            if (index == length // 2 - 1):
                if length % 2 == 0:
                    nodes[length - index - 1].next = None
                else:
                    nodes[index + 1].next = None

        return head

# Tests
def list_to_linked(values: [int]) -> ListNode:
    head = None
    node = head
    for value in values:
        new_node = ListNode(value)
        if node is None:
            head = new_node
        else:
            node.next = new_node
        node = new_node
    return head

def compare_linked(a: ListNode, b: ListNode) -> ListNode:
    if a is None:
        return b is None
    else:
        return a.val == b.val and compare_linked(a.next, b.next)


assert Solution().reorderList(None) == None
test_list = list_to_linked([1,2,3,4])
expected_list = list_to_linked([1,4,2,3])
assert compare_linked(Solution().reorderList(test_list), expected_list)
test_list = list_to_linked([1,2,3,4,5])
expected_list = list_to_linked([1,5,2,4,3])
assert compare_linked(Solution().reorderList(test_list), expected_list)
