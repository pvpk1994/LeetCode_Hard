# Trapping Rain Water 
# Author: Pavan Kumar Paluri
# Leetcode Question: https://leetcode.com/problems/trapping-rain-water/

class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) ==0:
            # No towers
            return 0
        ans = 0
        left_arr = [None]*len(height)
        right_arr = [None]*len(height)
        left_arr[0] = height[0]
        for i in range(1, len(height)):
            left_arr[i] = max(height[i], left_arr[i-1])
        right_arr[len(height)-1] = height[len(height)-1]
        for j in range(len(height)-2, -1, -1):
            right_arr[j] = max(height[j], right_arr[j+1])
        for k in range(0, len(height), 1):
            ans += min(left_arr[k], right_arr[k])-height[k]
        return ans 
