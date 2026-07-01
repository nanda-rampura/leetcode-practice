class Solution:
    """
Problem: Palindrome Number
Difficulty: Easy
LeetCode: https://leetcode.com/problems/palindrome-number/

Pattern: Math / Reverse Number

Approach:
- Reverse half or full number
- Compare with original
- Early reject negative numbers and trailing zero cases

Time Complexity: O(log10(n))
Space Complexity: O(1)
"""
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        original = x
        reversed_num = 0

        while x > 0:
            reversed_num = reversed_num * 10 + (x % 10)
            x //= 10

        return original == reversed_num