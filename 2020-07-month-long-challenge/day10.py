#!/usr/bin/env python3

# Day 10: Flatten a Multilevel Doubly Linked List
#
# You are given a doubly linked list which in addition to the next and previous
# pointers, it could have a child pointer, which may or may not point to a
# separate doubly linked list. These child lists may have one or more children
# of their own, and so on, to produce a multilevel data structure.
# Flatten the list so that all the nodes appear in a single-level, doubly
# linked list. You are given the head of the first level of the list.
#
# Constraints:
# - Number of Nodes will not exceed 1000.
# - 1 <= Node.val <= 10^5

# Definition for a Node.
class Node:
    def __init__(self, val, prev = None, next = None, child = None):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child

class Solution:
    def flatten(self, head: Node) -> Node:
        def flatten_rec(head: Node, tail: Node) -> Node:
            if head is None:
                return None
            if head.next is not None:
                head.next = flatten_rec(head.next, tail)
            elif tail is not None:
                head.next = tail
                tail.prev = head
            if head.child is not None:
                head.next = flatten_rec(head.child, head.next)
                head.next.prev = head
                head.child = None
            return head

        return flatten_rec(head, None)

# Tests
def list_to_linked(values: [int]) -> Node:
    head = None
    node = head
    for value in values:
        new_node = Node(value, node)
        if node is None:
            head = new_node
        else:
            node.next = new_node
        node = new_node
    return head

def compare_linked(a: Node, b: Node) -> Node:
    if a is None:
        return b is None
    else:
        return a.val == b.val and compare_linked(a.next, b.next)

assert Solution().flatten(None) == None
test_list = list_to_linked([1,2])
test_list.child = list_to_linked([3])
expected_list = list_to_linked([1,3,2])
assert compare_linked(Solution().flatten(test_list), expected_list)
test_list = list_to_linked([1,2,3,4,5,6])
test_list.next.next.child = list_to_linked([7,8,9,10])
test_list.next.next.child.next.child = list_to_linked([11,12])
expected_list = list_to_linked([1,2,3,7,8,11,12,9,10,4,5,6])
assert compare_linked(Solution().flatten(test_list), expected_list)
