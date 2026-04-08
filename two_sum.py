"""
LeetCode Problem: Two Sum
Difficulty: Easy
Topics: Array, Hash Table

Problem:
Given an array of integers nums and an integer target, 
return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution,
and you may not use the same element twice.
You can return the answer in any order.
"""

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in map:
                return [map[diff], i]
            else:
                map[nums[i]] = i

# List of test cases: each is a tuple (nums, target)
test_cases = [
    ([2, 7, 11, 15], 9),
    ([3, 2, 4], 6),
    ([3, 3], 6)
]

if __name__ == "__main__":
    solution = Solution()
    for i, (nums, target) in enumerate(test_cases, 1):
        result = solution.twoSum(nums, target)
        print(f"Test case {i}: nums={nums}, target={target} -> Output: {result}")