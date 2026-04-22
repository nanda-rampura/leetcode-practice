from typing import List

class Solution:
    """
Problem: Best Time to Buy and Sell Stock
Difficulty: Easy
LeetCode: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
Pattern: Greedy / One Pass
"""
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        
        minbuy = prices[0]
        maxProfit = 0
        
        for i in range(1, len(prices)):
            # Update maxProfit if current price minus minbuy is greater
            maxProfit = max(maxProfit, prices[i] - minbuy)
            # Update minbuy if current price is lower
            minbuy = min(minbuy, prices[i])

        return maxProfit


# -----------------------
# Test Cases
# -----------------------
if __name__ == "__main__":
    solution = Solution()
    
    test_cases = [
        ([7,1,5,3,6,4], 5),
        ([7,6,4,3,1], 0),
        ([1,2,3,4,5], 4),
        ([5,4,3,2,1], 0),
        ([2,4,1,7], 6)
    ]
    
    for i, (prices, expected) in enumerate(test_cases, 1):
        result = solution.maxProfit(prices)
        print(f"Test case {i}: prices={prices} -> Output: {result} | Expected: {expected} | {'✅' if result == expected else '❌'}")