# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional
from linked_list.merge_linked_lists import ListNode

class ReverseLinkedList:
    """
Problem: Reverse Linked List
Difficulty: Easy
LeetCode: https://leetcode.com/problems/reverse-linked-list/
Pattern: Linked List / In-place Reversal
"""
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head
        prev = None
        while node:
            next = node.next
            node.next = prev
            prev = node
            node = next
        return prev 