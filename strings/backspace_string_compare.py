class BackspaceStringCompare:
    """
Problem: Backspace String Compare
Difficulty: Easy
LeetCode: https://leetcode.com/problems/backspace-string-compare/
Pattern: Two Pointers / Reverse Traversal
Topics: String, Two Pointers

Time Complexity: O(n + m)
Space Complexity: O(1)

Key Insight:
Traverse both strings from right to left while maintaining
a skip counter for backspaces ('#').

Instead of building the final strings, dynamically skip
characters that would be deleted by backspaces.
"""
    def backspaceCompare(self, s: str, t: str) -> bool:
        skip_s = 0
        skip_t = 0
        i = len(s) - 1
        j = len(t) - 1
        while i >= 0 or j >= 0:
            while i >= 0:
                if s[i] == '#':
                   skip_s += 1
                   i -= 1 
                elif skip_s > 0:
                    skip_s -= 1
                    i -= 1 
                else:
                    break
            
            while j >= 0:
                if t[j] == '#':
                   skip_t += 1
                   j -= 1 
                elif skip_t > 0:
                    skip_t -= 1
                    j -= 1 
                else:
                    break

            if i >= 0 and j >= 0:
                if s[i] != t[j]:
                    return False
            elif i >= 0 or j >= 0:
                return False

            i -= 1
            j -= 1
        
        return True

