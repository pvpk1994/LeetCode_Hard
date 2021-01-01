# largest rectangle in histogram 
# Author: Pavan Kumar Paluri
# Leetcode Question: https://leetcode.com/problems/largest-rectangle-in-histogram/
# Issue: Incorrect Description of problem statement, the minimum height of the tower is to be considered while moving from left-> right
# Time Complexity: O(N) and Space Complexity: O(N) for stack 

# Time Complexity: O(N*2) and Space Complexity: O(1) -> Time Limit Exceeded
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        '''
        # Approach -1: Better Brute Force
        # edge case
        if len(heights) == 0:
            return 0
        left =0
        right = len(heights)-1
        max_area = 0
        for i in range(0, len(heights)):
            min_ht = math.inf
            for j in range(i, len(heights)):
                min_ht = min(min_ht, heights[j])
                max_area = max(max_area, min_ht*(j-i+1))
        return max_area
        '''
        # Approach -2: Using Stack Approach
        stack = [-1,]
        max_area = 0
        for i in range(0, len(heights)):
            while stack[-1] != -1 and heights[i] <= heights[stack[-1]]:
                # Time to pop out the topmost element and compute the max-area that can be obtained with that height
                current_index = stack.pop()
                current_ht = heights[current_index]
                max_area = max(max_area, current_ht*(i-stack[-1]-1))
            # if here: simply push the element
            stack.append(i)
        # if we reached the end of index with still some valid indices
        while stack[-1] != -1:
            current_index = stack.pop()
            current_ht = heights[current_index]
            max_area = max(max_area, current_ht*(len(heights)-stack[-1]-1))
        return max_area 
