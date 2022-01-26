#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 26-01-2022 15:24
# @Author  : Tushar Gupta
# One test case not passing

from collections import deque
import heapq


class Node:

    def __init__(self, key, value):
        self.key = key
        self.val = value
        self.prev = None
        self.next = None


class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.cache = {}
        self.head = Node(-1, -1)
        self.tail = self.head

    def remove(self, node):
        _prev = node.prev
        _next = node.next

        if _next is None:
            self.head = Node(-1, -1)
            self.tail = self.head
        else:
            _prev.next = _next
            _next.prev = _prev

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """

        if key in self.cache:
            # get the key
            # remove from linked list
            # insert at the tail

            node = self.cache[key]
            self.remove(node)
            node.prev = self.tail
            self.tail.next = node
            self.tail = node
            node.next = None
            return node.val
        else:
            return -1

    def insert(self, key, value):
        node = Node(key, value)
        self.cache[key] = node

        if self.head == self.tail:
            self.head.next = node
            node.prev = self.head
            self.tail = node
            node.next = None
            return

        node.prev = self.tail
        self.tail.next = node
        self.tail = node
        node.next = None

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        print("Here", key)
        print("before", self.cache)
        # check if key exists
        # update
        if key in self.cache:
            self.cache[key].val = value

        # else check at capacity
        if len(self.cache) < self.capacity:
            # create a new node
            # insert in cache
            # insert at tail

            self.insert(key, value)
        else:
            node_to_remove = self.head.next
            self.head.next = node_to_remove.next
            removed_val = self.cache.pop(node_to_remove.key)
            self.insert(key, value)

        print("after", self.cache)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)