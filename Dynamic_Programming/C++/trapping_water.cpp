// Trapping Rain water - Leetcode Hard 
// Author: Pavan Kumar Paluri
// Leetcode Question: https://leetcode.com/problems/trapping-rain-water/

class Solution {
public:
    int trap(vector<int>& height) {
        if(height.size() == 0)
            return 0;
        vector<int>left_arr(height.size());
        vector<int>right_arr(height.size());
        left_arr[0] = height[0];
        for(int i=1;i<height.size();i++)
        {
            left_arr[i] = max(left_arr[i-1], height[i]);
        }
        right_arr[height.size()-1] = height[height.size()-1];
        for(int j=height.size()-2; j>=0; j--)
        {
            right_arr[j] = max(right_arr[j+1], height[j]);
        }
        int ans = 0;
        for(int k=0; k<height.size(); k++)
            ans += min(right_arr[k], left_arr[k]) - height[k];
        return ans; 
    }
};
