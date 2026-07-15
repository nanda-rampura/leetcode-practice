from typing import List


class FindDuplicateNumber:
    """
Metadata:
    Problem: Find the Duplicate Number
    Difficulty: Medium
    LeetCode: https://leetcode.com/problems/find-the-duplicate-number/
    Pattern: Fast & Slow Pointers (Floyd's Cycle Detection)
    Key Idea: Treat the array as a linked list where nums[i] points to nums[nums[i]].
    The duplicate number creates a cycle. Use Floyd's algorithm to find the
    intersection point, then find the cycle entrance, which is the duplicate value.
"""
    def findDuplicate(self, nums: List[int]) -> int:
        slow = nums[0]
        fast = nums[0]

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        
        fast = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        
        return slow
