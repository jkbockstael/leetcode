#!/usr/bin/env python3

# Day 16: Odd Even Linked List
#
# Given a singly linked list, group all odd nodes together followed by the even
# nodes. Please note here we are talking about the node number and not the
# value in the nodes.
# You should try to do it in place. The program should run in O(1) space
# complexity and O(nodes) time complexity.
#
# Notes:
# - The relative order inside both the even and odd groups should remain as it
#   was in the input.
# - The first node is considered odd, the second node even and so on ...

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        result = head
        odd_pointer = None
        even_pointer = None
        even_head = None
        if head is not None:
            odd_pointer = head
            if head.next is not None:
                even_pointer = head.next
                even_head = head.next
        while odd_pointer is not None and even_pointer is not None:
            if even_pointer.next is None:
                break
            odd_pointer.next = even_pointer.next
            odd_pointer = odd_pointer.next
            even_pointer.next = odd_pointer.next
            even_pointer = even_pointer.next
        if odd_pointer is not None:
            odd_pointer.next = even_head
        return result

# Tests
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

def linked2list(root: ListNode) -> [int]:
    numbers = []
    node = root
    while node is not None:
        numbers.append(node.val)
        node = node.next
    return numbers

assert linked2list(Solution().oddEvenList(list2linked([1,2,3,4,5]))) == [1,3,5,2,4]
assert linked2list(Solution().oddEvenList(list2linked([2,1,3,5,6,4,7]))) == [2,3,6,7,1,5,4]
assert linked2list(Solution().oddEvenList(list2linked([1]))) == [1]
assert linked2list(Solution().oddEvenList(list2linked([1,2]))) == [1,2]
assert linked2list(Solution().oddEvenList(list2linked([1,2,3]))) == [1,3,2]
assert linked2list(Solution().oddEvenList(list2linked([]))) == []
