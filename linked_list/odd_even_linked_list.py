# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional
from linked_list.merge_linked_lists import ListNode

class OddEvenLinkedList:
    """
Problem: Odd Even Linked List
Difficulty: Medium
LeetCode: https://leetcode.com/problems/odd-even-linked-list/
Pattern: Linked List / Pointer Rewiring
Topics: Linked List, Two Pointers
Time Complexity: O(n)
Space Complexity: O(1)

Key Insight:
Maintain two separate chains:
- odd indexed nodes
- even indexed nodes

Rewire pointers in-place while traversing once,
then connect even list at the end of odd list.
"""
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head

        evenhead = head.next
        odd = head
        even = evenhead

        while even and even.next:
            odd.next = even.next
            odd = odd.next

            even.next = odd.next
            even = even.next

        odd.next = evenhead

        return head