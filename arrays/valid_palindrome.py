import unittest

class Solution:
    """
Problem: Valid Palindrome
Difficulty: Easy
LeetCode: https://leetcode.com/problems/valid-palindrome/
Pattern: Two Pointers / String Traversal
"""
    def is_palindrome(self, s: str) -> bool:
        """
        Determines if a string is a palindrome using a two-pointer approach.
        Time Complexity: O(n) | Space Complexity: O(1)
        """
        st, end = 0, len(s) - 1
        
        while st < end:
            # Skip non-alphanumeric characters from the start
            while st < end and not s[st].isalnum():
                st += 1
            # Skip non-alphanumeric characters from the end
            while st < end and not s[end].isalnum():
                end -= 1

            if s[st].lower() != s[end].lower():
                return False
            
            st += 1
            end -= 1
            
        return True

# --- Unit Tests ---

class TestPalindrome(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_standard_palindrome(self):
        self.assertTrue(self.solution.is_palindrome("A man, a plan, a canal: Panama"))

    def test_non_palindrome(self):
        # Because "race a car" is a tragedy, not a palindrome.
        self.assertFalse(self.solution.is_palindrome("race a car"))

    def test_empty_string(self):
        self.assertTrue(self.solution.is_palindrome(" "))

    def test_numeric_palindrome(self):
        self.assertTrue(self.solution.is_palindrome("12321"))

    def test_mismatched_alphanumeric(self):
        self.assertFalse(self.solution.is_palindrome("0P"))

    def test_only_symbols(self):
        self.assertTrue(self.solution.is_palindrome(".,"))

if __name__ == "__main__":
    unittest.main()