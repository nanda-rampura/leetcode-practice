from typing import List

class ContainsDuplicate:
    """
Problem: Contains Duplicate
Difficulty: Easy
LeetCode: https://leetcode.com/problems/contains-duplicate/
Pattern: Hash Set
"""
    def containsDuplicate(self, nums: List[int]) -> bool:
        duplicatecheckset = set()
        for num in nums:
            if num in duplicatecheckset:
                return True
            duplicatecheckset.add(num)
        
        return False