from typing import Optional
from linked_list.merge_linked_lists import ListNode

class LinkedListCycleDetector:
    """
Problem: Linked List Cycle
Difficulty: Easy
LeetCode: https://leetcode.com/problems/linked-list-cycle/
Pattern: Two Pointers / Fast & Slow (Floyd’s Cycle Detection)
"""
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                return True
            
        return False