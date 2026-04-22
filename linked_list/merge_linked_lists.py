
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    """
Problem: Merge Two Sorted Lists
Difficulty: Easy
LeetCode: https://leetcode.com/problems/merge-two-sorted-lists/
Pattern: Linked List / Two Pointers
"""
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        p0 = ListNode(-1)  # Dummy node
        p1 = p0
        while list1 and list2:
            if list1.val < list2.val:
                p1.next = list1
                list1 = list1.next
            else:
                p1.next = list2
                list2 = list2.next
            p1 = p1.next
        p1.next = list1 if list1 else list2
        return p0.next

# Helper function to convert Python list to ListNode
def list_to_linked(lst):
    dummy = ListNode(-1)
    current = dummy
    for val in lst:
        current.next = ListNode(val)
        current = current.next
    return dummy.next

# Helper function to convert ListNode to Python list
def linked_to_list(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result

# Test cases
test_cases = [
    ([1, 2, 4], [1, 3, 4]),  # Expected: [1,1,2,3,4,4]
    ([], []),                # Expected: []
    ([3,6], [5]),            # Expected: [3,5,6]
    ([], [0]),               # Expected: [0]
    ([5, 6, 7], [1, 2, 3]),  # Expected: [1,2,3,5,6,7]
]

if __name__ == "__main__":
    solution = Solution()
    for i, (lst1, lst2) in enumerate(test_cases, 1):
        l1 = list_to_linked(lst1)
        l2 = list_to_linked(lst2)
        merged_head = solution.mergeTwoLists(l1, l2)
        output = linked_to_list(merged_head)
        print(f"Test case {i}: list1={lst1}, list2={lst2} -> Merged: {output}")