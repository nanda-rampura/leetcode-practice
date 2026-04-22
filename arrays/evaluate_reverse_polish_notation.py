"""
Problem: Evaluate Reverse Polish Notation
Difficulty: Medium
LeetCode: https://leetcode.com/problems/evaluate-reverse-polish-notation/
Pattern: Stack / Expression Evaluation
"""

from typing import List


class EvaluateReversePolishNotation:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for ch in tokens:
            if ch not in "+-*/":
                stack.append(int(ch))
            else:
                b = stack.pop()
                a = stack.pop()

                if ch == '+':
                    stack.append(a + b)
                elif ch == '-':
                    stack.append(a - b)
                elif ch == '*':
                    stack.append(a * b)
                else:
                    stack.append(int(a / b))  # truncate toward zero

        return stack.pop()