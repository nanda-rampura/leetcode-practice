from typing import List

class NextPermutation:
    """
Problem: Next Permutation
Difficulty: Medium
LeetCode: https://leetcode.com/problems/next-permutation/
Pattern: Array / Two Pointers
Topics: Array, Two Pointers

Time Complexity: O(n)
Space Complexity: O(1)

Key Insight:
1. Traverse from right to left to find the first decreasing element (pivot).
2. Swap the pivot with the next greater element on the right side.
3. Reverse the suffix to obtain the smallest lexicographical arrangement.

The suffix after the pivot is always in descending order,
so reversing it makes it ascending.
"""
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #find the pivot
        pivot = -1
        for i in range(len(nums)-2, -1, -1):
            if nums[i] < nums[i+1]:
                pivot = i
                break

        if pivot == -1:
           nums.reverse()
           return

        #swap
        if pivot > -1:
            for i in range(len(nums)-1, -1, -1):
                if nums[i] > nums[pivot]:
                    nums[i], nums[pivot] = nums[pivot], nums[i]
                    break
        #reverse
        nums[pivot + 1:] = reversed(nums[pivot + 1:])
        