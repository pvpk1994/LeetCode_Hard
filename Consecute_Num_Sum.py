# Consecutive Number Sum 
# Author: Pavan Kumar Paluri
# Time Complexity: O(sqrt(N))
# Space Complexity: O(1)

class Solution:
    def consecutiveNumbersSum(self, N: int) -> int:
        counter = 0
        for k in range(1, int(sqrt(2*N))+1):
            if (N - k*(k+1)/2) % k == 0:
                counter += 1
        return counter
