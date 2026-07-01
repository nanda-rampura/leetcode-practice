from typing import List

class Solution:
    """
Problem: Missing Number
Difficulty: Easy
LeetCode: https://leetcode.com/problems/missing-number/

Pattern: Bit Manipulation / XOR / Math

Approach:
- XOR all indices + all numbers
- Missing number cancels out and remains
- Works because: a ^ a = 0 and 0 ^ x = x

Time Complexity: O(n)
Space Complexity: O(1)
"""
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        res = n

        for i in range(n):
            res ^= nums[i]
            res ^= i

        return res