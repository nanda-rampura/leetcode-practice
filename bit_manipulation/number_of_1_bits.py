class Solution:
    """
    Problem: Number of 1 Bits
    Difficulty: Easy
    LeetCode: https://leetcode.com/problems/number-of-1-bits/

    Pattern: Bit Manipulation

    Approach:
    - Check the least significant bit using n & 1.
    - Increment the count if the bit is 1.
    - Right shift the number until it becomes 0.

    Time Complexity: O(32) ≈ O(1)
    Space Complexity: O(1)
    """

    def hammingWeight(self, n: int) -> int:
        count = 0

        while n > 0:
            count += n & 1
            n >>= 1

        return count