from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class MiddleOfLinkedList:
    """
    Problem: Middle of the Linked List
    Difficulty: Easy
    LeetCode: https://leetcode.com/problems/middle-of-the-linked-list/
    Pattern: Fast and Slow Pointers
    Approach: Move slow by 1 step and fast by 2 steps. When fast reaches the end, slow is at the middle.
    Time Complexity: O(n)
    Space Complexity: O(1)
    """

    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow