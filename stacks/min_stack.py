class MinStack:
    """
Problem: Min Stack
Difficulty: Medium
Pattern: Stack / Design
LeetCode: https://leetcode.com/problems/min-stack/
"""
    def __init__(self):
        self.stack = []
        
    def push(self, val: int) -> None:
        current_min = val if not self.stack else min(val, self.stack[-1][1])
        self.stack.append((val, current_min))

    def pop(self) -> None:
        self.stack.pop() 
              
    def top(self) -> int:
        val,_ = self.stack[-1]
        return val

    def getMin(self) -> int:
        _,minimum = self.stack[-1]
        return minimum


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()