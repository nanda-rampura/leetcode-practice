from typing import List

class MajorityElement:
    """
    Problem: Majority Element
    Difficulty: Easy
    LeetCode: https://leetcode.com/problems/majority-element/
    Pattern: Boyer-Moore Voting Algorithm / Greedy
    """
    def majorityElement(self, nums: List[int]) -> int:
        candidate = None
        count = 0

        for num in nums:
            if count == 0:
                candidate = num

            if num == candidate:
                count += 1
            else:
                count -= 1

        return candidate