from typing import List


class ProductExceptSelf:
    """
Problem: Product of Array Except Self
Difficulty: Medium
Pattern: Prefix Sum / Suffix Product
LeetCode: https://leetcode.com/problems/product-of-array-except-self/
"""
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #build prefix array
        length = len(nums)
        results = [1] * length

        prefix = 1
        for i in range(length):
            results[i] = prefix
            prefix *= nums[i]

        suffix = 1
        for i in range(length-1, -1, -1):
            results[i] *= suffix
            suffix *= nums[i]
        return results
