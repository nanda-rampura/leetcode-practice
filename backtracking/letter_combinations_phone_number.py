from typing import List


class LetterCombinationsPhoneNumber:
    """
Problem: Letter Combinations of a Phone Number
Difficulty: Medium
LeetCode: https://leetcode.com/problems/letter-combinations-of-a-phone-number/
Pattern: Backtracking / DFS
Key Idea: Build combinations by exploring all letter mappings per digit recursively
"""
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        phone_map = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
        }

        results = []

        def backtracking(index, combination):
            if index == len(digits):
                results.append("".join(combination))
                return

            digit = digits[index]

            for ch in phone_map[digit]:
                combination.append(ch)
                backtracking(index + 1, combination)
                combination.pop()

        backtracking(0, [])

        return results