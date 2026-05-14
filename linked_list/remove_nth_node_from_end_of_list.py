# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional

from linked_list.middle_of_linked_list import ListNode


class Solution:
    """
Problem: Remove Nth Node From End of List
Difficulty: Medium
LeetCode: https://leetcode.com/problems/remove-nth-node-from-end-of-list/
Pattern: Linked List / Two Pointers (Fast & Slow) / Dummy Node Technique
Topics: Linked List, Two Pointers
Time Complexity: O(n)
Space Complexity: O(1)
"""
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        p0 = ListNode(0)
        p0.next = head
        slow = p0
        fast = p0

        while n > 0:
            fast = fast.next
            n -= 1

        while fast and fast.next:
            slow = slow.next
            fast = fast.next
        
        slow.next = slow.next.next

        return p0.next