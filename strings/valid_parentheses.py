class Solution:
    """
Problem: Valid Parentheses
Difficulty: Easy
LeetCode: https://leetcode.com/problems/valid-parentheses/
Pattern: Stack
"""
    def isValid(self, s: str) -> bool:
        stack = []

        def isvalidsofar(ch):
            if stack and ((ch == ')' and stack[-1] == '(') or
                          (ch == ']' and stack[-1] == '[') or
                          (ch == '}' and stack[-1] == '{')):
                stack.pop()
                return True
            return False

        for ch in s:
            if ch in '([{':
                stack.append(ch)
            else:
                if not isvalidsofar(ch):
                    return False
        
        return not stack

# List of test cases
test_cases = [
    "()",       # True
    "()[]{}",   # True
    "(]",       # False
    "([])",     # True
    "([)]",     # False
    "{[()]}",   # True
    "((()))",   # True
    "({[)})",   # False
]

if __name__ == "__main__":
    solution = Solution()
    for i, case in enumerate(test_cases, 1):
        result = solution.isValid(case)
        print(f"Test case {i}: s='{case}' -> Output: {result}")