"""
Problem: Best Time to Buy and Sell Stock

You are given an array `prices` where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

Examples:

1. Input: prices = [7,1,5,3,6,4]
   Output: 5
   Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6 - 1 = 5.

2. Input: prices = [7,6,4,3,1]
   Output: 0
   Explanation: No transactions are done, max profit = 0.

Constraints:
- 1 <= prices.length <= 10^5
- 0 <= prices[i] <= 10^4
"""

from typing import List

class Solution:
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