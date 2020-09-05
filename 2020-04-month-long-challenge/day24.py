#!/usr/bin/env python3

# Day 24: LRU Cache
#
# Design and implement a data structure for Least Recently Used (LRU) cache. It
# should support the following operations: get and put.
# - get(key) - Get the value (will always be positive) of the key if the key
#   exists in the cache, otherwise return -1.
# - put(key, value) - Set or insert the value if the key is not already
#   present. When the cache reached its capacity, it should invalidate the least
#   recently used item before inserting a new item.
# The cache is initialized with a positive capacity.
#
# Followup:
# Could you do both operations in O(1) time complexity?

# Constant time requires a data structure that can be rearranged quickly
class LRUCacheNode:
    def __init__(self, key: int, value: int):
        self.key: int = key
        self.value: int = value
        self.previous: LRUCacheNode = None
        self.next: LRUCacheNode = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity: int = capacity
        # This maps the keys to the actual storage values
        self.map: dict = {}
        # Values are a double linked list, head is the least recently used
        self.head: LRUCacheNode = None
        self.tail: LRUCacheNode = None

    def get(self, key: int) -> int:
        if key in self.map:
            # This value has been accessed, so it's the most recently used
            node = self.map[key]
            self.move_to_tail(node)
            return node.value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            node = self.map[key]
            node.value = value
            self.move_to_tail(node)
        else:
            if len(self.map) == self.capacity:
                self.map.pop(self.head.key)
                self.remove(self.head)
            node = LRUCacheNode(key, value)
            self.append(node)
            self.map[key] = node

    def remove(self, node: LRUCacheNode) -> None:
        if self.head == node:
            self.head = node.next
        else:
            node.previous.next = node.next
        if self.tail == node:
            self.tail = node.previous
        else:
            node.next.previous = node.previous

    def append(self, node: LRUCacheNode) -> None:
        node.previous = self.tail
        if self.tail is not None:
            self.tail.next = node
        self.tail = node
        if self.head is None:
            self.head = node

    def move_to_tail(self, node: LRUCacheNode) -> None:
        self.remove(node)
        self.append(node)

# Tests
cache = LRUCache(2)
cache.put(1, 1)
cache.put(2, 2)
assert cache.get(1) == 1
cache.put(3, 3)
assert cache.get(2) == -1
cache.put(4, 4)
assert cache.get(1) == -1
assert cache.get(3) == 3
assert cache.get(4) == 4
