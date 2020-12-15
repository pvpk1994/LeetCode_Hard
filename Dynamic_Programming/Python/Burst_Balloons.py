# Burst Balloons
# Leetcode Hard: https://leetcode.com/problems/burst-balloons/
# Author: Pavan Kumar Paluri

# Time, Space: O(N^3), O(N^2)

class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        # Construct a 2D matrix 
        dp = [[0 for _ in range(0, len(nums))] for _ in range(0, len(nums))]
        for A in range(1, len(nums)+1):
            for i in range(0, (len(nums)-A)+1):
                j = i + A -1 
                for k in range(i, j+1, 1):
                    left, right = 1,1
                    if i!=0:
                        left = nums[i-1]
                    if j!=len(nums)-1:
                        right = nums[j+1]
                    before, after = 0,0
                    if i!=k:
                        before = dp[i][k-1]
                    if j!=k:
                        after = dp[k+1][j]
                    dp[i][j] = max(dp[i][j], before+left*nums[k]*right+after)
        return dp[0][-1]
