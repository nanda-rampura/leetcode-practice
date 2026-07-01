from typing import List

class Solution:
    """
Problem: Move Zeroes
Difficulty: Easy
LeetCode: https://leetcode.com/problems/move-zeroes/

Pattern: Two Pointers / In-place Array Manipulation

Approach:
- Maintain a pointer for next non-zero position
- Swap non-zero elements forward
- Preserve relative order of non-zero elements

Time Complexity: O(n)
Space Complexity: O(1)
"""
    def moveZeroes(self, nums: List[int]) -> None:
        nonzero_index = 0

        for i in range(len(nums)):
            if nums[i] != 0:
                if i != nonzero_index:
                    nums[i], nums[nonzero_index] = nums[nonzero_index], nums[i]
                nonzero_index += 1