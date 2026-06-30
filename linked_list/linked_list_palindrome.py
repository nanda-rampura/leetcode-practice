from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class LinkedListPalindrome:
    """
Problem: Palindrome Linked List
Difficulty: Easy
LeetCode: https://leetcode.com/problems/palindrome-linked-list/

Pattern: Linked List / Fast & Slow Pointer + In-place Reversal

Approach:
- Use fast/slow pointers to find middle of list
- Reverse second half of linked list
- Compare both halves node by node
- Restore list structure after comparison

Time Complexity: O(n)
Space Complexity: O(1)
"""
    def isPalindrome(self, head: Optional[ListNode]) -> bool:

        def reverse(node):
            curr = node
            prev = None
            while curr:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            return prev

        if not head or not head.next:
            return True

        slow = head
        fast = head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        second_half = reverse(slow.next)
        slow.next = None

        first_half = head
        second_copy = second_half

        while first_half and second_half:
            if first_half.val != second_half.val:
                return False
            first_half = first_half.next
            second_half = second_half.next

        slow.next = reverse(second_copy)

        return True