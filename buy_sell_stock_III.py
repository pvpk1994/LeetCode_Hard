# Best Time to buy and sell stock - Level 3
# LeetCode Hard Problem
# Atmost 2 transactions - Using Left and right arrays 

import math
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <=1:
            return 0
        # left arr and right arr
        left_profit = [0]*len(prices)
        right_profit = [0]*(len(prices)+1)
        
        # fill the left_profit array 
        left_min = prices[0]
        for i in range(1, len(prices)):
            if prices[i] < left_min:
                left_min = prices[i]
            left_profit[i] = max(left_profit[i-1], prices[i]-left_min)
        print(left_profit)
        
        # fill the right_profit array
        right_max = prices[len(prices)-1]
        for i in range(len(prices)-2, -1, -1):
            if prices[i] > right_max:
                right_max = prices[i]
            right_profit[i] = max(right_profit[i+1], right_max-prices[i])
        print(right_profit)
        
        max_profit  =0
        for i in range(len(prices)):
            max_profit = max(max_profit, left_profit[i]+right_profit[i+1])
        print(max_profit)
        return max_profit
