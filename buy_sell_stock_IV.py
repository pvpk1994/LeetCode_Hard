# Best Time to buy and sell stocks with K transactions
# Author: Pavan Kumar Paluri
# Time Complexity: O(n*k)

import math
def maxProfitWithKTransactions(prices, k):
	if len(prices) ==0:
		return 0
    # create a 2D array 
	dp = [[0 for _ in range(0, len(prices))] for _ in range(0, k+1)]
	# print(dp)
	for trans in range(1, k+1):
		max_far = float("-inf")
		for day in range(1,len(prices)):
			max_far = max(max_far, dp[trans-1][day-1]-prices[day-1])
			dp[trans][day] = max(dp[trans][day-1], max_far+prices[day])
			#dp[trans][day] = max(dp[trans][day-1], prices[day]+max([-prices[i]+dp[trans-1][i] for i in range(0, day)]))
	# result should be gathered in last cell
	# print(dp)
	return dp[k][len(prices)-1]
