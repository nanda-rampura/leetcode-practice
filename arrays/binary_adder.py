class BinaryStringAdder:
    """
Problem: Add Binary Strings
Difficulty: Easy
LeetCode: https://leetcode.com/problems/add-binary/
Pattern: Two Pointers / Carry Simulation (String Traversal from Right to Left)
Key Idea: Simulate manual binary addition using carry instead of converting to integers
"""
    def addBinary(a: str, b: str) -> str:
        i, j = len(a) - 1, len(b) - 1
        carry = 0
        result = []

        while i >= 0 or j >= 0 or carry:
            total = carry

            if i >= 0:
                total += ord(a[i]) - ord('0')
                i -= 1

            if j >= 0:
                total += ord(b[j]) - ord('0')
                j -= 1

            result.append(str(total % 2))
            carry = total // 2

        return ''.join(reversed(result))