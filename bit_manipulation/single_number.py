from typing import List

class Solution:
    """
Problem: Single Number
Difficulty: Easy
LeetCode: https://leetcode.com/problems/single-number/

Pattern: Bit Manipulation (XOR)

Approach:
- XOR all numbers
- a ^ a = 0, a ^ 0 = a
- All duplicates cancel out, leaving the single number

Time Complexity: O(n)
Space Complexity: O(1)
"""
    def singleNumber(self, nums: List[int]) -> int:
        num = 0
        for n in nums:
            num ^= n
        return num