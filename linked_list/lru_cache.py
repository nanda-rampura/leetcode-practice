class LRUCache:
    """
Problem: LRU Cache
Difficulty: Medium
LeetCode: https://leetcode.com/problems/lru-cache/

Pattern: Design / Hash Map + Doubly Linked List

Approach:
- Use a hash map to provide O(1) access to cache entries.
- Maintain a doubly linked list to track usage order.
- Move accessed or updated nodes to the front.
- Remove the least recently used node from the tail when capacity is exceeded.

Time Complexity:
- get(): O(1)
- put(): O(1)

Space Complexity: O(capacity)
"""
    class Node:
        def __init__(self, key=0, value=0):
            self.key = key
            self.value = value
            self.prev = None
            self.next = None

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.map = {}

        # dummy head and tail
        self.head = self.Node()
        self.tail = self.Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    # ---------------- INTERNAL HELPERS ---------------- #

    def _remove(self, node):
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    def _add_front(self, node):
        first = self.head.next

        node.next = first
        node.prev = self.head

        self.head.next = node
        first.prev = node

    def _move_to_front(self, node):
        self._remove(node)
        self._add_front(node)


    def get(self, key: int) -> int:
        if key not in self.map:
            return -1

        node = self.map[key]
        self._move_to_front(node)
        return node.value

    def put(self, key: int, value: int) -> None:

        if key in self.map:
            node = self.map[key]
            node.value = value
            self._move_to_front(node)
            return

        if len(self.map) >= self.capacity:
            lru = self.tail.prev
            self._remove(lru)
            del self.map[lru.key]

        new_node = self.Node(key, value)
        self.map[key] = new_node
        self._add_front(new_node)