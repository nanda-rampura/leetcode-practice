"""
Problem: Valid Parentheses

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', 
determine if the input string is valid.

Rules:
- Open brackets must be closed by the same type of brackets.
- Open brackets must be closed in the correct order.

Constraints:
1 <= s.length <= 10^4
s consists of parentheses only '()[]{}'.
"""

class Solution:
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